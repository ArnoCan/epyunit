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

        self.displayargs['out'] = 'csv' 
        self.displayargs['outtarget'] = 'str' 


    def testCase010(self):
        _call  = self.scri
        _call += " OK "

        ret = self.sx.callit(_call,**self.callkargs)
        assert ret ==  [0, ['fromA', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'], []]

        d = self.sx.displayit(ret,**self.displayargs)
        dX = """exitcode;total-lines;stdout-line;stdout;stderr-line;stderr
0;1;0;fromA;;
0;2;1;arbitrary output;;
0;3;2;arbitrary signalling OK string;;
0;4;3;arbitrary output;;
"""
        assert d == dX
        pass

    def testCase011(self):
        _call  = self.scri
        _call += " NOK "

        ret = self.sx.callit(_call,**self.callkargs)
        assert ret ==  [0, ['fromB', 'arbitrary output', 'arbitrary output'], ['arbitrary signalling ERROR string']]

        d = self.sx.displayit(ret,**self.displayargs)
        dX = """exitcode;total-lines;stdout-line;stdout;stderr-line;stderr
0;1;0;fromB;0;arbitrary signalling ERROR string
0;2;1;arbitrary output;;
0;3;2;arbitrary output;;
"""
        assert d == dX
        pass

    def testCase012(self):
        _call  = self.scri
        _call += " PRIO "

        ret = self.sx.callit(_call,**self.callkargs)
        assert ret ==   [0, ['fromC', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'], ['arbitrary signalling ERROR string']]

        d = self.sx.displayit(ret,**self.displayargs)
        dX = """exitcode;total-lines;stdout-line;stdout;stderr-line;stderr
0;1;0;fromC;0;arbitrary signalling ERROR string
0;2;1;arbitrary output;;
0;3;2;arbitrary signalling OK string;;
0;4;3;arbitrary output;;
"""
        assert d == dX
        pass

    def testCase013(self):
        _call  = self.scri
        _call += " EXITOK "

        ret = self.sx.callit(_call,**self.callkargs)
        assert ret ==  [0, ['fromD', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'], []]

        d = self.sx.displayit(ret,**self.displayargs)
        dX = """exitcode;total-lines;stdout-line;stdout;stderr-line;stderr
0;1;0;fromD;;
0;2;1;arbitrary output;;
0;3;2;arbitrary signalling OK string;;
0;4;3;arbitrary output;;
"""
        assert d == dX
        pass

    def testCase014(self):
        _call  = self.scri
        _call += " EXITNOK "

        ret = self.sx.callit(_call,**self.callkargs)
        assert ret ==   [1, ['fromE', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'], []]

        d = self.sx.displayit(ret,**self.displayargs)
        dX = """exitcode;total-lines;stdout-line;stdout;stderr-line;stderr
1;1;0;fromE;;
1;2;1;arbitrary output;;
1;3;2;arbitrary signalling OK string;;
1;4;3;arbitrary output;;
"""
        assert d == dX
        pass

    def testCase015(self):
        _call  = self.scri
        _call += " EXIT7 "

        ret = self.sx.callit(_call,**self.callkargs)
        assert ret ==   [7, ['fromF', 'arbitrary output', 'arbitrary signalling NOK string', 'arbitrary output'], []]

        d = self.sx.displayit(ret,**self.displayargs)
        dX = """exitcode;total-lines;stdout-line;stdout;stderr-line;stderr
7;1;0;fromF;;
7;2;1;arbitrary output;;
7;3;2;arbitrary signalling NOK string;;
7;4;3;arbitrary output;;
"""
        assert d == dX
        pass

    def testCase016(self):
        _call  = self.scri
        _call += " EXIT8 "

        ret = self.sx.callit(_call,**self.callkargs)
        assert ret ==   [8, ['fromG', 'arbitrary output', 'arbitrary signalling NOK string', 'arbitrary output'], ['arbitrary err output', 'arbitrary err signalling NOK string', 'arbitrary err output']]

        d = self.sx.displayit(ret,**self.displayargs)
        dX = """exitcode;total-lines;stdout-line;stdout;stderr-line;stderr
8;1;0;fromG;0;arbitrary err output
8;2;1;arbitrary output;1;arbitrary err signalling NOK string
8;3;2;arbitrary signalling NOK string;2;arbitrary err output
8;4;3;arbitrary output;;
"""
        assert d == dX
        pass

    def testCase017(self):
        _call  = self.scri
        _call += " EXIT9OK3NOK2 "

        ret = self.sx.callit(_call,**self.callkargs)
        assert ret ==  [9, ['fromH', 'OK', 'OK', 'OK'], ['NOK', 'NOK']]

        d = self.sx.displayit(ret,**self.displayargs)
        dX = """exitcode;total-lines;stdout-line;stdout;stderr-line;stderr
9;1;0;fromH;0;NOK
9;2;1;OK;1;NOK
9;3;2;OK;;
9;4;3;OK;;
"""
        assert d == dX
        pass

    def testCase018(self):
        _call  = self.scri
        _call += " STDERRONLY "

        ret = self.sx.callit(_call,**self.callkargs)
        assert ret ==  [0, [], ['fromI', 'NOK', 'NOK']]

        d = self.sx.displayit(ret,**self.displayargs)
        dX = """exitcode;total-lines;stdout-line;stdout;stderr-line;stderr
0;1;;;0;fromI
0;2;;;1;NOK
0;3;;;2;NOK
"""
        assert d == dX
        pass

    def testCase100(self):
        _call  = self.scri
        _call += " DEFAULT "

        ret = self.sx.callit(_call,**self.callkargs)
        assert ret ==   [123, ['arbitrary output'], []]

        d = self.sx.displayit(ret,**self.displayargs)
        dX = """exitcode;total-lines;stdout-line;stdout;stderr-line;stderr
123;1;0;arbitrary output;;
"""
        assert d == dX
        pass

#
#######################
#
 
if __name__ == '__main__':
    unittest.main()
