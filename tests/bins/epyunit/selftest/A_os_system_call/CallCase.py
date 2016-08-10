"""Verifies 'jsondata --selftest'.
"""
from __future__ import absolute_import

import unittest
import os
import sys

#
#######################
#
class CallUnits(unittest.TestCase):
    name=os.path.curdir+__file__

    output=True
    output=False

    def testCase000(self):
        """Selftest.
        """
        p = os.path.abspath(__file__)
        p = os.path.dirname(p)
        p = os.path.dirname(p)
        p = os.path.dirname(p)
        p = os.path.dirname(p)
        p = os.path.dirname(p)
        p = os.path.dirname(p)
        call = 'export PYTHONPATH=$PYTHONPATH:'+str(p)+';python '+str(p)+os.sep+'bin'+os.sep+'epyunit --selftest'
        #print call
        exit_code = os.system(call)
        assert exit_code == 0

#
#######################
#
if __name__ == '__main__':
    unittest.main()
