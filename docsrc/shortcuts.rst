API Shortcuts - epyunit
=======================

epyunit - epydoc
^^^^^^^^^^^^^^^^
Epydoc - Javadoc style API documentation for Python.

* `API by Epydoc <epydoc/index.html>`_

epyunit - CLI
^^^^^^^^^^^^^
CLI Wrapper for filtered subprocess calls and streaming of results.
The call interface is provided by two flavours of names, where the executable is the same,
but with different 'shebang lines'.

* Main CLI interface

  * `epyu <epyunit_cli.html#>`_ - Prefered call on Linux, BSD, Unix, and MacOS for use in cimnjunction with the 'shebang line'.

  * `epyu.py <epyunit_cli.html#>`_ - Prefered call on MS-Windows for use in conjunction with PATHEXT.

  * `epyd.py <epyd_cli.html#>`_ - Support utility for remote debug by 'pydevd.py'.

  .

  +---------------------------------+----------------------------------------------------+
  | [docs]                          | [source]                                           |
  +=================================+====================================================+
  | `epyu`_                         | `epyu - CLI call`_                                 |
  +---------------------------------+----------------------------------------------------+
  | `epyu.py`_                      | `epyu.py - CLI call`_                              |
  +---------------------------------+----------------------------------------------------+
  | `epyd.py`_                      | `epyd.py - CLI call`_                              |
  +---------------------------------+----------------------------------------------------+

.. _epyu - CLI call: epyu_src.html#
.. _epyu: epyunit_cli.html#

.. _epyu.py - CLI call: epyu_src.html#
.. _epyu.py: epyunit_cli.html#

.. _epyd.py - CLI call: epyd_src.html#
.. _epyd.py: epyd_cli.html#

epyunit.unittest.subprocess
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Classes derived from unittest for seamless integration of subprocess tests into PyUnit.

* TestExecutable

  +---------------------------------+----------------------------------------------------+
  | [docs]                          | [source]                                           |
  +=================================+====================================================+
  | `TestExecutable`_               | `TestExecutable.__init__`_                         |
  +---------------------------------+----------------------------------------------------+
  | `assertEqual`_                  | `TestExecutable.assertEqual`_                      |
  +---------------------------------+----------------------------------------------------+
  | `assertExists`_                 | `TestExecutable.assertExists`_                     |
  +---------------------------------+----------------------------------------------------+
  | `assertExit`_                   | `TestExecutable.assertExit`_                       |
  +---------------------------------+----------------------------------------------------+
  | `assertStderr`_                 | `TestExecutable.assertStderr`_                     |
  +---------------------------------+----------------------------------------------------+
  | `assertStdout`_                 | `TestExecutable.assertStdout`_                     |
  +---------------------------------+----------------------------------------------------+
  | `callSubprocess`_               | `TestExecutable.callSubprocess`_                   |
  +---------------------------------+----------------------------------------------------+
  | `setkargs`_                     | `TestExecutable.setkargs`_                         |
  +---------------------------------+----------------------------------------------------+
  | `__str__ (0)`_                  | `TestExecutable.__str__`_                          |
  +---------------------------------+----------------------------------------------------+

.. _TestExecutable.__init__: _modules/epyunit/unittest/subprocess.html#TestExecutable.__init__
.. _TestExecutable: spunittest.html#init

.. _TestExecutable.assertEqual: _modules/epyunit/unittest/subprocess.html#TestExecutable.assertEqual
.. _assertEqual: spunittest.html#assertEqual

.. _TestExecutable.assertExists: _modules/epyunit/unittest/subprocess.html#TestExecutable.assertExists
.. _assertExists: spunittest.html#assertExists

.. _TestExecutable.assertExit: _modules/epyunit/unittest/subprocess.html#TestExecutable.assertExit
.. _assertExit: spunittest.html#assertExit

.. _TestExecutable.assertStderr: _modules/epyunit/unittest/subprocess.html#TestExecutable.assertStderr
.. _assertStderr: spunittest.html#assertstderr

.. _TestExecutable.assertStdout: _modules/epyunit/unittest/subprocess.html#TestExecutable.assertStdout52
.. _assertStdout: spunittest.html#assertstdout

.. _TestExecutable.callSubprocess: _modules/epyunit/unittest/subprocess.html#TestExecutable.callSubprocess
.. _callSubprocess: spunittest.html#callsubprocess

.. _TestExecutable.setkargs: _modules/epyunit/unittest/subprocess.html#TestExecutable.setkargs
.. _setkargs: spunittest.html#setkargs

.. _TestExecutable.__str__: _modules/epyunit/unittest/subprocess.html#TestExecutable.__str__
.. _\__str__ (0): spunittest.html#str

epyunit.SubprocUnit
^^^^^^^^^^^^^^^^^^^
Library for subprocesses as units.
Based on 'epyunit.SystemCalls' for execution and fetch of results.
Adds a state machine for decision on fuzzy results based on multiple sources.

* SubprocessUnit

  +---------------------------------+----------------------------------------------------+
  | [docs]                          | [source]                                           |
  +=================================+====================================================+
  | `SubprocessUnit`_               | `SubprocessUnit.__init__`_                         |
  +---------------------------------+----------------------------------------------------+
  | `apply (0)`_                    | `SubprocessUnit.apply`_                            |
  +---------------------------------+----------------------------------------------------+
  | `get_proceed (0)`_              | `SubprocessUnit.get_proceed`_                      |
  +---------------------------------+----------------------------------------------------+
  | `setkargs (1)`_                 | `SubprocessUnit.setkargs`_                         |
  +---------------------------------+----------------------------------------------------+
  | `__repr__ (1)`_                 | `SubprocessUnit.__repr__`_                         |
  +---------------------------------+----------------------------------------------------+
  | `__str__ (1)`_                  | `SubprocessUnit.__str__`_                          |
  +---------------------------------+----------------------------------------------------+

.. _SubprocessUnit.__init__: _modules/epyunit/SubprocUnit.html#SubprocessUnit.__init__
.. _SubprocessUnit: subprocessunit.html#init
.. _SubprocessUnit.apply: _modules/epyunit/SubprocUnit.html#SubprocessUnit.apply
.. _apply (0): subprocessunit.html#apply
.. _SubprocessUnit.setkargs: _modules/epyunit/SubprocUnit.html#SubprocessUnit.setkargs
.. _setkargs (1): subprocessunit.html#setkargs
.. _SubprocessUnit.get_proceed: _modules/epyunit/SubprocUnit.html#SubprocessUnit.get_proceed
.. _get_proceed (0): subprocessunit.html#get-proceed
.. _SubprocessUnit.__repr__: _modules/epyunit/SubprocUnit.html#SubprocessUnit.__repr__
.. _\__repr__ (1): subprocessunit.html#repr
.. _SubprocessUnit.__str__: _modules/epyunit/SubprocUnit.html#SubprocessUnit.__str__
.. _\__str__ (1): subprocessunit.html#str

* SProcUnitRules

  +---------------------------------+----------------------------------------------------+
  | [docs]                          | [source]                                           |
  +=================================+====================================================+
  | `SProcUnitRules`_               | `SProcUnitRules.__init__`_                         |
  +---------------------------------+----------------------------------------------------+
  | `apply (2)`_                    | `SProcUnitRules.apply`_                            |
  +---------------------------------+----------------------------------------------------+
  | `reset`_                        | `SProcUnitRules.reset`_                            |
  +---------------------------------+----------------------------------------------------+
  | `setkargs (2)`_                 | `SProcUnitRules.setkargs`_                         |
  +---------------------------------+----------------------------------------------------+
  | `setrules`_                     | `SProcUnitRules.setrules`_                         |
  +---------------------------------+----------------------------------------------------+

.. _SProcUnitRules.__init__: _modules/epyunit/SubprocUnit.html#SProcUnitRules.__init__
.. _\SProcUnitRules: subprocessunit.html#epyunit.SubprocUnit.SProcUnitRules.__init__

.. _SProcUnitRules.apply: _modules/epyunit/SubprocUnit.html#SProcUnitRules.apply
.. _apply (2): subprocessunit.html#epyunit.SubprocUnit.SProcUnitRules.apply

.. _SProcUnitRules.reset: _modules/epyunit/SubprocUnit.html#SProcUnitRules.reset
.. _reset: subprocessunit.html#epyunit.SubprocUnit.SProcUnitRules.reset

.. _SProcUnitRules.setkargs: _modules/epyunit/SubprocUnit.html#SProcUnitRules.setkargs
.. _setkargs (2): subprocessunit.html#epyunit.SubprocUnit.SProcUnitRules.setkargs

.. _SProcUnitRules.setrules: _modules/epyunit/SubprocUnit.html#SProcUnitRules.setrules
.. _setrules: subprocessunit.html#epyunit.SubprocUnit.SProcUnitRules.setrules


epyunit.myscript
^^^^^^^^^^^^^^^^
Test data generators:

* Data generators written in various languages for integration of heterogenous debugging into unit tests.

  +---------------+-------------------+-------------+------------------------+--------------------------------+
  | [prog-lang]   | debug integration | remote host | [docs]                 | [source]                       |
  +===============+===================+=============+========================+================================+
  | bash          |                   |             | `myscript.sh`_         | `epyunit.myscript.sh`_         |
  +---------------+-------------------+-------------+------------------------+--------------------------------+
  | C             |                   |             |                        |                                |
  +---------------+-------------------+-------------+------------------------+--------------------------------+
  | C++           |                   |             |                        |                                |
  +---------------+-------------------+-------------+------------------------+--------------------------------+
  | Java          |                   |             |                        |                                |
  +---------------+-------------------+-------------+------------------------+--------------------------------+
  | JavaScript    |                   |             |                        |                                |
  +---------------+-------------------+-------------+------------------------+--------------------------------+
  | Perl          |                   |             | `myscript.pl`_         | `epyunit.myscript.pl`_         |
  +---------------+-------------------+-------------+------------------------+--------------------------------+
  | Python        | yes               | yes         | `myscript.py`_         | `epyunit.myscript.py`_         |
  +---------------+-------------------+-------------+------------------------+--------------------------------+
  | Python/SWIG   |                   |             |                        |                                |
  +---------------+-------------------+-------------+------------------------+--------------------------------+
  | Ruby          |                   |             |                        |                                |
  +---------------+-------------------+-------------+------------------------+--------------------------------+

.. _epyunit.myscript.sh: myscript-sh.html#epyunit.myscript-sh
.. _\myscript.sh: myscript-sh.html#epyunit.myscript-sh

.. _epyunit.myscript.py: _modules/epyunit/myscript.html#
.. _\myscript.py: myscript-py.html#epyunit.myscript-py

.. _epyunit.myscript.pl: myscript-pl.html#epyunit.myscript-pl
.. _\myscript.pl: myscript-pl.html#epyunit.myscript-pl


epyunit.SystemCalls
^^^^^^^^^^^^^^^^^^^
Wrapper library for subprocesses and caching of the results.

* SystemCalls

  +---------------------------------+----------------------------------------------------+
  | [docs]                          | [source]                                           |
  +=================================+====================================================+
  | `SystemCalls`_                  | `SystemCalls.__init__`_                            |
  +---------------------------------+----------------------------------------------------+
  | `callit`_                       | `SystemCalls.callit`_                              |
  +---------------------------------+----------------------------------------------------+
  | `displayit`_                    | `SystemCalls.displayit`_                           |
  +---------------------------------+----------------------------------------------------+
  | `get_proceed`_                  | `SystemCalls.get_proceed`_                         |
  +---------------------------------+----------------------------------------------------+
  | `_mode_batch_posix`_            | `SystemCalls._mode_batch_posix`_                   |
  +---------------------------------+----------------------------------------------------+
  | `_mode_batch_win`_              | `SystemCalls._mode_batch_win`_                     |
  +---------------------------------+----------------------------------------------------+
  | `_mode_dialogue`_               | `SystemCalls._mode_dialogue`_                      |
  +---------------------------------+----------------------------------------------------+
  | `setkargs (3)`_                 | `SystemCalls.setkargs`_                            |
  +---------------------------------+----------------------------------------------------+
  | `sub_get_lines`_                | `SystemCalls.sub_get_lines`_                       |
  +---------------------------------+----------------------------------------------------+

.. _SystemCalls.__init__: _modules/epyunit/SystemCalls.html#SystemCalls.__init__
.. _\SystemCalls: systemcalls.html#init

.. _SystemCalls.callit: _modules/epyunit/SystemCalls.html#SystemCalls.callit
.. _callit: systemcalls.html#callit

.. _SystemCalls.displayit: _modules/epyunit/SystemCalls.html#SystemCalls.displayit
.. _displayit: systemcalls.html#displayit

.. _SystemCalls.get_proceed: _modules/epyunit/SystemCalls.html#SystemCalls.get_proceed
.. _get_proceed: systemcalls.html#get-proceed

.. _SystemCalls._mode_batch_posix: _modules/epyunit/SystemCalls.html#SystemCalls._mode_batch_posix
.. _\_mode_batch_posix: systemcalls.html#mode-batch-posix

.. _SystemCalls._mode_batch_win: _modules/epyunit/SystemCalls.html#SystemCalls._mode_batch_win
.. _\_mode_batch_win: systemcalls.html#mode-batch-win

.. _SystemCalls._mode_dialogue: _modules/epyunit/SystemCalls.html#SystemCalls._mode_dialogue
.. _\_mode_dialogue: systemcalls.html#mode-dialogue

.. _SystemCalls.setkargs: _modules/epyunit/SystemCalls.html#SystemCalls.setkargs
.. _setkargs (3): systemcalls.html#setkargs

.. _SystemCalls.sub_get_lines: _modules/epyunit/SystemCalls.html#SystemCalls.sub_get_lines
.. _sub_get_lines: systemcalls.html#sub_get_lines


epyunit.debug
^^^^^^^^^^^^^
Automation of the seamless cross-process debugging of subprocesses by PyDev RemoteDebugServer.

* checkRDbg

  Helper function for initialization and bootstrap of debugging components.

  +------------------------------------+----------------------------------------------------+
  | [docs]                             | [source]                                           |
  +====================================+====================================================+
  | `checkRDbg`_                       | `checkRDbg.checkAndRemoveRDbgOptions`_             |
  +------------------------------------+----------------------------------------------------+

.. _checkRDbg.checkAndRemoveRDbgOptions: _modules/epyunit/debug/checkRDbg.html#checkAndRemoveRDbgOptions
.. _checkRDbg: pydeverdbgchk.html#checkandinitrdbg

* PyDevRDC

  +------------------------------------+----------------------------------------------------+
  | [docs]                             | [source]                                           |
  +====================================+====================================================+
  | `PyDevRDC`_                        | `PyDevRDC.__init__`_                               |
  +------------------------------------+----------------------------------------------------+
  | `scanEclipseForPydevd`_            | `PyDevRDC.scanEclipseForPydevd`_                   |
  +------------------------------------+----------------------------------------------------+
  | `setDebugParams`_                  | `PyDevRDC.setDebugParams`_                         |
  +------------------------------------+----------------------------------------------------+
  | `startDebug`_                      | `PyDevRDC.startDebug`_                             |
  +------------------------------------+----------------------------------------------------+
  | `stopDebug`_                       | `PyDevRDC.stopDebug`_                              |
  +------------------------------------+----------------------------------------------------+
  | `setFork`_                         | `PyDevRDC.setFork`_                                |
  +------------------------------------+----------------------------------------------------+
  | `__str__`_                         | `PyDevRDC.__str__`_                                |
  +------------------------------------+----------------------------------------------------+
  | `__repr__`_                        | `PyDevRDC.__repr__`_                               |
  +------------------------------------+----------------------------------------------------+

.. _PyDevRDC.__init__: _modules/epyunit/debug/pydevrdc.html#PyDevRDC.__init__
.. _\PyDevRDC: pydeverdbg.html#init
.. _PyDevRDC.__str__: _modules/epyunit/debug/pydevrdc.html#PyDevRDC.__str__
.. _\__str__: pydeverdbg.html#str
.. _PyDevRDC.__repr__: _modules/epyunit/debug/pydevrdc.html#PyDevRDC.__repr__
.. _\__repr__: pydeverdbg.html#repr
.. _PyDevRDC.setFork: _modules/epyunit/debug/pydevrdc.html#PyDevRDC.setFork
.. _setFork: pydeverdbg.html#setfork
.. _PyDevRDC.scanEclipseForPydevd: _modules/epyunit/debug/pydevrdc.html#PyDevRDC.scanEclipseForPydevd
.. _scanEclipseForPydevd: pydeverdbg.html#scaneclipseforpydevd
.. _PyDevRDC.setDebugParams: _modules/epyunit/debug/pydevrdc.html#PyDevRDC.setDebugParams
.. _setDebugParams: pydeverdbg.html#setdebugparams
.. _PyDevRDC.startDebug: _modules/epyunit/debug/pydevrdc.html#PyDevRDC.startDebug
.. _startDebug: pydeverdbg.html#startdebug
.. _PyDevRDC.stopDebug: _modules/epyunit/debug/pydevrdc.html#PyDevRDC.stopDebug
.. _stopDebug: pydeverdbg.html#stopdebug

