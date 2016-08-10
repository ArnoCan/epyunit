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
        
        self.slst = []
        setUpperTreeSearchPath(os.path.abspath(os.path.dirname(__file__)),'epyunit',self.slst)
        
        syskargs = {}
        self.sx = epyunit.SystemCalls.SystemCalls(**syskargs)

        self.epyu = findRelPathInSearchPath('bin/epyunit',self.slst,matchidx=0)
        self.scri = findRelPathInSearchPath('epyunit/myscript.sh',self.slst,matchidx=0)
        self.scri = self.scri

        self.callkargs = {}
        self.displayargs = {} 

        self.displayargs['out'] = 'xml' 
        self.displayargs['outtarget'] = 'str' 


    def testCase010(self):
        _call  = self.scri
        _call += " OK "

        ret = self.sx.callit(_call,**self.callkargs)
        assert ret ==  [0, ['fromA', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'], []]

        d = self.sx.displayit(ret,**self.displayargs)
        dX = """<?xml version="1.0" encoding="UTF-8"?>
<test-result >
    <exit-code>0</exit-code>
    <stdout>
        <line cnt=0>fromA</line>
        <line cnt=1>arbitrary output</line>
        <line cnt=2>arbitrary signalling OK string</line>
        <line cnt=3>arbitrary output</line>
    </stdout>
    <stderr>
    </stderr>
</test-result>"""
        assert d == dX
        pass

    def testCase011(self):
        _call  = self.scri
        _call += " NOK "

        ret = self.sx.callit(_call,**self.callkargs)
        assert ret ==  [0, ['fromB', 'arbitrary output', 'arbitrary output'], ['arbitrary signalling ERROR string']]

        d = self.sx.displayit(ret,**self.displayargs)
        dX = """<?xml version="1.0" encoding="UTF-8"?>
<test-result >
    <exit-code>0</exit-code>
    <stdout>
        <line cnt=0>fromB</line>
        <line cnt=1>arbitrary output</line>
        <line cnt=2>arbitrary output</line>
    </stdout>
    <stderr>
        <line cnt=0>arbitrary signalling ERROR string</line>
    </stderr>
</test-result>"""
        assert d == dX
        pass

    def testCase012(self):
        _call  = self.scri
        _call += " PRIO "

        ret = self.sx.callit(_call,**self.callkargs)
        assert ret ==   [0, ['fromC', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'], ['arbitrary signalling ERROR string']]

        d = self.sx.displayit(ret,**self.displayargs)
        dX = """<?xml version="1.0" encoding="UTF-8"?>
<test-result >
    <exit-code>0</exit-code>
    <stdout>
        <line cnt=0>fromC</line>
        <line cnt=1>arbitrary output</line>
        <line cnt=2>arbitrary signalling OK string</line>
        <line cnt=3>arbitrary output</line>
    </stdout>
    <stderr>
        <line cnt=0>arbitrary signalling ERROR string</line>
    </stderr>
</test-result>"""
        assert d == dX
        pass

    def testCase013(self):
        _call  = self.scri
        _call += " EXITOK "

        ret = self.sx.callit(_call,**self.callkargs)
        assert ret ==  [0, ['fromD', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'], []]

        d = self.sx.displayit(ret,**self.displayargs)
        dX = """<?xml version="1.0" encoding="UTF-8"?>
<test-result >
    <exit-code>0</exit-code>
    <stdout>
        <line cnt=0>fromD</line>
        <line cnt=1>arbitrary output</line>
        <line cnt=2>arbitrary signalling OK string</line>
        <line cnt=3>arbitrary output</line>
    </stdout>
    <stderr>
    </stderr>
</test-result>"""
        assert d == dX
        pass

    def testCase014(self):
        _call  = self.scri
        _call += " EXITNOK "

        ret = self.sx.callit(_call,**self.callkargs)
        assert ret ==   [1, ['fromE', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'], []]

        d = self.sx.displayit(ret,**self.displayargs)
        dX = """<?xml version="1.0" encoding="UTF-8"?>
<test-result >
    <exit-code>1</exit-code>
    <stdout>
        <line cnt=0>fromE</line>
        <line cnt=1>arbitrary output</line>
        <line cnt=2>arbitrary signalling OK string</line>
        <line cnt=3>arbitrary output</line>
    </stdout>
    <stderr>
    </stderr>
</test-result>"""
        assert d == dX
        pass

    def testCase015(self):
        _call  = self.scri
        _call += " EXIT7 "

        ret = self.sx.callit(_call,**self.callkargs)
        assert ret ==   [7, ['fromF', 'arbitrary output', 'arbitrary signalling NOK string', 'arbitrary output'], []]

        d = self.sx.displayit(ret,**self.displayargs)
        dX = """<?xml version="1.0" encoding="UTF-8"?>
<test-result >
    <exit-code>7</exit-code>
    <stdout>
        <line cnt=0>fromF</line>
        <line cnt=1>arbitrary output</line>
        <line cnt=2>arbitrary signalling NOK string</line>
        <line cnt=3>arbitrary output</line>
    </stdout>
    <stderr>
    </stderr>
</test-result>"""
        assert d == dX
        pass

    def testCase016(self):
        _call  = self.scri
        _call += " EXIT8 "

        ret = self.sx.callit(_call,**self.callkargs)
        assert ret ==   [8, ['fromG', 'arbitrary output', 'arbitrary signalling NOK string', 'arbitrary output'], ['arbitrary err output', 'arbitrary err signalling NOK string', 'arbitrary err output']]

        d = self.sx.displayit(ret,**self.displayargs)
        dX = """<?xml version="1.0" encoding="UTF-8"?>
<test-result >
    <exit-code>8</exit-code>
    <stdout>
        <line cnt=0>fromG</line>
        <line cnt=1>arbitrary output</line>
        <line cnt=2>arbitrary signalling NOK string</line>
        <line cnt=3>arbitrary output</line>
    </stdout>
    <stderr>
        <line cnt=0>arbitrary err output</line>
        <line cnt=1>arbitrary err signalling NOK string</line>
        <line cnt=2>arbitrary err output</line>
    </stderr>
</test-result>"""
        assert d == dX
        pass

    def testCase017(self):
        _call  = self.scri
        _call += " EXIT9OK3NOK2 "

        ret = self.sx.callit(_call,**self.callkargs)
        assert ret ==  [9, ['fromH', 'OK', 'OK', 'OK'], ['NOK', 'NOK']]

        d = self.sx.displayit(ret,**self.displayargs)
        dX = """<?xml version="1.0" encoding="UTF-8"?>
<test-result >
    <exit-code>9</exit-code>
    <stdout>
        <line cnt=0>fromH</line>
        <line cnt=1>OK</line>
        <line cnt=2>OK</line>
        <line cnt=3>OK</line>
    </stdout>
    <stderr>
        <line cnt=0>NOK</line>
        <line cnt=1>NOK</line>
    </stderr>
</test-result>"""
        assert d == dX
        pass

    def testCase018(self):
        _call  = self.scri
        _call += " DEFAULT "

        ret = self.sx.callit(_call,**self.callkargs)
        assert ret ==   [123, ['arbitrary output'], []]

        d = self.sx.displayit(ret,**self.displayargs)
        dX = """<?xml version="1.0" encoding="UTF-8"?>
<test-result >
    <exit-code>123</exit-code>
    <stdout>
        <line cnt=0>arbitrary output</line>
    </stdout>
    <stderr>
    </stderr>
</test-result>"""
        assert d == dX
        pass

#
#######################
#
 
if __name__ == '__main__':
    unittest.main()

