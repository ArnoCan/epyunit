#
# NAME:      myscript.sh
# VERSION:   01.01.001
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
     arbitrary output
     arbitrary signalling OK string
     arbitrary output
  STDERR:
     -

# B: fail: NOK
   EXIT:
     0
   STDOUT:
     arbitrary output
     arbitrary output
   STDERR:
     arbitrary signalling ERROR string

# C: redundancy resolved by user defined priority: PRIO
   EXIT:
     0
   STDOUT:
     arbitrary output
     arbitrary signalling OK string
     arbitrary output
   STDERR:
     arbitrary signalling ERROR string


# D: exit value: EXITOK
   EXIT:
     0
   STDOUT:
     arbitrary output
     arbitrary signalling OK string
     arbitrary output
   STDERR:
     -

# E: exit value: EXITNOK
   EXIT:
     1
   STDOUT:
     arbitrary output
     arbitrary signalling OK string
     arbitrary output
   STDERR:
     -

# F: exit value: EXIT7
   EXIT:
     7
   STDOUT:
     arbitrary output
     arbitrary signalling NOK string
     arbitrary output
   STDERR:
     -

# G: exit value: EXIT8
   EXIT:
     8
   STDOUT:
     arbitrary output
     arbitrary signalling NOK string
     arbitrary output
   STDERR:
     arbitrary err output
     arbitrary err signalling NOK string
     arbitrary err output

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

# A: succeed
if test "X$1" == "XOK";then
    echo arbitrary output
    echo arbitrary signalling OK string
    echo arbitrary output

# B: fail
elif test "X$1" == "XNOK";then
    echo arbitrary output
    echo arbitrary signalling ERROR string >&2
    echo arbitrary output

# C: redundancy resolved by user defined priority
elif test "X$1" == "XPRIO";then
    echo arbitrary output
    echo arbitrary signalling OK string
    echo arbitrary signalling ERROR string >&2
    echo arbitrary output

# D: exit value
elif test "X$1" == "XEXITOK";then
    echo arbitrary output
    echo arbitrary signalling OK string
    echo arbitrary output
    exit 0

# E: exit value
elif test "X$1" == "XEXITNOK";then
    echo arbitrary output
    echo arbitrary signalling OK string
    echo arbitrary output
    exit 1

# F: exit value
elif test "X$1" == "XEXIT7";then
    echo arbitrary output
    echo arbitrary signalling NOK string
    echo arbitrary output
    exit 7

# G: exit value
elif test "X$1" == "XEXIT8";then
    echo arbitrary output
    echo arbitrary signalling NOK string
    echo arbitrary output
    echo arbitrary err output >&2
    echo arbitrary err signalling NOK string >&2
    echo arbitrary err output >&2
    exit 8


# DEFAULT: define: here succeed '--default-ok'
else
    echo arbitrary output
    exit 123

fi
