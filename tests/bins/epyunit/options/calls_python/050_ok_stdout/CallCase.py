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
 
import unittest
import os,sys
 
from filesysobjects.FileSysObjects import setUpperTreeSearchPath,findRelPathInSearchPath
import epyunit.SystemCalls 

#
#######################
#
slst = []
setUpperTreeSearchPath(os.path.abspath(os.path.dirname(__file__)),'epyunit',slst)

epyu = findRelPathInSearchPath('bin/epyunit',slst,matchidx=0)
scri = findRelPathInSearchPath('epyunit/myscript.py',slst,matchidx=0)

 
class CallUnits(unittest.TestCase):
    def testCase010(self):
        _call  = epyu + " "
        _call += scri + " OK "

        syskargs = {}
        sx = epyunit.SystemCalls.SystemCalls(**syskargs)

        callkargs = {}
        ret = sx.callit(_call,**callkargs)

        retX = [0, ['fromA', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'],[]]
        self.assertEqual(ret,retX)
 
    def testCase020(self):
        _call  = epyu + " "
        _call += scri + " NOK "

        syskargs = {}
        sx = epyunit.SystemCalls.SystemCalls(**syskargs)

        callkargs = {}
        ret = sx.callit(_call,**callkargs)

        retX = [0, ['fromB', 'arbitrary output', 'arbitrary output'],['arbitrary signalling ERROR string']]
        self.assertEqual(ret,retX)
 
    def testCase030(self):
        _call  = epyu + " "
        _call += scri + " EXIT7 "

        syskargs = {}
        sx = epyunit.SystemCalls.SystemCalls(**syskargs)

        callkargs = {}
        ret = sx.callit(_call,**callkargs)

        retX = [1, ['fromF', 'arbitrary output', 'arbitrary signalling NOK string', 'arbitrary output'],[]]
        self.assertEqual(ret,retX)
#
#######################
#
 
if __name__ == '__main__':
    unittest.main()

