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
from cStringIO import StringIO

from testdata import epyu,call_scripy
import epyunit.SubprocUnit
import epyunit.SystemCalls

#
#######################
#
class CallUnits(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
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

        cls.sx = epyunit.SystemCalls.SystemCalls(**_kargs)

        # buffers for evaluation after intercepted exit.
        cls.stdoutbuf=StringIO()
        cls.stderrbuf=StringIO()
        cls.stdout = sys.stdout
        cls.stderr = sys.stderr

        cls._call  = epyu
        cls._call += " --raw "
        cls._call += " -- "
        cls._call += call_scripy

        cls.cache = True

    def setUp(self):
        syskargs = {}
        syskargs['emptyiserr'] = True
        self.sx = epyunit.SubprocUnit.SubprocessUnit(**syskargs)

    def testCallTwoLevelsOfSubprocesses(self):
        """Selftest of the remote debugging feature.
        """
        call  = self._call 
        call += ' OK'

        ret = self.sx.callit(call)
        
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
