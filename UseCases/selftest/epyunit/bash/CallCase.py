"""Verifies 'epyunit --selftest'.
"""
from __future__ import absolute_import


import unittest
from testdata import epyu
import sys
from cStringIO import StringIO

from epyunit.SystemCalls import SystemCalls

#
#######################
#
class CallUnits(unittest.TestCase):

    def testCase000(self):
        """Selftest.
        """
        call   = epyu
        call  += " --selftest "
        call  += " --slang=bash "

#4TEST:
#        call  += " --rdbg "

        # buffers for evaluation after intercepted exit.
        stdoutbuf=StringIO()
        stderrbuf=StringIO()
        stdout = sys.stdout
        stderr = sys.stderr

        sys.stdout = stdoutbuf
        sys.stderr = stderrbuf

        self.sx = SystemCalls()
        #exit_code = os.system(call)
        exit_code = self.sx.callit(call)[0]
        sys.stdout = stdout
        sys.stderr = stderr


        if sys.platform == 'win32':
            if exit_code != 0:
                self.skipTest("Missing bash")
        else:
            self.assertEqual(exit_code, 0)

#
#######################
#
if __name__ == '__main__':
    unittest.main()
