UseCase-Shortcuts - Selected Common UsesCases
=============================================

For a complete list refer to `[UseCases] <UseCases.html>`_.

binaries and selftest
^^^^^^^^^^^^^^^^^^^^^

  +-----------------------------------------------+--------------------------------------+
  | UseCase                                       | [doc/source]                         | 
  +===============================================+======================================+
  | selftest units - basic operational checks     | `selftest_unittests`_                |
  +-----------------------------------------------+--------------------------------------+
  | CLI call interface - no options - default     | `epyunit_cli_noopts`_                |
  +-----------------------------------------------+--------------------------------------+
  | CLI call interface - basic wrapper options    | `epyunit_cli`_                       |
  +-----------------------------------------------+--------------------------------------+

.. _selftest_unittests: UseCases.selftest.epyunit.html#
.. _epyunit_cli_noopts: UseCases.API_subproces_unittests_binaries_IF.noopts.040_EXITOK.html#
.. _epyunit_cli: UseCases.API_subproces_unittests_binaries_IF.opts.exitign_True.html#

Unit tests @CLI
^^^^^^^^^^^^^^^
Unit tests @CLI includes PyUnit.

  +-------------------------------------------------------+-------------------------------------------+
  | UseCase                                               | [doc/source]                              | 
  +=======================================================+===========================================+
  | Call one subprocess - success - EXITOK                | `call_one_success`_                       |
  +-------------------------------------------------------+-------------------------------------------+
  | Call one subprocess - failure - EXITNOK               | `call_one_failure`_                       |
  +-------------------------------------------------------+-------------------------------------------+
  | Call one subprocess - success+failure criteria        | `call_one_success_and_failure`_           |
  +-------------------------------------------------------+-------------------------------------------+
  | Call one subprocess - exit-value == 7                 | `call_one_exit_value`_                    |
  +-------------------------------------------------------+-------------------------------------------+
  | Call one subprocess - multiple parameters             | `call_one_multiple_parameters`_           |
  +-------------------------------------------------------+-------------------------------------------+

.. _call_one_success: UseCases.API_subproces_unittests_binaries_IF.noopts.040_EXITOK.html#
.. _call_one_failure: UseCases.API_subproces_unittests_binaries_IF.noopts.050_EXITNOK.html#
.. _call_one_success_and_failure: UseCases.API_subproces_unittests_binaries_IF.noopts.080_EXIT9OK3NOK2.html#
.. _call_one_exit_value: UseCases.API_subproces_unittests_binaries_IF.noopts.060_EXIT7.html#
.. _call_one_multiple_parameters: UseCases.subprocesses.call_one__multiple_parameters.html#

Unit tests @GUI
^^^^^^^^^^^^^^^
Unit tests @GUI includes PyDev + PyUnit + Eclipse.

  +-----------------------------------------------+-------------------------------------------+
  | UseCase                                       | [doc/source]                              | 
  +===============================================+===========================================+
  | Call one subprocess - success                 | `call_one_success_gui`_                   |
  +-----------------------------------------------+-------------------------------------------+
  | Call one subprocess - failure                 | `call_one_failure_gui`_                   |
  +-----------------------------------------------+-------------------------------------------+
  | Call one subprocess - success+failure         | `call_one_success_and_failure_gui`_       |
  +-----------------------------------------------+-------------------------------------------+
  | Call one subprocess - exit-value              | `call_one_exit_value_gui`_                |
  +-----------------------------------------------+-------------------------------------------+

.. _call_one_success_gui: UseCases.subprocesses.call_one_success.html#
.. _call_one_failure_gui: UseCases.subprocesses.call_one_failure.html#
.. _call_one_success_and_failure_gui: UseCases.subprocesses.call_one_success_and_failure.html#
.. _call_one_exit_value_gui: UseCases.subprocesses.call_one_exit_value.html#

Subprocess Debugging
^^^^^^^^^^^^^^^^^^^^
Subprocess Debugging includes PyDev + Eclipse.

  +------------------------------------------------------+----------------------------------------------+
  | UseCase                                              | [doc/source]                                 | 
  +======================================================+==============================================+
  | Remote Debug - selftest - basic operational checks   | `selftest_remote_debug`_                     |
  +------------------------------------------------------+----------------------------------------------+
  | Basic Control - preset basic params, locations       | `basic_control`_                             |
  +------------------------------------------------------+----------------------------------------------+
  | Detailed Control - preset all params                 | `detailed_control`_                          |
  +------------------------------------------------------+----------------------------------------------+
  | Multiple subprocesses - setup multiple controls      | `multiple_control_instances`_                |
  +------------------------------------------------------+----------------------------------------------+

.. _selftest_remote_debug: UseCases.remote_debug.html#
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

