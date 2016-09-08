'epyunit.debug.pydevrdc' - Module
*********************************
The PyDev plugin provides for the remote debugging of Python processes. This
is also supported for processes started outside the control of the debugger. 
Here stub code is required in the process started outside the control domain
of 'pydevd.py'. The module 'epyunit.debug' supports the localization
and load of 'pydevd.py' fromvarious versions and locations.

.. automodule:: epyunit.debug.checkRDbg


Module Variables
----------------

* **epyunit.debug.checkRDbg._dbg_self**: 
  For debug of the debug subpackage itself.

* **epyunit.debug.checkRDbg._dbg_unit**: 
  For unittest of the debug subpackage itself.

* **epyunit.debug.checkRDbg._pderd_inTestMode_suppress_init**: 
  Force erroneous settings for the test of the debug subpackage itself.

Functions
---------

checkAndRemoveRDbgOptions
"""""""""""""""""""""""""

.. autofunction:: checkAndRemoveRDbgOptions

checkRDbg
"""""""""

.. autofunction:: checkRDbg

