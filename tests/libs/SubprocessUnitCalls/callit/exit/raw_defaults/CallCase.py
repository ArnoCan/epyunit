"""Initial raw tests by SubprocessUnit with hard-coded defaults.

Due to the basic character of the test these are done a little more than less.

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
from testdata import call_scripy,epyu

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

        cls.epyu = epyu

        cls.scri = call_scripy
        cls.scri = cls.scri

    def setUp(self):
        syskargs = {}
        self.sx = epyunit.SubprocUnit.SubprocessUnit(**syskargs)

        # epyunit.SProcUnitRules
        if self.sx.getruleset():
            _repr = repr(self.sx.getruleset())
            _reprX = """{'default': True, 'cflags': 0, 'multiline': 0, 'ignorecase': 0, 'unicode': 0, 'dotall': 0, 'debug': 0, 'priotype': 1, 'result': 0, 'resultok': 0, 'resultnok': 0, 'exitign': False, 'exittype': 8, 'exitval': 0, 'stderrchk': False, 'stderrnok': [], 'stderrok': [], 'stdoutchk': False, 'stdoutnok': [], 'stdoutok': []}"""
            assert _repr == _reprX

            _s0 = self.sx.getruleset().states()
            _s0X = {'resultok': 0, 'stdoutok': [], 'exit': 0, '_exitcond': False, 'stdoutnok': [], 'resultnok': 0, 'stderrnok': [], 'stderrok': [], 'result': 0}
            assert _s0 == _s0X

    def testCaseOK(self):
        _call  = self.scri
        _call += " OK "

        callkargs = {}

        ret = self.sx.callit(_call,**callkargs)
        assert ret ==  [0, ['fromA', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'], []]

        state = self.sx.apply(ret)
        assert state
        pass

    def testCaseNOK(self):
        callkargs = {}
        _call = self.scri
        _call += " NOK "

        ret = self.sx.callit(_call,**callkargs)
        assert ret ==   [0, ['fromB', 'arbitrary output', 'arbitrary output'], ['arbitrary signalling ERROR string']]

        state = self.sx.apply(ret)
        assert state
        pass

    def testCasePRIO(self):
        callkargs = {}
        _call = self.scri
        _call += " PRIO "

        ret = self.sx.callit(_call,**callkargs)
        assert ret ==  [0, ['fromC', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'], ['arbitrary signalling ERROR string']]

        state = self.sx.apply(ret)
        assert state
        pass

    def testCaseEXITOK(self):
        callkargs = {}
        _call = self.scri
        _call += " EXITOK "

        ret = self.sx.callit(_call,**callkargs)
        assert ret ==  [0, ['fromD', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'], []]

        state = self.sx.apply(ret)
        assert state
        pass

    def testCaseEXITNOK(self):
        callkargs = {}
        _call = self.scri
        _call += " EXITNOK "

        ret = self.sx.callit(_call,**callkargs)
        assert ret ==  [1, ['fromE', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'], []]

        state = self.sx.apply(ret)
        assert not state
        pass

    def testCaseEXIT7(self):
        callkargs = {}
        _call = self.scri
        _call += " EXIT7 "

        ret = self.sx.callit(_call,**callkargs)
        assert ret ==  [7, ['fromF', 'arbitrary output', 'arbitrary signalling NOK string', 'arbitrary output'], []]

        state = self.sx.apply(ret)
        assert not state
        pass

    def testCaseEXIT8(self):
        callkargs = {}
        _call = self.scri
        _call += " EXIT8 "

        ret = self.sx.callit(_call,**callkargs)
        assert ret ==   [8, ['fromG', 'arbitrary output', 'arbitrary signalling NOK string', 'arbitrary output'], ['arbitrary err output', 'arbitrary err signalling NOK string', 'arbitrary err output']]

        state = self.sx.apply(ret)
        assert not state
        pass

    def testCaseEXIT9OK3NOK2(self):
        callkargs = {}
        _call = self.scri
        _call += " EXIT9OK3NOK2 "

        ret = self.sx.callit(_call,**callkargs)
        assert ret ==   [9, ['fromH', 'OK', 'OK', 'OK'], ['NOK', 'NOK']]

        state = self.sx.apply(ret)
        assert not state
        pass

    def testCaseDEFAULT(self):
        callkargs = {}
        _call = self.scri
        _call += " DEFAULT "

        ret = self.sx.callit(_call,**callkargs)
        assert ret ==   [123, ['arbitrary output'], []]

        state = self.sx.apply(ret)
        assert not state
        pass

#
#######################
#

if __name__ == '__main__':
    unittest.main()

