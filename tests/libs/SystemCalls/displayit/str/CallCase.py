from __future__ import absolute_import
from __future__ import print_function
from testdata import call_scripy
 
__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.10'
__uuid__='9de52399-7752-4633-9fdc-66c87a9200b8'
 
__docformat__ = "restructuredtext en"
 
import unittest
import os,sys
 
from filesysobjects.FileSysObjects import setUpperTreeSearchPath,findRelPathInSearchPath
import epyunit.SystemCalls 

from testdata import call_scripy,epyu

#
#######################
# 
class CallUnits(unittest.TestCase):

    def __init__(self,*args,**kargs):
        super(CallUnits,self).__init__(*args,**kargs)
        
    @classmethod
    def setUpClass(cls):
        cls.epyu = epyu
        cls.scri = call_scripy

        cls.callkargs = {}
        cls.displayargs = {} 

        cls.displayargs['out'] = 'str' 
        cls.displayargs['outtarget'] = 'str' 

    def setUp(self):
        syskargs = {}
        self.sx = epyunit.SystemCalls.SystemCalls(**syskargs)

    def testCaseOK(self):
        _call  = self.scri
        _call += " OK "

        ret = self.sx.callit(_call,**self.callkargs)
        assert ret ==  [0, ['fromA', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'], []]

        d = self.sx.displayit(ret,**self.displayargs)
        dX = """exit:   0
stdout: ['fromA', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output']
stderr: []
"""
        assert d == dX
        pass

    def testCaseNOK(self):
        _call  = self.scri
        _call += " NOK "

        ret = self.sx.callit(_call,**self.callkargs)
        assert ret ==  [0, ['fromB', 'arbitrary output', 'arbitrary output'], ['arbitrary signalling ERROR string']]

        d = self.sx.displayit(ret,**self.displayargs)
        dX = """exit:   0
stdout: ['fromB', 'arbitrary output', 'arbitrary output']
stderr: ['arbitrary signalling ERROR string']
"""
        assert d == dX
        pass

    def testCasePRIO(self):
        _call  = self.scri
        _call += " PRIO "

        ret = self.sx.callit(_call,**self.callkargs)
        assert ret ==   [0, ['fromC', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'], ['arbitrary signalling ERROR string']]

        d = self.sx.displayit(ret,**self.displayargs)
        dX = """exit:   0
stdout: ['fromC', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output']
stderr: ['arbitrary signalling ERROR string']
"""
        assert d == dX
        pass

    def testCaseEXITOK(self):
        _call  = self.scri
        _call += " EXITOK "

        ret = self.sx.callit(_call,**self.callkargs)
        assert ret ==  [0, ['fromD', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'], []]

        d = self.sx.displayit(ret,**self.displayargs)
        dX = """exit:   0
stdout: ['fromD', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output']
stderr: []
"""
        assert d == dX
        pass

    def testCaseEXITNOK(self):
        _call  = self.scri
        _call += " EXITNOK "

        ret = self.sx.callit(_call,**self.callkargs)
        assert ret ==   [1, ['fromE', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'], []]

        d = self.sx.displayit(ret,**self.displayargs)
        dX = """exit:   1
stdout: ['fromE', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output']
stderr: []
"""
        assert d == dX
        pass

    def testCaseEXIT7(self):
        _call  = self.scri
        _call += " EXIT7 "

        ret = self.sx.callit(_call,**self.callkargs)
        assert ret ==   [7, ['fromF', 'arbitrary output', 'arbitrary signalling NOK string', 'arbitrary output'], []]

        d = self.sx.displayit(ret,**self.displayargs)
        dX = """exit:   7
stdout: ['fromF', 'arbitrary output', 'arbitrary signalling NOK string', 'arbitrary output']
stderr: []
"""
        assert d == dX
        pass

    def testCaseEXIT8(self):
        _call  = self.scri
        _call += " EXIT8 "

        ret = self.sx.callit(_call,**self.callkargs)
        assert ret ==   [8, ['fromG', 'arbitrary output', 'arbitrary signalling NOK string', 'arbitrary output'], ['arbitrary err output', 'arbitrary err signalling NOK string', 'arbitrary err output']]

        d = self.sx.displayit(ret,**self.displayargs)
        dX = """exit:   8
stdout: ['fromG', 'arbitrary output', 'arbitrary signalling NOK string', 'arbitrary output']
stderr: ['arbitrary err output', 'arbitrary err signalling NOK string', 'arbitrary err output']
"""
        assert d == dX
        pass

    def testCaseEXIT9OK3NOK2(self):
        _call  = self.scri
        _call += " EXIT9OK3NOK2 "

        ret = self.sx.callit(_call,**self.callkargs)
        assert ret ==  [9, ['fromH', 'OK', 'OK', 'OK'], ['NOK', 'NOK']]

        d = self.sx.displayit(ret,**self.displayargs)
        dX = """exit:   9
stdout: ['fromH', 'OK', 'OK', 'OK']
stderr: ['NOK', 'NOK']
"""
        assert d == dX
        pass

    def testCase018_STDERRONLY(self):
        _call  = self.scri
        _call += " STDERRONLY "

        ret = self.sx.callit(_call,**self.callkargs)
        assert ret ==  [0, [], ['fromI', 'NOK', 'NOK']]

        d = self.sx.displayit(ret,**self.displayargs)
        dX = """exit:   0
stdout: []
stderr: ['fromI', 'NOK', 'NOK']
"""
        assert d == dX
        pass

    def testCase100_DEFAULT(self):
        _call  = self.scri
        _call += " DEFAULT "

        ret = self.sx.callit(_call,**self.callkargs)
        assert ret ==   [123, ['arbitrary output'], []]

        d = self.sx.displayit(ret,**self.displayargs)
        dX = """exit:   123
stdout: ['arbitrary output']
stderr: []
"""
        assert d == dX
        pass

#
#######################
#
 
if __name__ == '__main__':
    unittest.main()

