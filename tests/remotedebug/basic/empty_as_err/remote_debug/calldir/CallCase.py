"""
Verifies basic facilities for remote debugging by starting a subprocess.
Uses:

* epyunit.SystemCalls()

* epyunit.callit()

Applies a two-level subprocess stack:

0. This UseCase

1. The wrapper 'epyunit4RDbg.py'

2. The script with dummy responses for tests 'myscript.sh'

"""
from __future__ import absolute_import

import unittest
import os,sys

#
#######################
#
class CallUnits(unittest.TestCase):
    def testCallTwoLevelsOfSubprocesses(self):
        """Selftest of the remote debugging feature.
        """
        #
        #--- fetch options
        #
        try:
            from epyunit.SystemCalls import SystemCalls
        except Exception as e:
            print "\n#\n#*** Set 'PYTHONPATH' ("+str(e)+")\n#\n"
            sys.exit(1)

        #
        # *** first level subprocess - call Python process and bring it under control of PyDev ***
        #
        tstcall = os.path.abspath(os.path.dirname(__file__)+os.sep+'../subprocdir/bin/epyunit4RDbg.py')
        tstcall = os.path.normpath(tstcall)
        call  = 'python ' + tstcall  # call the wrapper 

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

        sx = SystemCalls(**_kargs)
        ret = sx.callit(call)
        
        #
        retX = [ 
            2, 
            ["[]"], # for now literally from sub-sub-process
            [ "['ERROR:MissingCallstr']"] # for now literally from sub-sub-process
        ]
        self.assertEqual(retX, ret) 

#
#######################
#
if __name__ == '__main__':
    unittest.main()
