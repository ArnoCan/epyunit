# -*- coding: utf-8 -*-
from __future__ import absolute_import

import unittest
import os,sys

from testdata import epyu,call_scripy
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

        call  = epyu
        call += ' ' + call_scripy
        call += ' OK'

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
        retX = [0, ['fromA', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'], []]
        self.assertEqual(ret, retX)

#
#######################
#
if __name__ == '__main__':
    unittest.main()
