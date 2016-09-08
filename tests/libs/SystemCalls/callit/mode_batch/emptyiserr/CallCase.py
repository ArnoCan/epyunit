from __future__ import absolute_import
#from __future__ import print_function

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.2.0'
__uuid__='9de52399-7752-4633-9fdc-66c87a9200b8'

__docformat__ = "restructuredtext en"

import unittest

from testdata import call_scripy

import epyunit.SystemCalls 


import os,sys
from cStringIO import StringIO

#
#######################
#
class CallUnits(unittest.TestCase):

    def __init__(self,*args,**kargs):
        super(CallUnits,self).__init__(*args,**kargs)

    @classmethod
    def setUpClass(cls):
        cls.sx = epyunit.SystemCalls.SystemCalls()

    def setUp(self):
        syskargs = {}
        syskargs['emptyiserr'] = True

        # buffers for evaluation after intercepted exit.
        self.stdoutbuf=StringIO()
        self.stderrbuf=StringIO()
        self.stdout = sys.stdout
        self.stderr = sys.stderr

    def testCase010(self):
        _call  = call_scripy+" "
        _call += "OK"
        retX = [0, ["fromA", 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'],[]]
        callkargs = {}
        ret = self.sx.callit(_call,**callkargs)
        self.assertEqual(ret, retX)
 
    def testCase011(self):
        _call  = call_scripy+" "
        _call += "NOK"
        retX = [0, ['fromB', 'arbitrary output', 'arbitrary output'], ['arbitrary signalling ERROR string']]
        callkargs = {}
        ret = self.sx.callit(_call,**callkargs)
        self.assertEqual(ret, retX)


    def testCase012(self):
        _call  = call_scripy+" "
        _call += " PRIO "
        retX = [0, ['fromC', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'], ['arbitrary signalling ERROR string']]
        callkargs = {}
        ret = self.sx.callit(_call,**callkargs)
        self.assertEqual(ret, retX)

    def testCase013(self):
        _call  = call_scripy+" "
        _call += " EXITOK "
        retX = [0, ['fromD', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'], []]
        callkargs = {}
        ret = self.sx.callit(_call,**callkargs)
        self.assertEqual(ret, retX)

    def testCase014(self):
        _call  = call_scripy+" "
        _call += " EXITNOK "
        retX = [1, ['fromE', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'], []]
        callkargs = {}
        ret = self.sx.callit(_call,**callkargs)
        self.assertEqual(ret, retX)

    def testCase015(self):
        _call  = call_scripy+" "
        _call += " EXIT7 "
        retX = [7, ['fromF', 'arbitrary output', 'arbitrary signalling NOK string', 'arbitrary output'], []]
        callkargs = {}
        ret = self.sx.callit(_call,**callkargs)
        self.assertEqual(ret, retX)

    def testCase016(self):
        _call  = call_scripy+" "
        _call += " EXIT8 "
        retX = [8, ['fromG', 'arbitrary output', 'arbitrary signalling NOK string', 'arbitrary output'], ['arbitrary err output', 'arbitrary err signalling NOK string', 'arbitrary err output']]
        callkargs = {}
        ret = self.sx.callit(_call,**callkargs)
        self.assertEqual(ret, retX)

    def testCase017(self):
        _call  = call_scripy+" "
        _call += " EXIT9OK3NOK2 "
        retX = [9, ['fromH', 'OK', 'OK', 'OK'], ['NOK', 'NOK']]
        callkargs = {}
        ret = self.sx.callit(_call,**callkargs)
        self.assertEqual(ret, retX)

    def testCase018(self):
        _call  = call_scripy+" "
        _call += " DEFAULT "
        retX = [123, ['arbitrary output'], []]
        callkargs = {}
        ret = self.sx.callit(_call,**callkargs)
        self.assertEqual(ret, retX)

    def testCase100(self):
        callkargs = {}
        _call  = " "
        syskargs = { 'emptyiserr': False, }
        ret = self.sx.setkargs(**syskargs) #@UnusedVariable
        ret = self.sx.callit(_call,**callkargs) #@UnusedVariable
        retRef = [0, [], []]
        self.assertEqual(ret, retRef)
        pass

    def testCase110(self):
        callkargs = {}
        _call  = ""

        syskargs = { 'emptyiserr': True, }
        ret = self.sx.setkargs(**syskargs) #@UnusedVariable
        ret = self.sx.callit(_call,**callkargs) #@UnusedVariable
        retRef = [2, [], ['ERROR:MissingCallstr']]
        self.assertEqual(ret, retRef)
        pass

    def testCase120(self):
        callkargs = {}
        _call  = ""

        syskargs = { 'emptyiserr': False, }
        ret = self.sx.setkargs(**syskargs) #@UnusedVariable
        ret = self.sx.callit(_call,**callkargs) #@UnusedVariable
        retRef = [0, [], []]
        self.assertEqual(ret, retRef)
        pass

#
#######################
#

if __name__ == '__main__':
    unittest.main()

