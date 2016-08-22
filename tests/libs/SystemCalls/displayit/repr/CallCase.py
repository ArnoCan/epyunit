from __future__ import absolute_import
from __future__ import print_function
 
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


        cls.callkargs = {}
        cls.displayargs = {} 

        cls.displayargs['out'] = 'repr' 
        cls.displayargs['outtarget'] = 'str' 


    def setUp(self):
        syskargs = {}
        self.sx = epyunit.SystemCalls.SystemCalls(**syskargs)


    def testCase010_OK(self):
        _call  = self.scri
        _call += " OK "

        ret = self.sx.callit(_call,**self.callkargs)
        assert ret ==  [0, ['fromA', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'], []]

        d = self.sx.displayit(ret,**self.displayargs)
        dX = """[0, ['fromA', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'], []]"""
        assert d == dX
        pass

    def testCase011_NOK(self):
        _call  = self.scri
        _call += " NOK "

        ret = self.sx.callit(_call,**self.callkargs)
        assert ret ==  [0, ['fromB', 'arbitrary output', 'arbitrary output'], ['arbitrary signalling ERROR string']]

        d = self.sx.displayit(ret,**self.displayargs)
        dX = """[0, ['fromB', 'arbitrary output', 'arbitrary output'], ['arbitrary signalling ERROR string']]"""
        assert d == dX
        pass

    def testCase012_PRIO(self):
        _call  = self.scri
        _call += " PRIO "

        ret = self.sx.callit(_call,**self.callkargs)
        assert ret ==   [0, ['fromC', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'], ['arbitrary signalling ERROR string']]

        d = self.sx.displayit(ret,**self.displayargs)
        dX = """[0, ['fromC', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'], ['arbitrary signalling ERROR string']]"""
        assert d == dX
        pass

    def testCase013_EXITOK(self):
        _call  = self.scri
        _call += " EXITOK "

        ret = self.sx.callit(_call,**self.callkargs)
        assert ret ==  [0, ['fromD', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'], []]

        d = self.sx.displayit(ret,**self.displayargs)
        dX = """[0, ['fromD', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'], []]"""
        assert d == dX
        pass

    def testCase014_EXITNOK(self):
        _call  = self.scri
        _call += " EXITNOK "

        ret = self.sx.callit(_call,**self.callkargs)
        assert ret ==   [1, ['fromE', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'], []]

        d = self.sx.displayit(ret,**self.displayargs)
        dX = """[1, ['fromE', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'], []]"""
        assert d == dX
        pass

    def testCase015_EXIT7(self):
        _call  = self.scri
        _call += " EXIT7 "

        ret = self.sx.callit(_call,**self.callkargs)
        assert ret ==   [7, ['fromF', 'arbitrary output', 'arbitrary signalling NOK string', 'arbitrary output'], []]

        d = self.sx.displayit(ret,**self.displayargs)
        dX = """[7, ['fromF', 'arbitrary output', 'arbitrary signalling NOK string', 'arbitrary output'], []]"""
        assert d == dX
        pass

    def testCase016_EXIT8(self):
        _call  = self.scri
        _call += " EXIT8 "

        ret = self.sx.callit(_call,**self.callkargs)
        assert ret ==   [8, ['fromG', 'arbitrary output', 'arbitrary signalling NOK string', 'arbitrary output'], ['arbitrary err output', 'arbitrary err signalling NOK string', 'arbitrary err output']]

        d = self.sx.displayit(ret,**self.displayargs)
        dX = """[8, ['fromG', 'arbitrary output', 'arbitrary signalling NOK string', 'arbitrary output'], ['arbitrary err output', 'arbitrary err signalling NOK string', 'arbitrary err output']]"""
        assert d == dX
        pass

    def testCase017_EXIT9OK3NOK2(self):
        _call  = self.scri
        _call += " EXIT9OK3NOK2 "

        ret = self.sx.callit(_call,**self.callkargs)
        assert ret ==  [9, ['fromH', 'OK', 'OK', 'OK'], ['NOK', 'NOK']]

        d = self.sx.displayit(ret,**self.displayargs)
        dX = """[9, ['fromH', 'OK', 'OK', 'OK'], ['NOK', 'NOK']]"""
        assert d == dX
        pass

    def testCase018_STDERRONLY(self):
        _call  = self.scri
        _call += " STDERRONLY "

        ret = self.sx.callit(_call,**self.callkargs)
        assert ret ==  [0, [], ['fromI', 'NOK', 'NOK']]

        d = self.sx.displayit(ret,**self.displayargs)
        dX = """[0, [], ['fromI', 'NOK', 'NOK']]"""
        assert d == dX
        pass

    def testCase100_DEFAULT(self):
        _call  = self.scri
        _call += " DEFAULT "

        ret = self.sx.callit(_call,**self.callkargs)
        assert ret ==   [123, ['arbitrary output'], []]

        d = self.sx.displayit(ret,**self.displayargs)
        dX = """[123, ['arbitrary output'], []]"""
        assert d == dX
        pass

#
#######################
#
 
if __name__ == '__main__':
    unittest.main()

