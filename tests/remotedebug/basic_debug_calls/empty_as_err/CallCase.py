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

from testdata import epyu
import epyunit.SubprocUnit

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
        #call  = epyu
        call  = None
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
        ret = sx.callit(call)
        
        #
        retX = [ 
            2, 
            [],
            ['ERROR:MissingCallstr']
        ]
        self.assertEqual(retX, ret) 

#
#######################
#
if __name__ == '__main__':
    unittest.main()
