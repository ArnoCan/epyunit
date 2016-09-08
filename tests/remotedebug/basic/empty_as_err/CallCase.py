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

        cls.sx = epyunit.SubprocUnit.SubprocessUnit(**_kargs)

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

    def testCallTwoLevelsOfSubprocesses(self):
        """Selftest of the remote debugging feature.
        """
        call  = self._call 
        ret = self.sx.callit(call)
        retX =  [123, ['arbitrary output'], []]
        self.assertEqual(retX, ret) 

#
#######################
#
if __name__ == '__main__':
    unittest.main()
