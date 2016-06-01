PROJECT='epyunit'
VERSION="0.0.1"
RELEASE="0.0.1"
NICKNAME="Dromi"
AUTHOR='Arno-Can Uestuensoez'
COPYRIGHT='Copyright (C) 2015-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez'
LICENSE='Artistic-License-2.0 + Forced-Fairplay-Constraints'

MYPATH=${BASH_SOURCE%/*}/
if [ "X${MYPATH#./}" != "X$MYPATH" ];then
	MYPATH=${PWD}${MYPATH#.}
fi

# input base directory
INDIR=${INDIR:-$MYPATH}

# output base directory
OUTDIR=${OUTDIR:-build/}
if [ ! -e "${OUTDIR}" ];then
	mkdir -p "${OUTDIR}"
fi
export PYTHONPATH=$PYTHONPATH:$PWD:${MYPATH}

# source entities
FILEDIRS=""
FILEDIRS="$FILEDIRS `find ${INDIR}epyunit -type f -name '*.py'`"
FILEDIRS="$FILEDIRS `find ${INDIR}bin -type f -name '*.py'`"

CALL=epydoc
CALL="$CALL --graph=all"
CALL="$CALL --html"
#CALL="$CALL --pdf"
CALL="$CALL --pstat pstatfile"
CALL="$CALL -o ${OUTDIR}/apidoc/epydoc/"
CALL="$CALL "
CALL="$CALL $@"
CALL="$CALL ${FILEDIRS} "
cat <<EOF
#
# Create apidoc builder...
#
EOF
echo "CALL=<$CALL>"
eval $CALL

echo
echo "call: firefox -P preview.simple -new-instance ${OUTDIR}/epydoc/index.html"
echo
