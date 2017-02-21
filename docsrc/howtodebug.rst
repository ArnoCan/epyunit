HowTo Remote Debug
******************

Debug Features
""""""""""""""

The PyDev plugin provides for the remote debugging of Python processes. This
is also supported for processes started outside the control of the debugger. 
Here stub code is required in the process started outside the control domain
of 'pydevd.py'. The module 'epyunit.debug' supports the localization
and load of 'pydevd.py' fromvarious versions and locations.

Detection of 'pydevd.py'
""""""""""""""""""""""""

The following path variables are required for automated detection of the module 'pydevd.py'
in case of an arbitrary but standard Eclipse-Installation:
  ::

     PATH
     PYTHONPATH

For example:

* Windows:
  ::

     set PYTHONPATH=C:\temp\eclipse\epyunit;%PYTHONPATH%
     set PATH=C:\ide\eclipse\eclipse-cpp-mars-R-win32-x86_64;C:\Python27;C:\Python27\Scripts;C:\Python27\bin;%PATH%

* POSIX:
  ::

     export PYTHONPATH=<project-dir>:$PYTHONPATH
     export PATH=$HOME/eclipse  # see default search of epyunit

* CYGWIN:
  ::

     export PYTHONPATH=<project-dir>:$PYTHONPATH
     export PATH=/cygdrive/c/ide/eclipse/eclipse-modeling-luna-SR1-win32-x86_64/:$PATH
     # see default search of epyunit

For alternative parameters of the search algorithm - e.g. ENVVAR - refer to 'checkRDbg' module.
Some tests for nested subprocesses require in PATH to be inherited, so put these for
Windows into the environment, or export them on POSIX compatible systems.

The UseCases and tests related to cross-process debugging or RemoteDebugServer with pydevd.py
require a running server instance within Eclipse/PyDev - see `<http://www.pydev.org/manual_adv_remote_debugger.html>`_

Debug by Reverse-Tunnel
"""""""""""""""""""""""

The debug module of PyDev supports for remote debugging by the stub 'pydevd.py'.
This has to be located on the target machine, where the debugged process is executed.

ePyUnit supports the packaging and the scan and selection of the required components.

1. Create a package containing the appropriate version of 'pydevd.py'.
   The default call is:
   ::

      epyd.py -v  --force --package --package-type=tar.gz --package-print

2. Copy and unpack the package at the host the debuggee is executed.
   ::

     scp <package> <debuggee-host>:<path>
     ssh <debuggee-host>
     cd <path>
     tar xvf <package> or unzip <package> 

3. Start within Eclipse/PyDev the debug server.

4. Create a reverse tunnel to the machine the debuggee is going to be executed.
   For example by::

     ssh -R  5678:localhost:5678 -l <ruser> <debuggee-host> 

5. Start the debuggee with appropriate command line options. 
   For example by::

     <debuggee> --rdbg  

   