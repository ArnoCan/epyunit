"""
The UseCase **EXITNOK** demonstrates and verifies the basic facilities start of a script
by epyunit.SysCall.

* **CallUseCase.py**
  
  The main primary call of the UseCase. In dialogue mode this
  should be started by PyDev debugger from Eclipse.

* **epyunit/myscript.sh**

  The script provides hard-coded response output for the test
  of ePyUnit itself, but also wrapper processes in general.

The following figure depicts the components.
  ::

    +------------------+         +-------------+
    |                  |         |             |
    |  CallUseCase.py  |  <--->  | myscript.sh |  
    |                  |         |             |
    +------------------+         +-------------+
             A                          A
             |                          |
          UseCase                   a resource
       frame for tests               simulator

"""
__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2015-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.0'
__uuid__='9de52399-7752-4633-9fdc-66c87a9200b8'
