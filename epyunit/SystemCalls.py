# -*- coding: utf-8 -*-
"""The module 'epyunit.SystemCalls' provides the controlled execution of subprocesses as units.

The features are foreseen to support easy setups for unit and regression 
tests on complex command line options and their combinations. 
These are in designed to be used in conjunction with
with PyUnit, either within Eclipse and PyDev, or from the command line.

A quick example call is::

  python -c 'from epyunit.SystemCalls import SystemCalls;x=SystemCalls(**{"proceed":"trace"});x.callit("myscript.sh xOK")'

or::

  python -c 'from epyunit.SystemCalls import SystemCalls;x=SystemCalls(**{"proceed":"trace"});x.callit("myscript.py xOK")'

**SECURITY REMARK**: Current version supports for subprocesses the ShellMode only.
For test environments in R&D this - hopefully - is perfectly OK, 
else eventual security issues has to be considered.

"""
from __future__ import absolute_import

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.14'
__uuid__='9de52399-7752-4633-9fdc-66c87a9200b8'

__docformat__ = "restructuredtext en"

import sys,datetime
version = '{0}.{1}'.format(*sys.version_info[:2])
if version < '2.7': # pragma: no cover
    raise Exception("Requires Python-2.7.* or higher")

import subprocess

# output enums
_O_STD = 1 #: output to STDOUT
_O_ERR = 2 #: output to STDERR
_O_STR = 3 #: output to STRING

class SystemCallsException(Exception):
    """Common error within epyunit.SystemCalls. 
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
    """Wraps system calls for subprocesses.
    
    For supported parameters refer to 'epyunit.SystemCalls.setkargs()'.
    
    """
    def __init__(self,**kargs):
        """Prepares the interface for subprocess calls with output cache.
        
        The initial setup includes the preparation of the result 
        cache for the response data from stdout and stderr.

        Args:
            **kargs: Parameters specific for the operations,
                passed through to **setkargs**.

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
        self.myexe = self._mode_batch #: preconfigured call back for actual execution
        self.out = 'pass' #: output format/stream
        self.outtarget = 'stdout' #: output format/stream
        self.passerr = False
        self.proceed = 'doit' #: what to do...
        self.raw = False
        self.useexit = True
        self.usestderr = False
        self.verbose = 0

        self._appname = None 
        self._testid = None 
        self._timestamp = None 
        self._environment = None 

        self.setkargs(**kargs)
        pass

    def callit(self,callstr,**kargs):
        """Executes a prepared callstr by the preset function pointer 'self.myexe'.
        
        Args:
            callstr: a prepared shell-style call.
        
            **kargs: kargs is passed through, for values refer
                to **setkargs**.

                debug: Sets debug for rule data flow.

                env: Passed through.

                proceed: Changes predefined value and
                    dispatches to the subcall.

                raw: Suppress the split of lines for
                    stdout and stderr.

                verbose: Sets verbose for rule data flow.

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
            print str(callstr)
            return [0,[],[]]

        elif proceed=="trace":
            print >>sys.stderr, "TRACE:"+str(callstr)
            ret=self.myexe(callstr,**kargs)

        elif proceed=="doit":
            ret=self.myexe(callstr,**kargs)

        if ret[0] not in (0,5):
            if self.verbose>0:
                print "ret:"+str(ret)+" =>call:"+str(callstr)

        if not _raw and not self.raw:
            ret = self.splitLines(ret)
        return ret

    def displayit(self,ret,**kargs):
        """Displays result list ret in selected format.

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
        """Verifies valid proceed type."""
        if s in ('print','trace', 'doit'):
            return s
        else:
            raise Exception('STATE:ERROR:proceed not supported:'+str(s))
    
    def _mode_batch(self,callstr,**kargs):
        """Internal call reference for processing a batch mode call. 
        
        The IO by stdout/stdin/stderr are redirected. Supports 
        shell-style parameters only.

        Args:
            callstr: a prepared shell-style call.
            
            **kargs:

                env: Current environment.
                    
        Returns:
            When successful returns 'True', else returns either 'False', or
            raises an exception.

        Raises:
            for parameter 'errasexcept': SystemCallsExceptionSubprocessError
            passed through exceptions:
        
        For further information refer to 'console' option of constructor/setkargs.

        """
        if self.emptyiserr and ( not callstr or callstr == ''):
            return [2,'', 'ERROR:MissingCallstr']

        ret=[1,]
        _env = kargs.get('env')
        if not _env:
            self.p=subprocess.Popen(
                    callstr,
                    shell=True,
                    bufsize=self.bufsize,
                    stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    close_fds=True
                    )
        else:
            self.p=subprocess.Popen(
                    callstr,
                    shell=True,
                    bufsize=self.bufsize,
                    stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    close_fds=True,
                    env=_env
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
            #raise SystemCallsExceptionSubprocessError(self.p.returncode,**{'exitmsg':"FROM:"+str(callstr) +"\n"+ str(self.res[1]),'exitval':self.p.returncode,})
            raise SystemCallsExceptionSubprocessError(self.p.returncode,**{'exitmsg':"FROM:"+str(callstr) +"\n",})
        
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

    def _mode_dialogue(self,callstr,**kargs):
        """Internal call reference for processing an interactive dialogue call.
        
        Supports shell-style parameters only.

        For further information refer to 'console' option of constructor/setkargs.

        """
        
        #FIXME: has to be tested
        if self.emptyiserr and ( not callstr or callstr == ''):
            return [2,'', 'ERROR:MissingCallstr']
        
        ret=[0,]
        try:
            self.p=subprocess.check_call(
                callstr,
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

                bufsize: The size of the output buffer for the 
                    called subprocess. Refer to **subprocess.Popen**.
                    Default value is -1.

                console ('cli','dialogue')
                    ffs ('batch','ui','gtk', 'qt')

                    cli: Works in batch mode, particularly the
                        stdin, stdout, and stderr streams are
                        caught into a string buffer by the 
                        calling process via a pipe. The content
                        is passed after termination of the called 
                        sub-process.

                    dialogue: Works without buffered io streams.
                        Thus allows for interaction, but not
                        post-processing.

                    verbose: Verbose.

                debug: Sets debug for rule data flow.

                emptyiserr: Treats passed empty call strings as error.
                    The applied 'subprocess.Popen()' treats them as
                    success, which may cover errors in generated
                    call strings, particularly in loops.

                    default := False
 
                errasexcept: Passes errors as exceptions, transforms the resuls from
                    subprocesses into Exceptions data. Exits the process.

                    default := False

                out: Output for display. Supported types are:
                
                    csv: CSV seperated by ';', with sparse records
                    
                    pass: Pass through STDOUT and STDERR from 
                        subprocess

                    repr: Python 'repr()'
        
                    str: Python 'str()'

                    xml: XML

                passerr: Passes errors from subprocesses transparently 
                    through by stdout, stderr, and exit code. Exits 
                    the process.

                    default := False
 
                proceed ('print','trace', 'doit')
                    print - trace only
                    
                    trace - execute and trace
                    
                    doit  - execute    

                raw: Pass through STDOUT and STDERR.

                rules: Sets the rules object.

                useexit: Use exit code for error detection of
                    subprocess.
                    
                    default := True 

                usestderr: Use 'sys.stderr' output for error 
                    detection of subprocess. When set to 'True',
                    the presence of a string is treated as error
                    condition.
                    
                    default := False

                verbose: Sets verbose for rule data flow.

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
                    self.myexe=self._mode_batch
            elif k=='debug':
                self.debug=v
            elif k=='emptyiserr':
                self.emptyiserr=v
            elif k=='env': # to be evaluated by the caller case by case only
                pass
            elif k=='errasexcept':
                self.errasexcept=v
            elif k=='out':
                self.out = v
                if v in ('csv', 'pass', 'repr', 'str', 'xml', ):
                    self.out = v
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

#             else:
#                 raise Exception('STATE:ERROR:parameter not supported:'+str(k))
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
            res[1] = oldres[1].split('\n')
        if res[1] and res[1][-1] == '':
            res[1].pop()
        if res[1] and res[1][0] == '':
            res[1].pop(0)

        if len(oldres) > 2:
            res[2] = oldres[2].split('\n')
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
        ret += "\nemptyiserr   = "+str(self.emptyiserr)
        ret += "\nerrasexcept  = "+str(self.errasexcept)
        ret += "\nmyexe        = "+str(self.myexe)
        ret += "\npasserr      = "+str(self.passerr)
        ret += "\nproceed      = "+str(self.proceed)
        ret += "\nraw          = "+str(self.raw)
        ret += "\nuseexit      = "+str(self.useexit)
        ret += "\nusestderr    = "+str(self.usestderr)
        return ret

    def __repr__(self):
        """Prints the current representation of call parameters for subprocesses.
        """
        ret = "{"
        ret += "'bufsize': "+str(self.bufsize)
        ret += ", 'console': "+str(self.console)
        ret += ", 'emptyiserr': "+str(self.emptyiserr)
        ret += ", 'errasexcept': "+str(self.errasexcept)
        ret += ", 'myexe': "+str(self.myexe.__name__)
        ret += ", 'passerr': "+str(self.passerr)
        ret += ", 'proceed': "+str(self.proceed)
        ret += ", 'raw': "+str(self.raw)
        ret += ", 'useexit': "+str(self.useexit)
        ret += ", 'usestderr': "+str(self.usestderr)
        ret += "}"
        return ret
