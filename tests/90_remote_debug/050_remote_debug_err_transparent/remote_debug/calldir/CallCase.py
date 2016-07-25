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

from epyunit.SystemCalls import SystemCalls,SystemCallsExceptionSubprocessError

#
#######################
#
class CallUnits(unittest.TestCase):
    def testSubprocessesWithErrorAsException(self):
        """Selftest of the remote debugging feature.
        """

        #
        # *** first level subprocess - call Python process and bring it under control of PyDev ***
        #
        tstcall = os.path.abspath(os.path.dirname(__file__)+os.sep+'../subprocdir/bin/epyunit4RDbg.py')
        tstcall = os.path.normpath(tstcall)
        call  = 'python ' + tstcall  # call the wrapper 

        #
        # *** second level subprocess - call bash process and evaluate hard-coded response ***
        #
        scall = os.path.dirname(tstcall)+'/../../scriptdir/libexec/myscript.sh'       # add a script
        scall = os.path.normpath(scall)
        call += ' ' + scall
        call += ' EXIT8'

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
        ret = sx.callit(call) #@UnusedVariable

        #
        # Verify results here manually, thus requires the default tuple.
        # In normal operations we should prefer one of the others for
        # prepared error handling.
        #
        if ret[0] != 8:
            print 'Received custom:STDOUT:'
            if type([1]) is str:
                print ret[1]
            else:
                print '\n'.join(ret[1])
                 
            print 'Received custom:STDERR:'
            if type([2]) is str:
                print >>sys.stderr , ret[2] 
            else:
                print >>sys.stderr , '\n'.join(ret[2]) 

        #
        # *** the default tuple - with demo-labels for stdout + stderr ***
        #
        assert ret[0] == 8

#
#######################
#
if __name__ == '__main__':
    unittest.main()
