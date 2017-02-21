from __future__ import absolute_import

import unittest
import os

import epyunit.debug.checkRDbg

#
#######################
#
class CallUnits(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.tstcall = os.path.abspath(os.path.dirname(__file__)+os.sep+'../subprocdir/bin/epyunit4RDbg.py')
        self.tstcall = os.path.normpath(self.tstcall)

        self.scall = os.path.dirname(self.tstcall)+'/../../scriptdir/libexec/myscript.sh'       # add a script
        self.scall = os.path.normpath(self.scall)
        self.scall += ' OK'

    def setUp(self):
        self.call  = self.tstcall  # emulate original Python sys.argv behaviour

    def testCall_host(self):
        self.call += ' --rdbg-forward=all'
        self.call += ' ' + self.scall

        epyunit.debug.checkRDbg.setDefaults()
        ret = epyunit.debug.checkRDbg.checkAndRemoveRDbgOptions(self.call)
        retX = (
            True,
            'localhost:5678',
            'all',
            epyunit.debug.checkRDbg._rdbgroot_default,
            epyunit.debug.checkRDbg._rdbgsub_default,
        )
        epyunit.debug.checkRDbg.setDefaults()
        self.assertEqual(ret, retX)

    def testCall_host_surrounded(self):
        self.call += ' --abc '
        self.call += ' --rdbg host01'
        self.call += ' --rdbg-forward=all'
        self.call += ' --def '
        self.call += ' ' + self.scall

        epyunit.debug.checkRDbg.setDefaults()
        ret = epyunit.debug.checkRDbg.checkAndRemoveRDbgOptions(argv=self.call)
        retX = (
            True,
            'host01:5678',
            'all',
            epyunit.debug.checkRDbg._rdbgroot_default,
            epyunit.debug.checkRDbg._rdbgsub_default
        )
        epyunit.debug.checkRDbg.setDefaults()
        self.assertEqual(ret, retX)

    def testCall_host_at_begin(self):
        self.call += ' --rdbg host01'
        self.call += ' --rdbg-forward=all'
        self.call += ' --def '
        self.call += ' ' + self.scall

        epyunit.debug.checkRDbg.setDefaults()
        ret = epyunit.debug.checkRDbg.checkAndRemoveRDbgOptions(argv=self.call)
        retX = (
            True,
            'host01:5678',
            'all',
            epyunit.debug.checkRDbg._rdbgroot_default,
            epyunit.debug.checkRDbg._rdbgsub_default,
        )
        epyunit.debug.checkRDbg.setDefaults()
        self.assertEqual(ret, retX)

    def testCall_host_at_end(self):
        #self.call += ' --pderd_debug_self '
        self.call += ' --rdbg-forward=all '
        self.call += ' --abc '
        self.call += ' --rdbg host01'
        self.call += ' ' + self.scall

        epyunit.debug.checkRDbg.setDefaults()
        ret = epyunit.debug.checkRDbg.checkAndRemoveRDbgOptions(argv=self.call)
        retX = (
            True,
            'host01:5678',
            'all',
            epyunit.debug.checkRDbg._rdbgroot_default,
            epyunit.debug.checkRDbg._rdbgsub_default,
        )
        epyunit.debug.checkRDbg.setDefaults()
        self.assertEqual(ret, retX)


#
#######################
#
if __name__ == '__main__':
    unittest.main()
