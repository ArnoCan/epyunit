'epyunit.PyDevERDbg' - Module
*****************************
The PyDev plugin provides for the remote debugging of Python processes. This
is also supported for processes started outside the control of the debugger. 
Here stub code is required in the process started outside the control domain
of 'pydevd.py'. The module 'epyunit.PyDevERDbg' supports the localization
and load of 'pydevd.py' fromvarious versions and locations.

.. automodule:: epyunit.PyDevERDbg


Module Variables
----------------

* **epyunit.Eclipse.PYDEVD**: 
    Provides a pre-allocated controller object 
    for remote debugging by PyDev as Eclipse plugin. 
    Could be extended by custom instances as required.
    Just requires a simple import statement and could
    thereafter be controlled by options.

Environment Variables
---------------------

* **PYDEVDSCAN**: 
    The start directory for search on 'pydevd.py'. 
    If not set, the default is::

      px = $HOME/eclipse/eclipse
      px = os.path.abspath(px)
      px = os.path.realname(px)
      px = os.path.dirname(px)
      px = os.path.normpath(px)

    The start directory for search on 'pydevd.py'. is due to the 
    manual(`PyDevRemoteDebugging`_) located in::

      eclipse/plugins/org.python.pydev_x.x.x/pysrc/pydevd.py

    Apply 'pyfilesysobjects' with 're' and 'glob' expressions for
    casual application of a specific version or iteration through
    the present.

.. _PyDevRemoteDebugging: http://pydev.org/manual_adv_remote_debugger.html

Function: checkRDbg
-------------------

.. autofunction:: checkRDbg


Class: PyDevERDbg
-----------------

.. autoclass:: PyDevERDbg

Methods
^^^^^^^

__init__
""""""""
.. automethod:: PyDevERDbg.__init__

scanEclipseForPydevd
""""""""""""""""""""
.. automethod:: PyDevERDbg.scanEclipseForPydevd

setDebugParams
""""""""""""""
.. automethod:: PyDevERDbg.setDebugParams

startDebug
""""""""""
.. automethod:: PyDevERDbg.startDebug

stopDebug
"""""""""
.. automethod:: PyDevERDbg.stopDebug

__str__
"""""""
.. automethod:: PyDevERDbg.__str__

__repr__
""""""""
.. automethod:: PyDevERDbg.__repr__


Exceptions
^^^^^^^^^^

.. autoexception:: PyDevERDbgException

.. autoexception:: PyDevERDbgLoadException

.. autoexception:: PyDevERDbgServerException

