# -*- coding: utf-8 -*-
"""Initialize PyDevRDC.
Manages command line parameters. Extracts rdbg-options and provides
values for the main module 'epyunit.debug'.

"""
from __future__ import absolute_import

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.14'
__uuid__='9de52399-7752-4633-9fdc-66c87a9200b8'

__docformat__ = "restructuredtext en"

import sys,os
version = '{0}.{1}'.format(*sys.version_info[:2])
if version < '2.7': # pragma: no cover
    raise Exception("Requires Python-2.7.* or higher")

_pderd_inTestMode_suppress_init = False
"""Forces test mode, enables the setting of partially erroneous parameters. 
"""
_dbg_self = False
"""Debugs the debugging.
"""
_dbg_unit = False
"""Debugs units.
"""

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
"""The default values for the peer RemoteDebugServer as defined by PyDev.
"""

def checkAndInitRDbg(**kargs):
    """Checks input options from sys.argv and returns resulting debug parameters.
    The following options are checked and removed from sys.argv, thus has to be
    added by the caller application again  when required for following nested calls:

        --rdbg:

            Enables local debugging by default, provides optionally altered
            connection parameters for the RemoteDebugServer.
        
        --rdbg-forward:

            Defines forwarding of debugging state, either by passing
            the current instance, or by additionally debugging the next level(s)
            of nested subprocesses. 

    Test options and flags:

        --pderd_inTestMode_suppress_init:

            Control initialization of the preconfigured debug stub.
            It is foreseen to be the only instance under normal
            circumstances.

        --pderd_debug_self:

            Enabled debugging messages for debug, this also includes
            the pre-debug initialization of the remote debug server.

        --pderd_unit_self:

            Enabled log messages for unittests.    

    Args:
        callstr: a prepared shell-style call.
        
        **kargs:

            fpname: The file path name of the main file for the current process, default:=callname.

            label: The label identifying the current process, default:=callname.

            noargv: Suppresses argv processing completely for the previous 
                arguments. The testflags are still processed.

            rdbg: Same as '--rdbg', for additional processing see 'noargv'.
        
            rdbgforward: Same as '--rdbg-forward', for additional processing see 'noargv'.

    Returns:
        When successful returns tuple of the following debug parameters.
        
        return/value := ( rdbgthis, rdbg, rdbgfwd, )

            rdbgthis = (True|False): Debugging of current process/thread is enabled.

            rdbg = [host][:port]: Connection parameter of peer RemoteDebugServer
            
            rdbgfwd = <partialprocessed>: Forward debug parameters

                partialprocessed: One of:

                    hop = hopcnt - 1

                    'all'

                    label

    Raises:
    
    """
    global _pderd_inTestMode_suppress_init
    global _dbg_self
    global _dbg_unit
    
    _noarg = False
    _rdbgthis = False
    _rdbg = None
    _rdbgfwd = None

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
            _rdbg = v
            
        elif k == 'rdbgforward':
            _rdbgfwd = v

        elif k == 'noargv':
            _noarg = v
            
        elif k == 'argv':
            _argv = v

        elif k == 'argvclear':
            _argv = v
            _argvclr = v

        else:
            raise("Unknown option:"+str(k))

    if not _lbl:
        _lbl = os.path.basename(sys.argv[0])
    if not _fpname:
        _fpname = os.path.abspath(sys.argv[0])

    # prevents init, for test only
    if '--pderd_inTestMode_suppress_init' in sys.argv:
        _pderd_inTestMode_suppress_init = True
        for px in sys.argv:
            sys.argv.pop(sys.argv.index(px))
    else:
        _pderd_inTestMode_suppress_init = False

    # activates self debug
    if '--pderd_debug_self' in sys.argv:
        _dbg_self = True
        sys.argv.pop(sys.argv.index('--pderd_debug_self'))
    else:
        _dbg_self = False

    # activates self unittests
    if '--pderd_unit_self' in sys.argv:
        _dbg_unit = True
        sys.argv.pop(sys.argv.index('--pderd_unit_self'))
    else:
        _dbg_unit = False
    
    if not _noarg and "--rdbg" in sys.argv:
        _ai = sys.argv.index("--rdbg")
        _a = sys.argv.pop(_ai) #--rdbg
        if _ai < len(sys.argv)-1:
            if os.path.exists(sys.argv[_ai]): # a file path name - final opt without value
                _rdbg = _rdbg_default
            elif sys.argv[_ai][:1] != '-': # opt with value
                _rdbg = sys.argv.pop(_ai) #value
            elif sys.argv[_ai][0] == ':': # opt with port value
                _rdbg = sys.argv.pop(_ai) #value
            else: # assume for now opt without value, may require '--'
                _rdbg = _rdbg_default
        else: # opt without value
            _rdbg = _rdbg_default

    if not _noarg and "--rdbg-forward" in sys.argv:
        _ai = sys.argv.index("--rdbg-forward")
        _a = sys.argv.pop(_ai) #--rdbg
        if _ai < len(sys.argv)-1:
            if os.path.exists(sys.argv[_ai]): # a file path name - final opt without value
                _rdbgfwd = _rdbg_default
            elif sys.argv[_ai][:1] != '-': # opt with value
                _rdbgfwd = sys.argv.pop(_ai) #value
            else: # assume for now opt without value, may require '--'
                _rdbgfwd = _rdbgfwd_default
        else:
            _rdbgfwd = _rdbgfwd_default

    # activates connection to remote debug server
    if _rdbg:
        _rdbgthis = True # here for now active, could be reset when forwarding only, see following

        # forwards debugging state to nested subprocesses
        if _rdbgfwd:
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
                if os.path.abspath(_fpname) == os.path.abspath(sys.argv[0]): 
                    _rdbgthis = True
                else:
                    _rdbgthis = False

            elif type(_rdbgfwd) is str: # label
                if _rdbgfwd == _lbl:
                    _rdbgthis = True

            else:
                _rdbgthis = False

    return (_rdbgthis,_rdbg,_rdbgfwd,)
