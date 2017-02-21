from __future__ import absolute_import

import unittest
import os,sys

import epyunit.debug.checkRDbg

from filesysobjects.FileSysObjects import setUpperTreeSearchPath,findRelPathInSearchPath
from epyunit.SystemCalls import SystemCalls,SystemCallsExceptionSubprocessError
import filesysobjects

from testdata import call_scripy,epyu

#
#######################
#
class CallUnits(unittest.TestCase):

    def testCall_host(self):
        _call  = epyu
        _call += ' --rdbg host01 '
        _call += ' ' + call_scripy

        _cl = _call.split()
        ret = epyunit.debug.checkRDbg.checkAndRemoveRDbgOptions(_cl)
        retX = (
            True,
            'host01:5678',
            0,
            epyunit.debug.checkRDbg._rdbgroot_default,
            epyunit.debug.checkRDbg._rdbgsub_default,
        )
        self.assertEqual(ret, retX)
        pass

    def testCall_host_equal(self):
        _call  = epyu
        _call += ' --rdbg=host01'
        _call += ' ' + call_scripy

        _cl = _call.split()
        ret = epyunit.debug.checkRDbg.checkAndRemoveRDbgOptions(_cl)
        retX = (
            True,
            'host01:5678',
            0,
            epyunit.debug.checkRDbg._rdbgroot_default,
            epyunit.debug.checkRDbg._rdbgsub_default,
        )
        self.assertEqual(ret, retX)
        pass

    def testCall_host_at_begin(self):
        _call  = epyu
        _call += ' --rdbg host01'
        _call += ' --def '
        _call += ' ' + call_scripy

        _cl = _call.split()
        ret = epyunit.debug.checkRDbg.checkAndRemoveRDbgOptions(_cl)
        retX = (
            True,
            'host01:5678',
            0,
            epyunit.debug.checkRDbg._rdbgroot_default,
            epyunit.debug.checkRDbg._rdbgsub_default,
        )
        self.assertEqual(ret, retX)
        pass

    def testCall_host_at_end(self):
        _call  = epyu
        _call += ' --abc '
        _call += ' --rdbg host01'
        _call += ' ' + call_scripy

        _cl = _call.split()
        ret = epyunit.debug.checkRDbg.checkAndRemoveRDbgOptions(_cl)
        retX = (
            True,
            'host01:5678',
            0,
            epyunit.debug.checkRDbg._rdbgroot_default,
            epyunit.debug.checkRDbg._rdbgsub_default,
        )
        self.assertEqual(ret, retX)
        pass

    def testCall_host_surrounded_equal(self):
        _call  = epyu
        _call += ' --abc '
        _call += ' --rdbg=host01'
        _call += ' --def '
        _call += ' ' + call_scripy

        _cl = _call.split()
        ret = epyunit.debug.checkRDbg.checkAndRemoveRDbgOptions(_cl)
        retX = (
            True,
            'host01:5678',
            0,
            epyunit.debug.checkRDbg._rdbgroot_default,
            epyunit.debug.checkRDbg._rdbgsub_default,
        )

        self.assertEqual(ret, retX)
        pass

    def testCall_host_at_begin_equal(self):
        _call  = epyu
        _call += ' --rdbg=host01'
        _call += ' --def '
        _call += ' ' + call_scripy

        _cl = _call.split()
        ret = epyunit.debug.checkRDbg.checkAndRemoveRDbgOptions(_cl)
        retX = (
            True,
            'host01:5678',
            0,
            epyunit.debug.checkRDbg._rdbgroot_default,
            epyunit.debug.checkRDbg._rdbgsub_default,
        )
        self.assertEqual(ret, retX)
        pass

    def testCall_host_at_end_equal(self):
        _call  = epyu
        _call += ' --abc '
        _call += ' --rdbg=host01'
        _call += ' ' + call_scripy

        _cl = _call.split()
        ret = epyunit.debug.checkRDbg.checkAndRemoveRDbgOptions(_cl)
        retX = (
            True,
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
