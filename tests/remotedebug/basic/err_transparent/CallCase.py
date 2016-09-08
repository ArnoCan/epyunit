"""
Verifies basic facilities for remote debugging by starting a subprocess.
Uses:

* epyunit.SystemCalls()

* epyunit.callit()

Applies a two-level subprocess stack:

0. This UseCase

1. The wrapper 'epyunit4RDbg.py'

2. The script with dummy responses for tests 'myscript.py'

"""
from __future__ import absolute_import

import unittest
import sys
from cStringIO import StringIO

from testdata import epyu,call_scripy
import epyunit.SubprocUnit

#
#######################
#
class CallUnits(unittest.TestCase):
    def __init__(self,*args,**kargs):
        super(CallUnits,self).__init__(*args,**kargs)

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

        cls._call  = epyu
        cls._call += " --raw "
        cls._call += ' --rdbg ' #: activate remote debugging
        cls._call += ' --rdbg-forward all ' #: forward flag to all nested levels of subprocesses - consider port connection limits to RemoteDebugServer
        cls._call += " -- "
        cls._call += call_scripy

        cls.cache = True
    
    def testSubprocessesWithErrorAsException(self):
        """Selftest of the remote debugging feature.
        """

        call  = self._call
        call += ' EXIT8'

        ret = self.sx.callit(call) #@UnusedVariable
        retX =  [
            8, 
            [
                'fromG', 
                'arbitrary output', 
                'arbitrary signalling NOK string', 
                'arbitrary output'
            ], 
            [
                'arbitrary err output', 
                'arbitrary err signalling NOK string', 
                'arbitrary err output'
            ]
        ]
        self.maxDiff = None
        self.assertEqual(ret,retX)

#
#######################
#
if __name__ == '__main__':
    unittest.main()
