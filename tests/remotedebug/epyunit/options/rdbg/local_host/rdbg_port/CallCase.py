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
from epyunit.unittest.subprocess import TestExecutable
 
#
#######################
#
 
class CallUnits(TestExecutable):

    @classmethod
    def setUpClass(cls):
        slst = []
        setUpperTreeSearchPath(os.path.abspath(os.path.dirname(__file__)),'epyunit',slst)
        
        cls.epyu = findRelPathInSearchPath('bin/epyunit',slst,matchidx=0)
        cls.scri = findRelPathInSearchPath('epyunit/myscript.sh',slst,matchidx=0)

        cls.cache = True

    def setUp(self):
        self.call  = self.epyu
        self.call += " --passall "
        self.call += self.scri

        self.call += " EXIT9OK3NOK2 "
        self.retX = [9, ['fromH', 'OK', 'OK', 'OK'], ['NOK', 'NOK', ]]

    def testCase000(self):
        self.callSubprocess(self.call)
        self.assertEqual(self.retX)
        pass
 
    def testCase010(self):
        self.call  = self.epyu
        self.call += " --rdbg :5678"
        self.call += " --passall "
        self.call += " -- "
        self.call += self.scri
        self.call += " EXIT9OK3NOK2 "

        self.callSubprocess(self.call)
        self.assertEqual(self.retX)
        pass
 
    def testCase011(self):
        self.call  = self.epyu
        self.call += " --passall "
        self.call += " --rdbg :5678"
        self.call += " -- "
        self.call += self.scri
        self.call += " EXIT9OK3NOK2 "

        self.callSubprocess(self.call)
        self.assertEqual(self.retX)
        pass
 
    def testCase020(self):
        self.call  = self.epyu
        self.call += " --rdbg :5678 "
        self.call += " --passall "
        self.call += self.scri
        self.call += " EXIT9OK3NOK2 "

        self.callSubprocess(self.call)
        self.assertEqual(self.retX)
        pass

    def testCase021(self):
        self.call  = self.epyu
        self.call += " --passall "
        self.call += " --rdbg :5678 "
        self.call += self.scri
        self.call += " EXIT9OK3NOK2 "

        self.callSubprocess(self.call)
        self.assertEqual(self.retX)
        pass

#
#######################
#
 
if __name__ == '__main__':
    unittest.main()

