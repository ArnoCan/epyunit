"""
The UseCase **selftest.epyunit** demonstrates and verifies the '--selftest' option
for a basic quick check.

* **CallUseCase.py**
  
  The main primary call of the UseCase. In dialogue mode this
  should be started by PyDev debugger from Eclipse.

* **bin/epyunit**

  The commandline interface wrapper.

The following figure depicts the components.
  ::

    +------------------+         +-------------+
    |                  |         |             |
    |  CallUseCase.py  |  <--->  | bin/epyunit |  
    |                  |         |             |
    +------------------+         +-------------+
             A                          A
             |                          |
          UseCase                 the CLI wrapper
       frame for tests

"""
__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2015-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.0'
__uuid__='9de52399-7752-4633-9fdc-66c87a9200b8'
