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
import sys

from testdata import epyu,call_scripy

#
#######################
#
class CallUnits(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cache = True

    def testCallTwoLevelsOfSubprocesses(self):
        """Selftest of the remote debugging feature.
        """
        try:
            from epyunit.SystemCalls import SystemCalls
        except Exception as e:
            print "\n#\n#*** Set 'PYTHONPATH' ("+str(e)+")\n#\n"
            sys.exit(1)

        call  = epyu
        call += ' ' + call_scripy
        call += ' OK'

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

        sx = SystemCalls(**_kargs)
        ret = sx.callit(call)

        #
        # *** the default tuple - with demo-labels for stdout + stderr ***
        #
        retX = [0, ['fromA', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'], []]
        self.assertEqual(ret, retX)

#
#######################
#
if __name__ == '__main__':
    unittest.main()
