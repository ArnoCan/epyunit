"""example_D

Case for a testee with success, exit 0: EXITOK

   EXIT:
     0
   STDOUT:
     arbitrary output
     arbitrary signalling OK string
     arbitrary output
   STDERR:
     -

"""
from __future__ import absolute_import
#from __future__ import print_function

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.2.0'
__uuid__='9de52399-7752-4633-9fdc-66c87a9200b8'

__docformat__ = "restructuredtext en"

import sys
import unittest
from cStringIO import StringIO

from testdata import call_scripy

import epyunit.SystemCalls

#
#######################
#

class CallUnits(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        kargs = {}
        kargs['inp'] = 'readl'
        kargs['cache'] = [{ 'type':'pipe',},] 
        cls.sx = epyunit.SystemCalls.SystemCalls(**kargs)
        
        # buffers for evaluation after intercepted exit.
        cls.stdoutbuf=StringIO()
        cls.stderrbuf=StringIO()
        cls.stdout = sys.stdout
        cls.stderr = sys.stderr

    def testCase100(self):
        _call  = call_scripy+" "
        _call += "EXITOK"
        retX = [
            0,
            ["fromD", 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'],
            []
        ]

        kargs = {}
#         kargs['inp'] = 'readl'
#         kargs['cache'] = [{ 'type':'pipe',},] 
        
        # prep stdout/stderr cache
        sys.stdout = self.stdoutbuf
        sys.stderr = self.stderrbuf

        einfo = None
        try:
            ret = self.sx.callit(_call,**kargs) #@UnusedVariable
        except:
            # save the exception
            einfo = sys.exc_info()

        # assure it is actually the sys.exit
        self.assertIsNone(einfo)

        stdval = self.stdoutbuf.getvalue().replace('\r','')
        stdref = """fromD
arbitrary output
arbitrary signalling OK string
arbitrary output
""".replace('\r','')
        try:
            assert stdval == stdref
        except Exception as e:
            # switch back from stdout and stderr buffers
            sys.stdout = self.stdout
            sys.stderr = self.stderr
            raise e

        errval = self.stderrbuf.getvalue()
        errref = """"""
        try:
            assert errval == errref
        except Exception as e:
            # switch back from stdout and stderr buffers
            sys.stdout = self.stdout
            sys.stderr = self.stderr
            raise e

        # switch back from stdout and stderr buffers
        sys.stdout = self.stdout
        sys.stderr = self.stderr

        # verify return value
        self.assertEqual(ret, retX)

        # verify settings
        _repr = repr(self.sx)
        if sys.platform in ('win32'):
            _reprX = """{'bufsize': 16384, 'console': cli, 'emptyiserr': False, 'env': None, 'errasexcept': False, 'myexe': _mode_batch_win, 'out': pass, 'passerr': False, 'proceed': doit, 'raw': False, 'rules': None, 'useexit': True, 'usestderr': False}"""
        else:
            _reprX = """{'bufsize': 16384, 'console': cli, 'emptyiserr': False, 'env': None, 'errasexcept': False, 'myexe': _mode_batch_posix, 'out': pass, 'passerr': False, 'proceed': doit, 'raw': False, 'rules': None, 'useexit': True, 'usestderr': False}"""

#         print _repr
#         print _reprX

        self.assertEqual(_repr, _reprX)
        pass


if __name__ == '__main__':
    unittest.main()
