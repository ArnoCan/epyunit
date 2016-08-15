API Shortcuts - epyunit
=======================

epyunit - epydoc
^^^^^^^^^^^^^^^^
Epydoc - Javadoc style API documentation for Python.

* `API by Epydoc <epydoc/index.html>`_

epyunit - CLI
^^^^^^^^^^^^^
CLI Wrapper for filtered subprocess calls and streaming of results.

* `epyunit <epyunit_cli.html#>`_

epyunit.spUnittest
^^^^^^^^^^^^^^^^^^

Classes derived from unittest for seamless integration of subprocess tests into PyUnit.

* TestExecutable

  +---------------------------------+----------------------------------------------------+
  | [docs]                          | [source]                                           | 
  +=================================+====================================================+
  | `TestExecutable`_               | `TestExecutable.__init__`_                         |
  +---------------------------------+----------------------------------------------------+
  | `callSubprocess`_               | `TestExecutable.callSubprocess`_                   |
  +---------------------------------+----------------------------------------------------+
  | `assertExit`_                   | `TestExecutable.assertExit`_                       |
  +---------------------------------+----------------------------------------------------+
  | `assertStdout`_                 | `TestExecutable.assertStdout`_                     |
  +---------------------------------+----------------------------------------------------+
  | `assertStderr`_                 | `TestExecutable.assertStderr`_                     |
  +---------------------------------+----------------------------------------------------+
  | `__str__ (0)`_                  | `TestExecutable.__str__`_                          |
  +---------------------------------+----------------------------------------------------+

.. _TestExecutable.__init__: _modules/epyunit/spUnittest.html#TestExecutable.__init__
.. _TestExecutable: spunittest.html#init
.. _TestExecutable.callSubprocess: _modules/epyunit/spUnittest.html#TestExecutable.callSubprocess
.. _callSubprocess: spunittest.html#callsubprocess
.. _TestExecutable.assertExit: _modules/epyunit/spUnittest.html#TestExecutable.assertExit
.. _assertExit: spunittest.html#assertExit
.. _TestExecutable.assertStdout: _modules/epyunit/spUnittest.html#TestExecutable.assertStdout
.. _assertStdout: spunittest.html#assertstdout
.. _TestExecutable.assertStderr: _modules/epyunit/spUnittest.html#TestExecutable.assertStderr
.. _assertStderr: spunittest.html#assertstderr
.. _TestExecutable.__str__: _modules/epyunit/spUnittest.html#TestExecutable.__str__
.. _\__str__ (0): spunittest.html#str

epyunit.SubprocUnit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
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
  | `setkargs (0)`_                 | `SubprocessUnit.setkargs`_                         |
  +---------------------------------+----------------------------------------------------+
  | `__str__ (1)`_                  | `SubprocessUnit.__str__`_                          |
  +---------------------------------+----------------------------------------------------+

.. _SubprocessUnit.__init__: _modules/epyunit/SubprocUnit.html#SubprocessUnit.__init__
.. _SubprocessUnit: subprocessunit.html#init
.. _SubprocessUnit.apply: _modules/epyunit/SubprocUnit.html#SubprocessUnit.apply
.. _apply (0): subprocessunit.html#apply
.. _SubprocessUnit.setkargs: _modules/epyunit/SubprocUnit.html#SubprocessUnit.setkargs
.. _setkargs (0): subprocessunit.html#setkargs
.. _SubprocessUnit.get_proceed: _modules/epyunit/SubprocUnit.html#SubprocessUnit.get_proceed
.. _get_proceed (0): subprocessunit.html#get-proceed
.. _SubprocessUnit.__str__: _modules/epyunit/SubprocUnit.html#SubprocessUnit.__str__
.. _\__str__ (1): subprocessunit.html#str

* SProcUnitRules

  +---------------------------------+----------------------------------------------------+
  | [docs]                          | [source]                                           | 
  +=================================+====================================================+
  | `SProcUnitRules`_               | `SProcUnitRules.__init__`_                         |
  +---------------------------------+----------------------------------------------------+
  | `apply (1)`_                    | `SProcUnitRules.apply`_                            |
  +---------------------------------+----------------------------------------------------+
  | `reset`_                        | `SProcUnitRules.reset`_                            |
  +---------------------------------+----------------------------------------------------+
  | `setkargs (1)`_                 | `SProcUnitRules.setkargs`_                         |
  +---------------------------------+----------------------------------------------------+
  | `setrules`_                     | `SProcUnitRules.setrules`_                         |
  +---------------------------------+----------------------------------------------------+

.. _SProcUnitRules.__init__: _modules/epyunit/SubprocUnit.html#SProcUnitRules.__init__
.. _\SProcUnitRules: subprocessunit.html#epyunit.SubprocUnit.SProcUnitRules.__init__

.. _SProcUnitRules.apply: _modules/epyunit/SubprocUnit.html#SProcUnitRules.apply
.. _apply (1): subprocessunit.html#epyunit.SubprocUnit.SProcUnitRules.apply

.. _SProcUnitRules.reset: _modules/epyunit/SubprocUnit.html#SProcUnitRules.reset
.. _reset: subprocessunit.html#epyunit.SubprocUnit.SProcUnitRules.reset

.. _SProcUnitRules.setkargs: _modules/epyunit/SubprocUnit.html#SProcUnitRules.setkargs
.. _setkargs (1): subprocessunit.html#epyunit.SubprocUnit.SProcUnitRules.setkargs

.. _SProcUnitRules.setrules: _modules/epyunit/SubprocUnit.html#SProcUnitRules.setrules
.. _setrules: subprocessunit.html#epyunit.SubprocUnit.SProcUnitRules.setrules


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
  | `_mode_batch`_                  | `SystemCalls._mode_batch`_                         |
  +---------------------------------+----------------------------------------------------+
  | `_mode_dialogue`_               | `SystemCalls._mode_dialogue`_                      |
  +---------------------------------+----------------------------------------------------+
  | `setkargs`_                     | `SystemCalls.setkargs`_                            |
  +---------------------------------+----------------------------------------------------+

.. _SystemCalls.__init__: _modules/epyunit/SystemCalls.html#SystemCalls.__init__
.. _\SystemCalls: systemcalls.html#init

.. _SystemCalls.callit: _modules/epyunit/SystemCalls.html#SystemCalls.callit
.. _callit: systemcalls.html#callit

.. _SystemCalls.displayit: _modules/epyunit/SystemCalls.html#SystemCalls.displayit
.. _displayit: systemcalls.html#displayit

.. _SystemCalls.get_proceed: _modules/epyunit/SystemCalls.html#SystemCalls.get_proceed
.. _get_proceed: systemcalls.html#get-proceed

.. _SystemCalls._mode_batch: _modules/epyunit/SystemCalls.html#SystemCalls._mode_batch
.. _\_mode_batch: systemcalls.html#mode-batch

.. _SystemCalls._mode_dialogue: _modules/epyunit/SystemCalls.html#SystemCalls._mode_dialogue
.. _\_mode_dialogue: systemcalls.html#mode-dialogue

.. _SystemCalls.setkargs: _modules/epyunit/SystemCalls.html#SystemCalls.setkargs
.. _setkargs: systemcalls.html#setkargs




epyunit.PyDevERDbg
^^^^^^^^^^^^^^^^^^
Automation of the seamless cross-process debugging of subprocesses by PyDev RemoteDebugServer.

* checkRDbg

  Helper function for initialization and bootstrap of debugging components.

  +------------------------------------+----------------------------------------------------+
  | [docs]                             | [source]                                           | 
  +====================================+====================================================+
  | `checkRDbg`_                       | `checkRDbg.checkAndInitRDbg`_                      |
  +------------------------------------+----------------------------------------------------+

.. _checkRDbg.checkAndInitRDbg: _modules/epyunit/checkRDbg.html#checkAndInitRDbg
.. _checkRDbg: checkrdbg.html#checkandinitrdbg

* PyDevERDbg

  +------------------------------------+----------------------------------------------------+
  | [docs]                             | [source]                                           | 
  +====================================+====================================================+
  | `PyDevERDbg`_                      | `PyDevERDbg.__init__`_                             |
  +------------------------------------+----------------------------------------------------+
  | `scanEclipseForPydevd`_            | `PyDevERDbg.scanEclipseForPydevd`_                 |
  +------------------------------------+----------------------------------------------------+
  | `setDebugParams`_                  | `PyDevERDbg.setDebugParams`_                       |
  +------------------------------------+----------------------------------------------------+
  | `startDebug`_                      | `PyDevERDbg.startDebug`_                           |
  +------------------------------------+----------------------------------------------------+
  | `stopDebug`_                       | `PyDevERDbg.stopDebug`_                            |
  +------------------------------------+----------------------------------------------------+

.. _PyDevERDbg.__init__: _modules/epyunit/PyDevERDbg.html#PyDevERDbg.__init__
.. _\PyDevERDbg: pydeverdbg.html#init
.. _PyDevERDbg.scanEclipseForPydevd: _modules/epyunit/PyDevERDbg.html#PyDevERDbg.scanEclipseForPydevd
.. _\scanEclipseForPydevd: pydeverdbg.html#scaneclipseforpydevd
.. _PyDevERDbg.setDebugParams: _modules/epyunit/PyDevERDbg.html#PyDevERDbg.setDebugParams
.. _\setDebugParams: pydeverdbg.html#setdebugparams
.. _PyDevERDbg.startDebug: _modules/epyunit/PyDevERDbg.html#PyDevERDbg.startDebug
.. _\startDebug: pydeverdbg.html#startdebug
.. _PyDevERDbg.stopDebug: _modules/epyunit/PyDevERDbg.html#PyDevERDbg.stopDebug
.. _\stopDebug: pydeverdbg.html#stopdebug

