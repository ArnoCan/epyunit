# -*- coding: utf -*-
"""Provides a slim interface for the initialization and extraction of command line parameters for pydevrdc.

Extracts rdbg-options and provides values for the main module 'epyunit.debug.pydevrdc'.
"""
from __future__ import absolute_import

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.2.7'
__uuid__='9de52399-7752-4633-9fdc-66c87a9200b8'

__docformat__ = "restructuredtext en"

import sys,os,re
from types import NoneType
import glob

from filesysobjects.FileSysObjects import findRelPathInSearchPath,clearPath,addPathToSearchPath,getHome

version = '{0}.{1}'.format(*sys.version_info[:2])
if not version in ('2.6', '2.7',): # pragma: no cover
    raise Exception("Requires Python-2.6.* or higher")


_pderd_inTestMode_suppress_init = False
"""Forces test mode, enables the setting of partially erroneous parameters."""

_testflags = None
"""Testflags"""

_testflags_valid = ['ignorePydevd','ignorePydevdSysPath','ignorePydevdCallParam',]
"""Valid values for testflags"""


_dbg_self = False
"""Debugs the debugging."""

_dbg_unit = False
"""Debugs units."""

_rdbgroot_default = ''
"""Platform specific Default root for eclipse."""
#
# Initialize for current platform
#
if sys.platform.startswith('linux'): # Linux
    _rdbgroot_default = os.environ['HOME']+os.sep+'eclipse'
elif 'win32' in sys.platform : # Windows
    _rdbgroot_default = "C:\eclipse"
elif sys.platform in ('cygwin',): # Cygwin
    _rdbgroot_default = "/cygdrive/c/eclipse"
elif sys.platform in ('darwin'): # Mac-OS
    _rdbgroot_default = os.environ['HOME']+os.sep+'eclipse'
else: # Else: Unix, BSD
    _rdbgroot_default = os.environ['HOME']+os.sep+'eclipse'

_rdbgsub_default = "org.python.pydev_[0-9]*.[0-9]*.[0-9]*/pysrc/pydevd.py"
"""Default eclipse sub path."""

_rdbgfwd_default = 0
"""Control of forwarding the debugging enabled state.
Possible values are:

    hopcnt: The nested subprocesses to be debugged.

        hopcnt >=0 : The number of nested subprocess
            hops to be debugged.

        hopcnt <0 : The number of nested subprocess
            hops NOT to be debugged.

    'all': Debug all nested levels of subprocesses.

    label: Activate remote debug for the process with the previously
        assigned label only.

    label = [label-lst]: List of labels.

"""

_rdbg_default = "localhost:5678"
"""The default values for the peer RemoteDebugServer as defined by PyDev."""

rdbgoptions = None
"""The cached options from sys.argv by checkAndRemoveRDbgOptions."""

#
# The current values for external module access
#
_rdbgthis = False
_rdbgsrv = _rdbg_default
_rdbgfwd  = _rdbgfwd_default
_rdbgroot = _rdbgroot_default
_rdbgsub  = _rdbgsub_default
_rdbgoptions = (_rdbgthis,_rdbgsrv,_rdbgfwd,_rdbgroot,_rdbgsub,)

_verbose = False
#
# static re
#
_reRDSAddr = re.compile(ur"([^:]*):([^:]*)")
#
# RemoteDebugServer address
if "win32" in sys.platform:
    _reHostOnly  = re.compile(ur"""^[^:\\\\]+$""")
else:
    _reHostOnly  = re.compile(ur"""^[^:"""+os.sep+"""]+$""")
_rePortOnly  = re.compile(ur"""^:[0-9]+$""")
_reHostPort  = re.compile(ur"""^([^:]+):([0-9]+)$""")

_rdbgenv = False
"""Force or prohibit the read of environment variables, by default used in priority order when present."""

#
# buffer for options evaluation
_clibuf = []

class checkAndRemoveRDbgOptionsException(Exception):
    pass

def checkAndRemoveRDbgOptions(argv=None,**kargs):
    """Checks input options from sys.argv and returns the tuple of resulting
    debug parameters. The options are removed from sys.argv by default.

    The options are kept as provided, or when missing filled with default values.
    The final resolution of the values like file system globs is performed within
    the PyDevRDC class.

    The following options are checked and removed from sys.argv, thus by default
    has to be added by the caller application again when required for following
    nested calls:

        --rdbg [[host]:[port]]:

            Enables debugging of subprocesses via RemoteDebugServer. By default
            for local instance 'localhost:5679', provides optionally altered
            connection parameters:

                host: Host address, DNS or IP.

                port: Port number.

        --rdbg-env:

            Forces or disables the use of specific environment variables.
                ::

                    RDBGROOT, RDBGSUB

                * True: Forces the use of present variables

                * False: disables use

                * default: Applied in normal order when scanning the filesystem

        --rdbg-forward [<depth>]:

            Defines forwarding of debugging state, either by passing
            the current instance, or by additionally debugging the next level(s)
            of nested subprocesses. The value of <depth> is one of:

                #hopcnt:  Number of levels for nested subprocesses.

                'all': All nested levels.

                label: The subprocesses with matching label only.

            The design of passing options into nested calls is considered as
            insertion of the forwarded options before the first option of the next
            level caller:
              ::

                epyu --rdbg --rdbg-froward=2 nextlevel -a --bxy ....

            This results in:
              ::

                nextlevel --rdbg --rdbg-froward=2 -a --bxy ....

            In case of optional sub-parameters the temination option '--'
            could be applied:
              ::

                epyu --rdbg --rdbg-froward=2 nextlevel -- arguments

            results in:
              ::

                nextlevel --rdbg --rdbg-froward=2  -- arguments

            The current version requiresthis to be proceeded by the application,
            refer to 'epyu..py'.

        --rdbg-root (<rootforscan>|<FQDN>|<path-glob>):

            Defines the initial root path for scan, the following defaults
            are scanned initially when this parameter is provided without
            a value.

                Linux, BSD, and Unix:
                    ::

                        $HOME/eclipse

                Mac-OS:
                    ::

                        $HOME/eclipse

                Windows:
                    ::

                        C:\eclipse

                Cygwin:
                    ::

                        /cygdrive/c/eclipse

            When the value is not found, the additional defaults
            are scanned as provided by 'PyDevRDC.scanEclipseForPydevd'.

            Each root is searched by the the following order of
            sub-pattern matching.
                ::

                    0. plugins/<rdbgsub>

                    1. dropins/<rdbgsub>

                    2. dropins/*/plugins/<rdbgsub>

            For details refer to 'pydevrdc.scanEclipseForPydevd'
            `[see] <pydeverdbg.html#scaneclipseforpydevd>`_.

        --rdbg-sub (<literal>|<path-glob>):

            Defines the initial subpath within the Eclipse installation.
            When not present, the extended defaults are scanned, for
            further details refer to 'PyDevRDC.scanEclipseForPydevd':
                ::

                    pydevd_subpath = "org.python.pydev_[0-9]*.[0-9]*.[0-9]*/pysrc/pydevd.py"

    Test options and flags:

        The test options are foreseen for the test and debug of 'epyunit.debug'
        itself.

        --pderd_inTestMode_suppress_init:

            Control initialization of the preconfigured debug stub.
            It is foreseen to be the only instance under normal
            circumstances.

        --pderd_debug_self:

            Enabled debugging messages for debug, this also includes
            the pre-debug initialization of the remote debug server.

        --pderd_unit_self:

            Enabled log messages for unittests.

        --pderd_testflags:

            Sets specific testflags, valid values for testflags are:

            ignorePydevd: ignores loaded pydevd.py, for search test only

            ignorePydevdSysPath: ignores sys.path, for search test only

            ignorePydevdCallParam: ignores call parameters

    Environment variables:

        The provided environment variables are read out, when no related
        option is available. In case both are not provided, the hard-coded
        defaults are applied. The read of environment variables could be
        supressed in general by the option 'noenv'/'--no-env'.

            RDBGROOT => --rdbg-root

            RDBGSUB => --rdbg-sub

    Args:

        argv: Alternative argv, default:=sys.argv

        **kargs:

            debug:

                Same as '--debug', developer output.

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

                Same as '--rdbg-forward', for additional processing see 'noargv'.

            rdbgroot:

                Same as '--rdbg-root', for additional processing see 'noargv'.

            rdbgsub:

                Same as '--rdbg-sub', for additional processing see 'noargv'.

            verbose:

                Same as '--verbose', user output.

    Returns:
        When successful returns tuple of the following debug parameters. The
        options are removed from 'sys.argv'.

        return/value := ( rdbgthis, rdbg, rdbgfwd, rdbgroot, rdbgsub, )

            rdbgthis = (True|False): Debugging of current process/thread is enabled.

            rdbg = [host][:port]: Connection parameter of peer RemoteDebugServer

            rdbgfwd = <partialprocessed>: Forward debug parameters

                partialprocessed: One of:

                    hop = hopcnt - 1

                    'all'

                    label

            rdbgroot = <rootforscan>: Base for search, when None the defaults apply.

            rdbgsub = <eclipse-subpath>: Subpath within Eclipse.

    Raises:

    """
    
#     print "4TEST:A:"+str(argv)
#     print "4TEST:K:"+str(kargs)
    
    
    global _pderd_inTestMode_suppress_init
    global _dbg_self
    global _dbg_unit
    global _verbose

    global _rdbgoptions
    global _rdbgenv
    global _rdbgthis
    global _rdbgsrv
    global _rdbgfwd
    global _rdbgroot
    global _rdbgsub

    global _testflags

    _noarg = False
    _rdbg = False

    _verbose = False

    _argv = False
    _argvclr = False

    _lbl = None
    _fpname = None

    for k,v in kargs.items():
        if k == 'label':
            _lbl = v

        elif k == 'fpname':
            _fpname = v

        elif k == 'rdbg':
            _rdbg = True
            _rdbgthis = True
            _rdbgsrv = v

        elif k == 'rdbgsrv':
            _rdbg = True
            _rdbgsrv = v

        elif k == 'rdbgforward':
            _rdbg = True
            _rdbgfwd = v
            _rdbgthis = True

        elif k == 'rdbgroot':
            _rdbgroot = v

        elif k == 'rdbgsub':
            _rdbgsub = v

        elif k == 'rdbgenv':
            _rdbgenv = v

        elif k == 'noargv':
            _noarg = v

        elif k == 'argv':
            _argv = v

        elif k == 'argvclear':
            _argv = v
            _argvclr = v

        elif k == 'verbose':
            _verbose = v

        elif k == 'debug':
            _dbg_self = v

        else:
            raise Exception("Unknown option:"+str(k))

    # prep argv for extraction of rdbg options
    if argv and type(argv) in (str,unicode,):
        _ty = argv.split()
    elif argv == None:
        _ty = sys.argv
    else:
        _ty = argv

    # label of current process
    if not _lbl:
        _lbl = os.path.basename(_ty[0])
    if not _fpname:
        _fpname = os.path.abspath(_ty[0])

    # prevents init, for test only
    if '--pderd_inTestMode_suppress_init' in _ty:
        _pderd_inTestMode_suppress_init = True
        for px in _ty:
            _ty.pop(_ty.index(px))
    else:
        _pderd_inTestMode_suppress_init = False

    # activates self debug
    if '--pderd_debug_self' in _ty:
        _dbg_self = True
        _ty.pop(_ty.index('--pderd_debug_self'))
    else:
        _dbg_self = False

    # activates self unittests
    if '--pderd_unit_self' in _ty:
        _dbg_unit = True
        _ty.pop(_ty.index('--pderd_unit_self'))
    else:
        _dbg_unit = False

    global _clibuf
    import argparse
    class RDBGSaction(argparse.Action):
        """Connection parameters for the RemoteDebugServer - --rdbg
        """
        def __init__(self, option_strings, dest, nargs=None, **kwargs):
            super(RDBGSaction, self).__init__(option_strings, dest, nargs, **kwargs)

        def __call__(self, parser, namespace, values, option_string=None):
            _ix=-1
            _eq = False
            try:
                _ix = namespace._argv.index(option_string)
            except:
                try:
                    _ix = namespace._argv.index(option_string+"="+values)
                    _eq = True
                except:
                    pass
            if _ix>0:
                _ai = namespace._argv.pop(_ix)
            if not values:
                #print '%r %r %r' % (namespace, _rdbg_default, option_string)
                setattr(namespace, self.dest, _rdbg_default)
                return
            elif _reHostOnly.match(values):
                #print '%r %r %r' % (namespace, values+":5678", option_string)
                setattr(namespace, self.dest, values+":5678")
            elif _rePortOnly.match(values):
                #print '%r %r %r' % (namespace, "localhost"+values, option_string)
                setattr(namespace, self.dest, "localhost"+values)
            elif _reHostPort.match(values):
                #print '%r %r %r' % (namespace, values, option_string)
                setattr(namespace, self.dest, values)
            else: # no valid argument
                #print '%r %r %r' % (namespace, _rdbg_default, option_string)
                setattr(namespace, self.dest, _rdbg_default)
                return

    class FWDaction(argparse.Action):
        """Enabling nested subprocesses by forwarding - --rdbg-forward
        """
        def __call__(self, parser, namespace, values, option_string=None):
            _ix=-1
            _eq = False
            try:
                _ix = namespace._argv.index(option_string)
            except:
                try:
                    _ix = namespace._argv.index(option_string+"="+values)
                    _eq = True
                except:
                    pass
            if _ix>0:
                _ai = namespace._argv.pop(_ix)

            if not values: # default
                #print '%r %r %r' % (namespace, _rdbgfwd_default, option_string)
                setattr(namespace, self.dest, _rdbgfwd_default)
                return

            elif type(values) is int and values > 0: # integer
                #print '%r %r %r' % (namespace, values-1, option_string)
                setattr(namespace, self.dest, (values))

            elif values.isdigit() and int(values) > 0: # integer
                #print '%r %r %r' % (namespace, values-1, option_string)
                setattr(namespace, self.dest, int(values))

            elif values == 'all': # all levels
                #print '%r %r %r' % (namespace, values, option_string)
                setattr(namespace, self.dest, values)

    class ROOTaction(argparse.Action):
        """Set the root for scan - --rdbg-root
        """
        def __call__(self, parser, namespace, values, option_string=None):
            _ix=-1
            _eq = False
            try:
                _ix = namespace._argv.index(option_string)
            except:
                try:
                    _ix = namespace._argv.index(option_string+"="+values)
                    _eq = True
                except:
                    pass
            if _ix>0:
                _ai = namespace._argv.pop(_ix)

            if not values:
                #print '%r %r %r' % (namespace, _rdbgroot_default, option_string)
                setattr(namespace, self.dest, _rdbgroot_default)
                return

            else:
                #print '%r %r %r' % (namespace, values, option_string)
                setattr(namespace, self.dest, values)

    class SUBaction(argparse.Action):
        """Set the subdirectory in 'plugins' for scan - --rdbg-sub
        """
        def __call__(self, parser, namespace, values, option_string=None):
            _ix=-1
            _eq = False
            try:
                _ix = namespace._argv.index(option_string)
            except:
                try:
                    _ix = namespace._argv.index(option_string+"="+values)
                    _eq = True
                except:
                    pass
            if _ix>0:
                _ai = namespace._argv.pop(_ix)

            if not values:
                #print '%r %r %r' % (namespace, _rdbgsub_default, option_string)
                setattr(namespace, self.dest, _rdbgsub_default)
            else:
                #print '%r %r %r' % (namespace, values, option_string)
                setattr(namespace, self.dest, values)

    class ENVaction(argparse.Action):
        """Enable/Disable the environment variables RDBGROOT and RDBGSUB - --rdbg-env
        """
        def __call__(self, parser, namespace, values, option_string=None):
            _ix=-1
            _eq = False
            try:
                _ix = namespace._argv.index(option_string)
            except:
                try:
                    _ix = namespace._argv.index(option_string+"="+values)
                    _eq = True
                except:
                    pass
            if _ix>0:
                _ai = namespace._argv.pop(_ix)

            if type(values) is NoneType:
                #print '%r %r %r' % (namespace, _rdbgsub_default, option_string)
                setattr(namespace, self.dest, True)
            else:
                #print '%r %r %r' % (namespace, values, option_string)
                if values.lower() in ('on','true','1',True,1,):
                    setattr(namespace, self.dest, True)
                elif values.lower() in ('off','false','0',False,0,):
                    setattr(namespace, self.dest, False)
                else:
                    raise checkAndRemoveRDbgOptionsException("Unknown value:"+str(values))

    class DBGaction(argparse.Action):
        """Set the debugging of RDBG itself for scan - --rdbg-self
        """
        def __call__(self, parser, namespace, values, option_string=None):
            _ix=-1
            _eq = False
            try:
                _ix = namespace._argv.index(option_string)
            except:
                try:
                    _ix = namespace._argv.index(option_string+"="+values)
                    _eq = True
                except:
                    pass
            if _ix>0:
                _ai = namespace._argv.pop(_ix)

            if type(values) is NoneType:
                #print '%r %r %r' % (namespace, _rdbgsub_default, option_string)
                setattr(namespace, self.dest, True)
            else:
                #print '%r %r %r' % (namespace, values, option_string)
                setattr(namespace, self.dest, values)

    class TFLAGaction(argparse.Action):
        """Set for the debugging of RDBG itself some testflags --pderd_testflags
        For valid values see '_testflags_valid'
        """
        def __call__(self, parser, namespace, values, option_string=None):
            _ix=-1
            _eq = False
            try:
                _ix = namespace._argv.index(option_string)
            except:
                try:
                    _ix = namespace._argv.index(option_string+"="+values)
                    _eq = True
                except:
                    pass
            if _ix>0:
                _ai = namespace._argv.pop(_ix)

            if type(values) is NoneType:
                #print '%r %r %r' % (namespace, _rdbgsub_default, option_string)
                setattr(namespace, self.dest, [_testflags_valid[0]])
            else:
                #print '%r %r %r' % (namespace, values, option_string)
                _tfv = []
                for tf in values.split(','):
                    if tf in _testflags_valid:
                        _tfv.append(tf)
                        pass
                    else:
                        raise checkAndRemoveRDbgOptionsException("Unknown value "+str(option_string)+"="+str(values))
                _testflags = _tfv
                setattr(namespace, self.dest, _testflags)

    class Sx(object):
        def __init__(self):
            self._argv = _ty
            self.rdbgenv = _rdbgenv

    _myspace = Sx()
    parser = argparse.ArgumentParser()
    parser.add_argument('--rdbg',nargs='?',action=RDBGSaction,default=None)
    parser.add_argument('--rdbg-forward',nargs='?',action=FWDaction,default=None)
    parser.add_argument('--rdbg-root',nargs='?',action=ROOTaction,default=None)
    parser.add_argument('--rdbg-sub',nargs='?',action=SUBaction,default=None)
    parser.add_argument('--rdbg-env',nargs='?',action=ENVaction,default=None)
    parser.add_argument('--rdbg-self',nargs='?',action=DBGaction,default=None)

    parser.add_argument('--pderd_testflags',nargs='?',action=TFLAGaction,default=None)

    _clibuf = parser.parse_known_args(_ty,namespace=_myspace)
    if type(_clibuf[0].rdbg_env) is NoneType:
        _rdbgenv = _clibuf[0].rdbg_env

    if _clibuf[0].rdbg or _clibuf[0].rdbg_forward:
        _rdbg = True
    else:
        if _clibuf[0].rdbg_root:
            raise checkAndRemoveRDbgOptionsException("Missing activation option '--rdbg', provided:'--rdbg-root'")
        if _clibuf[0].rdbg_sub:
            raise checkAndRemoveRDbgOptionsException("Missing activation option '--rdbg', provided:'--rdbg-sub'")


    _rdbgenv = _clibuf[0].rdbg_env

    if _clibuf[0].rdbg:
        _rdbg = True
        _rdbgsrv = _clibuf[0].rdbg

        import socket
        hn = socket.gethostbyaddr(socket.gethostname())

        if _clibuf[0].rdbg.startswith('localhost') or _clibuf[0].rdbg.startswith('127.0.0.1'):
            _rdbgthis = True

        elif _clibuf[0].rdbg == hn[0] or _clibuf[0].rdbg in hn[1] or _clibuf[0].rdbg in hn[2]:
            _rdbgthis = True

    if _rdbg: # modify only valid options
        if type(_clibuf[0].rdbg_forward) != NoneType:
            _rdbgfwd  = _clibuf[0].rdbg_forward
        if type(_clibuf[0].rdbg_root) != NoneType:
            _rdbgroot = _clibuf[0].rdbg_root
        if type(_clibuf[0].rdbg_sub) != NoneType:
            _rdbgsub  = _clibuf[0].rdbg_sub
        if type(_clibuf[0].rdbg_self) != NoneType:
            _dbg_self  = _clibuf[0].rdbg_self

        if type(_clibuf[0].pderd_testflags) != NoneType:
            _testflags  = _clibuf[0].pderd_testflags

    if _dbg_self:
        print >>sys.stderr, "RDBG:"+__name__+":_rdbgenv="+str(_rdbgenv)
        print >>sys.stderr, "RDBG:"+__name__+":_rdbgthis="+str(_rdbgthis)
        print >>sys.stderr, "RDBG:"+__name__+":_rdbgsrv="+str(_rdbgsrv)
        print >>sys.stderr, "RDBG:"+__name__+":_rdbgfwd="+str(_rdbgfwd)
        print >>sys.stderr, "RDBG:"+__name__+":_rdbgroot="+str(_rdbgroot)
        print >>sys.stderr, "RDBG:"+__name__+":_rdbgsub="+str(_rdbgsub)

        print >>sys.stderr, "RDBG:"+__name__+":_testflags="+str(_testflags)

    _ty = _clibuf[1]

    # forwards debugging state to nested subprocesses
    if _rdbgfwd and not _rdbgthis:
        if _rdbgfwd.lower() == 'all': # all
            _rdbgthis = True

        elif type(_rdbgfwd) == int and _rdbgfwd: # hopcount
            if _rdbgfwd >= 0: # debug the first:  [0:hopcnt]
                _rdbgfwd -= 1
                if _rdbgfwd >= 0:
                    _rdbgthis = True
                else:
                    _rdbgthis = False

            else: # debug from hopcnt on: [hopcnt:]
                _rdbgfwd += 1
                if _rdbgfwd < 0:
                    _rdbgthis = False
                else:
                    _rdbgthis = True

        elif type(_fpname) is str and os.path.exists(_fpname): # fpname
            if os.path.abspath(_fpname) == os.path.abspath(_ty[0]):
                _rdbgthis = True
            else:
                _rdbgthis = False

        elif type(_rdbgfwd) is str: # label
            if _rdbgfwd == _lbl:
                _rdbgthis = True

    #
    # set now missing as defaults
    #
    if _rdbgthis and not _rdbgsrv:
        _rdbgsrv = _rdbg_default

    if _rdbgenv: # if set, force when present
        if os.environ.get('RDBGROOT'):
            _rdbgroot = os.environ['RDBGROOT']
        if os.environ.get('RDBGSUB'):
            _rdbgsub = os.environ['RDBGSUB']

    try:
        while True:
            _ix = sys.argv.index('--rdbg')
            _ai = sys.argv.pop(_ix)
    except:
        pass

    try:
        while True:
            _ix = sys.argv.index('--rdbg')
            _ai = sys.argv.pop(_ix)
    except:
        pass

    try:
        while True:
            _ix = sys.argv.index('--rdbg-forward')
            _ai = sys.argv.pop(_ix)
    except:
        pass

    try:
        while True:
            _ix = sys.argv.index('--rdbg-root')
            _ai = sys.argv.pop(_ix)
    except:
        pass
    try:
        while True:
            _ix = sys.argv.index('--rdbg-sub')
            _ai = sys.argv.pop(_ix)
    except:
        pass
    try:
        while True:
            _ix = sys.argv.index('--env')
            _ai = sys.argv.pop(_ix)
    except:
        pass
    try:
        while True:
            _ix = sys.argv.index('--self')
            _ai = sys.argv.pop(_ix)
    except:
        pass

    _rdbgoptions = (_rdbgthis,_rdbgsrv,_rdbgfwd,_rdbgroot,_rdbgsub,)

    if _verbose or _dbg_self:
        print >>sys.stderr, "RDBG:"+__name__+":_rdbgoptions="+str(_rdbgoptions)

    return _rdbgoptions

def checkRDbg(argv=None):
    """Checks presence of '--rdbg' option.

    Args:
        argv:

            Alternative argv, default:=sys.argv.

    Returns:

        When present True, else False.

    Raises:

    """
    if argv == NoneType:
        return '--rdbg' in sys.argv
    return '--rdbg' in argv

def getDefaults(res=None):
    """Returns the current defaults.

    Args:
        res:

            Result, the type of 'res' defines the return type.
            The default when 'None' is tuple.

    Returns:

        Returns the collection of default. The following options are
        available:

            res == None: (default)

                result is a new created tuple:

                res := (
                )

            res in (tuple, list,):

                see default, container type as provided.

            res == dict:

                res := {

                }

            res is epyunit.Namespace

                Similar to argparse.Namespace, foreseen to be used also
                as predefined default input for 'epyunit.debug.checkRDbg'.

    """
    pass
#     if argv == NoneType:
#         return '--rdbg' in sys.argv
#     return '--rdbg' in argv

def setDefaults(res=None):
    """Sets defaults.

    """
    global _rdbgthis
    global _rdbgsrv
    global _rdbgfwd
    global _rdbgroot
    global _rdbgsub
    global _rdbgoptions

    global _rdbgthis_default
    global _rdbgsrv_default
    global _rdbgfwd_default
    global _rdbgroot_default
    global _rdbgsub_default

    _rdbgthis = False
    _rdbgsrv = _rdbg_default
    _rdbgfwd  = _rdbgfwd_default
    _rdbgroot = _rdbgroot_default
    _rdbgsub  = _rdbgsub_default
    _rdbgoptions = (_rdbgthis,_rdbgsrv,_rdbgfwd,_rdbgroot,_rdbgsub,)

    return True

class RDBGScanPydevdException(Exception):
    pass

_clrargs = {'abs':True, 'non-existent':True,'split':True,'redundant':True,'shrink':True,'normpath':True}
"""
Args for 'filesysobjects.clearPath'
"""

def scanEclipseForPydevd(rootforscan=None, **kargs):
    """Scans filesystem directory tree of Eclipse for PyDev plugin containing 'pydevd'.

    Scans for 'pydevd' required for subprocess debugging
    by the Debug-Server of PyDev. See PyDev manual for
    path reference, the default pattern for 'marketplace' installation is:
        ::

            eclipse/plugins/org.python.pydev_x.x.x/pysrc/pydevd.py

    in case of drop-in installation
        ::

            eclipse/dropins/<pydev-dropin-name>/plugins/org.python.pydev_x.x.x/pysrc/pydevd.py

    The matching versions could be varied by glob-expressions.

    The provided parameters match as follows:
        ::

            rdbgroot := /path/to/eclipse
            rdbgsub  := org.python.pydev_x.x.x/pysrc/pydevd.py

    The glue-hook depends on the type of installation and is determined
    dynamically:
        ::

            dropin-install       := dropins/<pydev-dropin-name>/plugins
            market-place-install :=  plugins

    Basically any path could be used, in particular a rdbgsub directory
    containing a subset for 'pydevd.py' on a remote machine as stated
    by the PyDev project for remote debugging of server processes. The
    filesystem resolution is performed on a local filesystem only, but
    could be performed by command line start of the headless process
    on the remote machine too.

    The path is the containment path of the file *pydevd.py* and has to be
    included in the *sys.path* variable for activation.

    The *scanEclipseForPydevd* method performs a search and returns the
    absolute path in case of a match.

    The search for the root directory into the Eclipse package installation
    is performed in the following order and priority:

        1. **parameters**

           Consume call/command line parameters, ENV, and hard/coded.

           Parameter mix by environment variables as present:
           For the actual main control of environment variables
           refer to epyunit.checkRDbg.checkAndRemoveRDbgOptions.
            ::

               (rdbgroot or RDBGROOT) + ( rdbgsub or RDBGSUB )

            Contains the value for the option '--rdbg-root',
            either literal or as a 'glob' pattern.
            The following priorities are applied:

                1. CLI call option
                2. API call option
                3. RDBGROOT/RDBGSUB + missing from
                4. Code defaults

        2. **sys.path**

            Each separate path is tried with the sub-path pattern,
            first match wins.

        3. **PATH - which eclipse**

            Each separate path is tried with the sub-path pattern,
            first match wins.

        4. **<HOME>/eclipse/eclipse**

            A convention of the author, where the the path is
            a symbolic link to the executable.
            When present, the realpath is evaluated from the link.

        5. **search install directory - dropins**

            When 'ePyUnit' itself is installed as a drop-in within eclipse,
            the search is performed within the current Eclipse release
            only::

               os.path.dirname(__file__) + rdbgsub

            For example::

               eclipse/dropins/epyunit

    The first match of containing directory for 'pydevd.py'
    is returned, thus ambiguity in case of multiple occurrences
    has to be avoided.

    The pattern resolution into the PyDev dir is performed by the steps:
        ::

            0. <eclipse-root>/plugins/<rdbgsub>

            1. <eclipse-root>/dropins/<rdbgsub>

            2. <eclipse-root>/dropins/*/plugins/<rdbgsub>

    Args:
        rootforscan: Start directory for tree-scan, either a
            single, multiple in PATH notation. Each path points
            to an Eclipse installation directory.

    **kargs:
        altpat=(<literal>|<glob>): Alternative pattern, varies 'eclipse_glob',
            and 'pydevd_glob'.

        strict: Provided parameter has to match, else error.

            Default is to try all, when supplied params do not
            match default values are checked.

        version=(a,b,c): Provide version to be requested. It is recommended
            to combine this with 'strict'.

            The parameters 'altpat' and 'version' are EXOR.

            version=(a,b,c)
            a := [0-9]+
            b := [0-9]+
            b := [0-9]+

    Returns:
        The location of pydevd.py

    Raises:
        AttributeError:

    """
    pydevd_glob = _rdbgoptions[4]
    _itfp = False
    _itfs = False
    _itfcp = False

    if _testflags: # CLI interaction has priority
        for tf in _testflags:
            if tf == 'ignorePydevd':
                _itfp = True
            elif tf == 'ignorePydevdSysPath':
                _itfs = True
            elif tf == 'ignorePydevdCallParam':
                _itfcp = True   
 
    _mlist = [] # list of matches

    _apat = kargs.get('altpat')
    _vers = kargs.get('version')
    _pg = pydevd_glob

    def _matchsub(_apat,_rfs):
        # almost literal
        p = findRelPathInSearchPath(_apat,_rfs)
        if p: # a match trial
            return p

        # plugins
        p = findRelPathInSearchPath("plugins"+os.path.sep+_apat,_rfs)
        if p: # a match trial
            return p

        # dropins
        p = findRelPathInSearchPath("dropins"+os.path.sep+"*"+os.path.sep+"plugins"+os.path.sep+_apat,_rfs)
        if p: # a match trial
            return p

    # 0. fetch call parameters which also reflect the resulting command line parameters
    if _apat and _vers:
        raise RDBGScanPydevdException("One only supported (version, altpat)=('"+str(_vers)+"', '"+str(_apat)+"')")
    elif _vers:
        _apat  = "org.python.pydev_"+_vers[0]+"."+_vers[1]+"."+_vers[2]+"*/pysrc/pydevd.py"
    elif not _apat:
        if pydevd_glob:
            _apat = pydevd_glob
        else:
            _apat = _rdbgsub_default

    if not _apat:
        raise RDBGScanPydevdException("Cannot evaluate rdbgsub-pattern")

    _st = kargs.get('strict',False)

    if type(rootforscan) == NoneType:
        _rfs = [_rdbgroot]
    elif type(rootforscan) != list:
        _rfs = [rootforscan]
        clearPath(_rfs,**_clrargs)
    else:
        _rfs = rootforscan[:]
        clearPath(_rfs,**_clrargs)

    if not _rfs:
        _rfs = [ _rdbgroot_default ]
    if not _rfs:
        raise RDBGScanPydevdException("Cannot evaluate rdbgroot for scan")

    p = None

    # 1. call parameter
    if not _itfcp:
        p = _matchsub(_apat,_rfs)
        if p:
            return p
        if _rfs and _st: # has to match immediately when STRICT is choosen
            return

    # 2. environment RDBGROOT and/or RDBGSUB
    if not p:
        try:
            if _rdbgenv:
                _r = os.environ['RDBGROOT']
                if not _r:
                    _r = _rfs
                else:
                    _r = [_r,]

                _s = os.environ['RDBGSUB']
                if not _s:
                    _s = _apat

                clearPath(_r,**_clrargs)
                p = _matchsub(_s,_r)
                if p:
                    return p
                elif _r and _s: # has to match immediately when STRICT is choosen
                    return
            else:
                _r = _rfs
                _s = _apat

        except:
            pass

    #
    # following are the preset and hard-coded defaults
    #

    # 3. search 'pydevd.p' by sys.path
    if not _itfs and not rootforscan:
        p = _matchsub('pydevd.py',sys.path)
        if p:
            return p

    # 4. search pattern by sys.path
    if not _itfs and not rootforscan:
        p = _matchsub(_apat,sys.path)
        if p:
            return p

    # 5. search pattern by PATH
    if not _itfs and not rootforscan:
        p = _matchsub(_apat,os.environ.get('PATH',None))
        if p:
            return p

    # 6. <HOME>/eclipse/eclipse
    if not p:
        _r = getHome()
        _r += os.sep+'eclipse'+os.sep+'eclipse'
        if os.path.exists(_r):
            if kargs.get('altpat'):
                _apat = kargs.get('altpat')
                if _apat.startswith('eclipse/plugins/'):
                    _apat = _apat[7:]
            else:
                _apat = pydevd_glob
            _r = os.path.normpath(os.path.dirname(os.path.realpath(_r))+"/plugins/")

        p = _matchsub(_apat,[_r])
        if p:
            return p

    # 7. search install directory when installed within the 'dropins' directory
    if not p:
        if os.path.exists(os.path.normpath("../plugins")) and os.path.exists(os.path.normpath("../eclipse")):
            _r = glob.glob(os.path.normpath("../plugins/"+_pg))
        p = _matchsub(_apat,_r)
        if p:
            return p

