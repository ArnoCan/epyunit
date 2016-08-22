"""example_DEFAULT

Case for a testee with default failure, exit 123: DEFAULT

   EXIT:
     123
   STDOUT:
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

import unittest
import os
 
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
        
        self.call += " DEFAULT "
        self.retX = [123, ['arbitrary output'],[]]
        pass

    def testCase000(self):
        ret = self.callSubprocess(self.call)
        self.assertEqual(self.retX, ret)
        pass
 
    def testCase010(self):
        self.assertSubprocess(self.call, self.retX)
        pass
 
    def testCase011(self):
        self.assertSubprocess(
            self.call, 
            [123, ['arbitrary output'],[]]
        )
        pass 
 
#
#######################
#
 
if __name__ == '__main__':
    unittest.main()

