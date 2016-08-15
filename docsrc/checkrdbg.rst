'epyunit.checkRDbg' - Module
****************************
The 'checkRDbg' function check the remote debugging status of 
the current process, and performs required actions, returns 
the connection paraeters for the configured peer server:

* when required loads the debugging facilities and activates
  current process instance

* when configured prepares and returns the forwarding
  parameters for the next levels of nested subprocesses

* when parameters do not match simply ignores debugging

.. automodule:: epyunit.checkRDbg


Function: checkAndInitRDbg
--------------------------

.. autofunction:: checkAndInitRDbg


