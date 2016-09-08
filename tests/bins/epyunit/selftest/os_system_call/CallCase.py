"""Verifies 'jsondata --selftest'.
"""
from __future__ import absolute_import

import sys,os
from cStringIO import StringIO
import unittest

from testdata import epyu

import epyunit.SystemCalls 

#
#######################
#

class CallUnits(unittest.TestCase):

    def __init__(self,*args,**kargs):
        super(CallUnits,self).__init__(*args,**kargs)

    @classmethod
    def setUpClass(cls):
        syskargs = {}
        cls.sx = epyunit.SystemCalls.SystemCalls(**syskargs)

        # buffers for evaluation after intercepted exit.
        cls.stdoutbuf=StringIO()
        cls.stderrbuf=StringIO()
        cls.stdout = sys.stdout
        cls.stderr = sys.stderr

    def setUp(self):
        syskargs = {}
        syskargs['emptyiserr'] = True

        self.fpath = os.path.abspath(__file__)
        self.fpath = os.path.dirname(self.fpath)
        self.fpath = os.path.dirname(self.fpath)
        self.fpath = os.path.dirname(self.fpath)
        self.fpath = os.path.dirname(self.fpath)
        self.fpath = os.path.dirname(self.fpath)
        self.fpath = os.path.dirname(self.fpath)


    def testCase010(self):
        """Selftest.
        """
        if sys.platform == 'win32':
            call = 'set PYTHONPATH=%PYTHONPATH%'+os.pathsep+str(self.fpath)+'; python '+str(self.fpath)+os.sep+'bin'+os.sep+'epyu --selftest'
        else:
            call = 'export PYTHONPATH=$PYTHONPATH'+os.pathsep+str(self.fpath)+'; python '+str(self.fpath)+os.sep+'bin'+os.sep+'epyu --selftest'
        # print "4TEST:call="+call
        exit_code = os.system(call)
        assert exit_code == 0

    def testCase020(self):
        """Selftest.
        """
        if sys.platform == 'win32':
            call = 'set PYTHONPATH=%PYTHONPATH%'+os.pathsep+str(self.fpath)+'; python '+str(self.fpath)+os.sep+'bin'+os.sep+'epyu.py --selftest'
        else:
            call = 'export PYTHONPATH=$PYTHONPATH'+os.pathsep+str(self.fpath)+'; python '+str(self.fpath)+os.sep+'bin'+os.sep+'epyu.py --selftest'
        # print "4TEST:call="+call
        exit_code = os.system(call)
        assert exit_code == 0

#
#######################
#
if __name__ == '__main__':
    unittest.main()
