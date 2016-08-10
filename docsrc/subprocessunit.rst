'epyunit.SubprocUnit' - Module
******************************

The module 'epyunit.SubprocUnit' provides atoms for unittest on subprocess calls.

The main classes are:

* `SubprocessUnit <#class-subprocessunit>`_  - Extends SystemCalls for the application of a state decision engine
  onto the execution results.

* `SProcUnitRules <#class-sprocunitrules>`_ - Stores, manages, and applies the defined rule set for the final
  result state.

.. automodule:: epyunit.SubprocUnit

Class: SubprocessUnit
---------------------

.. autoclass:: SubprocessUnit

Methods
^^^^^^^

__init__
""""""""
.. automethod:: SubprocessUnit.__init__

apply
"""""
.. automethod:: SubprocessUnit.apply

get_proceed
"""""""""""
.. automethod:: SubprocessUnit.get_proceed

setkargs
""""""""
.. automethod:: SubprocessUnit.setkargs

setruleset
""""""""""
.. automethod:: SubprocessUnit.setruleset

__str__
"""""""
.. automethod:: SubprocessUnit.__str__

__repr__
""""""""
.. automethod:: SubprocessUnit.__repr__


Exceptions
^^^^^^^^^^

.. autoexception:: SubprocessUnitException



Class: SProcUnitRules
---------------------

.. autoclass:: SProcUnitRules

Methods
^^^^^^^

__init__
""""""""
.. automethod:: SProcUnitRules.__init__

apply
"""""
.. automethod:: SProcUnitRules.apply

reset
"""""
.. automethod:: SProcUnitRules.reset

setkargs
"""""""""
.. automethod:: SProcUnitRules.setkargs

setrules
""""""""
.. automethod:: SProcUnitRules.setrules

states
""""""
.. automethod:: SProcUnitRules.states

__str__
"""""""
.. automethod:: SProcUnitRules.__str__

__repr__
""""""""
.. automethod:: SProcUnitRules.__repr__

Exceptions
^^^^^^^^^^

.. autoexception:: SProcUnitRulesException

