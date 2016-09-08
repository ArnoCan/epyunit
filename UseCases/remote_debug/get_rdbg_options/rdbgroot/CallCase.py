from __future__ import absolute_import

import unittest
import sys,os
from cStringIO import StringIO

from testdata import epyu,call_scripy
import epyunit.SubprocUnit
import epyunit.debug.checkRDbg

import filesysobjects
import testdata

from filesysobjects.FileSysObjects import setUpperTreeSearchPath,findRelPathInSearchPath
from epyunit.SystemCalls import SystemCalls,SystemCallsExceptionSubprocessError

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

    def setUp(self):
        self.subreset = epyunit.debug.checkRDbg._rdbgsub_default
        epyunit.debug.checkRDbg._rdbgsub = epyunit.debug.checkRDbg._rdbgsub_default

    def testCall_host(self):
        _call  = epyu
        _call += ' --passall '

        _call += ' --rdbg  '
        _call += ' --rdbg-root ' + self.eclipsepath

        _call += ' ' + call_scripy

        _cl = _call.split()
        ret = epyunit.debug.checkRDbg.checkAndRemoveRDbgOptions(_cl)
        retX = (
            True,
            'localhost:5678',
            0,
            self.eclipsepath,
            epyunit.debug.checkRDbg._rdbgsub_default
        )
        self.assertEqual(ret, retX)
        pass

    def testCall_host_surrounded(self):
        _call  = epyu
        _call += ' --passall '

        _call += ' --rdbg  '
        _call += ' --rdbg-root ' + self.eclipsepath
        _call += ' --def '

        _call += ' ' + call_scripy

        _cl = _call.split()
        ret = epyunit.debug.checkRDbg.checkAndRemoveRDbgOptions(_cl)
        retX = (
            True,
            'localhost:5678',
            0,
            self.eclipsepath,
            epyunit.debug.checkRDbg._rdbgsub_default
        )
        self.assertEqual(ret, retX)
        pass

    def testCall_host_at_begin(self):
        _call  = epyu
        _call += ' --rdbg-root ' + self.eclipsepath

        _call += ' --passall '

        _call += ' --rdbg  '
        _call += ' --def '

        _call += ' ' + call_scripy

        _cl = _call.split()
        ret = epyunit.debug.checkRDbg.checkAndRemoveRDbgOptions(_cl)
        retX = (
            True,
            'localhost:5678',
            0,
            self.eclipsepath,
            epyunit.debug.checkRDbg._rdbgsub_default
        )
        self.assertEqual(ret, retX)
        pass

    def testCall_host_at_end(self):
        _call  = epyu
        _call += ' --passall '

        _call += ' --rdbg  '
        _call += ' --def '
        _call += ' --rdbg-root ' + self.eclipsepath

        _call += ' ' + call_scripy

        _cl = _call.split()
        ret = epyunit.debug.checkRDbg.checkAndRemoveRDbgOptions(_cl)
        retX = (
            True,
            'localhost:5678',
            0,
            self.eclipsepath,
            epyunit.debug.checkRDbg._rdbgsub_default
        )
        self.assertEqual(ret, retX)
        pass

    def testCall_host_equal(self):
        _call  = epyu
        _call += ' --passall '

        _call += ' --rdbg=localhost'
        _call += ' --def '
        _call += ' --rdbg-root=' + self.eclipsepath

        _call += ' ' + call_scripy

        _cl = _call.split()
        ret = epyunit.debug.checkRDbg.checkAndRemoveRDbgOptions(_cl)
        retX = (
            True,
            'localhost:5678',
            0,
            self.eclipsepath,
            epyunit.debug.checkRDbg._rdbgsub_default
        )
        self.assertEqual(ret, retX)
        pass

    def testCall_host_surrounded_equal(self):
        _call  = epyu
        _call += ' --passall '

        _call += ' --rdbg=localhost'
        _call += ' --rdbg-root=' + self.eclipsepath
        _call += ' --def '

        _call += ' ' + call_scripy

        _cl = _call.split()
        ret = epyunit.debug.checkRDbg.checkAndRemoveRDbgOptions(_cl)
        retX = (
            True,
            'localhost:5678',
            0,
            self.eclipsepath,
            self.subreset, #epyunit.debug.checkRDbg._rdbgsub_default
        )
        self.assertEqual(ret, retX)
        pass

    def testCall_host_at_begin_equal(self):
        _call  = epyu
        _call += ' --rdbg-root=' + self.eclipsepath
        _call += ' --passall '

        _call += ' --rdbg=localhost'
        _call += ' --def '

        _call += ' ' + call_scripy

        _cl = _call.split()
        ret = epyunit.debug.checkRDbg.checkAndRemoveRDbgOptions(_cl)
        retX = (
            True,
            'localhost:5678',
            0,
            self.eclipsepath,
            epyunit.debug.checkRDbg._rdbgsub_default
        )
        self.assertEqual(ret, retX)
        pass

    def testCall_host_at_end_equal(self):
        _call  = epyu
        _call += ' --passall '

        _call += ' --rdbg=localhost'
        _call += ' --def '
        _call += ' --rdbg-root=' + self.eclipsepath

        _call += ' ' + call_scripy

        _cl = _call.split()
        ret = epyunit.debug.checkRDbg.checkAndRemoveRDbgOptions(_cl)
        retX = (
            True,
            'localhost:5678',
            0,
            self.eclipsepath,
            epyunit.debug.checkRDbg._rdbgsub_default
        )
        self.assertEqual(ret, retX)
        pass

#
#######################
#
if __name__ == '__main__':
    unittest.main()
