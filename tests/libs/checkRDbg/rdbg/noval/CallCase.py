from __future__ import absolute_import

import unittest
import os

import epyunit.debug.checkRDbg

#
#######################
#
class CallUnits(unittest.TestCase):

    def setUp(self):
        self.tstcall = os.path.normpath(os.path.dirname(__file__)+os.sep+'../subprocdir/bin/epyunit4RDbg.py')
        self.tstcall = os.path.abspath(self.tstcall)

        self.scall = os.path.normpath(self.tstcall)+'/../../scriptdir/libexec/myscript.sh'       # add a script
        self.scall = os.path.dirname(self.scall)
        self.scall += ' OK'

        self.call  = self.tstcall  # emulate original Python sys.argv behaviour

    def testCall_defaults(self):
        self.call += ' --rdbg '
        self.call += ' ' + self.scall

        ret = epyunit.debug.checkRDbg.checkAndRemoveRDbgOptions(argv=self.call)
        retX = (
            True,
            'localhost:5678',
            0,
            epyunit.debug.checkRDbg._rdbgroot_default,
            epyunit.debug.checkRDbg._rdbgsub_default,
        )
        self.assertEqual(ret, retX)

    def testCall_defaults_surrounded_0(self):
        self.call += ' --abc '
        self.call += ' --rdbg '
        self.call += ' --def '
        self.call += ' ' + self.scall

        ret = epyunit.debug.checkRDbg.checkAndRemoveRDbgOptions(argv=self.call)
        retX = (
            True,
            'localhost:5678',
            0,
            epyunit.debug.checkRDbg._rdbgroot_default,
            epyunit.debug.checkRDbg._rdbgsub_default,
        )
        self.assertEqual(ret, retX)

    def testCall_surrounded_1(self):
        self.call += ' --abc '
        self.call += ' --abc '
        self.call += ' --rdbg '
        self.call += ' --def '
        self.call += ' ' + self.scall

        ret = epyunit.debug.checkRDbg.checkAndRemoveRDbgOptions(argv=self.call)
        retX = (
            True,
            'localhost:5678',
            0,
            epyunit.debug.checkRDbg._rdbgroot_default,
            epyunit.debug.checkRDbg._rdbgsub_default,
        )
        self.assertEqual(ret, retX)

    def testCall_surrounded_2(self):
        self.call += ' --abc '
        self.call += ' --rdbg '
        self.call += ' --def '
        self.call += ' --def '
        self.call += ' ' + self.scall

        ret = epyunit.debug.checkRDbg.checkAndRemoveRDbgOptions(argv=self.call)
        retX = (
            True,
            'localhost:5678',
            0,
            epyunit.debug.checkRDbg._rdbgroot_default,
            epyunit.debug.checkRDbg._rdbgsub_default,
        )
        self.assertEqual(ret, retX)

    def testCall_surrounded_3(self):
        self.call += ' --abc '
        self.call += ' --abc '
        self.call += ' --rdbg '
        self.call += ' --def '
        self.call += ' --def '
        self.call += ' ' + self.scall

        ret = epyunit.debug.checkRDbg.checkAndRemoveRDbgOptions(argv=self.call)
        retX = (
            True,
            'localhost:5678',
            0,
            epyunit.debug.checkRDbg._rdbgroot_default,
            epyunit.debug.checkRDbg._rdbgsub_default,
        )
        self.assertEqual(ret, retX)

    def testCall_surrounded_4(self):
        self.call += ' --abc '
        self.call += ' --abc '
        self.call += ' --rdbg '
        self.call += ' --def '
        self.call += ' --abc '
        self.call += ' --abc '
        self.call += ' --rdbg '
        self.call += ' --def '
        self.call += ' ' + self.scall

        ret = epyunit.debug.checkRDbg.checkAndRemoveRDbgOptions(argv=self.call)
        retX = (
            True,
            'localhost:5678',
            0,
            epyunit.debug.checkRDbg._rdbgroot_default,
            epyunit.debug.checkRDbg._rdbgsub_default,
        )
        self.assertEqual(ret, retX)

    def testCall_surrounded_5(self):
        self.call += ' --abc '
        self.call += ' --abc '
        self.call += ' --rdbg '
        self.call += ' --def '
        self.call += ' --rdbg '
        self.call += ' --def '
        self.call += ' --rdbg '
        self.call += ' --rdbg '
        self.call += ' --rdbg '
        self.call += ' --rdbg '
        self.call += ' ' + self.scall

        ret = epyunit.debug.checkRDbg.checkAndRemoveRDbgOptions(argv=self.call)
        retX = (
            True,
            'localhost:5678',
            0,
            epyunit.debug.checkRDbg._rdbgroot_default,
            epyunit.debug.checkRDbg._rdbgsub_default,
        )
        self.assertEqual(ret, retX)

    def testCall_port_begin(self):
        self.call += ' --rdbg '
        self.call += ' --def '
        self.call += ' ' + self.scall

        ret = epyunit.debug.checkRDbg.checkAndRemoveRDbgOptions(argv=self.call)
        retX = (
            True,
            'localhost:5678',
            0,
            epyunit.debug.checkRDbg._rdbgroot_default,
            epyunit.debug.checkRDbg._rdbgsub_default,
        )
        self.assertEqual(ret, retX)

    def testCall_end(self):
        self.call += ' --abc '
        self.call += ' --rdbg '
        self.call += ' ' + self.scall

        ret = epyunit.debug.checkRDbg.checkAndRemoveRDbgOptions(argv=self.call)
        retX = (
            True,
            'localhost:5678',
            0,
            epyunit.debug.checkRDbg._rdbgroot_default,
            epyunit.debug.checkRDbg._rdbgsub_default,
        )
        self.assertEqual(ret, retX)

#
#######################
#
if __name__ == '__main__':
    unittest.main()
