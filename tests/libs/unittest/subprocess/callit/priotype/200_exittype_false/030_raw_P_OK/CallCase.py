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
import os,sys
from testdata import epyu,call_scripy
from filesysobjects.FileSysObjects import setUpperTreeSearchPath,findRelPathInSearchPath
import epyunit.SubprocUnit

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

        cls._call  = epyu
        cls._call += " --raw "
        cls._call += " --priotype=True "
        cls._call += " --exittype=False "
        cls._call += " " + call_scripy

    def setUp(self):
        syskargs = {}
        self.sx = epyunit.SubprocUnit.SubprocessUnit(**syskargs)

    def testCase010(self):
        _call  = self._call
        _call += " OK "

        # epyunit.SProcUnitRules
        if self.sx.getruleset():
            _repr = repr(self.sx.getruleset())
            _reprX = """{'default': True, 'cflags': 0, 'multiline': 0, 'ignorecase': 0, 'unicode': 0, 'dotall': 0, 'debug': 0, 'priotype': 1, 'result': 0, 'resultok': 0, 'resultnok': 0, 'exitign': False, 'exittype': 8, 'exitval': 0, 'stderrchk': False, 'stderrnok': [], 'stderrok': [], 'stdoutchk': False, 'stdoutnok': [], 'stdoutok': []}"""
            assert _repr == _reprX

            _s0 = self.sx.getruleset().states() # For debug
            _s0X = {'resultok': 0, 'stdoutok': [], 'exit': 0, '_exitcond': False, 'stdoutnok': [], 'resultnok': 0, 'stderrnok': [], 'stderrok': [], 'result': 0}
            assert _s0 == _s0X

        ret = self.sx.callit(_call)
        assert ret ==  [0, ['fromA', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'], []]

        state = self.sx.apply(ret)
        _s1 = self.sx.getruleset().states() # For debug
        assert state

        # epyunit.SProcUnitRules
        if self.sx.getruleset():
            _repr = repr(self.sx.getruleset())
            _reprX = """{'default': True, 'cflags': 0, 'multiline': 0, 'ignorecase': 0, 'unicode': 0, 'dotall': 0, 'debug': 0, 'priotype': 1, 'result': 0, 'resultok': 0, 'resultnok': 0, 'exitign': False, 'exittype': 8, 'exitval': 0, 'stderrchk': False, 'stderrnok': [], 'stderrok': [], 'stdoutchk': False, 'stdoutnok': [], 'stdoutok': []}"""
            assert _repr == _reprX

            _s = self.sx.getruleset().states() # For debug
            _sX = {'resultok': 0, 'stdoutok': [], 'exit': 0, '_exitcond': True, 'stdoutnok': [], 'resultnok': 0, 'stderrnok': [], 'stderrok': [], 'result': 0}
            assert _s == _sX

        pass

    def testCase011(self):
        _call  = self._call
        _call += " NOK "

        # epyunit.SProcUnitRules
        if self.sx.getruleset():
            _repr = repr(self.sx.getruleset())
            _reprX = """{'default': True, 'cflags': 0, 'multiline': 0, 'ignorecase': 0, 'unicode': 0, 'dotall': 0, 'debug': 0, 'priotype': 1, 'result': 0, 'resultok': 0, 'resultnok': 0, 'exitign': False, 'exittype': 8, 'exitval': 0, 'stderrchk': False, 'stderrnok': [], 'stderrok': [], 'stdoutchk': False, 'stdoutnok': [], 'stdoutok': []}"""
            assert _repr == _reprX

            _s0 = self.sx.getruleset().states() # For debug
            _s0X = {'resultok': 0, 'stdoutok': [], 'exit': 0, '_exitcond': False, 'stdoutnok': [], 'resultnok': 0, 'stderrnok': [], 'stderrok': [], 'result': 0}
            assert _s0 == _s0X

        ret = self.sx.callit(_call)
        assert ret ==   [0, ['fromB', 'arbitrary output', 'arbitrary output'], ['arbitrary signalling ERROR string']]

        state = self.sx.apply(ret)
        _s1 = self.sx.getruleset().states() # For debug
        assert state

        # epyunit.SProcUnitRules
        if self.sx.getruleset():
            _repr = repr(self.sx.getruleset())
            _reprX = """{'default': True, 'cflags': 0, 'multiline': 0, 'ignorecase': 0, 'unicode': 0, 'dotall': 0, 'debug': 0, 'priotype': 1, 'result': 0, 'resultok': 0, 'resultnok': 0, 'exitign': False, 'exittype': 8, 'exitval': 0, 'stderrchk': False, 'stderrnok': [], 'stderrok': [], 'stdoutchk': False, 'stdoutnok': [], 'stdoutok': []}"""
            assert _repr == _reprX

            _s = self.sx.getruleset().states() # For debug
            _sX = {'resultok': 0, 'stdoutok': [], 'exit': 0, '_exitcond': True, 'stdoutnok': [], 'resultnok': 0, 'stderrnok': [], 'stderrok': [], 'result': 0}
            assert _s == _sX

        pass

    def testCase012(self):
        _call  = self._call
        _call += " PRIO "

        # epyunit.SProcUnitRules
        if self.sx.getruleset():
            _repr = repr(self.sx.getruleset())
            _reprX = """{'default': True, 'cflags': 0, 'multiline': 0, 'ignorecase': 0, 'unicode': 0, 'dotall': 0, 'debug': 0, 'priotype': 1, 'result': 0, 'resultok': 0, 'resultnok': 0, 'exitign': False, 'exittype': 8, 'exitval': 0, 'stderrchk': False, 'stderrnok': [], 'stderrok': [], 'stdoutchk': False, 'stdoutnok': [], 'stdoutok': []}"""
            assert _repr == _reprX

            _s0 = self.sx.getruleset().states() # For debug
            _s0X = {'resultok': 0, 'stdoutok': [], 'exit': 0, '_exitcond': False, 'stdoutnok': [], 'resultnok': 0, 'stderrnok': [], 'stderrok': [], 'result': 0}
            assert _s0 == _s0X

        ret = self.sx.callit(_call)
        assert ret ==  [0, ['fromC', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'], ['arbitrary signalling ERROR string']]

        state = self.sx.apply(ret)
        _s1 = self.sx.getruleset().states() # For debug
        assert state

        # epyunit.SProcUnitRules
        if self.sx.getruleset():
            _repr = repr(self.sx.getruleset())
            _reprX = """{'default': True, 'cflags': 0, 'multiline': 0, 'ignorecase': 0, 'unicode': 0, 'dotall': 0, 'debug': 0, 'priotype': 1, 'result': 0, 'resultok': 0, 'resultnok': 0, 'exitign': False, 'exittype': 8, 'exitval': 0, 'stderrchk': False, 'stderrnok': [], 'stderrok': [], 'stdoutchk': False, 'stdoutnok': [], 'stdoutok': []}"""
            assert _repr == _reprX

            _s = self.sx.getruleset().states() # For debug
            _sX = {'resultok': 0, 'stdoutok': [], 'exit': 0, '_exitcond': True, 'stdoutnok': [], 'resultnok': 0, 'stderrnok': [], 'stderrok': [], 'result': 0}
            assert _s == _sX

        pass

    def testCase013(self):
        _call  = self._call
        _call += " EXITOK "

        # epyunit.SProcUnitRules
        if self.sx.getruleset():
            _repr = repr(self.sx.getruleset())
            _reprX = """{'default': True, 'cflags': 0, 'multiline': 0, 'ignorecase': 0, 'unicode': 0, 'dotall': 0, 'debug': 0, 'priotype': 1, 'result': 0, 'resultok': 0, 'resultnok': 0, 'exitign': False, 'exittype': 8, 'exitval': 0, 'stderrchk': False, 'stderrnok': [], 'stderrok': [], 'stdoutchk': False, 'stdoutnok': [], 'stdoutok': []}"""
            assert _repr == _reprX

            _s0 = self.sx.getruleset().states() # For debug
            _s0X = {'resultok': 0, 'stdoutok': [], 'exit': 0, '_exitcond': False, 'stdoutnok': [], 'resultnok': 0, 'stderrnok': [], 'stderrok': [], 'result': 0}
            assert _s0 == _s0X

        ret = self.sx.callit(_call)
        assert ret ==  [0, ['fromD', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'], []]

        state = self.sx.apply(ret)
        _s1 = self.sx.getruleset().states() # For debug
        assert state

        # epyunit.SProcUnitRules
        if self.sx.getruleset():
            _repr = repr(self.sx.getruleset())
            _reprX = """{'default': True, 'cflags': 0, 'multiline': 0, 'ignorecase': 0, 'unicode': 0, 'dotall': 0, 'debug': 0, 'priotype': 1, 'result': 0, 'resultok': 0, 'resultnok': 0, 'exitign': False, 'exittype': 8, 'exitval': 0, 'stderrchk': False, 'stderrnok': [], 'stderrok': [], 'stdoutchk': False, 'stdoutnok': [], 'stdoutok': []}"""
            assert _repr == _reprX

            _s = self.sx.getruleset().states() # For debug
            _sX = {'resultok': 0, 'stdoutok': [], 'exit': 0, '_exitcond': True, 'stdoutnok': [], 'resultnok': 0, 'stderrnok': [], 'stderrok': [], 'result': 0}
            assert _s == _sX

        pass

    def testCase014(self):
        _call  = self._call
        _call += " EXITNOK "

        # epyunit.SProcUnitRules
        if self.sx.getruleset():
            _repr = repr(self.sx.getruleset())
            _reprX = """{'default': True, 'cflags': 0, 'multiline': 0, 'ignorecase': 0, 'unicode': 0, 'dotall': 0, 'debug': 0, 'priotype': 1, 'result': 0, 'resultok': 0, 'resultnok': 0, 'exitign': False, 'exittype': 8, 'exitval': 0, 'stderrchk': False, 'stderrnok': [], 'stderrok': [], 'stdoutchk': False, 'stdoutnok': [], 'stdoutok': []}"""
            assert _repr == _reprX

            _s0 = self.sx.getruleset().states() # For debug
            _s0X = {'resultok': 0, 'stdoutok': [], 'exit': 0, '_exitcond': False, 'stdoutnok': [], 'resultnok': 0, 'stderrnok': [], 'stderrok': [], 'result': 0}
            assert _s0 == _s0X

        ret = self.sx.callit(_call)
        assert ret ==  [1, ['fromE', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'], []]

        state = self.sx.apply(ret)
        _s1 = self.sx.getruleset().states() # For debug
        assert not state

        # epyunit.SProcUnitRules
        if self.sx.getruleset():
            _repr = repr(self.sx.getruleset())
            _reprX = """{'default': True, 'cflags': 0, 'multiline': 0, 'ignorecase': 0, 'unicode': 0, 'dotall': 0, 'debug': 0, 'priotype': 1, 'result': 0, 'resultok': 0, 'resultnok': 0, 'exitign': False, 'exittype': 8, 'exitval': 0, 'stderrchk': False, 'stderrnok': [], 'stderrok': [], 'stdoutchk': False, 'stdoutnok': [], 'stdoutok': []}"""
            assert _repr == _reprX

            _s = self.sx.getruleset().states() # For debug
            _sX = {'resultok': 0, 'stdoutok': [], 'exit': 1, '_exitcond': False, 'stdoutnok': [], 'resultnok': 0, 'stderrnok': [], 'stderrok': [], 'result': 0}
            assert _s == _sX

        pass

    def testCase015(self):
        _call  = self._call
        _call += " EXIT7 "

        # epyunit.SProcUnitRules
        if self.sx.getruleset():
            _repr = repr(self.sx.getruleset())
            _reprX = """{'default': True, 'cflags': 0, 'multiline': 0, 'ignorecase': 0, 'unicode': 0, 'dotall': 0, 'debug': 0, 'priotype': 1, 'result': 0, 'resultok': 0, 'resultnok': 0, 'exitign': False, 'exittype': 8, 'exitval': 0, 'stderrchk': False, 'stderrnok': [], 'stderrok': [], 'stdoutchk': False, 'stdoutnok': [], 'stdoutok': []}"""
            assert _repr == _reprX

            _s0 = self.sx.getruleset().states() # For debug
            _s0X = {'resultok': 0, 'stdoutok': [], 'exit': 0, '_exitcond': False, 'stdoutnok': [], 'resultnok': 0, 'stderrnok': [], 'stderrok': [], 'result': 0}
            assert _s0 == _s0X

        ret = self.sx.callit(_call)
        assert ret ==  [7, ['fromF', 'arbitrary output', 'arbitrary signalling NOK string', 'arbitrary output'], []]

        state = self.sx.apply(ret)
        _s1 = self.sx.getruleset().states() # For debug
        assert not state

        # epyunit.SProcUnitRules
        if self.sx.getruleset():
            _repr = repr(self.sx.getruleset())
            _reprX = """{'default': True, 'cflags': 0, 'multiline': 0, 'ignorecase': 0, 'unicode': 0, 'dotall': 0, 'debug': 0, 'priotype': 1, 'result': 0, 'resultok': 0, 'resultnok': 0, 'exitign': False, 'exittype': 8, 'exitval': 0, 'stderrchk': False, 'stderrnok': [], 'stderrok': [], 'stdoutchk': False, 'stdoutnok': [], 'stdoutok': []}"""
            assert _repr == _reprX

            _s = self.sx.getruleset().states() # For debug
            _sX = {'resultok': 0, 'stdoutok': [], 'exit': 7, '_exitcond': False, 'stdoutnok': [], 'resultnok': 0, 'stderrnok': [], 'stderrok': [], 'result': 0}
            assert _s == _sX

        pass

    def testCase016(self):
        _call  = self._call
        _call += " EXIT8 "

        # epyunit.SProcUnitRules
        if self.sx.getruleset():
            _repr = repr(self.sx.getruleset())
            _reprX = """{'default': True, 'cflags': 0, 'multiline': 0, 'ignorecase': 0, 'unicode': 0, 'dotall': 0, 'debug': 0, 'priotype': 1, 'result': 0, 'resultok': 0, 'resultnok': 0, 'exitign': False, 'exittype': 8, 'exitval': 0, 'stderrchk': False, 'stderrnok': [], 'stderrok': [], 'stdoutchk': False, 'stdoutnok': [], 'stdoutok': []}"""
            assert _repr == _reprX

            _s0 = self.sx.getruleset().states() # For debug
            _s0X = {'resultok': 0, 'stdoutok': [], 'exit': 0, '_exitcond': False, 'stdoutnok': [], 'resultnok': 0, 'stderrnok': [], 'stderrok': [], 'result': 0}
            assert _s0 == _s0X

        ret = self.sx.callit(_call)
        assert ret ==   [8, ['fromG', 'arbitrary output', 'arbitrary signalling NOK string', 'arbitrary output'], ['arbitrary err output', 'arbitrary err signalling NOK string', 'arbitrary err output']]

        state = self.sx.apply(ret)
        _s1 = self.sx.getruleset().states() # For debug
        assert not state

        # epyunit.SProcUnitRules
        if self.sx.getruleset():
            _repr = repr(self.sx.getruleset())
            _reprX = """{'default': True, 'cflags': 0, 'multiline': 0, 'ignorecase': 0, 'unicode': 0, 'dotall': 0, 'debug': 0, 'priotype': 1, 'result': 0, 'resultok': 0, 'resultnok': 0, 'exitign': False, 'exittype': 8, 'exitval': 0, 'stderrchk': False, 'stderrnok': [], 'stderrok': [], 'stdoutchk': False, 'stdoutnok': [], 'stdoutok': []}"""
            assert _repr == _reprX

            _s = self.sx.getruleset().states() # For debug
            _sX = {'resultok': 0, 'stdoutok': [], 'exit': 8, '_exitcond': False, 'stdoutnok': [], 'resultnok': 0, 'stderrnok': [], 'stderrok': [], 'result': 0}
            assert _s == _sX

        pass

    def testCase017(self):
        _call  = self._call
        _call += " EXIT9OK3NOK2 "

        # epyunit.SProcUnitRules
        if self.sx.getruleset():
            _repr = repr(self.sx.getruleset())
            _reprX = """{'default': True, 'cflags': 0, 'multiline': 0, 'ignorecase': 0, 'unicode': 0, 'dotall': 0, 'debug': 0, 'priotype': 1, 'result': 0, 'resultok': 0, 'resultnok': 0, 'exitign': False, 'exittype': 8, 'exitval': 0, 'stderrchk': False, 'stderrnok': [], 'stderrok': [], 'stdoutchk': False, 'stdoutnok': [], 'stdoutok': []}"""
            assert _repr == _reprX

            _s0 = self.sx.getruleset().states() # For debug
            _s0X = {'resultok': 0, 'stdoutok': [], 'exit': 0, '_exitcond': False, 'stdoutnok': [], 'resultnok': 0, 'stderrnok': [], 'stderrok': [], 'result': 0}
            assert _s0 == _s0X

        ret = self.sx.callit(_call)
        assert ret ==   [9, ['fromH', 'OK', 'OK', 'OK'], ['NOK', 'NOK']]

        state = self.sx.apply(ret)
        _s1 = self.sx.getruleset().states() # For debug
        assert not state

        # epyunit.SProcUnitRules
        if self.sx.getruleset():
            _repr = repr(self.sx.getruleset())
            _reprX = """{'default': True, 'cflags': 0, 'multiline': 0, 'ignorecase': 0, 'unicode': 0, 'dotall': 0, 'debug': 0, 'priotype': 1, 'result': 0, 'resultok': 0, 'resultnok': 0, 'exitign': False, 'exittype': 8, 'exitval': 0, 'stderrchk': False, 'stderrnok': [], 'stderrok': [], 'stdoutchk': False, 'stdoutnok': [], 'stdoutok': []}"""
            assert _repr == _reprX

            _s = self.sx.getruleset().states() # For debug
            _sX = {'resultok': 0, 'stdoutok': [], 'exit': 9, '_exitcond': False, 'stdoutnok': [], 'resultnok': 0, 'stderrnok': [], 'stderrok': [], 'result': 0}
            assert _s == _sX

        pass

    def testCase018(self):
        _call  = self._call
        _call += " DEFAULT "

        # epyunit.SProcUnitRules
        if self.sx.getruleset():
            _repr = repr(self.sx.getruleset())
            _reprX = """{'default': True, 'cflags': 0, 'multiline': 0, 'ignorecase': 0, 'unicode': 0, 'dotall': 0, 'debug': 0, 'priotype': 1, 'result': 0, 'resultok': 0, 'resultnok': 0, 'exitign': False, 'exittype': 8, 'exitval': 0, 'stderrchk': False, 'stderrnok': [], 'stderrok': [], 'stdoutchk': False, 'stdoutnok': [], 'stdoutok': []}"""
            assert _repr == _reprX

            _s0 = self.sx.getruleset().states() # For debug
            _s0X = {'resultok': 0, 'stdoutok': [], 'exit': 0, '_exitcond': False, 'stdoutnok': [], 'resultnok': 0, 'stderrnok': [], 'stderrok': [], 'result': 0}
            assert _s0 == _s0X

        ret = self.sx.callit(_call)
        assert ret ==   [123, ['arbitrary output'], []]

        state = self.sx.apply(ret)
        _s1 = self.sx.getruleset().states() # For debug
        assert not state

        # epyunit.SProcUnitRules
        if self.sx.getruleset():
            _repr = repr(self.sx.getruleset())
            _reprX = """{'default': True, 'cflags': 0, 'multiline': 0, 'ignorecase': 0, 'unicode': 0, 'dotall': 0, 'debug': 0, 'priotype': 1, 'result': 0, 'resultok': 0, 'resultnok': 0, 'exitign': False, 'exittype': 8, 'exitval': 0, 'stderrchk': False, 'stderrnok': [], 'stderrok': [], 'stdoutchk': False, 'stdoutnok': [], 'stdoutok': []}"""
            assert _repr == _reprX

            _s = self.sx.getruleset().states() # For debug
            _sX = {'resultok': 0, 'stdoutok': [], 'exit': 123, '_exitcond': False, 'stdoutnok': [], 'resultnok': 0, 'stderrnok': [], 'stderrok': [], 'result': 0}
            assert _s == _sX

        pass

#
#######################
#

if __name__ == '__main__':
    unittest.main()

