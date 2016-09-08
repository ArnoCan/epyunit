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
 
from testdata import epyu,call_scripy
from epyunit.unittest.subprocess import TestExecutable
 
#
#######################
#
 
class CallUnits(TestExecutable):

    @classmethod
    def setUpClass(cls):
        cls.cache = True

    def setUp(self):
        self.call  = epyu
        self.call += " --passall "
        self.call += call_scripy
        self.call += " EXIT9OK3NOK2 "
        self.retX = [9, ['fromH', 'OK', 'OK', 'OK'], ['NOK', 'NOK', ]]

    def testCase000(self):
        ret = self.callSubprocess(self.call)
        self.assertEqual(self.retX,ret)
        pass
 
    def testCase010(self):
        self.call  = epyu
        self.call += " --rdbg 127.0.0.1:5678 "
        self.call += " --passall "
        self.call += call_scripy
        self.call += " EXIT9OK3NOK2 "

        ret = self.callSubprocess(self.call)
        self.assertEqual(self.retX,ret)
        pass
 
    def testCase011(self):
        self.call  = epyu
        self.call += " --passall "
        self.call += " --rdbg 127.0.0.1:5678 "
        self.call += call_scripy
        self.call += " EXIT9OK3NOK2 "

        ret = self.callSubprocess(self.call)
        self.assertEqual(self.retX,ret)
        pass
 
    def testCase020(self):
        self.call  = epyu
        self.call += " --rdbg 127.0.0.1:5678 "
        self.call += " --passall "
        self.call += call_scripy
        self.call += " EXIT9OK3NOK2 "

        ret = self.callSubprocess(self.call)
        self.assertEqual(self.retX,ret)
        pass

    def testCase021(self):
        self.call  = epyu
        self.call += " --passall "
        self.call += " --rdbg 127.0.0.1:5678 "
        self.call += call_scripy
        self.call += " EXIT9OK3NOK2 "

        ret = self.callSubprocess(self.call)
        self.assertEqual(self.retX,ret)
        pass

#
#######################
#
 
if __name__ == '__main__':
    unittest.main()

