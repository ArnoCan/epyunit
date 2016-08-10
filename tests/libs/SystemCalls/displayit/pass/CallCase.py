from __future__ import absolute_import
#from __future__ import print_function
 
__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.10'
__uuid__='9de52399-7752-4633-9fdc-66c87a9200b8'
 
__docformat__ = "restructuredtext en"
 
import unittest
import os
 
from filesysobjects.FileSysObjects import setUpperTreeSearchPath,findRelPathInSearchPath
import epyunit.SystemCalls 

#
#######################
# 
class CallUnits(unittest.TestCase):

    def __init__(self,*args,**kargs):
        super(CallUnits,self).__init__(*args,**kargs)
        
        self.slst = []
        setUpperTreeSearchPath(os.path.abspath(os.path.dirname(__file__)),'epyunit',self.slst)
        
        syskargs = {}
        self.sx = epyunit.SystemCalls.SystemCalls(**syskargs)

        self.epyu = findRelPathInSearchPath('bin/epyunit',self.slst,matchidx=0)
        self.scri = findRelPathInSearchPath('epyunit/myscript.sh',self.slst,matchidx=0)
        self.scri = self.scri

        self.callkargs = {}
        self.displayargs = {} 

        self.displayargs['out'] = 'pass' 
        self.displayargs['outtarget'] = 'str' 


    def testCase010(self):
        _call  = self.scri
        _call += " OK "

        ret = self.sx.callit(_call,**self.callkargs)
        assert ret ==  [0, ['fromA', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'], []]

        d = self.sx.displayit(ret,**self.displayargs)
        dX = """fromA
arbitrary output
arbitrary signalling OK string
arbitrary output
"""
        assert d == dX
        pass

    def testCase011(self):
        _call  = self.scri
        _call += " NOK "

        ret = self.sx.callit(_call,**self.callkargs)
        assert ret ==  [0, ['fromB', 'arbitrary output', 'arbitrary output'], ['arbitrary signalling ERROR string']]

        d = self.sx.displayit(ret,**self.displayargs)
        dX = """fromB
arbitrary output
arbitrary output
arbitrary signalling ERROR string
"""
        assert d == dX
        pass

    def testCase012(self):
        _call  = self.scri
        _call += " PRIO "

        ret = self.sx.callit(_call,**self.callkargs)
        assert ret ==   [0, ['fromC', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'], ['arbitrary signalling ERROR string']]

        d = self.sx.displayit(ret,**self.displayargs)
        dX = """fromC
arbitrary output
arbitrary signalling OK string
arbitrary output
arbitrary signalling ERROR string
"""
        assert d == dX
        pass

    def testCase013(self):
        _call  = self.scri
        _call += " EXITOK "

        ret = self.sx.callit(_call,**self.callkargs)
        assert ret ==  [0, ['fromD', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'], []]

        d = self.sx.displayit(ret,**self.displayargs)
        dX = """fromD
arbitrary output
arbitrary signalling OK string
arbitrary output
"""
        assert d == dX
        pass

    def testCase014(self):
        _call  = self.scri
        _call += " EXITNOK "

        ret = self.sx.callit(_call,**self.callkargs)
        assert ret ==   [1, ['fromE', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'], []]

        d = self.sx.displayit(ret,**self.displayargs)
        dX = """fromE
arbitrary output
arbitrary signalling OK string
arbitrary output
"""
        assert d == dX
        pass

    def testCase015(self):
        _call  = self.scri
        _call += " EXIT7 "

        ret = self.sx.callit(_call,**self.callkargs)
        assert ret ==   [7, ['fromF', 'arbitrary output', 'arbitrary signalling NOK string', 'arbitrary output'], []]

        d = self.sx.displayit(ret,**self.displayargs)
        dX = """fromF
arbitrary output
arbitrary signalling NOK string
arbitrary output
"""
        assert d == dX
        pass

    def testCase016(self):
        _call  = self.scri
        _call += " EXIT8 "

        ret = self.sx.callit(_call,**self.callkargs)
        assert ret ==   [8, ['fromG', 'arbitrary output', 'arbitrary signalling NOK string', 'arbitrary output'], ['arbitrary err output', 'arbitrary err signalling NOK string', 'arbitrary err output']]

        d = self.sx.displayit(ret,**self.displayargs)
        dX = """fromG
arbitrary output
arbitrary signalling NOK string
arbitrary output
arbitrary err output
arbitrary err signalling NOK string
arbitrary err output
"""
        assert d == dX
        pass

    def testCase017(self):
        _call  = self.scri
        _call += " EXIT9OK3NOK2 "

        ret = self.sx.callit(_call,**self.callkargs)
        assert ret ==  [9, ['fromH', 'OK', 'OK', 'OK'], ['NOK', 'NOK']]

        d = self.sx.displayit(ret,**self.displayargs)
        dX = """fromH
OK
OK
OK
NOK
NOK
"""
        assert d == dX
        pass

    def testCase018(self):
        _call  = self.scri
        _call += " STDERRONLY "

        ret = self.sx.callit(_call,**self.callkargs)
        assert ret ==  [0, [], ['fromI', 'NOK', 'NOK']]

        d = self.sx.displayit(ret,**self.displayargs)
        dX = """fromI
NOK
NOK
"""
        assert d == dX
        pass

    def testCase100(self):
        _call  = self.scri
        _call += " DEFAULT "

        ret = self.sx.callit(_call,**self.callkargs)
        assert ret ==   [123, ['arbitrary output'], []]

        d = self.sx.displayit(ret,**self.displayargs)
        dX = """arbitrary output
"""
        assert d == dX
        pass

#
#######################
#
 
if __name__ == '__main__':
    unittest.main()

