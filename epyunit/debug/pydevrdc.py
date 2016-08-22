# -*- coding: utf-8 -*-
"""Support for the automation of cross-process remote debugging with PyDev and Eclipse.

The module provides helpers for the debugging with the PyDev in the Eclipse IDE.
This includes utilities for the **cross-process debugging** by **Remote-Debugging**.
The PyDevRDC module provides processes started outside the PyDev environment,
as well as processes under control of PyDev.

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
import pysourceinfo

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.14'
__uuid__='9de52399-7752-4633-9fdc-66c87a9200b8'

__docformat__ = "restructuredtext en"

import os,sys
version = '{0}.{1}'.format(*sys.version_info[:2])
if version < '2.7': # pragma: no cover
    raise Exception("Requires Python-2.7.* or higher")

from types import NoneType
import glob
#import termcolor
#import copy

from filesysobjects.FileSysObjects import findRelPathInSearchPath,clearPath,addPathToSearchPath

from epyunit.debug.checkRDbg import _pderd_inTestMode_suppress_init, _dbg_self, _dbg_unit

PYDEVD = None



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

    eclipse_glob = "eclipse/plugins/"+pydevd_glob
    """
    Subpath glob pattern for any eclipse based PyDev installation.
    """

    _clrargs = {'abs':True, 'non-existent':True,'split':True,'redundant':True,'shrink':True,'normpath':True}
    """
    Args for 'filesysobjects.clearPath'
    """

    def __init__(self,**kargs):
        """Create a control stub for a remote debugger.
        
        Search and load 'pydevd' for cross-process 
        remote debugging.
        
        Args:
            **kargs:
                label=<name>: An optional label for identifying the currrent instance.
                    The label could be provided as debugging flag.

                remotedebug: Switches remote debugging support On/Off.
                    Dependent of this parameter an internal 
                    call of startRemoteDebugExt is performed 
                    and a new instance initialized.
                
                rootforscan: Directory path for the module
                    'pydevd.py', else defaults of 
                    'scanEclipseForPydevd'.

                testflags: Flags to force specific behaviour
                    - mostly faulty - in order to test the module
                    itself. So, **do not use** these if you do not
                    know what these actually do. 
                     
                    These partially fail, but provide a sufficient
                    part of the control flow for the aspect of interest.
                     
                        ignorePydevd: Debugging the initial bootstrap
                            of an simulated external process. Ignores 
                            present loaded debug support. For debugging
                            of the debug support.

                        ignorePydevdSysPath: Debugging the initial
                            bootstrap of an simulated external process.
                            Ignores load by current 'sys.path'. For debugging
                            of the debug support.

                        ignorePydevdCallParam: Debugging the initial
                            bootstrap of an simulated external process.
                            Ignores current parameter for load. For debugging 
                            of the debug support.

        Returns:
            Creates a proxy instance.

        Raises:
            passed through exceptions:
        """
        self._itfp = False
        self._itfs = False
        self._itfcp = False
        for k,v in kargs.items():
            if k == 'testflags':
                for tf in v.split(','):
                    if tf == 'ignorePydevd':
                        self._itfp = True
                    elif tf == 'ignorePydevdSysPath':
                        self._itfs = True
                    elif tf == 'ignorePydevdCallParam':
                        self._itfcp = True
            elif k == 'label':
                self.label = v

        # check whether running in pydevd.py
        if not self._itfp and sys.modules.get('pydevd'): # already loaded
            self.runningInPyDevDbg = True
            self.pydevdpath = sys.modules.get('pydevd')
            self.setDebugParams(**kargs)
        else: # has to be loaded
            self.pydevdpath = self.scanEclipseForPydevd(kargs.get('rootforscan'),**kargs)
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
        self.dbgargs = self.dgbargs_default
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

    def scanEclipseForPydevd(self,rootforscan=None, **kargs):    
        """Scans filesystem directory tree of Eclipse for PyDev plugin containing 'pydevd'. 

        Scans for 'pydevd' required for subprocess debugging
        by the Debug-Server of PyDev. See PyDev manual for 
        path reference, the default pattern is:
            ::

                eclipse/plugins/org.python.pydev_x.x.x/pysrc/pydevd.py

        The path is the containment path of the file *pydevd.py* and has to be 
        included in the *sys.path* variable for activation.
        
        The *scanEclipseForPydevd* method performs a search and returns the 
        path in case of a match.
         
        Searches in following priority:
        
            1. call parameter
                
            2. environment PYDEVDSCAN

                Contains either a hook for the pydevd_glob pattern,
                or an FQPN to the appropriate 'pydevd.py'.
            
            3. sys.path
                
            4. <HOME>/eclipse/eclipse
            
                Where the path is a symbolic link to the executable,
                the realpath will be evaluated from the link.

            5. search install directory when installed within the
                'dropins' directory::

                os.path.dirname(__file__)+""

        The first match of containing directory for 'pydevd.py'
        is returned, thus ambiguity in case of multiple occurrences
        has to be avoided.

        Args:
            rootforscan: Start directory for tree-scan, either a
                single, multiple in PATH notation.
    
        **kargs:
            altpat=(<literal>|<glob>): Alternative pattern, varies 'eclipse_glob',
                and 'pydevd_glob'.

            strict: Provided parameter has to match, else error.

                Default is to try all, when supplied params do not
                match default values are checked.

            version=(a,b,c): Provide version to be requested. It is recommended
                to combine this with 'strict'.
    
                version=(a,b,c)
                a := [0-9]+
                b := [0-9]+
                b := [0-9]+
    
        Returns:
            The location of pydevd.py
    
        Raises:
            AttributeError:

        """
        _mlist = [] # list of matches

        _apat = kargs.get('altpat')
        _vers = kargs.get('version')
        _pg = self.pydevd_glob
        if _apat and _vers:
            raise PyDevRDCLoadException("One only supported (version, altpat)=('"+str(_vers)+"', '"+str(_apat)+"')")
        elif _vers:
            _pg = "org.python.pydev_"+_vers[0]+"."+_vers[1]+"."+_vers[2]+"*/pysrc/pydevd.py"
            _apat = "eclipse/plugins/"+_pg
        elif not _apat:
            _apat = self.eclipse_glob

        _st = kargs.get('strict',False)
        
        if rootforscan == NoneType:
            _rfs = []
        elif type(rootforscan) != list:
            _rfs = [rootforscan]
            clearPath(_rfs,**self._clrargs)
        else:
            _rfs = rootforscan[:]
            clearPath(_rfs,**self._clrargs)

        p = None
        
        # 1. call parameter
        if not self._itfcp:
            p = findRelPathInSearchPath(_apat,_rfs)
            if p:
                return p
            elif _rfs and _st:
                return

        # 2. environment PYDEVDSCAN
        if not p:
            try:
                _rfs = os.environ['PYDEVDSCAN']
                clearPath(_rfs,**self._clrargs)
                p = findRelPathInSearchPath(_apat,_rfs)
                if p:
                    return p
                elif _rfs and _st:
                    return
            except:
                pass

        #
        # following are the preset and hard-coded defaults
        #
        
        # 3. search 'pydevd.p' by sys.path
        if not self._itfs and not rootforscan:
            p = findRelPathInSearchPath('pydevd.py',sys.path)
            if p:
                return p

        # 4. <HOME>/eclipse/eclipse
        if not p:
            _r = os.environ['HOME']
            _r += os.sep+'eclipse'+os.sep+'eclipse'
            if os.path.exists(_r):
                if kargs.get('altpat'):
                    _apat = kargs.get('altpat')
                    if _apat.startswith('eclipse/plugins/'):
                        _apat = _apat[7:]
                else:
                    _apat = self.pydevd_glob
                _r = os.path.normpath(os.path.dirname(os.path.realpath(_r))+"/plugins/")

            p = findRelPathInSearchPath(_apat,[_r])
            if p:
                return p

        # 5. search install directory when installed within the 'dropins' directory::
        if not p:
            if os.path.exists(os.path.normpath("../plugins")) and os.path.exists(os.path.normpath("../eclipse")):
                _r = glob.glob(os.path.normpath("../plugins/"+_pg))
            p = findRelPathInSearchPath(_apat,_r)
            if p:
                return p

    def startDebug(self):
        """Starts remote debugging for PyDev.
        """        
        # already loaded
        if self.runningInPyDevDbg:
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
        print >>sys.stderr,"RDBG:init PYDEVD"
    if not PYDEVD or not PyDevRDC._initok:
        PYDEVD=PyDevRDC()
        _pydevd = PYDEVD.scanEclipseForPydevd()
        if _dbg_self:
            print >>sys.stderr,"RDBG:found pydevd.py:"+str(_pydevd)
        if _dbg_unit:
            print >>sys.stderr,"RDBG:found pydevd.py"
        addPathToSearchPath(os.path.dirname(_pydevd),**{'exist':True,'prepend':True,}) 
        import pydevd #@UnresolvedImport
        pass
pass
