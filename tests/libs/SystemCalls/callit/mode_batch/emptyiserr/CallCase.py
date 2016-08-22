from __future__ import absolute_import
#from __future__ import print_function
 
__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.10'
__uuid__='9de52399-7752-4633-9fdc-66c87a9200b8'
 
__docformat__ = "restructuredtext en"
 
import unittest
import os,sys
from cStringIO import StringIO
 
from filesysobjects.FileSysObjects import setUpperTreeSearchPath,findRelPathInSearchPath
import epyunit.SystemCalls 

#
#######################
# 
class CallUnits(unittest.TestCase):

    def __init__(self,*args,**kargs):
        super(CallUnits,self).__init__(*args,**kargs)
        
    @classmethod
    def setUpClass(cls):
        cls.slst = []
        setUpperTreeSearchPath(os.path.abspath(os.path.dirname(__file__)),'epyunit',cls.slst)
        
        cls.epyu = findRelPathInSearchPath('bin/epyunit',cls.slst,matchidx=0)
        cls.scri = findRelPathInSearchPath('epyunit/myscript.sh',cls.slst,matchidx=0)
        cls.scri = cls.scri

        # buffers for evaluation after intercepted exit.
        cls.stdoutbuf=StringIO()
        cls.stderrbuf=StringIO()
        cls.stdout = sys.stdout
        cls.stderr = sys.stderr

    def setUp(self):
        syskargs = {}
        syskargs['emptyiserr'] = True
        
        self.sx = epyunit.SystemCalls.SystemCalls(**syskargs)

    def testCase010(self):
        callkargs = {}
        _call  = self.scri
        _call += " OK "

        ret = self.sx.callit(_call,**callkargs)
        assert ret ==  [0, ['fromA', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'], []]
        pass

    def testCase011(self):
        callkargs = {}
        _call  = self.scri
        _call += " NOK "

        ret = self.sx.callit(_call,**callkargs)
        assert ret ==  [0, ['fromB', 'arbitrary output', 'arbitrary output'], ['arbitrary signalling ERROR string']]
        pass

    def testCase012(self):
        callkargs = {}
        _call  = self.scri
        _call += " PRIO "

        ret = self.sx.callit(_call,**callkargs)
        assert ret ==   [0, ['fromC', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'], ['arbitrary signalling ERROR string']]
        pass

    def testCase013(self):
        callkargs = {}
        _call  = self.scri
        _call += " EXITOK "

        ret = self.sx.callit(_call,**callkargs)
        assert ret ==  [0, ['fromD', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'], []]
        pass

    def testCase014(self):
        callkargs = {}
        _call  = self.scri
        _call += " EXITNOK "

        ret = self.sx.callit(_call,**callkargs) #@UnusedVariable
        retRef = [1, ['fromE', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'], []]
        self.assertEqual(ret, retRef)
        pass

    def testCase015(self):
        callkargs = {}
        _call  = self.scri
        _call += " EXIT7 "

        ret = self.sx.callit(_call,**callkargs) #@UnusedVariable
        retRef =  [7, ['fromF', 'arbitrary output', 'arbitrary signalling NOK string', 'arbitrary output'], []]
        self.assertEqual(ret, retRef)
        pass


    def testCase016(self):
        callkargs = {}
        _call  = self.scri
        _call += " EXIT8 "

        ret = self.sx.callit(_call,**callkargs) #@UnusedVariable
        retRef = [8, ['fromG', 'arbitrary output', 'arbitrary signalling NOK string', 'arbitrary output'], ['arbitrary err output', 'arbitrary err signalling NOK string', 'arbitrary err output']]
        self.assertEqual(ret, retRef)
        pass

    def testCase017(self):
        callkargs = {}
        _call  = self.scri
        _call += " EXIT9OK3NOK2 "

        ret = self.sx.callit(_call,**callkargs) #@UnusedVariable
        retRef = [9, ['fromH', 'OK', 'OK', 'OK'], ['NOK', 'NOK']]
        self.assertEqual(ret, retRef)
        pass

    def testCase018(self):
        callkargs = {}
        _call  = self.scri
        _call += " DEFAULT "

        ret = self.sx.callit(_call,**callkargs) #@UnusedVariable
        retRef = [123, ['arbitrary output'], []]
        self.assertEqual(ret, retRef)
        pass

    def testCase100(self):
        callkargs = {}
        _call  = ""

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

