# -*- coding: utf-8 -*-
"""The module 'epyunit.SystemCalls' provides the controlled execution of subprocesses as units.

The features are foreseen to support easy setups for unit and regression
tests on complex command line options and their combinations.
These are in designed to be used in conjunction with
with PyUnit, either within Eclipse and PyDev, or from the command line.

The provided feature set is supported on the platforms: Linux, MacOS, BSD, Solaris, and Windows.

A quick example call is::

  python -c 'from epyunit.SystemCalls import SystemCalls;x=SystemCalls(**{"proceed":"trace"});x.callit("myscript.sh xOK")'

or::

  python -c 'from epyunit.SystemCalls import SystemCalls;x=SystemCalls(**{"proceed":"trace"});x.callit("myscript.py xOK")'

**SECURITY REMARK**: Current version supports for subprocesses the ShellMode only.
For test environments in R&D this - hopefully - is perfectly OK,
else eventual security issues has to be considered.

The SystemCalls class optionally uses subprocess32 when present, this is recommended.
See https://pypi.python.org/pypi/subprocess32/.

"""
from __future__ import absolute_import

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.2.7'
__uuid__='9de52399-7752-4633-9fdc-66c87a9200b8'

__docformat__ = "restructuredtext en"

import os,sys,datetime,time
version = '{0}.{1}'.format(*sys.version_info[:2])
if not version in ('2.6', '2.7',): # pragma: no cover
    raise Exception("Requires Python-2.6.* or higher")

if os.name == 'posix' and sys.version_info[0] < 3 and sys.version_info[1] < 7:
    import subprocess32 as subprocess
else:
    import subprocess

#import subprocess,platform
import platform
import shlex,re
import fcntl

# output enums
_O_STD = 1 #: output to STDOUT
_O_ERR = 2 #: output to STDERR
_O_STR = 3 #: output to STRING
_outdefault = _O_STR

# input enums
_I_SCOM = 0 #: reads Subproces.communicate
_I_READC = 1 #: reads characters - does not sync between threads/procs
_I_READL = 2 #: reads characters - writes units of lines for multiple thread/procs
_indefault = _I_SCOM

# cache enums
_C_QUIET   = 0 #: not display
_C_PIPE    = 1 #: STDOUT and STDERR written in realtime by unit of lines
_C_FOUT    = 2 #: STDOUT buffered by seperate file
_C_FERR    = 4 #: STDERR buffered by seperate file
_C_FOUTERR = 8 #: STDERR and STDOUT buffered by common file
_cachedefault = _C_QUIET
"""Management of read buffer for further caching of data."""

_CSPLTL = re.compile(ur'\r*\n')
"""Split lines on Windows too including with contained multiple(???) '\r' """

def output(s,_o=None):
    """Directs the output stream
    Args:

        s: String for output

        _o: Output channel:
            _O_STD, _O_ERR, _O_STR

    Returns:

        _o == _O_STD: string

        _o == _O_ERR: prints to STDERR, returns True

        _o == _O_STR: prints to STDOUT, returns True

        else:         returns False

    Raises:

        pass/through
    """
    global _outdefault
    if not _o:
        _o = _outdefault
    if _o == _O_STR:
        return s
    elif _o == _O_ERR:
        sys.stderr.write(s)
    else:
        sys.stdout.write(s)
    return True

class SystemCallsException(Exception):
    """Common error within epyunit.SystemCalls.
    """
    pass

class SystemCallsTimeout(SystemCallsException):
    """Timeout of subprocess epyunit.SystemCalls.
    """
    pass

#class SystemCallsExceptionSubprocessError(SystemCallsException):

class SystemCallsExceptionSubprocessError(SystemExit):
    """Error from subprocess.
    """
    def __init__(self,*args,**kargs):
        """Calls the 'exceptions.SystemExit' with pass through of parameters.

        Args:

            **kargs: Additional parameters specific for ePyUnit
                where the interface is not actually clear.
                These are removed before the pass-through call.

                exitval: Replaces 'exceptions.SystemExit.code', the
                    first param value when of type 'int'. The default
                    is defined as '1'.

                    REMARK: Did not found an official interface for
                        'exceptions.SystemExit.__init__', thus opted
                        to temporary injection.

                exitmsg: Defines display test.

        Returns:
            None/Itself

        Raises:
            itself

        """
        _code = kargs.get('exitval')
        if _code:
            kargs.pop('exitval')
        _msg = kargs.get('exitmsg')
        if _msg:
            kargs.pop('exitmsg')
        super(SystemCallsExceptionSubprocessError,self).__init__(*args,**kargs)
        if _code:
            self.code = _code
        if _msg:
            self.message = _msg
        pass

class SystemCalls(object):
    """Wraps system calls for the execution of subprocesses.
    For supported parameters refer to 'epyunit.SystemCalls.setkargs()'.

    """
    def __init__(self,**kargs):
        """Prepares the interface for subprocess calls with output cache.
        The initial setup includes the preparation of the result
        cache for the response data from stdout and stderr.

        Args:

            **kargs:
                Parameters specific for the operations,
                passed through to **SystemCalls.setkargs**
                `[see setkargs] <#setkargs>`_.

        Returns:

            When successful returns 'True', else returns either 'False', or
            raises an exception.
            Success is the complete addition only, thus one failure returns
            False.

            *REMARK*
                When errors occur in buffered mode the
                output from the called process is possibly
                not completely cached. In that case
                switch to 'dialogue' mode in order to get an
                unbuffered console display.

        Raises:

            passed through exceptions:

        """
        # initial defaults
        self.console = 'cli' #: console type for output
        self.bufsize = 16384 #: size of cache for output received from subprocess
        #self.bufsize=-1

        self.emptyiserr = False
        """The subprocess call for an empty string is 'success',
        thus this has to be checked independently for eventually erroneously missing call string
        """

        self.errasexcept = False #: raises in case of errors an exception

        if sys.platform == 'win32':
            self.myexe = self._mode_batch_win
        else:
            self.myexe = self._mode_batch_posix

        self.out = 'pass' #: output format/stream
        self.outtarget = 'stdout' #: output format/stream
        self.passerr = False

        self.inp = _indefault #: input call
        self.cache = _cachedefault
        
        self.proceed = 'doit' #: what to do...
        self.raw = False
        self.useexit = True
        self.usestderr = False
        self.verbose = 0

        self.exectype = 'inproc' #: Type of execution
        self.synctype = 'async' #: Type of synchronization
        self.forcecmdcall = 'list' #: Force type of option passing
        self.tsig = 'TERM' #: Termination signal
        self.tmax = 15 #: timeout until tsig emission


        self._appname = None
        self._testid = None
        self._timestamp = None
        self._environment = None
        self.env = None

        self.rules = None
        self.useexit = True
        self.usestderr = False

        self.setkargs(**kargs)
        pass

    def callit(self,cmdcall,**kargs):
        """Executes a prepared 'cmdcall' synchronous by the a preset function pointer 'self.myexe'.
        For the full scope of call parameters including multiple subprocesses use the method
        `[see create] <#create>`_.

        Args:

            cmdcall:

                A prepared call, either shell-style call-string,
                or a list in accordance to the call convention of
                'subprocess' package. The 'shell' parameter is
                by default set in accordance to the provided type.

            **kargs:

                Parameters specific for the operations,
                passed through to **SystemCalls.setkargs**
                `[see setkargs] <#setkargs>`_.

                The following are also evaluated instantly within
                the call prologue:

                proceed:

                    Changes predefined value and dispatches to the subcall.

                raw:

                    Suppress the split of lines for
                    stdout and stderr.


        Returns:

            Result of call, the format is:

                ret[0]::= exit value

                ret[1]::= STDOUT as non-processed string.

                ret[2]::= STDERR as non-processed string.

            *REMARK*
                When errors occur in buffered mode the
                output from the called process is possibly
                not completely cached, e.g. in case of exeptions.
                In that case try switching to 'dialogue' mode in order
                to get an unbuffered console display. This will deliver
                - hopefully - the complete output.

        Raises:

            SystemCallsTimeout:

                Rised in case of timeout by tmax/tsig.
                Terminates also the outstanding subprocess.

            passed through exceptions:

        """
        proceed = self.proceed
        _raw = False
        for k,v in kargs.iteritems():
            if k=='proceed':
                proceed=self.get_proceed(v)
                kargs.pop('proceed')
            elif k=='raw':
                _raw=True
                kargs.pop('raw')
        self.setkargs(**kargs)

        ret=[1,]
        if proceed=="print":
            print str(cmdcall)
            return [0,[],[]]

        elif proceed=="trace":
            print >>sys.stderr, "TRACE:"+str(cmdcall)
            ret=self.myexe(cmdcall,**kargs)

        elif proceed=="doit":
            ret=self.myexe(cmdcall,**kargs)

        if ret[0] not in (0,5):
            if self.verbose>0:
                print "ret:"+str(ret)+" =>call:"+str(cmdcall)

        if not _raw and not self.raw:
            ret = self.splitLines(ret)
        return ret

    def cancel(self,proc=None):
        """Cancels a running process.
        """
        if not proc:
            proc = self.p

        pass

    def create(self,proc=None):
        """Executes a prepared 'cmdcall' with a variety of parameters.

        For now a placeholder only - implementation is going to follow soon.

        """
        if not proc:
            proc = self.p

        pass

    def displayit(self,ret,**kargs):
        """Streams result list 'ret' in selected format to selected outtarget.

        Args:

            ret: Data to be displayed.

            **kargs:

                outtarget: The target of display:

                    str: return as formatted string

                    stdout: print to sys.stdout

                    stderr: print to sys.stderr

                out: Output for display, valid:

                    csv   : CSV with sparse records

                    pass  : pass through STDOUT and STDERR from subprocess

                    repr  : Python 'repr()'

                    str   : Python 'str()'

                    xml   : XML

                default:=self.out

        Returns:

            When successful returns

                outtarget=='str': returns a printable formatted string

                outtarget in ('stdout', 'stderr',):

                    'True':  for success

                    'False': for failure

        Raises:

            passed through exceptions:

        """
        _target = kargs.get('outtarget',self.outtarget)
        if _target == 'str':
            _t = _O_STR
        elif _target == 'stderr':
            _t = _O_ERR
        else:
            _t = _O_STD
        self._oc = ""

        _out = kargs.get('out',self.out)

        def _output(s,_o=None):
            if not _o:
                _o = _t
            if _o == _O_STR:
                self._oc += s
            elif _o == _O_ERR:
                sys.stderr.write(s)
            else:
                sys.stdout.write(s)


        if _out in ("pass","passall","raw",): # pass through STDOUT and STDERR from subprocess
            if ret[1]:
                if type(ret[1]) == list:
                    _output("\n".join(ret[1])+'\n')
                else:
                    _output(ret[1])
            if ret[2]:
                if _t == _O_STD:
                    _tx = _O_ERR
                else:
                    _tx = _t
                if type(ret[2]) == list:
                    _output("\n".join(ret[2])+'\n',_tx)
                else:
                    _output(ret[2],_tx)

        elif _out == "repr": # Python 'repr()'
            _output(repr(ret))

        elif _out == "str": # Python 'str()'
            _output("exit:   "+str(ret[0])+'\n')
            _output("stdout: "+str(ret[1])+'\n')
            _output("stderr: "+str(ret[2])+'\n')

        elif _out == "xml": # XML
            _output("""<?xml version="1.0" encoding="UTF-8"?>\n""")

            # take timestamp
            _dn = datetime.datetime.now()
            _date=str(_dn.year)+'-'+str(_dn.month)+'-'+str(_dn.day)
            _time=str(_dn.hour)+':'+str(_dn.minute)+':'+str(_dn.second)
            _head="<test-result "
            if self._testid:
                _head +=  " id="+str(self._testid)
            if self._appname:
                _head +=  " appname='"+str(self._appname)+"'"
            if self._timestamp:
                _head +=  " date='"+str(_date)+"'"
                _head +=  " time='"+str(_time)+"'"
            if self._environment:
                _head +=  " host='"+str(self._host)+"'"
                _head +=  " user='"+str(self._user)+"'"
                _head +=  " os='"+str(self._os)+"'"
                _head +=  " osver='"+str(self._osver)+"'"
                _head +=  " dist='"+str(self._dist)+"'"
                _head +=  " distver='"+str(self._distver)+"'"
            _head += ">"

            _output(str(_head)+'\n')

            # exit code
            _output("    <exit-code>"+str(ret[0])+"</exit-code>\n")

            # STDOUT
            _output("    <stdout>\n")
            lx = 0
            for l in ret[1]:
                _output("        <line cnt="+str(lx)+">"+str(l)+"</line>\n")
                lx += 1
            _output("    </stdout>\n")

            # STDERR
            _output("    <stderr>\n")
            lx = 0
            for l in ret[2]:
                _output("        <line cnt="+str(lx)+">"+str(l)+"</line>\n")
                lx += 1
            _output("    </stderr>\n")

            _output("""</test-result>""")

        elif _out == "csv": # CSV with sparse records
            _head = None

            if self._testid:
                if _head: _head = ';'
                _head += "testid"
            if self._appname:
                if _head: _head = ';'
                _head +=  ";appname"
            if self._timestamp:
                if _head: _head = ';'
                _head += ";date;time"
            if self._environment:
                if _head: _head = ';'
                _head += ";host;user;os;osver;dist;distver"

            if _head: _head = ';'
            else: _head = ""
            _head += "exitcode;total-lines;stdout-line;stdout;stderr-line;stderr"

            _output(str(_head)+'\n')

            # take timestamp
            _dn = datetime.datetime.now()
            _date=str(_dn.year)+'-'+str(_dn.month)+'-'+str(_dn.day)
            _time=str(_dn.hour)+':'+str(_dn.minute)+':'+str(_dn.second)

            _lxtot=0

            # output record prefix
            _recpre = None

            # common prefix
            if self._testid:
                if _recpre: _recpre += ';'
                _recpre += str(self._testid)
            if self._appname:
                if _recpre: _recpre += ';'
                _recpre +=  str(self._appname)
            if self._timestamp:
                if _recpre: _recpre += ';'
                _recpre += str(_date)+";"+str(_time)
            if self._environment:
                if _recpre: _recpre += ';'
                _recpre += str(self._host)+";"+str(self._user)+";"+str(self._os)+";"+str(self._osver)+";"+str(self._dist)+";"+str(self._distver)

            _lx1 = 0
            _lx2 = 0

            _r1 = len(ret[1])
            _r2 = len(ret[2])
            if _r1 > _r2:
                _rmax = _r1
            else:
                _rmax = _r2

            for _ri in range(_rmax):
                _lxtot +=1
                _rec = _recpre
                if _rec: _rec += ';'
                else: _rec = ''
                _rec += str(ret[0])+";"+str(_lxtot)

                # STDOUT
                if len(ret[1]) > _ri:
                    if _rec: _rec += ';'
                    else: _rec = ''
                    _rec += str(_lx1)+";"+str(ret[1][_ri])
                    _lx1 += 1
                else:
                    if _rec: _rec += ';;'
                    else: _rec = ';'

                # STDERR
                if len(ret[2]) > _ri:
                    if _rec: _rec += ';'
                    else: _rec = ''
                    _rec += str(_lx2)+";"+str(ret[2][_ri])
                    _lx2 += 1
                else:
                    if _rec: _rec += ';;'
                    else: _rec = ';'

                _output(str(_rec)+'\n')

        if _t == _O_STR:
            return self._oc
        return True

    def get_proceed(self,s):
        """Verifies valid proceed type.
        """
        if s in ('print','trace', 'doit'):
            return s
        else:
            raise Exception('STATE:ERROR:proceed not supported:'+str(s))

    def sub_get_lines(self,fds,fde,**kargs):
        """Reads non-blocking from stdout and stderr into
        a buffer and displays each line immediately.
        
        Args:

            fds:

                File descriptor for the STDOUT of the called subprocess.

            fde:

                File descriptor for the STDERR of the called subprocess.

            **kargs:

                rtd:

        Returns:
        
        Raises:
         
        """
        fls = fcntl.fcntl(fds, fcntl.F_GETFL)
        fle = fcntl.fcntl(fde, fcntl.F_GETFL)
        fcntl.fcntl(fds, fcntl.F_SETFL, fls | os.O_NONBLOCK)
        fcntl.fcntl(fde, fcntl.F_SETFL, fle | os.O_NONBLOCK)

        chs = ''
        che = ''
        bufs = ""
        bufe = ""

        res = [[], [],]
        
        while True:
            try:

                #
                # collect data form subproc
                #
                while chs != '\n':
                    chs = os.read(fds.fileno(), 1)
                    if not chs :
                        break
                    bufs += chs

                while che != '\n':
                    che = os.read(fde.fileno(), 1)
                    if not che:
                        break
                    bufe += che

                if not chs and not che:
                    # finished
                    break

                #
                # caching
                #
                if bufs: # stdout
                    if bufs[-1] == '\n':
                        res[0].append(bufs[:-1])
                    else:
                        res[0].append(bufs)
                if bufe: # stderr
                    if bufe[-1] == '\n':
                        res[1].append(bufe[:-1])
                    else:
                        res[1].append(bufe)

                if self.cache & _C_FOUTERR: # write stdout and stderr into one log-file
                    pass

                if self.cache & _C_FOUT: # write stdout into a seperate log-file
                    pass
                
                if self.cache & _C_FERR: # write stderr into a seperate log-file
                    pass

                if self.cache & _C_PIPE: # write to stdout and stderr
                    if bufs: # stdout
                        sys.stdout.write(bufs)
                        sys.stdout.flush()
                    if bufe: # stderr
                        sys.stderr.write(bufe)
                        sys.stderr.flush()

                bufs =''
                chs = ''
                bufe =''
                che = ''

            except OSError:
                # waiting for data be available on fd
                pass

        return res

    def _mode_batch_postproc(self,cmdcall,**kargs):
        """Postprocess
        """
        pass

    def _mode_batch_posix(self,cmdcall,**kargs):
        """Creates and calls a process instance on POSIX based systems.

        The IO by stdout/stdin/stderr are redirected. Supports
        shell-style parameters only.

        Args:
            cmdcall:
                A prepared shell-style call.

            **kargs:

                mode:
                    Execution mode for the created process instance.

                    * batch:
                        Proceeds headless, collects reponses from STDOUT
                        and STDERR.

                    * dialogue
                        Proeceeds interactive.

                env:
                    Inherited environment, by default the current.

                tmax:
                    Timeout in seconds.

                tsig:
                    Termination signal, default is KILL.

        Returns:
            When successful returns 'True', else returns either 'False', or
            raises an exception.

        Raises:
            for parameter 'errasexcept': SystemCallsExceptionSubprocessError
            passed through exceptions:

        For further information refer to 'console' option of constructor/setkargs.

        """
        if self.emptyiserr and ( not cmdcall or cmdcall.lstrip(' ') == ''):
            return [2,'', 'ERROR:MissingCallstr']

        ret=[1,]
        _env = kargs.get('env',os.environ)
        _mode = kargs.get('mode','batch')

        if type(cmdcall) in (str,unicode,):
            _shell = True
        elif type(cmdcall) is list:
            _shell = False

        _close_fds = False
        self.stdioIN = subprocess.PIPE
        self.stdioOUT = subprocess.PIPE
        self.stdioERR = subprocess.PIPE

        self.p=subprocess.Popen(
                cmdcall,
                shell=_shell,
                bufsize=self.bufsize,
                stdin=self.stdioIN,
                stdout=self.stdioOUT,
                stderr=self.stdioERR,
                close_fds=_close_fds,
                env=_env
                )

        # prep cache
        if self.cache == _C_PIPE:
            self.res = ['','',]
        
        #FIXME:
        elif self.cache == _C_FOUT:
            self.res = ['','',]
        elif self.cache == _C_FERR:
            self.res = ['','',]

        else:
            self.res = ['','',]

        # fetch the results from subprocess
        self.stdin=self.p.stdin
        self.stdout=self.p.stdout
        self.stderr=self.p.stderr

        if self.inp == _I_SCOM: # uses communicate, blocks until subprocess is finished
            #
            # collect data form subproc
            #
            self.res=self.p.communicate()
            self.p.poll()

            if self.cache & _C_FOUTERR: # write stdout and stderr into one log-file
                pass

            if self.cache & _C_FOUT: # write stdout into a seperate log-file
                pass
            
            if self.cache & _C_FERR: # write stderr into a seperate log-file
                pass

            if self.cache & _C_PIPE: # write to stdout and stderr
                if self.res[0]: # stdout
                    sys.stdout.write(self.res[0])
                    sys.stdout.flush()
                if self.res[1]: # stderr
                    sys.stderr.write(self.res[1])
                    sys.stderr.flush()

        elif self.inp == _I_READC: # uses read-char
            while True:
                out = self.p.stderr.read(1)
                if out == '' and self.p.poll() != None:
                    break
                if out != '':
                    if self.cache & _C_PIPE:
                        pass
                    elif self.cache & _C_FOUT:
                        self.res[0] += out
                        pass
                    elif self.cache & _C_FERR:
                        self.res[1] += out
                        pass
                     
                    sys.stdout.write(out)
                    sys.stdout.flush()
        
        elif self.inp == _I_READL: # uses read-line
            while True:

                sout,serr = self.sub_get_lines(self.p.stdout, self.p.stderr)
                if not sout and not serr and self.p.poll() != None:
                    break

                self.res[0] += '\n'.join(sout)
                self.res[1] += '\n'.join(serr)

        _errcond = False
        if self.useexit and self.usestderr:
            if self.p.returncode or self.res[1]:
                _errcond = True
        elif self.useexit and self.p.returncode:
            _errcond = True
        elif self.usestderr and self.res[1]:
            _errcond = True

        if _errcond and self.errasexcept: # transforms errors from subprocesses into Exceptions
            # flush cache...
            if self.res[0]:
                sys.stdout.write(self.res[0])
            if self.res[1]:
                sys.stderr.write(self.res[1])
            # .. raise exception
            #raise SystemCallsExceptionSubprocessError(self.p.returncode,**{'exitmsg':"FROM:"+str(cmdcall) +"\n"+ str(self.res[1]),'exitval':self.p.returncode,})
            raise SystemCallsExceptionSubprocessError(self.p.returncode,**{'exitmsg':"FROM:"+str(cmdcall) +"\n",})

        elif _errcond and self.passerr: # passes errors from subprocesses simply through as error exit
            # flush cache...
            if self.res[0]: # stdout
                sys.stdout.write(self.res[0])
            if self.res[1]: # stderr
                sys.stderr.write(str(self.res[1]))
            # ..now exit
            sys.exit(self.p.returncode)

        elif _errcond and not self.p.returncode and self.usestderr: # treats any presence of stderr as error
            ret[0] = 1
            ret.extend(self.res)
            return ret

        else: # wraps result of subprocess call into a tuple
            ret[0]=self.p.returncode
            ret.extend(self.res)
            return ret

    def _mode_batch_win(self,cmdcall,**kargs):
        """Creates and calls a process instance on Windows based systems.

        The IO by stdout/stdin/stderr are redirected. Supports
        shell-style parameters only.

        Args:
            cmdcall:
                A prepared shell-style call.

            **kargs:

                mode:
                    Execution mode for the created process instance.
                    * batch:
                        Proceeds headless, collects reponses from STDOUT
                        and STDERR.

                    * dialogue
                        Proeceeds interactive.

                env:
                    Current environment.

                tmax:
                    Timeout in seconds.

                tsig:
                    Termination signal, default is KILL.

        Returns:
            When successful returns 'True', else returns either 'False', or
            raises an exception.

        Raises:
            for parameter 'errasexcept': SystemCallsExceptionSubprocessError
            passed through exceptions:

        For further information refer to 'console' option of constructor/setkargs.

        """
        if self.emptyiserr and ( not cmdcall or cmdcall.lstrip(' ') == ''):
            return [2,'', 'ERROR:MissingCallstr']

        ret=[1,]
        _env = kargs.get('env',None)

        _env = os.environ

        _mode = kargs.get('mode','batch')

        if type(cmdcall) is str:
            _shell = True
        elif type(cmdcall) is list:
            _shell = False

        si = subprocess.STARTUPINFO()
        si.dwFlags  = subprocess.STARTF_USESHOWWINDOW
        si.dwFlags |= subprocess.CREATE_NEW_PROCESS_GROUP
#        si.dwFlags |= subprocess.CREATE_NEW_PROCESS_GROUP
#        si.dwFlags |= subprocess.STARTF_USESTDHANDLES
#        si.dwFlags |= subprocess.SW_HIDE
#        si.dwFlags |= subprocess.CREATE_NEW_CONSOLE


        self.stdio = subprocess.PIPE

        _close_fds = False
        self.p=subprocess.Popen(
                cmdcall,
                shell=_shell,
                bufsize=self.bufsize,
                stdin=self.stdio,
                stdout=self.stdio,
                stderr=self.stdio,
                close_fds=_close_fds,
                env=_env,
                startupinfo=si,
                )

        # fetch the results from subprocess
        self.stdin=self.p.stdin
        self.stdout=self.p.stdout
        self.stderr=self.p.stderr
        self.res=self.p.communicate()

        self.p.poll()

        _errcond = False
        if self.useexit and self.usestderr:
            if self.p.returncode or self.res[1]:
                _errcond = True
        elif self.useexit and self.p.returncode:
            _errcond = True
        elif self.usestderr and self.res[1]:
            _errcond = True

        if _errcond and self.errasexcept: # transforms errors from subprocesses into Exceptions
            # flush cache...
            if self.res[0]:
                sys.stdout.write(self.res[0])
            if self.res[1]:
                sys.stderr.write(self.res[1])
            # .. raise exception
            #raise SystemCallsExceptionSubprocessError(self.p.returncode,**{'exitmsg':"FROM:"+str(cmdcall) +"\n"+ str(self.res[1]),'exitval':self.p.returncode,})
            raise SystemCallsExceptionSubprocessError(self.p.returncode,**{'exitmsg':"FROM:"+str(cmdcall) +"\n",})

        elif _errcond and self.passerr: # passes errors from subprocesses simply through as error exit
            # flush cache...
            if self.res[0]: # stdout
                sys.stdout.write(self.res[0])
            if self.res[1]: # stderr
                sys.stderr.write(str(self.res[1]))
            # ..now exit
            sys.exit(self.p.returncode)

        elif _errcond and not self.p.returncode and self.usestderr: # treats any presence of stderr as error
            ret[0] = 1
            ret.extend(self.res)

        else: # wraps result of subprocess call into a tuple
            ret[0]=self.p.returncode
            ret.extend(self.res)

        #close the pipes
        self.p.stderr.close()
        self.p.stdout.close()

        return ret

    def _mode_dialogue(self,cmdcall,**kargs):
        """Internal call reference for processing an interactive dialogue call.

        Supports shell-style parameters only.

        For further information refer to 'console' option of constructor/setkargs.

        """

        #FIXME: has to be tested
        if self.emptyiserr and ( not cmdcall or cmdcall == ''):
            return [2,'', 'ERROR:MissingCallstr']

        ret=[0,]
        try:
            self.p=subprocess.check_call(
                cmdcall,
                shell=True,
                bufsize=self.bufsize
                )
        except subprocess.CalledProcessError as e:
            try:
                ret[0]=self.p.returncode
                ret.append(self.p.output)
            except:
                ret[0]=99
                ret.append(str(e))
                pass
        return ret

    def setkargs(self,**kargs):
        """Sets provided parameters for the subprocess call context.

        Applicable for the initial call of self.__init__(),
        and later modification. Called for each start of
        a subprocess in order to update optional the specific
        call context modification.

        Args:
            **kargs: Parameter specific for the operation,


                bufsize:

                    The size of the output buffer for the called
                    subprocess, refer to **subprocess.Popen**.
                    Default value is -1.

                cache:=<cache-param=list>

                    Defines the type and thus target caching 
                    of the output of the raw data.
                    The output streams could be combined by
                    defining multiple types:
                    ::

                      cache-param-list:=cache-param[,cache-param-list]
                      cache-param:=(
                          {type:pipe}
                        | {type:fout,fpname:''}
                        | {type:ferr,fpname:''}
                        | {type:fouterr,fpname:''}
                      )

                      pipe:None

                        the Subprocess.PIPE for stdout and stderr

                      fout:<fpathname>:

                        reads stdout into a file

                      ferr:<fpathname>:

                        reads stderr into a file
                    
                    default := pipe

                console ('cli','dialogue')

                    ffs ('batch','ui','gtk', 'qt')

                      cli:

                        Works in batch mode, particularly the
                        stdin, stdout, and stderr streams are
                        caught into a string buffer by the
                        calling process via a pipe. The content
                        is passed after termination of the
                        called sub-process.

                      dialogue:

                        Works without buffered io streams.
                        Thus allows for interaction, but not
                        post-processing.

                debug:

                    Sets debug for rule data flow.

                emptyiserr:

                    Treats passed empty call strings as error.
                    The applied 'subprocess.Popen()' treats them as
                    success, which may cover errors in generated
                    call strings, particularly in loops.

                    default := False

                env:

                    Environment to be passed through to the subprocess.
                    
                    Default := current

                errasexcept:

                    Passes errors as exceptions, transforms the resuls from
                    subprocesses into Exceptions data. Exits the process.

                    default := False

                exectype:

                    Type of execution.

                      inproc:

                        Calls 'Popen' directly from within the process.

                      bythread:

                        Starts an intermediate thread within current
                        process and executes 'Popen'.

                      byfork

                        Starts an intermediate process by fork and
                        executes 'Popen'.

                forcecmdcall:

                    Forces type of the command call option passed to 'Popen'.

                    * shell
                    * list

                inp:

                    Defines the read-in of the output of called subprocess.

                      communicate: 

                        Calls Subproces.communicate, blocks until 
                        completion of subprocess.

                      readc:

                        Reads characters from subprocess, does not 
                        accurately synchronize for multiple threads
                        onto one output stream.
                        
                        Displays each character in real-time.

                      readl:

                        Reads characters from subprocess, does 
                        accurately synchronize for multiple threads
                        onto one output stream in units of lines.
                        
                        Displays each line in real-time.

                    default := communicate
                    
                out: 

                    Output for display. Supported types are:

                    csv:

                        CSV seperated by ';', with sparse records

                    pass:

                        Pass through STDOUT and STDERR from
                        subprocess

                    repr:

                        Python 'repr()'

                    str:

                        Python 'str()'

                    xml:

                        XML

                passerr:

                    Passes errors from subprocesses transparently
                    through by stdout, stderr, and exit code. Exits
                    the process.

                    default := False

                proceed ('print','trace', 'doit')

                    print - trace only

                    trace - execute and trace

                    doit  - execute

                raw:

                    Pass through strings from STDOUT and STDERR unprocessed.
                    Default is to split the lines into a list for post 
                    processing line scope.

                rules:

                    Sets the rules object.

                synctype:

                    Type of call synchronization.

                      async:

                        Executes the subprocess asynchronously, this e.g. enables
                        in current implementation for platform independent timeouts.

                      sync:

                        Executes synchronously, thus blocks any other execution.

                tsig:

                    Termination signal, default is KILL.

                tmax:

                    Timeout in seconds.

                useexit:

                    Use exit code for error detection of subprocess.

                    default := True

                usestderr:

                    Use 'sys.stderr' output for error detection of subprocess.
                    When set to 'True', the presence of a string is treated as error
                    condition.

                    default := False

                verbose:

                    Sets verbose for rule data flow.

        Returns:

            When successful returns 'True', else returns either 'False', or
            raises an exception.
            Success is the complete addition only, thus one failure returns
            False.

        Raises:

            passed through exceptions:

        """
        for k,v in kargs.iteritems():
            if k=='bufsize':
                self.bufsize=int(v)
            elif k=='cache':
                for vx in v:
                    if vx.get('type').lower() == 'pipe':
                        self.cache|=_C_PIPE
                    elif vx.get('type').lower() == 'fout':
                        self.cache|=_C_FOUT
                        self.cacheo = vx.get('fpname')
                    elif vx.get('type').lower() == 'ferr':
                        self.cache|=_C_FERR
                        self.cachee = vx.get('fpname')
                    elif vx.get('type').lower() == 'fouterr':
                        self.cache|=_C_FERR
                        self.cacheoe = vx.get('fpname')

            elif k=='console':
                self.console=v
                if v == 'cli':
                    self.out = v
                if v == 'dialogue':
                    self.myexe=self._mode_dialogue
                elif v=='batch':
                    raise Exception('STATE:ERROR:console not supported:'+str(v))
                elif v in ('ui','gtk', 'qt'):
                    pass
                else:
                    self.myexe=self._mode_dialogue
            elif k=='debug':
                self.debug=v
            elif k=='emptyiserr':
                self.emptyiserr=v
            elif k=='env': # to be evaluated by the caller case by case only
                self.env = v
                pass
            elif k=='errasexcept':
                self.errasexcept=v
            elif k=='out':
                self.out = v
                if v in ('csv', 'pass', 'repr', 'str', 'xml', ):
                    pass
                else:
                    raise SystemCallsException("Unknown output type:"+str(self.out))
            elif k=='passerr':
                self.passerr=v
            elif k=='proceed':
                self.proceed=self.get_proceed(v)
            elif k=='raw':
                self.raw=v
            elif k=='rules':
                self.rules=v
            elif k=='useexit':
                self.useexit=v
            elif k=='usestderr':
                self.usestderr=v
            elif k=='verbose':
                self.verbose=v
            elif k=='inp':
                if v.lower() == 'communicate':
                    self.inp=_I_SCOM
                elif v.lower() == 'readc':
                    self.inp=_I_READC
                elif v.lower() == 'readl':
                    self.inp=_I_READL
        return True

    def splitLines(self,oldres):
        """Converts the raw string fields including '\n' of a return value into line arrays.

        Args:

            oldres: The raw result of a previous call.

        Returns:

            Result of call, the format is:

                ret[0]::=exit value

                ret[1]::=list of lines from former stdout output, each as
                    a partial non-processed string.

                ret[2]::=list of lines from former stderr output, each as
                    a partial non-processed string.

        Raises:

            passed through exceptions:

        """
        res = [oldres[0],[],[]]

        if len(oldres) > 1:
            res[1] = _CSPLTL.split(oldres[1])
        if res[1] and res[1][-1] == '':
            res[1].pop()
        if res[1] and res[1][0] == '':
            res[1].pop(0)

        if len(oldres) > 2:
            res[2] = _CSPLTL.split(oldres[2])
        if res[2] and res[2][-1] == '':
            res[2].pop()
        if res[2] and res[2][0] == '':
            res[2].pop(0)
        return res

    def __str__(self):
        """Prints preset call parameters.
        """
        ret = ""
        ret += "\nbufsize      = "+str(self.bufsize)
        ret += "\nconsole      = "+str(self.console)

        if getattr(self, 'debug', None):
            ret += "\ndebug        = "+str(self.debug)

        ret += "\nemptyiserr   = "+str(self.emptyiserr)
        ret += "\nenv          = "+str(self.env)
        ret += "\nerrasexcept  = "+str(self.errasexcept)
        ret += "\nmyexe        = "+str(self.myexe)
        ret += "\nout          = "+str(self.out)
        ret += "\npasserr      = "+str(self.passerr)
        ret += "\nproceed      = "+str(self.proceed)
        ret += "\nraw          = "+str(self.raw)
        ret += "\nrules        = "+str(self.rules)
        ret += "\nuseexit      = "+str(self.useexit)
        ret += "\nusestderr    = "+str(self.usestderr)

        if getattr(self, 'verbose', None):
            ret += "\nverbose      = "+str(self.get('verbose'))

        return ret

    def __repr__(self):
        """Prints the current representation of call parameters for subprocesses.
        """
        ret = "{"
        ret += "'bufsize': "+str(self.bufsize)
        ret += ", 'console': "+str(self.console)
        
        if getattr(self, 'debug', None):
            ret += ", 'debug': "+str(self.get('debug'))
        
        ret += ", 'emptyiserr': "+str(self.emptyiserr)
        ret += ", 'env': "+str(self.env)
        ret += ", 'errasexcept': "+str(self.errasexcept)
        ret += ", 'myexe': "+str(self.myexe.__name__)
        ret += ", 'out': "+str(self.out)
        ret += ", 'passerr': "+str(self.passerr)
        ret += ", 'proceed': "+str(self.proceed)
        ret += ", 'raw': "+str(self.raw)
        ret += ", 'rules': "+str(self.rules)
        ret += ", 'useexit': "+str(self.useexit)
        ret += ", 'usestderr': "+str(self.usestderr)
        
        if getattr(self, 'verbose', None):
            ret += ", 'verbose': "+str(self.get('verbose'))
        ret += "}"
        return ret
