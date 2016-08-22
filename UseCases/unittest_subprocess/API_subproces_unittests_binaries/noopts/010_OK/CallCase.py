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

"""
from __future__ import absolute_import
from __future__ import print_function
 
__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__='9de52399-7752-4633-9fdc-66c87a9200b8'
 
__docformat__ = "restructuredtext en"
 
import os
import unittest
 
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
        self.assertExists(self.epyu)
        self.assertExists(self.scri)
        self.call = self.epyu
        self.call += " --raw "
        self.call += " " + self.scri
        
        self.call += " OK "
        self.retX = [0, ['fromA', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output' ], [],]

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
            [0, ['fromA', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output' ], [],]
        )
        pass

#
#######################
#
 
if __name__ == '__main__':
    unittest.main()

