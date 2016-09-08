"""
Verifies basic facilities for remote debugging by starting a subprocess.
Uses:

* epyunit.SystemCalls()

* epyunit.callit()

Applies a two-level subprocess stack:

0. This UseCase

1. The wrapper 'epyunit4RDbg.py'

2. The script with dummy responses for tests 'myscript.py'

"""
from __future__ import absolute_import

import unittest

from testdata import epyu,call_scripy
import epyunit.SubprocUnit

#
#######################
#
class CallUnits(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cache = True

    def testSubprocessesWithErrorAsException(self):
        """Selftest of the remote debugging feature.
        """

        call  = epyu
        call += ' --rdbg ' #: activate remote debugging
        #call += ' --rdbg-forward=1 '
        #call += ' --rdbg-forward=all ' #: forward flag to all nested levels of subprocesses - consider port connection limits to RemoteDebugServer

        # test rdbg
        # call += ' --rdbg-self ' #: activate remote debugging

        call += ' -- '
        call += ' ' + call_scripy
        call += ' EXIT8'

        _kargs = {}

        #
        # *** some error passing options, refer to API ***
        #
        # _kargs['passerr'] = True
        # _kargs['errasexcept'] = True
        # _kargs['useexit'] = True
        # _kargs['usestderr'] = True

        #
        _kargs['emptyiserr'] = True

        sx = epyunit.SubprocUnit.SubprocessUnit(**_kargs)
        ret = sx.callit(call) #@UnusedVariable

        #
        # *** the default tuple - with demo-labels for stdout + stderr ***
        #
        #assert ret[0] == 8
        self.maxDiff = None
        retX =  [
            1,
            ['fromG', 'arbitrary output', 'arbitrary signalling NOK string', 'arbitrary output'],
            ['arbitrary err output', 'arbitrary err signalling NOK string', 'arbitrary err output']
        ]
        self.assertEqual(ret,retX)

#
#######################
#
if __name__ == '__main__':
    unittest.main()
