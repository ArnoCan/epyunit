"""
The UseCase **remote_debug** demonstrates and verifies the basic facilities for remote 
debugging of external Python subprocesses by the PyDev/Eclipse framework.

Therefore three components are provided:

* **calldir/CallUseCase.py**
  
  The main primary call of the UseCase. In dialogue mode this
  should be started by PyDev debugger from Eclipse.

* **subprocdir/bin/epyunit4RDbg.py**

  When stepping over the 'callit' statement, the subprocess
  'epyunit4RDbg.py' initializes itself with the 'pydevd.py',
  and continues under control of the PyDev debugger.
  The remote debug server has to be started before, 
  see manuals ePyDev! 
  
* **scriptdir/bin/myscript.sh**

  The script provides hard-coded response output for the test
  of ePyUnit itself, but also wrapper processes in general.

"""
__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2015-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.0'
__uuid__='9de52399-7752-4633-9fdc-66c87a9200b8'
