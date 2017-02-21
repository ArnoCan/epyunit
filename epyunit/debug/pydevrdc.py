# -*- coding: utf-8 -*-
"""Support for the automation of cross-process remote debugging with PyDev and Eclipse.

The module provides helpers for the debugging with the PyDev in the Eclipse IDE.
This includes utilities for the **cross-process debugging** by **Remote-Debugging**.
The PyDevRDC module provides processes started outside the PyDev environment,
as well as processes under control of PyDev.

In case the module epyunit.debug.checkRDbg is not yet loaded, this is done
and the provided parameters are passed through to the initial call::

    epyunit.debug.checkRDbg.checkAndRemoveRDbgOptions()

See 'http://pydev.org/manual_adv_remote_debugger.html'

The following parameters modify the control flow:

* Module Variables:

    * **epyunit.debug.pydevrdc.PYDEVD**:
        Provides a pre-allocated controller object
        for remote debugging by PyDev as Eclipse plugin.
        Could be extended by custom instances as required.
        Just requires a simple import statement and could
        thereafter be controlled by parameters.

* Environment Variables:

    * **PYDEVDSCAN**:
        The start directory for search on 'pydevd.py'.
        If not set, the default is::

          px = $HOME/eclipse/eclipse
          px = os.path.abspath(px)
          px = os.path.realname(px)
          px = os.path.dirname(px)
          px = os.path.normpath(px)


"""
from __future__ import absolute_import

#FIXME: test-defaults
try:
    from tests.libs.checkRDbg import rdbg_root
except:
    pass

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.2.7'
__uuid__='9de52399-7752-4633-9fdc-66c87a9200b8'

__docformat__ = "restructuredtext en"

import os,sys
version = '{0}.{1}'.format(*sys.version_info[:2])
if not version in ('2.6', '2.7',): # pragma: no cover
    raise Exception("Requires Python-2.6.* or higher")

from types import NoneType
import glob

from filesysobjects.FileSysObjects import findRelPathInSearchPath,clearPath,addPathToSearchPath,getHome
from epyunit.debug.checkRDbg import _pderd_inTestMode_suppress_init, _dbg_self, _dbg_unit,\
    _verbose
from epyunit.debug.checkRDbg import _rdbgroot,_rdbgroot_default, _rdbgsub_default,_rdbgenv
import epyunit.debug.checkRDbg

PYDEVD = None

#
# check whether epyunit.debug.checkRDbg has been called before, if not do it now
#
if not epyunit.debug.checkRDbg._rdbgoptions:
    epyunit.debug.checkRDbg.checkAndRemoveRDbgOptions()

class PyDevRDCException(Exception):
    pass

class PyDevRDCLoadException(PyDevRDCException):
    """Failed load of 'pydevd.py'.
    """
    def __init__(self):
        ret="\n"
        ret+="\n"
        ret+="Cannot load module 'pydevd':\n"
        ret+="\n"
        ret+="   Set PYTHONPATH, or use more call parameters.\n"
        ret+="   See PyDev manual for path reference:\n"
        ret+="     'eclipse/plugins/org.python.pydev_x.x.x/pysrc/pydevd.py'\n"
        ret+="\n"
        super(PyDevRDCException,self).__init__(ret)

class PyDevRDCServerException(PyDevRDCException):
    """Debug server of PyDev is not running - cannot be reached.
    """
    def __init__(self):
        ret="\n"
        ret+="\n"
        ret+="Cannot connect to debug server, start it using Eclipse menu:\n"
        ret+="\n"
        ret+="   In Debug-Perspective: 'PyDev -> Start Debug Server'\n"
        ret+="\n"
        super(PyDevRDCException,self).__init__(ret)

class PyDevRDC(object):
    """Provides automation for remote debugging of external Python process with PyDev.

    This particularly provides a prepared environment for
    cross-process debugging by 'pydevd'.
    """

    _initok=False
    """Controls whether to be initialized."""

    defaultargs={}

    dgbargs_default = {
        'host': 'localhost', # host(None)
        'stdoutToServer': True, # stdoutToServer(False)
        'stderrToServer': True, # stderrToServer(False)
        'port': 5678, # port(5678)
        'suspend': False, # suspend(True) :
        'trace_only_current_thread': True, # trace_only_current_thread(False)
        'overwrite_prev_trace': False, # 'ignore' == overwrite_prev_trace(False)
        'patch_multiprocessing': True, # patch_multiprocessing(False),
    }
    """
    Final default configuration arguments for a debug controller, see pydevd.settrace.
    """

    pydevd_glob = "org.python.pydev_[0-9]*.[0-9]*.[0-9]*/pysrc/pydevd.py"
    """
    Subpath glob pattern of PyDev plugin.
    """

    eclipse_glob = _rdbgroot
    """
    Subpath glob pattern for any eclipse based PyDev installation.
    """

    def __init__(self,**kargs):
        """Create a control stub for a remote debugger.

        Search and load 'pydevd' for cross-process remote debugging.

        Args:
            **kargs:

                debug:

                    Debug RDBG itself, developer output.

                label=<name>:

                    An optional label for identifying the currrent instance.
                    The label could be provided as debugging flag.

                remotedebug:

                    Switches remote debugging support On/Off. Dependent of
                    this parameter an internal call of startRemoteDebugExt
                    is performed and a new instance initialized.

                rootforscan:

                    Directory path for the module 'pydevd.py', else defaults
                    of 'scanEclipseForPydevd'.

                fpname:

                    The file path name of the main file for the current
                    process, default:=callname.

                label:

                    The label identifying the current process, default:=callname.

                noargv:

                    Suppresses argv processing completely for the previous
                    arguments. The testflags are still processed.

                rdbg:

                    Same as '--rdbg', for additional processing see 'noargv'.

                rdbgsrv:

                    Same as '--rdbg'srv, for additional processing see 'noargv'.

                rdbgforward:

                    Same as '--rdbg-forward', for additional processing
                    see 'noargv'.

                rdbgroot:

                    Same as '--rdbg-root', for additional processing see 'noargv'.

                rdbgsub:

                    Same as '--rdbg-sub', for additional processing see 'noargv'.


                testflags:

                    Flags to force specific behaviour - mostly faulty -
                    in order to test the module itself. So, **do not use**
                    these if you do not know what these actually do.

                    These partially fail, but provide a sufficient
                    part of the control flow for the aspect of interest.

                        ignorePydevd:

                            Debugging the initial bootstrap of an simulated
                            external process. Ignores present loaded debug
                            support. For debugging of the debug support.

                        ignorePydevdSysPath:

                            Debugging the initial bootstrap of an simulated
                            external process. Ignores load by current 'sys.path'.
                            For debugging of the debug support.

                        ignorePydevdCallParam:

                            Debugging the initial bootstrap of an simulated
                            external process. Ignores current parameter for
                            load. For debugging of the debug support.

                verbose:

                    Display data for user parameters.

        Returns:
            Creates a proxy instance.

        Raises:
            passed through exceptions:
        """
        self._verbose = False
        self._dbg_self= False
        if sys.modules.get('epyunit.debug.checkRDbg'):
            self._verbose = epyunit.debug.checkRDbg._verbose
            self._dbg_self = epyunit.debug.checkRDbg._dbg_self
        if self._verbose or self._dbg_self:
            print >>sys.stderr, "RDBG:"+__name__+":options from checkRDbg:rdbgoptions = "+str(epyunit.debug.checkRDbg._rdbgoptions)

        self._itfp = False
        self._itfs = False
        self._itfcp = False

        # set initial defaults
        self.dbgargs = self.dgbargs_default

        for k,v in kargs.items():
            if k == 'testflags':
                try:
                    if epyunit.debug.checkRDbg._testflags: # CLI interaction has priority
                        continue
                except:
                    pass
                for tf in v.split(','):
                    if tf == 'ignorePydevd':
                        self._itfp = True
                    elif tf == 'ignorePydevdSysPath':
                        self._itfs = True
                    elif tf == 'ignorePydevdCallParam':
                        self._itfcp = True
            elif k == 'label':
                self.label = v
            elif k == 'verbose':
                self._verbose = v
            elif k == 'debug':
                self._dbg_self= v

        #
        # fetch CLI values from epyunit.debug.checkRDbg
        try:
            if sys.modules.get('epyunit.debug.checkRDbg'):
                if self._verbose:
                    print >>sys.stderr, "RDBG:"+__name__+":options from checkRDbg:rdbgoptions = "+str(epyunit.debug.checkRDbg._rdbgoptions)

                if epyunit.debug.checkRDbg._rdbgoptions[1]: # _rdbgsrv
                    h,p = epyunit.debug.checkRDbg._rdbgoptions[1].split(':')
                    if h:
                        self.dbgargs['host'] = h
                    if p:
                        self.dbgargs['port'] = int(p)

                if epyunit.debug.checkRDbg._rdbgoptions[3]: # _rdbgroot
                    self.eclipse_glob = epyunit.debug.checkRDbg._rdbgoptions[3]

                if epyunit.debug.checkRDbg._rdbgoptions[4]: # _rdbgsub
                    self.pydevd_glob = epyunit.debug.checkRDbg._rdbgoptions[4]

                if epyunit.debug.checkRDbg._testflags: # CLI interaction has priority
                    for tf in epyunit.debug.checkRDbg._testflags:
                        if tf == 'ignorePydevd':
                            self._itfp = True
                        elif tf == 'ignorePydevdSysPath':
                            self._itfs = True
                        elif tf == 'ignorePydevdCallParam':
                            self._itfcp = True

        except:
            pass


        # check whether running in pydevd.py
        if not self._itfp and sys.modules.get('pydevd'): # already loaded
            if self._dbg_self or self._verbose:
                print "RDBG:"+__name__+":use pydevd.py"

            self.runningInPyDevDbg = True
            self.pydevdpath = sys.modules.get('pydevd')
            self.setDebugParams(**kargs)

        else: # has to be loaded, do the initial first-time work
            if self._dbg_self or self._verbose:
                print "RDBG:"+__name__+":load pydevd.py"

#            self.pydevdpath = self.scanEclipseForPydevd(kargs.get('rootforscan'),**kargs)
            self.pydevdpath = epyunit.debug.checkRDbg.scanEclipseForPydevd(kargs.get('rootforscan'),**kargs)

            if self.pydevdpath:
                addPathToSearchPath(os.path.dirname(self.pydevdpath),**{'exist':True,'prepend':True,})
                try:
                    import pydevd #@UnresolvedImport #@UnusedImport
                except Exception as e:
                    raise PyDevRDCException("Load of 'pydevd' failed:"+str(os.path.dirname(self.pydevdpath))+"\n"+str(e))
                self.runningInPyDevDbg = True
            else:
                self.runningInPyDevDbg = False

            self.setDebugParams(**kargs)

        # starts remote debug immediately
        self.remotedebug = kargs.get("remotedebug",False)
        if self.remotedebug:
            self.startDebug()
        self._initok=True

        if self._dbg_self:
            print >>sys.stderr, "RDBG:"+__name__+":dbgargs = "+str(self.dbgargs)
            print >>sys.stderr, "RDBG:"+__name__+":eclipse_glob = "+str(self.eclipse_glob)
            print >>sys.stderr, "RDBG:"+__name__+":pydevd_glob = "+str(self.pydevd_glob)

    def setDebugParams(self,**kargs):
        """Sets the parameters for debug.

        Args:
            **kargs:
                host:

                    Hostname where the debug server is running.

                    From **pdevd.py**:
                    The user may specify another host, if the debug server
                    is not in the same machine (default is the local host).

                ignore:

                    When set to False success is mandatory, else
                    an exception it raised.
                    Set this to True/default, when in production
                    systems.

                port:

                    Port the debug server is listening on.
                    From **pdevd.py**:
                    Specifies which port to use for communicating with the
                    server (note that the server must be started in the
                    same port).
                    **Note**: currently it's hard-coded at 5678
                    in the client

                pydevdpath:

                    Required path pointing to directory for
                    source of pydevd in PyDev subdirectory tree.

                remotedebug:

                    Switches remote debugging support On/Off.

                stderrToServer:

                    Sets whether stderr is directed to debugserver.
                    From **pdevd.py**:
                    When this is true, the stderr is passed to the debug server
                    so that they are printed in its console and not in this
                    process console.

                stdoutToServer:

                    Sets whether stdout is directed to debugserver.
                    From **pdevd.py**:
                    When this is true, the stdout is passed to the debug server.

                suspend:

                    If set to True, stops immediately after settrace() call,
                    else at next valid break-condition.
                    From **pdevd.py**:
                    Whether a breakpoint should be emulated as soon as
                    this function is called.

                trace_only_current_thread:

                    From **pdevd.py**:
                    Determines if only the current thread will be traced or all
                    future threads will also have the tracing enabled.

        Returns:
            The location of pydevd.py

        Raises:
            AttributeError:

        """
        for k,v in kargs.iteritems():
            if k=='pydevdpath':
                pydevdpath=v
            elif k=='ignore':
                ignore=v
            elif k=='remotedebug':
                remotedebug=v

            elif k=='host':
                self.dbgargs['host'] = v
            elif k=='stdoutToServer':
                self.dbgargs['stdoutToServer'] = v
            elif k=='stderrToServer':
                self.dbgargs['stderrToServer'] = v
            elif k=='port':
                self.dbgargs['port'] = v
            elif k=='suspend':
                self.dbgargs['suspend'] = v
            elif k=='trace_only_current_thread':
                self.dbgargs['trace_only_current_thread'] = v
            elif k=='overwrite_prev_trace':
                self.dbgargs['overwrite_prev_trace'] = v
            elif k=='patch_multiprocessing':
                self.dbgargs['patch_multiprocessing'] = v

    def startDebug(self,**kargs):
        """Starts remote debugging for PyDev.
        """
        for k,v in kargs.items():
            if k == 'debug':
                self._dbg_self = v
            elif k == 'verbose':
                self._dbg_self = v

        if self._dbg_self or self._verbose:
            print >>sys.stderr,"RDBG:debug starting "

        # already loaded
        if self.runningInPyDevDbg:
            if self._dbg_self or self._verbose:
                print >>sys.stderr,"RDBG:dbgargs="+str(self.dbgargs)
            try:
                pydevd.settrace(
                    host=self.dbgargs['host'],
                    port=self.dbgargs['port'],
                    stdoutToServer=self.dbgargs['stdoutToServer'],
                    stderrToServer=self.dbgargs['stderrToServer'],
                    suspend=self.dbgargs['suspend'],
                    trace_only_current_thread=self.dbgargs['trace_only_current_thread']
                    )
                #OK-ref: pydevd.settrace(host=None,port=5678,stdoutToServer=False,stderrToServer=False,suspend=False,trace_only_current_thread=True)
            except Exception as e:
                raise PyDevRDCException(e)
        else:
            raise PyDevRDCException("ERROR:Requires init:self.runningInPyDevDbg="+str(self.runningInPyDevDbg))
        if _dbg_self or _dbg_unit:
            print >>sys.stderr,"RDBG:debug started"

    def stopDebug(self):
        """Stops remote debugging for PyDev.
        """
        try:
            if self.runningInPyDevDbg:
                pydevd.stopdebug()
        except Exception as e:
            raise PyDevRDCException()

    def setFork(self):
        """Prepares debugging after fork.
        """
        if self.runningInPyDevDbg:
            pydevd.settrace_forked()
        pass

    def __str__(self):
        """Prints current remote debug parameters.
        """
        ret  = ""
        ret += "\nPyDevRDC.host                      = "+str(self.host)
        ret += "\nPyDevRDC.stdoutToServer            = "+str(self.stdoutToServer)
        ret += "\nPyDevRDC.stderrToServer            = "+str(self.stderrToServer)
        ret += "\nPyDevRDC.port                      = "+str(self.port)
        ret += "\nPyDevRDC.suspend                   = "+str(self.suspend)
        ret += "\nPyDevRDC.trace_only_current_thread = "+str(self.trace_only_current_thread)
        ret += "\nPyDevRDC.overwrite_prev_trace      = "+str(self.overwrite_prev_trace)
        ret += "\nPyDevRDC.patch_multiprocessing     = "+str(self.patch_multiprocessing)
        return ret

    def __repr__(self):
        """Prints the current representation of remote debug parameters.
        """
        ret = "{"
        ret += "'host': "+str(self.host)
        ret += ", 'stdoutToServer': "+str(self.stdoutToServer)
        ret += ", 'stderrToServer': "+str(self.stderrToServer)
        ret += ", 'port': "+str(self.port)
        ret += ", 'suspend': "+str(self.suspend)
        ret += ", 'trace_only_current_thread': "+str(self.trace_only_current_thread)
        ret += ", 'overwrite_prev_trace': "+str(self.overwrite_prev_trace)
        ret += ", 'patch_multiprocessing': "+str(self.patch_multiprocessing)
        ret += "}"
        return ret


if not _pderd_inTestMode_suppress_init:
    if _dbg_self or _dbg_unit:
        print >>sys.stderr,"RDBG:init:pydevrdc"
    if not PYDEVD or not PyDevRDC._initok:
        if _dbg_self or _verbose:
            print >>sys.stderr, "RDBG:create:epyunit.pydevrdc.PYDEVD"
        PYDEVD=PyDevRDC()
        _pydevd = epyunit.debug.checkRDbg.scanEclipseForPydevd()
        
        if not _pydevd:
            if _dbg_self or _dbg_unit:
                print >>sys.stderr,"RDBG:Missing, pydevd.py not found"
            else:
                print >>sys.stderr,"RDBG:Remote debug deactive, missing pydevd.py - not found"
        else:
            if _dbg_self:
                print >>sys.stderr,"RDBG:found pydevd.py:"+str(_pydevd)
            if _dbg_unit:
                print >>sys.stderr,"RDBG:found pydevd.py"
            addPathToSearchPath(os.path.dirname(_pydevd),**{'exist':True,'prepend':True,})
            import pydevd #@UnresolvedImport
