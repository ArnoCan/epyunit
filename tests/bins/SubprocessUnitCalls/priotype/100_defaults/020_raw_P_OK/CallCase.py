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

import sys
from cStringIO import StringIO
import unittest

import epyunit.SubprocUnit 

from testdata import epyu,call_scripy

#
#######################
#
class CallUnits(unittest.TestCase):

    def __init__(self,*args,**kargs):
        super(CallUnits,self).__init__(*args,**kargs)

    @classmethod
    def setUpClass(cls):
        syskargs = {}
        syskargs['emptyiserr'] = True
        cls.sx = epyunit.SubprocUnit.SubprocessUnit(**syskargs)

        # buffers for evaluation after intercepted exit.
        cls.stdoutbuf=StringIO()
        cls.stderrbuf=StringIO()
        cls.stdout = sys.stdout
        cls.stderr = sys.stderr

        cls._call  = epyu
        cls._call += " --raw "
        cls._call += " --priotype=True "
        cls._call += " -- "
        cls._call += call_scripy

    def testCase000(self):
        # epyunit.SubprocessUnit
        _repr = repr(self.sx)
        if sys.platform == 'win32':
            _reprX = """{'bufsize': 16384, 'console': cli, 'emptyiserr': True, 'errasexcept': False, 'myexe': _mode_batch_win, 'passerr': False, 'proceed': doit, 'raw': False, 'useexit': True, 'usestderr': False, 'rules': SProcUnitRules}"""
        else:
            _reprX = """{'bufsize': 16384, 'console': cli, 'emptyiserr': True, 'errasexcept': False, 'myexe': _mode_batch_posix, 'passerr': False, 'proceed': doit, 'raw': False, 'useexit': True, 'usestderr': False, 'rules': SProcUnitRules}"""
        assert _repr == _reprX

    def testCase010(self):
        _call  = self._call
        _call += " OK "

        # epyunit.SProcUnitRules
        if self.sx.getruleset():
            _repr = repr(self.sx.getruleset())
            _reprX = """{'default': True, 'cflags': 0, 'multiline': 0, 'ignorecase': 0, 'unicode': 0, 'dotall': 0, 'debug': 0, 'priotype': 1, 'result': 0, 'resultok': 0, 'resultnok': 0, 'exitign': False, 'exittype': 8, 'exitval': 0, 'stderrchk': False, 'stderrnok': [], 'stderrok': [], 'stdoutchk': False, 'stdoutnok': [], 'stdoutok': []}"""
            assert _repr == _reprX

            _s0 = self.sx.getruleset().states()
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

            _s = self.sx.getruleset().states()
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

            _s0 = self.sx.getruleset().states()
            _s0X = {'resultok': 0, 'stdoutok': [], 'exit': 0, '_exitcond': True, 'stdoutnok': [], 'resultnok': 0, 'stderrnok': [], 'stderrok': [], 'result': 0}
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

            _s = self.sx.getruleset().states()
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

            _s0 = self.sx.getruleset().states()
            _s0X = {'resultok': 0, 'stdoutok': [], 'exit': 0, '_exitcond': True, 'stdoutnok': [], 'resultnok': 0, 'stderrnok': [], 'stderrok': [], 'result': 0}
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

            _s = self.sx.getruleset().states()
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

            _s0 = self.sx.getruleset().states()
            _s0X = {'resultok': 0, 'stdoutok': [], 'exit': 0, '_exitcond': True, 'stdoutnok': [], 'resultnok': 0, 'stderrnok': [], 'stderrok': [], 'result': 0}
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

            _s = self.sx.getruleset().states()
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

            _s0 = self.sx.getruleset().states()
            _s0X = {'resultok': 0, 'stdoutok': [], 'exit': 0, '_exitcond': True, 'stdoutnok': [], 'resultnok': 0, 'stderrnok': [], 'stderrok': [], 'result': 0}
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

            _s = self.sx.getruleset().states()
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

            _s0 = self.sx.getruleset().states()
            _s0X = {'resultok': 0, 'stdoutok': [], 'exit': 1, '_exitcond': False, 'stdoutnok': [], 'resultnok': 0, 'stderrnok': [], 'stderrok': [], 'result': 0}
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

            _s = self.sx.getruleset().states()
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

            _s0 = self.sx.getruleset().states()
            _s0X = {'resultok': 0, 'stdoutok': [], 'exit': 7, '_exitcond': False, 'stdoutnok': [], 'resultnok': 0, 'stderrnok': [], 'stderrok': [], 'result': 0}
            assert _s0 == _s0X

        ret = self.sx.callit(_call)
        assert ret ==   [8, ['fromG', 'arbitrary output', 'arbitrary signalling NOK string', 'arbitrary output'], ['arbitrary err output', 'arbitrary err signalling NOK string', 'arbitrary err output']]

        state = self.sx.apply(ret)
        _s1 = self.sx.getruleset().states()
        assert not state

        # epyunit.SProcUnitRules
        if self.sx.getruleset():
            _repr = repr(self.sx.getruleset())
            _reprX = """{'default': True, 'cflags': 0, 'multiline': 0, 'ignorecase': 0, 'unicode': 0, 'dotall': 0, 'debug': 0, 'priotype': 1, 'result': 0, 'resultok': 0, 'resultnok': 0, 'exitign': False, 'exittype': 8, 'exitval': 0, 'stderrchk': False, 'stderrnok': [], 'stderrok': [], 'stdoutchk': False, 'stdoutnok': [], 'stdoutok': []}"""
            assert _repr == _reprX

            _s = self.sx.getruleset().states()
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

            _s0 = self.sx.getruleset().states()
            _s0X = {'resultok': 0, 'stdoutok': [], 'exit': 8, '_exitcond': False, 'stdoutnok': [], 'resultnok': 0, 'stderrnok': [], 'stderrok': [], 'result': 0}
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

            _s = self.sx.getruleset().states()
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

            _s0 = self.sx.getruleset().states()
            _s0X = {'resultok': 0, 'stdoutok': [], 'exit': 9, '_exitcond': False, 'stdoutnok': [], 'resultnok': 0, 'stderrnok': [], 'stderrok': [], 'result': 0}
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

            _s = self.sx.getruleset().states()
            _sX = {'resultok': 0, 'stdoutok': [], 'exit': 123, '_exitcond': False, 'stdoutnok': [], 'resultnok': 0, 'stderrnok': [], 'stderrok': [], 'result': 0}
            assert _s == _sX

        pass

#
#######################
#

if __name__ == '__main__':
    unittest.main()

