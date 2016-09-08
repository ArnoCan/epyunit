from __future__ import absolute_import

import unittest
import os,sys

import epyunit.debug.checkRDbg

from filesysobjects.FileSysObjects import setUpperTreeSearchPath,findRelPathInSearchPath
from epyunit.SystemCalls import SystemCalls,SystemCallsExceptionSubprocessError
import filesysobjects

#
#######################
#
class CallUnits(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.slst = []
        setUpperTreeSearchPath(os.path.abspath(os.path.dirname(__file__)),'epyunit',self.slst)

        self.epyu = findRelPathInSearchPath('bin/epyu.py',self.slst,matchidx=0)
        self.scri =  " -- python " + findRelPathInSearchPath('epyunit/myscript.py',self.slst,matchidx=0)

    def testCall_host(self):
        _call  = " python " + self.epyu
        _call += ' --rdbg host01 '
        _call += ' ' + self.scri

        _cl = _call.split()
        ret = epyunit.debug.checkRDbg.checkAndRemoveRDbgOptions(_cl)
        retX = (
            False,
            'host01:5678',
            0,
            epyunit.debug.checkRDbg._rdbgroot_default,
            epyunit.debug.checkRDbg._rdbgsub_default,
        )
        self.assertEqual(ret, retX)
        pass

    def testCall_host_surrounded(self):
        _call  = " python " + self.epyu
        _call += ' --abc '
        _call += ' --rdbg host01'
        _call += ' --def '
        _call += ' ' + self.scri

        _cl = _call.split()
        ret = epyunit.debug.checkRDbg.checkAndRemoveRDbgOptions(_cl)
        retX = (
            False,
            'host01:5678',
            0,
            epyunit.debug.checkRDbg._rdbgroot_default,
            epyunit.debug.checkRDbg._rdbgsub_default,
        )
        self.assertEqual(ret, retX)
        pass

    def testCall_host_at_begin(self):
        _call  = " python " + self.epyu
        _call += ' --rdbg host01'
        _call += ' --def '
        _call += ' ' + self.scri

        _cl = _call.split()
        ret = epyunit.debug.checkRDbg.checkAndRemoveRDbgOptions(_cl)
        retX = (
            False,
            'host01:5678',
            0,
            epyunit.debug.checkRDbg._rdbgroot_default,
            epyunit.debug.checkRDbg._rdbgsub_default,
        )
        self.assertEqual(ret, retX)
        pass

    def testCall_host_at_end(self):
        _call  = " python " + self.epyu
        _call += ' --abc '
        _call += ' --rdbg host01'
        _call += ' ' + self.scri

        _cl = _call.split()
        ret = epyunit.debug.checkRDbg.checkAndRemoveRDbgOptions(_cl)
        retX = (
            False,
            'host01:5678',
            0,
            epyunit.debug.checkRDbg._rdbgroot_default,
            epyunit.debug.checkRDbg._rdbgsub_default,
        )
        self.assertEqual(ret, retX)
        pass

    def testCall_host_equal(self):
        _call  = " python " + self.epyu
        _call += ' --rdbg=host01'
        _call += ' ' + self.scri

        _cl = _call.split()
        ret = epyunit.debug.checkRDbg.checkAndRemoveRDbgOptions(_cl)
        retX = (
            False,
            'host01:5678',
            0,
            epyunit.debug.checkRDbg._rdbgroot_default,
            epyunit.debug.checkRDbg._rdbgsub_default,
        )
        self.assertEqual(ret, retX)
        pass

    def testCall_host_surrounded_equal(self):
        _call  = " python " + self.epyu
        _call += ' --abc '
        _call += ' --rdbg=host01'
        _call += ' --def '
        _call += ' ' + self.scri

        _cl = _call.split()
        ret = epyunit.debug.checkRDbg.checkAndRemoveRDbgOptions(_cl)
        retX = (
            False,
            'host01:5678',
            0,
            epyunit.debug.checkRDbg._rdbgroot_default,
            epyunit.debug.checkRDbg._rdbgsub_default,
        )
        self.assertEqual(ret, retX)
        pass

    def testCall_host_at_begin_equal(self):
        _call  = " python " + self.epyu
        _call += ' --rdbg=host01'
        _call += ' --def '
        _call += ' ' + self.scri

        _cl = _call.split()
        ret = epyunit.debug.checkRDbg.checkAndRemoveRDbgOptions(_cl)
        retX = (
            False,
            'host01:5678',
            0,
            epyunit.debug.checkRDbg._rdbgroot_default,
            epyunit.debug.checkRDbg._rdbgsub_default,
        )
        self.assertEqual(ret, retX)
        pass

    def testCall_host_at_end_equal(self):
        _call  = " python " + self.epyu
        _call += ' --abc '
        _call += ' --rdbg=host01'
        _call += ' ' + self.scri

        _cl = _call.split()
        ret = epyunit.debug.checkRDbg.checkAndRemoveRDbgOptions(_cl)
        retX = (
            False,
            'host01:5678',
            0,
            epyunit.debug.checkRDbg._rdbgroot_default,
            epyunit.debug.checkRDbg._rdbgsub_default,
        )
        self.assertEqual(ret, retX)
        pass

#
#######################
#
if __name__ == '__main__':
    unittest.main()
