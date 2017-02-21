from __future__ import absolute_import

import unittest
import sys,os
from cStringIO import StringIO

from testdata import epyu,call_scripy
import epyunit.SubprocUnit
import epyunit.debug.checkRDbg

import filesysobjects
import testdata

from epyunit.debug.pydevrdc import PYDEVD
from filesysobjects.FileSysObjects import findRelPathInSearchPath

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

        cls.eclipsepath  = testdata.mypath
        cls.eclipsepath += "/eclipse/dirs/single/generic"
        cls.eclipsepath += "/eclipse"
        cls.eclipsepath  = filesysobjects.FileSysObjects.normpathX(cls.eclipsepath) # adapt to platform

        cls.rdbgsub = "org.python.pydev_[0-9]*.[0-9]*.[0-9]*201*/pysrc/pydevd.py"

        cls.syspath_org = sys.path[:]

    def setUp(self):
        os.environ['RDBGROOT'] = self.eclipsepath+'environ'
        os.environ['RDBGSUB'] = self.rdbgsub+'environ'
        epyunit.debug.checkRDbg._rdbgenv = False
        epyunit.debug.checkRDbg._rdbgsub = epyunit.debug.checkRDbg._rdbgsub_default

        sys.path = self.syspath_org[:]


    def testCall_defaults(self):
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
            self.eclipsepath+"notvalid",
            epyunit.debug.checkRDbg._rdbgsub_default,
        )
        self.assertEqual(ret, retX)
        pass

    def testCall_cli(self):
        fx = findRelPathInSearchPath(self.rdbgsub,self.eclipsepath+os.sep+'plugins')
        sys.path.insert(0,fx)

        _call  = epyu
        _call += ' --passall '
        _call += ' --rdbg  '
        _call += ' --rdbg-root='+ self.eclipsepath + 'notvalid'
        _call += ' --rdbg-sub='+ self.rdbgsub + 'notvalid'
        _call += ' ' + call_scripy

        _cl = _call.split()
        ret = epyunit.debug.checkRDbg.checkAndRemoveRDbgOptions(_cl)
        retX = (
            True,
            'localhost:5678',
            0,
            self.eclipsepath + 'notvalid',
            self.rdbgsub + 'notvalid',
        )
        self.assertEqual(ret, retX)
        pass

    def testCall_sys_path(self):
        fx = findRelPathInSearchPath(self.rdbgsub,self.eclipsepath+os.sep+'plugins')
        sys.path.insert(0,fx)

        _call  = epyu
        _call += ' --passall '
        _call += ' --rdbg  '
#         _call += ' --rdbg-root='+ self.eclipsepath
#         _call += ' --rdbg-sub='+ self.rdbgsub
        _call += ' --rdbg-root='+ self.eclipsepath + 'notvalid'
        _call += ' --rdbg-sub='+ self.rdbgsub + 'notvalid'
        _call += ' ' + call_scripy

        _cl = _call.split()
        ret = epyunit.debug.checkRDbg.checkAndRemoveRDbgOptions(_cl)
        retX = (
            True,
            'localhost:5678',
            0,
            self.eclipsepath + 'notvalid',
            self.rdbgsub + 'notvalid',
        )
        self.assertEqual(ret, retX)

        sx = epyunit.debug.checkRDbg.scanEclipseForPydevd(**{'altpat':self.rdbgsub,})
        assert os.path.basename(sx) == 'pydevd.py'
        pass


#
#######################
#
if __name__ == '__main__':
    unittest.main()
