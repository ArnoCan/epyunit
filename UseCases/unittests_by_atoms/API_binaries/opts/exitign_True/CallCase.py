""" 
Default case for a testee with result: succeed: OK
 
  EXIT:
     0
  STDOUT:
     arbitrary output
     arbitrary signalling OK string
     arbitrary output
  STDERR:
     -

The actual unittest is processed within the subprocess, the current call
is used as an ordinary subprocess caller.

Call options:

  --exitign=True

"""
from __future__ import absolute_import
from __future__ import print_function
 
__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__='9de52399-7752-4633-9fdc-66c87a9200b8'
 
__docformat__ = "restructuredtext en"
 
import unittest
import os,sys
 
from filesysobjects.FileSysObjects import setUpperTreeSearchPath,findRelPathInSearchPath
import epyunit.SystemCalls 

#
#######################
#
 
class CallUnits(unittest.TestCase):
    def testCase000(self):
        """The original default output for case EXIT9OK3NOK2::

           EXIT:
              9
           STDOUT:
              fromH
              OK
              OK
              OK
           STDERR:
              NOK
              NOK

        """

        slst = []
        setUpperTreeSearchPath(os.path.abspath(os.path.dirname(__file__)),'epyunit',slst)
        
        epyu = findRelPathInSearchPath('bin/epyunit',slst,matchidx=0)
        scri = findRelPathInSearchPath('epyunit/myscript.sh',slst,matchidx=0)

        _call  = epyu
        _call += " --passall "
        _call += scri
        _call += " EXIT9OK3NOK2 "

        syskargs = {}
        
        #
        # make a simple system call, the actual unittest is processed within the subprocess 
        #
        sx = epyunit.SystemCalls.SystemCalls(**syskargs)

        callkargs = {}
        ret = sx.callit(_call,**callkargs)

        assert ret ==  [9, ['fromH', 'OK', 'OK', 'OK'], ['NOK', 'NOK']]
        pass
 
    def testCase010(self):
        """The mdofied output by the option::

           --exitign=True

        original default output for case EXIT9OK3NOK2::

           EXIT:
              0
           STDOUT:
              fromH
              OK
              OK
              OK
           STDERR:
              NOK
              NOK

        """

        slst = []
        setUpperTreeSearchPath(os.path.abspath(os.path.dirname(__file__)),'epyunit',slst)
        
        epyu = findRelPathInSearchPath('bin/epyunit',slst,matchidx=0)
        scri = findRelPathInSearchPath('epyunit/myscript.sh',slst,matchidx=0)

        _call  = epyu
#        _call += " --rdbg=127.0.0.1:5678 "
        _call += " --rdbg "
#        _call += " --pass "
#        _call += " --passall "
#        _call += " --exitign=True "
        _call += " -- "
        _call += scri
        _call += " EXIT9OK3NOK2 "

        syskargs = {}
        
        #
        # make a simple system call, the actual unittest is processed within the subprocess 
        #
        sx = epyunit.SystemCalls.SystemCalls(**syskargs)

        callkargs = {}
        ret = sx.callit(_call,**callkargs)

        assert ret ==  [1, ['fromH', 'OK', 'OK', 'OK'], ['NOK', 'NOK']]
        pass
 
#
#######################
#
 
if __name__ == '__main__':
    unittest.main()

