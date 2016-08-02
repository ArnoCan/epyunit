"""Verifies 'epyunit --selftest'.
"""
from __future__ import absolute_import

import unittest
import os

from filesysobjects.FileSysObjects import setUpperTreeSearchPath,findRelPathInSearchPath
from pysourceinfo.PySourceInfo import getCallerModulePythonPath

#
#######################
#
slst = []
setUpperTreeSearchPath(os.path.abspath(os.path.dirname(__file__)),'epyunit',slst)

epyu = findRelPathInSearchPath('bin/epyunit',slst,matchidx=0)

class CallUnits(unittest.TestCase):

    def testCase000(self):
        """Selftest.
        """
        call  = epyu + " --selftest "
        exit_code = os.system(call)
        assert exit_code == 0

#
#######################
#
if __name__ == '__main__':
    unittest.main()
