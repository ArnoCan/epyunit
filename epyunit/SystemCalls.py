# -*- coding: utf-8 -*-
"""The module 'epyunit.SystemCalls' provides the controlled execution of subprocesses as units.

The features are foreseen to support easy setups for unit and regression 
tests on complex command line options and their combinations. 
These are in designed to be used in conjunction with
with PyUnit, either within Eclipse and PyDev, or from the command line.

A quick example call is::

  python -c 'from epyunit.SystemCalls import SystemCalls;x=SystemCalls(**{"proceed":"trace"});x.callit("myscript.sh xOK")'

**SECURITY REMARK**: Current version supports for subprocesses the ShellMode only.
For test environments in R&D this - hopefully - is perfectly OK,
else eventual security issues has to be considered.

"""
from __future__ import absolute_import

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.10'
__uuid__='9de52399-7752-4633-9fdc-66c87a9200b8'

__docformat__ = "restructuredtext en"

import sys,datetime
version = '{0}.{1}'.format(*sys.version_info[:2])
if version < '2.7': # pragma: no cover
    raise Exception("Requires Python-2.7.* or higher")

import subprocess

class SystemCallsException(Exception):
    """Common error within epyunit.SystemCalls. 
    """
    pass

class SystemCallsExceptionSubprocessError(SystemCallsException):
    """Error from subprocess. 
    """
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
        self.console = 'cli' # console type for output
        self.bufsize = 16384 # size of cache for output received from subprocess 
        #self.bufsize=-1
        self.emptyiserr = False # the subprocess call for an empty string is 'success', 
                                # thus this has to be checked independently for eventually erroneously missing call string
        self.errasexcept = False # raises in case of errors an exception
        self.myexe = self._mode_batch # preconfigured call back for actual execution
        self.out = 'pass' # output format/stream
        self.passerr = False
        self.proceed = 'doit' # what to do...
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

                out: Output for display, valid:
                    
                    csv   : CSV with sparse records
                    
                    pass  : pass through STDOUT and STDERR from 
                            subprocess

                    repr  : Python 'repr()'
                    
                    str   : Python 'str()'
                    
                    xml   : XML
                    
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

                out: Output for display, valid:
                    
                    csv   : CSV with sparse records
                    
                    pass  : pass through STDOUT and STDERR from subprocess

                    repr  : Python 'repr()'
                    
                    str   : Python 'str()'
                    
                    xml   : XML
                
                default:=self.out

        Returns:
            When successful returns 'True', else returns either 'False', or
            raises an exception.

        Raises:
            passed through exceptions:
        
        """
        _out = kargs.get('out',self.out)
 
        if _out == "pass": # pass through STDOUT and STDERR from subprocess
            if ret[1]:
                if type(ret[1]) == list:
                    sys.stdout.write("\n".join(ret[1]))
                else:
                    sys.stdout.write(ret[1])
            if ret[2]:
                if type(ret[2]) == list:
                    sys.stderr.write("\n".join(ret[2]))
                else:
                    sys.stderr.write(ret[2])
    
        elif _out == "repr": # Python 'repr()'
            print repr(ret)
        
        elif _out == "str": # Python 'str()'
            print str(ret)
    
        elif _out == "xml": # XML
            print """<?xml version="1.0" encoding="UTF-8"?>"""
    
            # take timestamp        
            _dn = datetime.datetime.now()
            _date=str(_dn.year)+'-'+str(_dn.month)+'-'+str(_dn.day)
            _time=str(_dn.hour)+':'+str(_dn.minute)+':'+str(_dn.second)
            _head="<test-result id="+str(self._testid)
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
    
            print str(_head)
    
            # exit code
            print   "    <exit-code>"+str(ret[0])+"</exit-code>"
            
            # STDOUT
            print   "    <stdout>"
            lx = 0
            for l in ret[1]:
                print   "        <line cnt="+str(lx)+">"+str(l)+"</line>"
                lx += 1
            print   "    </stdout>"
            
            # STDERR
            print   "    <stderr>"
            lx = 0
            for l in ret[2]:
                print   "        <line cnt="+str(lx)+">"+str(l)+"</line>"
                lx += 1
            print   "    </stderr>"
    
            print """</test-result>"""
    
        elif _out == "csv": # CSV with sparse records
    
            _head = "testid"
            if self._appname:
                _head +=  ";appname"
            if self._timestamp:
                _head += ";date;time"
            if self._environment:
                _head += ";host;user;os;osver;dist;distver"
            _head += ";exitcode;stdout-line;stdout;stderr-line;stderr"
    
            print str(_head)
            
            # take timestamp        
            _dn = datetime.datetime.now()
            _date=str(_dn.year)+'-'+str(_dn.month)+'-'+str(_dn.day)
            _time=str(_dn.hour)+':'+str(_dn.minute)+':'+str(_dn.second)
    
            _lxtot=0
            
            # STDOUT
            lx = 0
            for l in ret[1]:    
                _rec = str(self._testid)
                if self._appname:
                    _rec +=  ";"+str(self._appname)
                if self._timestamp:
                    _rec += ";"+str(_date)+";"+str(_time)
                if self._environment:
                    _rec += ";"+str(self._host)+";"+str(self._user)+";"+str(self._os)+";"+str(self._osver)+";"+str(self._dist)+";"+str(self._distver)
                _rec += ";"+str(ret[0])+";"+str(_lxtot)+";"+str(lx)+";"+str(l)+";;"
                
                print str(_rec)
                lx += 1
                _lxtot +=1
            
            # STDERR
            lx = 0
            for l in ret[2]:
                _rec = str(self._testid)
                if self._appname:
                    _rec +=  ";"+str(self._appname)
                if self._timestamp:
                    _rec += ";"+str(_date)+";"+str(_time)
                if self._environment:
                    _rec += ";"+str(self._host)+";"+str(self._user)+";"+str(self._os)+";"+str(self._osver)+";"+str(self._dist)+";"+str(self._distver)
                _rec += ";"+str(ret[0])+";"+str(_lxtot)+";;;"+str(lx)+";"+str(l)
                
                print str(_rec)
                lx += 1
                _lxtot +=1

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
            passed through exceptions:
        
        For further information refer to 'console' option of constructor/setkargs.

        """
        if self.emptyiserr and ( not callstr or callstr == ''):
            return [1,'', 'ERROR:MissingCallstr']

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
        if self.errasexcept or self.passerr: 
            if self.useexit and self.usestderr:
                if self.p.returncode or self.res[2]:
                    _errcond = True
            elif self.useexit and self.p.returncode:
                _errcond = True
            elif self.usestderr and self.res[2]:
                _errcond = True

        if _errcond and self.errasexcept: # transforms errors from subprocesses into Exceptions
            if self.res[0]:
                print self.res[0]
            raise SystemCallsExceptionSubprocessError(str(callstr) +"\n"+ str(self.res[1]))
        elif _errcond and self.passerr: # passes errors from subprocesses simply through as error exit
            if self.res[0]:
                print self.res[0]
            print >>sys.stderr, str(callstr) +"\n"+ str(self.res[1])
            sys.exit(self.p.returncode)
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
            return [1,'', 'ERROR:MissingCallstr']
        
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
                    detection of subprocess.
                    
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
        ret += "\nSystemCalls.bufsize      = "+str(self.bufsize)
        ret += "\nSystemCalls.console      = "+str(self.console)
        ret += "\nSystemCalls.emptyiserr   = "+str(self.emptyiserr)
        ret += "\nSystemCalls.errasexcept  = "+str(self.errasexcept)
        ret += "\nSystemCalls.myexe        = "+str(self.myexe)
        ret += "\nSystemCalls.passerr      = "+str(self.passerr)
        ret += "\nSystemCalls.proceed      = "+str(self.proceed)
        ret += "\nSystemCalls.raw          = "+str(self.raw)
        ret += "\nSystemCalls.useexit      = "+str(self.useexit)
        ret += "\nSystemCalls.usestderr    = "+str(self.usestderr)
        return ret

