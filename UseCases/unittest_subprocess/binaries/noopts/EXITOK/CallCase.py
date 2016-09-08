"""example_D
 
Case for a testee with success, exit 0: EXITOK
 
   EXIT:
     0
   STDOUT:
     arbitrary output
     arbitrary signalling OK string
     arbitrary output
   STDERR:
     --
 
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
        slst = []
        cls.cache = True

    def setUp(self):
        self.call = epyu
        self.call += " --raw "
        self.call += " " + call_scripy
        
        self.call += " EXITOK "
        self.retX = [0, ['fromD', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'],[]]
        pass
 
        pass

    def testCase000(self):
        self.callSubprocess(self.call)
        self.assertEqual(self.retX)
        pass
 
    def testCase010(self):
        self.assertSubprocess(self.call, self.retX)
        pass
 
    def testCase011(self):
        self.assertSubprocess(
            self.call, 
            [0, ['fromD', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'],[]]
        )
        pass
 
#
#######################
#
 
if __name__ == '__main__':
    unittest.main()

