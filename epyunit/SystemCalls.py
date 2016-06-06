# -*- coding: utf-8 -*-
"""The module 'epyunit.SystemCalls' provides the execution of subprocesses.

The features are foreseen to support easy setups for unit and regression 
tests on complex command line options and their combinations. 
These are in particular designed to be used in conjunction with
with PyUnit, either within Eclipse and PyDev, or from the command line.

A quick example call is::

  python -c 'from epyunit.SystemCalls import SystemCalls;x=SystemCalls();x.callit("myscript.sh xOK")'

**REMARK**: Current version supports for subprocesses the ShellMode only.
For test environments in R&D this - hopefully - is perfectly OK,
else eventual security issues has to be considered.

"""
from __future__ import absolute_import

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__='9de52399-7752-4633-9fdc-66c87a9200b8'

__docformat__ = "restructuredtext en"

import sys
version = '{0}.{1}'.format(*sys.version_info[:2])
if version < '2.7': # pragma: no cover
    raise Exception("Requires Python-2.7.* or higher")

import subprocess

class SystemCallsException(Exception):
    pass

class SystemCalls(object):
    """Wraps system calls for subprocesses.
    
    For supported parameters refer to 'epyunit.SystemCalls.set_kargs()'.
    
    """
    def __init__(self,**kargs):
        """Prepares the caller interface for subprocesses.
        
        The initial setup also includes the preparation of the result 
        cache for the response data from stdout and stderr.

        Args:
            **kargs: Parameter specific for the operation,
                Passed to set_kargs.

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
        self.first=True
        self.verbose = 0
        self.proceed = 'doit'
        self.raw = False
        self.console = 'cli'
        self.bufsize = 16384
        #self.bufsize=-1
        self.myexe = self._callit

        self.set_kargs(**kargs)
        pass
    
    def set_kargs(self,**kargs):
        """Sets provided parameters.
        
        Applicable for the initial call of self.__init__(), 
        and later modification.
        
        Args:
            **kargs: Parameter specific for the operation,
                proceed ('print','trace', 'doit')
                    print - trace only
                    
                    trace - execute and trace
                    
                    doit  - execute    
                
                console ('cli','dialogue')
                    ffs ('batch','ui','gtk', 'qt')
                
                    cli
                        Works in batch mode, particularly the
                        stdin, stdout, and stderr streams are
                        caught into a string buffer by the 
                        calling process via a pipe. The content
                        is passed after termination of the called 
                        sub-process.
                    
                    dialogue
                        Works without buffered io streams.
                        Thus allows for interaction, but not
                        post-processing.
                    
                    verbose: Verbose.
                
                raw: Pass through STDOUT and STDERR.
                
                bufsize
                    The size of the output buffer for the called subprocess.
                    Refer to **subprocess.Popen**.
                    Default value is -1.


        Returns:
            When successful returns 'True', else returns either 'False', or
            raises an exception.
            Success is the complete addition only, thus one failure returns
            False.

        Raises:
            passed through exceptions:
        """
        for k,v in kargs.iteritems():
            if k=='proceed':
                self.proceed=self.get_proceed(v)
            elif k=='raw':
                self.raw=True
            elif k=='bufsize':
                self.bufsize=int(v)
            elif k=='console':
                self.console=v
                if v == 'cli':
                    self.myexe=self._callit
                if v == 'dialogue':
                    self.myexe=self._calldialogue
                elif v=='batch':
                    raise Exception('STATE:ERROR:console not supported:'+str(v))
                elif v in ('ui','gtk', 'qt'):
                    pass
                else:
                    self.myexe=self._callit

            elif k=='env': # to be evaluated by the caller case by case only
                pass
            else:
                raise Exception('STATE:ERROR:parameter not supported:'+str(k))
        pass

    def get_proceed(self,s):
        """Verifies valid proceed type."""
        if s in ('print','trace', 'doit'):
            return s
        else:
            raise Exception('STATE:ERROR:proceed not supported:'+str(s))
    
    def _callitdialogue(self,callstr,**kargs):
        """Internal call reference for processing an interactive dialogue call.
        
        Supports shell-style parameters only.

        For further information refer to 'console' option of constructor.

        """
        
        #FIXME: has to be tested
        
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

    def _callit(self,callstr,**kargs):
        """Internal call reference for processing a batch mode call. 
        
        The IO by stdout/stdin/stderr are redirected. Supports 
        shell-style parameters only.

        For further information refer to 'console' option of constructor.

        """
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

        self.stdin=self.p.stdin
        self.stdout=self.p.stdout
        self.stderr=self.p.stderr
        self.res=self.p.communicate()
        self.p.poll()
        ret[0]=self.p.returncode
        ret.extend(self.res)
        return ret

    def callit(self,callstr,**kargs):
        """Executes a prepared callstr as shell call.
        
        Args:
            callstr: a prepared shell-style call.
        
            **kargs:
                'proceed':
                    Changes predefined value and
                    dispatches to the subcall.
                    kargs is passed through,
                    for values refer to set_kargs().
                'raw':
                    Suppress the split of lines for
                    stdout and stderr.

                'env': Passed through.

        Returns:
            Result of call, the format is:
            
                ret[0]::=exit value
                ret[1]::=output as non-processed string.
                ret[2]::=error output as non-processed string.


            *REMARK*
                When errors occur in buffered mode the
                output from the called process is possibly
                not completely cached. In that case
                switch to 'dialogue' mode in order to get an 
                unbuffered console display.

        Raises:
            passed through exceptions:
        """
        proceed = self.proceed
        _raw = False
        for k,v in kargs.iteritems():
            if k=='proceed':
                proceed=self.get_proceed(v)
            elif k=='raw':
                _raw=True

        self.set_kargs(**kargs)
               
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

    def splitLines(self,oldres):
        """Converts the raw string fields of a return value into line arrays.
        
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

