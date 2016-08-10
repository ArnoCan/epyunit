"""
Verifies basic facilities for remote debugging by starting a subprocess with '--selftest'.

"""
from __future__ import absolute_import

import unittest
import os,sys
 
from filesysobjects.FileSysObjects import setUpperTreeSearchPath,findRelPathInSearchPath
from epyunit.SystemCalls import SystemCalls  

#
#######################
#
slst = []
setUpperTreeSearchPath(os.path.abspath(os.path.dirname(__file__)),'epyunit',slst)

epyu = findRelPathInSearchPath('bin/epyunit',slst,matchidx=0)

class CallUnits(unittest.TestCase):
    def testCallTwoLevelsOfSubprocesses(self):
        """Selftest of the remote debugging feature.
        """
        _call  = epyu + " -v --rdbg --selftest "

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

        callkargs = {}
        ret = sx.callit(_call,**callkargs)

        #
        # Verify results here manually, thus requires the default tuple.
        # In normal operations we should prefer one of the others for
        # prepared error handling.
        #
        if ret[0] != 0:
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
        assert ret[0] == 0
        retX = [
            0, 
            [
                '#*** epyunit/myscript.sh DEFAULT ***', 
                '', 
                '#*** epyunit/myscript.sh OK ***', 
                '', 
                '#*** epyunit/myscript.sh PRIO ***', 
                '', 
                '#*** epyunit/myscript.sh EXITOK ***', 
                '', 
                '#*** epyunit/myscript.sh EXITNOK ***', 
                '', 
                '#*** epyunit/myscript.sh EXIT7 ***', 
                '', 
                '#*** epyunit/myscript.sh EXIT8 ***', 
                '', 
                '#*** epyunit/myscript.sh DEFAULT ***'
            ], 
            []
        ]
        retX[1] = [ x for x in retX[1] if x!='']

        self.assertEqual(retX[1], retX[1])
        self.assertEqual(retX[2], [])
        

#
#######################
#
if __name__ == '__main__':
    unittest.main()
