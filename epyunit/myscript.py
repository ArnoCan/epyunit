#!/usr/bin/env python
from __future__ import absolute_import
# from __future__ import print_function

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.12'
__uuid__ = '9de52399-7752-4633-9fdc-66c87a9200b8'

__docformat__ = "restructuredtext en"

import sys

_rdbg = None
_rdbg_default = "localhost:5678"  # the defaults as defined by PyDev

if "--rdbg" in sys.argv:
    _ai = sys.argv.index("--rdbg")
    _a = sys.argv.pop(_ai)  # --rdbg
    if _ai < len(sys.argv) and sys.argv[_ai][:1] != '-':
        _rdbg = sys.argv.pop(_ai)  # value
    else:
        _rdbg = _rdbg_default

    import epyunit.PyDevERDbg
    epyunit.PyDevERDbg.PYDEVD.startDebug()  # start debugging here...
    #
    # remote breakpoints could be set from here on...
    #

for ax in sys.argv[1:]:
    ax = ax.upper()
    if ax in ("-h", "-help", "--help",):

        print """
            Provided test cases: ( OK, NOK, PRIO, EXITOK, EXITNOK, EXIT7, EXIT8, EXIT9OK3NOK2, STDERRONLY, DEFAULT )
            
            # A: succeed: OK
              EXIT:
                0
              STDOUT:
                fromA
                arbitrary output
                arbitrary signalling OK string
                arbitrary output
              STDERR:
                -
            
            # B: fail: NOK
               EXIT:
                 0
               STDOUT:
                 fromB
                 arbitrary output
                 arbitrary output
               STDERR:
                 arbitrary signalling ERROR string
            
            # C: redundancy resolved by user defined priority: PRIO
               EXIT:
                 0
               STDOUT:
                 fromC
                 arbitrary output
                 arbitrary signalling OK string
                 arbitrary output
               STDERR:
                 arbitrary signalling ERROR string
            
            
            # D: exit value: EXITOK
               EXIT:
                 0
               STDOUT:
                 fromD
                 arbitrary output
                 arbitrary signalling OK string
                 arbitrary output
               STDERR:
                 -
            
            # E: exit value: EXITNOK
               EXIT:
                 1
               STDOUT:
                 fromE
                 arbitrary output
                 arbitrary signalling OK string
                 arbitrary output
               STDERR:
                 -
            
            # F: exit value: EXIT7
               EXIT:
                 7
               STDOUT:
                 fromF
                 arbitrary output
                 arbitrary signalling NOK string
                 arbitrary output
               STDERR:
                 -
            
            # G: exit value: EXIT8
               EXIT:
                 8
               STDOUT:
                 fromG
                 arbitrary output
                 arbitrary signalling NOK string
                 arbitrary output
               STDERR:
                 arbitrary err output
                 arbitrary err signalling NOK string
                 arbitrary err output
            
            # H: exit value: EXIT9OK3NOK2
               EXIT:
                 9
               STDOUT:
                 fromG
                 OK
                 OK
                 OK
               STDERR:
                 NOK
                 NOK
            
            # I: exit value: STDERRONLY
               EXIT:
                0
               STDOUT:
                -
               STDERR:
                 NOK
                 NOK
            
            # DEFAULT: define: here succeed '--default-ok': DEFAULT
               EXIT:
                 123
               STDOUT:
                 arbitrary output
               STDERR:
                 -
            	
        """
        sys.exit(0)

    elif ax in ("OK",): 
        # A: succeed
        print "fromA"
        print "arbitrary output"
        print "arbitrary signalling OK string"
        print "arbitrary output"
        sys.exit(0)

    elif ax in ("NOK",):
        # B: fail
        print "fromB"
        print "arbitrary output"
        print >> sys.stderr, "arbitrary signalling ERROR string"
        print "arbitrary output"
        sys.exit(0)

    elif ax in ("PRIO",):
        # C: redundancy resolved by user defined priority
        print "fromC"
        print "arbitrary output"
        print "arbitrary signalling OK string"
        print "arbitrary output"
        print >> sys.stderr, "arbitrary signalling ERROR string"
        sys.exit(0)

    elif ax in ("EXITOK",):
        # D: exit value
        print "fromD"
        print "arbitrary output"
        print "arbitrary signalling OK string"
        print "arbitrary output"
        sys.exit(0)

    elif ax in ("EXITNOK",):
        # E: exit value
        print "fromE"
        print "arbitrary output"
        print "arbitrary signalling OK string"
        print "arbitrary output"
        sys.exit(1)

    elif ax in ("EXIT7",):
        # F: exit value
        print "fromF"
        print "arbitrary output"
        print "arbitrary signalling NOK string"
        print "arbitrary output"
        sys.exit(7)

    elif ax in ("EXIT8",):  # G: exit value
        print "fromG"
        print "arbitrary output"
        print "arbitrary signalling NOK string"
        print "arbitrary output"
        print >> sys.stderr, "arbitrary err output"
        print >> sys.stderr, "arbitrary err signalling NOK string"
        print >> sys.stderr, "arbitrary err output"
        sys.exit(8)

    elif ax in ("EXIT9OK3NOK2",):
        # H: exit value
        print "fromH"
        print "OK"
        print "OK"
        print "OK"
        print >> sys.stderr, "NOK"
        print >> sys.stderr, "NOK"
        sys.exit(9)

    elif ax in ("STDERRONLY",):
        # I: exit value
        print >> sys.stderr, "fromI"
        print >> sys.stderr, "NOK"
        print >> sys.stderr, "NOK"
        sys.exit(0)

    else:
        # DEFAULT: define: here succeed '--default-ok'
        print >>sys.stderr,"ERROR:Unknown parameter:"+str(ax)
        sys.exit(123)

# DEFAULT: define: here succeed '--default-ok'
print "arbitrary output"
sys.exit(123)
