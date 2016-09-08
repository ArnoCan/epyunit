"""
Verifies basic facilities for remote debugging by starting a subprocess with '--selftest'.

"""
from __future__ import absolute_import

import unittest

from testdata import epyu,call_scripy
import epyunit.SubprocUnit
from epyunit.unittest.subprocess import TestExecutable


#
#######################
#
class CallUnits(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.syskargs = {}
        #
        # *** some error passing options, refer to API ***
        #
        # _kargs['passerr'] = True
        # _kargs['errasexcept'] = True
        # _kargs['useexit'] = True
        # _kargs['usestderr'] = True
        #
        cls.syskargs['emptyiserr'] = True
        cls.sx = epyunit.SubprocUnit.SubprocessUnit(**cls.syskargs)

        #
        # wrapper call
        cls._call  = epyu
        cls._call += " -v "
        cls._call += " --rdbg "
        cls._call += " --selftest "

    def testCallTwoLevelsOfSubprocesses(self):
        """Selftest of the remote debugging feature.
        """
        callkargs = {}
        retX = [
            0,
            [
                '#*** epyunit/myscript.py DEFAULT ***',
                '',
                '#*** epyunit/myscript.py OK ***',
                '',
                '#*** epyunit/myscript.py PRIO ***',
                '',
                '#*** epyunit/myscript.py EXITOK ***',
                '',
                '#*** epyunit/myscript.py EXITNOK ***',
                '',
                '#*** epyunit/myscript.py EXIT7 ***',
                '',
                '#*** epyunit/myscript.py EXIT8 ***',
                '',
                '#*** epyunit/myscript.py EXIT9OK3NOK2 ***',
                '',
                '#*** epyunit/myscript.py STDERRONLY ***',
                '',
                '#*** epyunit/myscript.py DEFAULT ***'
            ],
            []
        ]
        #retX[1] = [ x for x in retX[1] if x!='']

        ret = self.sx.callit(self._call,**callkargs)
        self.assertEqual(ret, retX)


#
#######################
#
if __name__ == '__main__':
    unittest.main()
