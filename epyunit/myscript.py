#!/usr/bin/env python
"""Testee data simulator.

Simulates hard-coded test results for the test of the tool chain itself, 
as reference probe for validation of the chain,
and for test of base functions in case of derived classes.

Refer also to the probe simulators in other languages, when debug and step into
the probe itself is required:

* myscript.py - Python
* myscript.sh - bash
* ffs.


"""
from __future__ import absolute_import
# from __future__ import print_function

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.14'
__uuid__ = '9de52399-7752-4633-9fdc-66c87a9200b8'

__docformat__ = "restructuredtext en"

import sys

_rdbg = None
_rdbg_default = "localhost:5678"  # the defaults as defined by PyDev

if __name__ != '__main__':
    _doc_mode = True
else:
    _doc_mode = False
    
def call_A_OK():
    """
    # A: succeed: OK
      EXIT:
        0
      STDOUT:
        fromA
        
        arbitrary output
        
        arbitrary signalling OK string
        
        arbitrary output
      STDERR:
        --
    """
    print "fromA"
    print "arbitrary output"
    print "arbitrary signalling OK string"
    print "arbitrary output"
    if not _doc_mode:
        sys.exit(0)

def call_B_NOK():
    """
    # B: fail: NOK
       EXIT:
         0
       STDOUT:
         fromB
         
         arbitrary output
         
         arbitrary output
       STDERR:
         arbitrary signalling ERROR string
    """
    print "fromB"
    print "arbitrary output"
    print >> sys.stderr, "arbitrary signalling ERROR string"
    print "arbitrary output"
    if not _doc_mode:
        sys.exit(0)

def call_C_PRIO():
    """
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
    """
    print "fromC"
    print "arbitrary output"
    print "arbitrary signalling OK string"
    print "arbitrary output"
    print >> sys.stderr, "arbitrary signalling ERROR string"
    if not _doc_mode:
        sys.exit(0)

def call_D_EXITOK():
    """
    # D: exit value: EXITOK
       EXIT:
         0
       STDOUT:
         fromD
         
         arbitrary output
         
         arbitrary signalling OK string
         
         arbitrary output
       STDERR:
         --
    """
    print "fromD"
    print "arbitrary output"
    print "arbitrary signalling OK string"
    print "arbitrary output"
    if not _doc_mode:
        sys.exit(0)

def call_E_EXITNOK():
    """
    # E: exit value: EXITNOK
       EXIT:
         1
       STDOUT:
         fromE
         
         arbitrary output
         
         arbitrary signalling OK string
         
         arbitrary output
       STDERR:
         --
    """
    print "fromE"
    print "arbitrary output"
    print "arbitrary signalling OK string"
    print "arbitrary output"
    if not _doc_mode:
        sys.exit(1)

def call_F_EXIT7():
    """
    # F: exit value: EXIT7
       EXIT:
         7
       STDOUT:
         fromF
         
         arbitrary output
         
         arbitrary signalling NOK string
         
         arbitrary output
       STDERR:
         --
    """
    print "fromF"
    print "arbitrary output"
    print "arbitrary signalling NOK string"
    print "arbitrary output"
    if not _doc_mode:
        sys.exit(7)

def call_G_EXIT8():
    """
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
    """
    print "fromG"
    print "arbitrary output"
    print "arbitrary signalling NOK string"
    print "arbitrary output"
    print >> sys.stderr, "arbitrary err output"
    print >> sys.stderr, "arbitrary err signalling NOK string"
    print >> sys.stderr, "arbitrary err output"
    if not _doc_mode:
        sys.exit(8)

def call_H_EXIT9OK3NOK2():
    """
    # H: exit value: EXIT9OK3NOK2
       EXIT:
         9
       STDOUT:
         fromH
         
         OK
         
         OK
         
         OK
       STDERR:
         NOK
         
         NOK
    """
    print "fromH"
    print "OK"
    print "OK"
    print "OK"
    print >> sys.stderr, "NOK"
    print >> sys.stderr, "NOK"
    if not _doc_mode:
        sys.exit(9)

def call_I_STDERRONLY():
    """
    # I: exit value: STDERRONLY
       EXIT:
        0
       STDOUT:
        --
       STDERR:
         fromI
         
         NOK
         
         NOK
    """
    print >> sys.stderr, "fromI"
    print >> sys.stderr, "NOK"
    print >> sys.stderr, "NOK"
    if not _doc_mode:
        sys.exit(0)

def call_DEFAULT():
    """
    # DEFAULT: define: here succeed '--default-ok': DEFAULT
       EXIT:
         123
       STDOUT:
         arbitrary output
       STDERR:
         --
    """
    print >> sys.stdout, "arbitrary output"
    if not _doc_mode:
        sys.exit(123)

    
if "--rdbg" in sys.argv:
    _ai = sys.argv.index("--rdbg")
    _a = sys.argv.pop(_ai)  # --rdbg
    if _ai < len(sys.argv) and sys.argv[_ai][:1] != '-':
        _rdbg = sys.argv.pop(_ai)  # value
    else:
        _rdbg = _rdbg_default

    import epyunit.debug.pydevrdc
    epyunit.debug.pydevrdc.PYDEVD.startDebug()  # start debugging here...
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
                 fromH
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
                 fromI
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
        call_A_OK()
        if not _doc_mode:
            sys.exit(0)

    elif ax in ("NOK",):
        call_B_NOK()
        if not _doc_mode:
            sys.exit(0)

    elif ax in ("PRIO",):
        call_C_PRIO()
        if not _doc_mode:
            sys.exit(0)

    elif ax in ("EXITOK",):
        call_D_EXITOK()
        if not _doc_mode:
            sys.exit(0)

    elif ax in ("EXITNOK",):
        call_E_EXITNOK()
        if not _doc_mode:
            sys.exit(1)

    elif ax in ("EXIT7",):
        call_F_EXIT7()
        if not _doc_mode:
            sys.exit(7)

    elif ax in ("EXIT8",):  # G: exit value
        call_G_EXIT8()
        if not _doc_mode:
            sys.exit(8)

    elif ax in ("EXIT9OK3NOK2",):
        call_H_EXIT9OK3NOK2()
        if not _doc_mode:
            sys.exit(9)

    elif ax in ("STDERRONLY",):
        call_I_STDERRONLY()
        if not _doc_mode:
            sys.exit(0)

    else:
        call_DEFAULT()
        if not _doc_mode:
            sys.exit(123)

# DEFAULT: define: here succeed '--default-ok'
print "arbitrary output"
if not _doc_mode:
    sys.exit(123)
