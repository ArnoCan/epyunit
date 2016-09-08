from __future__ import absolute_import

import unittest
import os,sys

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
        self.call += ' --rdbg :1111'
        self.call += ' ' + self.scall

        ret = epyunit.debug.checkRDbg.checkAndRemoveRDbgOptions(argv=self.call)
        retX = (
            True,
            'localhost:1111',
            0,
            epyunit.debug.checkRDbg._rdbgroot_default,
            epyunit.debug.checkRDbg._rdbgsub_default,
        )
        self.assertEqual(ret, retX)

    def testCall_host_surrounded(self):
        self.call += ' --abc '
        self.call += ' --rdbg :2222'
        self.call += ' --def '
        self.call += ' ' + self.scall

        ret = epyunit.debug.checkRDbg.checkAndRemoveRDbgOptions(argv=self.call)
        retX = (
            True,
            'localhost:2222',
            0,
            epyunit.debug.checkRDbg._rdbgroot_default,
            epyunit.debug.checkRDbg._rdbgsub_default,
        )
        self.assertEqual(ret, retX)

    def testCall_host_at_begin(self):
        self.call += ' --rdbg :3333'
        self.call += ' --def '
        self.call += ' ' + self.scall

        ret = epyunit.debug.checkRDbg.checkAndRemoveRDbgOptions(argv=self.call)
        retX = (
            True,
            'localhost:3333',
            0,
            epyunit.debug.checkRDbg._rdbgroot_default,
            epyunit.debug.checkRDbg._rdbgsub_default,
        )
        self.assertEqual(ret, retX)

    def testCall_host_at_end(self):
        self.call += ' --abc '
        self.call += ' --rdbg :4444'
        self.call += ' ' + self.scall

        ret = epyunit.debug.checkRDbg.checkAndRemoveRDbgOptions(argv=self.call)
        retX = (
            True,
            'localhost:4444',
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
