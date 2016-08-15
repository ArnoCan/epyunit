"""Initial raw tests by SubprocessUnit with hard-coded defaults - active remote debug including self_debug-traces. 
"""
from __future__ import absolute_import
from __future__ import print_function
 
__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.10'
__uuid__='9de52399-7752-4633-9fdc-66c87a9200b8'
 
__docformat__ = "restructuredtext en"
 
import unittest
import os
 
from filesysobjects.FileSysObjects import setUpperTreeSearchPath,findRelPathInSearchPath
import epyunit.SubprocUnit 

#
#######################
# 
class CallUnits(unittest.TestCase):

    def __init__(self,*args,**kargs):
        super(CallUnits,self).__init__(*args,**kargs)
        
        self.slst = []
        setUpperTreeSearchPath(os.path.abspath(os.path.dirname(__file__)),'epyunit',self.slst)
        
        syskargs = {}
        self.sx = epyunit.SubprocUnit.SubprocessUnit(**syskargs)

        #
        # wrapper call
        self.epyu   = findRelPathInSearchPath('bin/epyunit',self.slst,matchidx=0)
        self._call  = self.epyu
        self._call += " --raw "
        self._call += " --rdbg "
        self._call += " --pderd_unit_self "
 
        #
        # script call
        self.scri   = findRelPathInSearchPath('epyunit/myscript.sh',self.slst,matchidx=0)
        self.scri   = " -- " + self.scri

    def testCase010(self):
        callkargs = {}
        _call  = self._call
        #_call += " --pderd_debug_self "
        _call += self.scri
        _call += " OK "
        ret = self.sx.callit(_call,**callkargs)
        assert ret[0] ==  0
        assert ret[1] ==  ['fromA', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output']
        assert ret[2] ==  ['RDBG:init PYDEVD', 'RDBG:found pydevd.py', 'RDBG:debug started']

        state = self.sx.apply(ret)
        assert state
        pass

    def testCase011(self):
        callkargs = {}
        _call  = self._call
        _call += self.scri
        _call += " NOK "
        ret = self.sx.callit(_call,**callkargs)
        assert ret[0] ==  0
        assert ret[1] ==  ['fromB', 'arbitrary output', 'arbitrary output']
        assert ret[2] ==  ['RDBG:init PYDEVD', 'RDBG:found pydevd.py', 'RDBG:debug started', 'arbitrary signalling ERROR string']

        state = self.sx.apply(ret)
        assert state
        pass

    def testCase012(self):
        callkargs = {}
        _call  = self._call
        _call += self.scri
        _call += " PRIO "
        ret = self.sx.callit(_call,**callkargs)
        assert ret[0] ==  0
        assert ret[1] ==  ['fromC', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output']
        assert ret[2] ==  ['RDBG:init PYDEVD', 'RDBG:found pydevd.py', 'RDBG:debug started', 'arbitrary signalling ERROR string']

        state = self.sx.apply(ret)
        assert state
        pass

    def testCase013(self):
        callkargs = {}
        _call  = self._call
        _call += self.scri
        _call += " EXITOK "
        ret = self.sx.callit(_call,**callkargs)
        assert ret[0] ==  0
        assert ret[1] ==  ['fromD', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output']
        assert ret[2] ==  ['RDBG:init PYDEVD', 'RDBG:found pydevd.py', 'RDBG:debug started']

        state = self.sx.apply(ret)
        assert state
        pass

    def testCase014(self):
        callkargs = {}
        _call  = self._call
        _call += self.scri
        _call += " EXITNOK "
        ret = self.sx.callit(_call,**callkargs)
        assert ret[0] ==  1
        assert ret[1] ==  ['fromE', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output']
        assert ret[2] ==  ['RDBG:init PYDEVD', 'RDBG:found pydevd.py', 'RDBG:debug started']

        state = self.sx.apply(ret)
        assert not state
        pass

    def testCase015(self):
        callkargs = {}
        _call  = self._call
        _call += self.scri
        _call += " EXIT7 "
        ret = self.sx.callit(_call,**callkargs)
        assert ret[0] ==  7
        assert ret[1] ==  ['fromF', 'arbitrary output', 'arbitrary signalling NOK string', 'arbitrary output']
        assert ret[2] ==  ['RDBG:init PYDEVD', 'RDBG:found pydevd.py', 'RDBG:debug started']

        state = self.sx.apply(ret)
        assert not state
        pass

    def testCase016(self):
        callkargs = {}
        _call  = self._call
        _call += self.scri
        _call += " EXIT8 "
        ret = self.sx.callit(_call,**callkargs)
        assert ret[0] ==  8
        assert ret[1] ==  ['fromG', 'arbitrary output', 'arbitrary signalling NOK string', 'arbitrary output']
        assert ret[2] ==  ['RDBG:init PYDEVD', 'RDBG:found pydevd.py', 'RDBG:debug started','arbitrary err output', 'arbitrary err signalling NOK string', 'arbitrary err output']

        state = self.sx.apply(ret)
        assert not state
        pass

    def testCase017(self):
        callkargs = {}
        _call  = self._call
        _call += self.scri
        _call += " EXIT9OK3NOK2 "
        ret = self.sx.callit(_call,**callkargs)
        assert ret[0] ==  9
        assert ret[1] ==  ['fromH', 'OK', 'OK', 'OK']
        assert ret[2] ==  ['RDBG:init PYDEVD', 'RDBG:found pydevd.py', 'RDBG:debug started', 'NOK', 'NOK']

        state = self.sx.apply(ret)
        assert not state
        pass

    def testCase018(self):
        callkargs = {}
        _call  = self._call
        _call += self.scri
        _call += " DEFAULT "
        ret = self.sx.callit(_call,**callkargs)
        assert ret[0] ==  123
        assert ret[1] ==  ['arbitrary output']
        assert ret[2] ==  ['RDBG:init PYDEVD', 'RDBG:found pydevd.py', 'RDBG:debug started']

        state = self.sx.apply(ret)
        assert not state
        pass

#
#######################
#
 
if __name__ == '__main__':
    unittest.main()

