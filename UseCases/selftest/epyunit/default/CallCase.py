"""Verifies 'epyunit --selftest'.
"""
from __future__ import absolute_import

import unittest
import os
from testdata import epyu


#
#######################
#
class CallUnits(unittest.TestCase):

    def testCase000(self):
        """Selftest.
        """
        call   = epyu
        call  += " --selftest "

        exit_code = os.system(call)
        assert exit_code == 0


#
#######################
#
if __name__ == '__main__':
    unittest.main()

