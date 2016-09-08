UseCase-Shortcuts - Selected Common UsesCases
=============================================

For a complete list refer to `[UseCases] <UseCases.html>`_.

Types of Call Interfaces
^^^^^^^^^^^^^^^^^^^^^^^^

  +-----------------------------------------------+--------------------------------------+
  | UseCase                                       | [doc/source]                         | 
  +===============================================+======================================+
  | binaries and selftest                         | `selftest_unittests`_                |
  +-----------------------------------------------+--------------------------------------+
  | Unit tests @CLI                               | `call_one_success`_                  |
  +-----------------------------------------------+--------------------------------------+
  | Unit tests @GUI                               |                                      |
  +-----------------------------------------------+--------------------------------------+
  | Subprocess Debugging                          | `[list] <#subprocess-debugging>`_    |
  +-----------------------------------------------+--------------------------------------+
  | Project Applications                          | `[list] <#project-applications>`_    |
  +-----------------------------------------------+--------------------------------------+


Selected Use-Cases
^^^^^^^^^^^^^^^^^^

Types of Simulator Responses
""""""""""""""""""""""""""""

Test response simulator for one subprocess.

  +---------------------------------------------+-------------------------------------+------------------+
  | UseCase                                     | [doc/source]                        | [simulator]      | 
  +=============================================+=====================================+==================+
  | selftest units - basic operational checks   | `selftest_unittests`_               |                  |
  +---------------------------------------------+-------------------------------------+------------------+
  | typical success - default                   | `cli_ok`_                           | `OK`_            |
  +---------------------------------------------+-------------------------------------+------------------+
  | typical success - default                   | `cli_nok`_                          | `NOK`_           |
  +---------------------------------------------+-------------------------------------+------------------+
  | success - default                           | `cli_noopts`_                       | `EXITOK`_        |
  +---------------------------------------------+-------------------------------------+------------------+
  | basic wrapper options                       | `epyunit_cli`_                      |                  |
  +---------------------------------------------+-------------------------------------+------------------+
  | success - EXITOK                            | `call_one_success`_                 | `EXITOK`_        |
  +---------------------------------------------+-------------------------------------+------------------+
  | failure - EXITNOK                           | `call_one_failure`_                 | `EXITNOK`_       |
  +---------------------------------------------+-------------------------------------+------------------+
  | success+failure criteria                    | `call_one_success_and_failure`_     | `EXIT9OK3NOK2`_  |
  +---------------------------------------------+-------------------------------------+------------------+
  | exit-value == 7, no STDERR                  | `call_one_exit_value`_              | `EXIT7`_         |
  +---------------------------------------------+-------------------------------------+------------------+
  | exit-value == 8, STDOUT+STDERR              | `call_one_exit_and_stderr`_         | `EXIT8`_         |
  +---------------------------------------------+-------------------------------------+------------------+
  | stdout out only                             | `call_one_stdout_out_only`_         | `STDOUTONLY`_    |
  +---------------------------------------------+-------------------------------------+------------------+
  | stderr out only                             | `call_one_stderr_out_only`_         | `STDERRONLY`_    |
  +---------------------------------------------+-------------------------------------+------------------+

.. _OK: myscript-py.html#call-a-ok
.. _NOK: myscript-py.html#call-b-nok
.. _EXITOK: myscript-py.html#call-d-exitok
.. _EXITNOK: myscript-py.html#call-e-exitnok
.. _EXIT9OK3NOK2: myscript-py.html#call-h-exit9ok3nok2
.. _EXIT7: myscript-py.html#call-f-exit7
.. _EXIT8: myscript-py.html#call-g-exit8
.. _STDOUTONLY: myscript-py.html#call-a-ok
.. _STDERRONLY: myscript-py.html#call-i-stderronly

.. _cli_ok: UseCases.unittest_subprocess.binaries.noopts.OK.html#
.. _cli_nok: UseCases.unittest_subprocess.binaries.noopts.NOK.html#
.. _selftest_unittests: UseCases.selftest.epyunit.html#
.. _cli_noopts: UseCases.unittest_subprocess.binaries.noopts.EXITOK.html#
.. _epyunit_cli: UseCases.unittest_subprocess.binaries.opts.exitign.True.html#
.. _call_one_success: UseCases.unittest_subprocess.binaries.noopts.EXITOK.html#
.. _call_one_failure: UseCases.unittest_subprocess.binaries.noopts.EXITNOK.html#
.. _call_one_success_and_failure: UseCases.unittest_subprocess.binaries.noopts.EXIT9OK3NOK2.html#
.. _call_one_exit_value: UseCases.unittest_subprocess.binaries.noopts.EXIT7.html#
.. _call_one_exit_and_stderr: UseCases.unittest_subprocess.binaries.noopts.EXIT8.html#
.. _call_one_stderr_out_only: UseCases.unittest_subprocess.binaries.noopts.EXIT8.html#
.. _call_one_stdout_out_only: UseCases.unittest_subprocess.binaries.noopts.OK.html#


Types of Expected Test Results
""""""""""""""""""""""""""""""

  +--------------------------------------------------------------------+-------------------------------------------+
  | UseCase                                                            | [doc/source]                              | 
  +====================================================================+===========================================+
  | selftest units - basic operational checks of all simlator params   | `selftest_unittests`_                     |
  +--------------------------------------------------------------------+-------------------------------------------+
  | CLI call interface - no options - default                          | `epyunit_cli_noopts`_                     |
  +--------------------------------------------------------------------+-------------------------------------------+
  | CLI call interface - basic wrapper options                         | `epyunit_cli`_                            |
  +--------------------------------------------------------------------+-------------------------------------------+
  | Call one subprocess with success                                   | `call_one_success`_                       |
  +--------------------------------------------------------------------+-------------------------------------------+
  | Call one subprocess with failure                                   | `call_one_failure`_                       |
  +--------------------------------------------------------------------+-------------------------------------------+
  | Call one subprocess - success+failure criteria                     | `call_one_success_and_failure`_           |
  +--------------------------------------------------------------------+-------------------------------------------+
  | Call one subprocess rely on EXIT only                              | `call_one_exit_value`_                    |
  +--------------------------------------------------------------------+-------------------------------------------+

.. _selftest_unittests: UseCases.selftest.epyunit.html#
.. _epyunit_cli_noopts: UseCases.unittest_subprocess.binaries.noopts.EXITOK.html#
.. _epyunit_cli: UseCases.unittest_subprocess.binaries.opts.exitign.True.html#
.. _call_one_success: UseCases.unittest_subprocess.binaries.noopts.EXITOK.html#
.. _call_one_failure: UseCases.unittest_subprocess.binaries.noopts.EXITNOK.html#
.. _call_one_success_and_failure: UseCases.unittest_subprocess.binaries.noopts.EXIT9OK3NOK2.html#
.. _call_one_exit_value: UseCases.unittest_subprocess.binaries.noopts.EXIT7.html#

Subprocess Debugging
^^^^^^^^^^^^^^^^^^^^
Subprocess Debugging includes PyDev + Eclipse.

  +------------------------------------------------------+----------------------------------------------+
  | UseCase                                              | [doc/source]                                 | 
  +======================================================+==============================================+
  | Remote Debug - selftest - basic operational checks   | `selftest_remote_debug_defaults`_            |
  +------------------------------------------------------+----------------------------------------------+

  **FOLLOWING COMING SOON**

  +------------------------------------------------------+----------------------------------------------+
  | UseCase                                              | [doc/source]                                 | 
  +======================================================+==============================================+
  | Basic Control - preset basic params, locations       | a.s.a.p. `basic_control`_                    |
  +------------------------------------------------------+----------------------------------------------+
  | Detailed Control - preset all params                 | a.s.a.p. `detailed_control`_                 |
  +------------------------------------------------------+----------------------------------------------+
  | Multiple subprocesses - setup multiple controls      | a.s.a.p. `multiple_control_instances`_       |
  +------------------------------------------------------+----------------------------------------------+

.. _selftest_remote_debug_defaults: UseCases.remote_debug.defaults.html#
.. _basic_control: UseCases.remote_debug.basic_control.html#
.. _detailed_control: UseCases.remote_debug.detailed_control.html#
.. _multiple_control_instances: UseCases.remote_debug.multiple_control_instances.html#

Project Applications
^^^^^^^^^^^^^^^^^^^^

  +-----------------------------------------------------+------------------------------------------------+
  | UseCase                                             | [doc/source]                                   | 
  +=====================================================+================================================+
  | bash OO features and extensions - core              | `<http://bash-core.sourceforge.net>`_          |
  +-----------------------------------------------------+------------------------------------------------+
  | bash apps - basic extensions library                | `<http://bashcorelib.sourceforge.net>`_        |
  +-----------------------------------------------------+------------------------------------------------+

