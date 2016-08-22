"""example_H
 
Case for a testee with mixed result, exit 9: EXIT9OK3NOK2
 
   EXIT:
     9
   STDOUT:
     OK
     OK
     OK
   STDERR:
     NOK
     NOK
 
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
        self.call = self.epyu
        self.call += " --raw "
        self.call += " --priotype=False " + self.scri

        self.call += " EXIT9OK3NOK2 "
        self.retX = [9, ['fromH', 'OK', 'OK', 'OK'], ['NOK', 'NOK']]

    
    def testCase000(self):
        self.callSubprocess(self.call)
        self.assertEqual(self.retX)
        pass
 
 
#
#######################
#
 
if __name__ == '__main__':
    unittest.main()

