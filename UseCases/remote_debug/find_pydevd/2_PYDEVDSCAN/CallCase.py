from __future__ import absolute_import

import unittest
import sys,os
from cStringIO import StringIO

from testdata import epyu,call_scripy
import epyunit.SubprocUnit
import epyunit.debug.checkRDbg

import filesysobjects
import testdata


#
#######################
#
class CallUnits(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        _kargs = {}
        #
        # *** some error passing options, refer to API ***
        #
        # _kargs['passerr'] = True
        # _kargs['errasexcept'] = True
        # _kargs['useexit'] = True
        # _kargs['usestderr'] = True
        #
        _kargs['emptyiserr'] = True

        cls.sx = epyunit.SubprocUnit.SubprocessUnit(**_kargs)


        # buffers for evaluation after intercepted exit.
        cls.stdoutbuf=StringIO()
        cls.stderrbuf=StringIO()
        cls.stdout = sys.stdout
        cls.stderr = sys.stderr

        cls.cache = True

        cls.eclipsepath  = testdata.mypath
        cls.eclipsepath += "/eclipse/dirs/single/generic"
        cls.eclipsepath += "/eclipse"
        cls.eclipsepath  = filesysobjects.FileSysObjects.normpathX(cls.eclipsepath) # adapt to platform

        cls.rdbgsub = "org.python.pydev_[0-9]*.[0-9]*.[0-9]*201*/pysrc/pydevd.py"


    def testCall_defaults(self):
        """disable use of RDBGROOT and RDBGSUB
        """
        os.environ['RDBGROOT'] = self.eclipsepath+'environ'
        os.environ['RDBGSUB'] = self.rdbgsub+'environ'

        epyunit.debug.checkRDbg._rdbgenv = False # suppress RDBGROOT and RDBGSUB
        epyunit.debug.checkRDbg._rdbgroot = epyunit.debug.checkRDbg._rdbgroot_default
        epyunit.debug.checkRDbg._rdbgsub = epyunit.debug.checkRDbg._rdbgsub_default

        _call  = epyu
        _call += ' --passall '
        _call += ' --rdbg  '
        _call += ' ' + call_scripy

        _cl = _call.split()
        ret = epyunit.debug.checkRDbg.checkAndRemoveRDbgOptions(_cl)
        retX = (
            True,
            'localhost:5678',
            0,
            epyunit.debug.checkRDbg._rdbgroot_default,
            epyunit.debug.checkRDbg._rdbgsub_default,
        )
        self.assertEqual(ret, retX)
        pass

    def testCall_environ_only(self):
        """enable use of RDBGROOT and RDBGSUB
        """
        os.environ['RDBGROOT'] = self.eclipsepath + 'RDBGROOT'
        os.environ['RDBGSUB'] = self.rdbgsub + 'RDBGSUB'

        _call  = epyu
        _call += ' --passall '
        _call += ' --rdbg  '
        _call += ' --rdbg-env=True  '  # enable use of RDBGROOT and RDBGSUB
        _call += ' ' + call_scripy

        _cl = _call.split()
        ret = epyunit.debug.checkRDbg.checkAndRemoveRDbgOptions(_cl)
        retX = (
            True,
            'localhost:5678',
            0,
            self.eclipsepath + 'RDBGROOT',
            self.rdbgsub + 'RDBGSUB',
        )
        self.assertEqual(ret, retX)
        pass

    def testCall_superposed_root(self):
        _call  = epyu
        _call += ' --passall '

        os.environ['RDBGROOT'] = self.eclipsepath+os.sep+'superposed'
        os.environ['RDBGSUB'] = self.rdbgsub+os.sep+'superposed'

        _call += ' --rdbg  '
        _call += ' --rdbg-env  '
        _call += ' --rdbg-root ' + self.eclipsepath
        _call += ' --def '

        _call += ' ' + call_scripy

        _cl = _call.split()
        ret = epyunit.debug.checkRDbg.checkAndRemoveRDbgOptions(_cl)
        retX = (
            True,
            'localhost:5678',
            0,
            self.eclipsepath+os.sep+'superposed',
            self.rdbgsub+os.sep+'superposed',
        )
        self.assertEqual(ret, retX)
        pass

    def testCall_sub_superposed(self):
        os.environ['RDBGSUB'] = self.rdbgsub+os.sep+'superposed'
        _call  = epyu
        _call += ' --rdbg-sub ' + self.rdbgsub
        _call += ' --passall '
        _call += ' --rdbg-env  '
        _call += ' --rdbg  '
        _call += ' --def '
        _call += ' ' + call_scripy

        _cl = _call.split()
        ret = epyunit.debug.checkRDbg.checkAndRemoveRDbgOptions(_cl)
        retX = (
            True,
            'localhost:5678',
            0,
            self.eclipsepath+'RDBGROOT',
            self.rdbgsub+os.path.sep+'superposed'
        )
        self.assertEqual(ret, retX)
        pass

    def testCall_both_superposed(self):
        os.environ['RDBGROOT'] = self.eclipsepath+os.sep+'RDBGROOT'
        os.environ['RDBGSUB'] = self.rdbgsub+os.sep+'RDBGSUB'

        _call  = epyu
        _call += ' --passall '

        _call += ' --rdbg  '
        _call += ' --rdbg-env  '
        _call += ' --def '
        _call += ' --rdbg-root ' + self.eclipsepath
        _call += ' --rdbg-sub ' + self.rdbgsub

        _call += ' ' + call_scripy

        _cl = _call.split()
        ret = epyunit.debug.checkRDbg.checkAndRemoveRDbgOptions(_cl)
        retX = (
            True,
            'localhost:5678',
            0,
            self.eclipsepath+os.sep+'RDBGROOT',
            self.rdbgsub+os.sep+'RDBGSUB',
        )
        self.assertEqual(ret, retX)
        pass


#
#######################
#
if __name__ == '__main__':
    unittest.main()
