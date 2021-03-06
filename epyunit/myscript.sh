#
# NAME:      myscript.sh
# VERSION:   01.01.003
# AUTHOR:    Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez
# COPYRIGHT: Copyright (C) 2015,2016 Arno-Can Uestuensoez
#

if test "X$1" == "X-h" -o "X$1" == "X-help" -o "X$1" == "X--help";then
	cat <<EOF

Provided test cases:

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
    fromG
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

EOF

	exit 0
fi

if test "X$1" == "X--";then
	shift
fi

# A: succeed
if test "X$1" == "XOK";then
    echo fromA
    echo arbitrary output
    echo arbitrary signalling OK string
    echo arbitrary output

# B: fail
elif test "X$1" == "XNOK";then
    echo fromB
    echo arbitrary output
    echo arbitrary signalling ERROR string >&2
    echo arbitrary output

# C: redundancy resolved by user defined priority
elif test "X$1" == "XPRIO";then
    echo fromC
    echo arbitrary output
    echo arbitrary signalling OK string
    echo arbitrary signalling ERROR string >&2
    echo arbitrary output

# D: exit value
elif test "X$1" == "XEXITOK";then
    echo fromD
    echo arbitrary output
    echo arbitrary signalling OK string
    echo arbitrary output
    exit 0

# E: exit value
elif test "X$1" == "XEXITNOK";then
    echo fromE
    echo arbitrary output
    echo arbitrary signalling OK string
    echo arbitrary output
    exit 1

# F: exit value
elif test "X$1" == "XEXIT7";then
    echo fromF
    echo arbitrary output
    echo arbitrary signalling NOK string
    echo arbitrary output
    exit 7

# G: exit value
elif test "X$1" == "XEXIT8";then
    echo fromG
    echo arbitrary output
    echo arbitrary signalling NOK string
    echo arbitrary output
    echo arbitrary err output >&2
    echo arbitrary err signalling NOK string >&2
    echo arbitrary err output >&2
    exit 8

# H: exit value
elif test "X$1" == "XEXIT9OK3NOK2";then
    echo fromH
    echo OK
    echo OK
    echo OK
    echo NOK >&2
    echo NOK >&2
    exit 9

# I: exit value
elif test "X$1" == "XSTDERRONLY";then
    echo fromI >&2
    echo NOK >&2
    echo NOK >&2
    exit 0

elif test "X$1" == "X--";then
    echo ' '

# DEFAULT: define: here succeed '--default-ok'
else
    echo arbitrary output
    exit 123

fi
