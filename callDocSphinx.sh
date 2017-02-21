PROJECT='epyunit'
VERSION="0.2.8"
RELEASE="0.2.8"
NICKNAME="Dromi"
AUTHOR='Arno-Can Uestuensoez'
COPYRIGHT='Copyright (C) 2010,2011,2015-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez'
LICENSE='Artistic-License-2.0 + Forced-Fairplay-Constraints'
STATUS='alpha'
MISSION='Support extensions for executables as Units of PyUnit.'

# the absolute pathname for this source
MYPATH=${BASH_SOURCE%/*}/
if [ "X${MYPATH#.}" != "X$MYPATH" ];then
	MYPATH=${PWD}/${MYPATH#.};MYPATH=${MYPATH//\/\//\/}
fi

# input base directory
INDIR=${INDIR:-$MYPATH}
if [ "X${INDIR#.}" != "X$INDIR" ];then
	INDIR=${PWD}/${INDIR#.};INDIR=${INDIR//\/\//\/}
fi

echo "MYPATH=$MYPATH"
echo "INDIR=$INDIR"
 
# output base directory
OUTDIR=${OUTDIR:-build/}
if [ ! -e "${OUTDIR}" ];then
	mkdir -p "${OUTDIR}"
fi
export PYTHONPATH=$PWD:$MYPATH:$PYTHONPATH

# import directory for entries of static reference 
STATIC="${OUTDIR}/apidoc/sphinx/_static"

# source entities
FILEDIRS=""
FILEDIRS="$FILEDIRS ${INDIR}UseCases"
FILEDIRS="$FILEDIRS ${INDIR}tests"
FILEDIRS="$FILEDIRS ${INDIR}testdata"

FILEDIRS="$FILEDIRS ${INDIR}bin"

CALL=""
CALL="$CALL export PYTHONPATH=$PWD:$MYPATH:$PYTHONPATH;"
CALL="$CALL sphinx-apidoc "
CALL="$CALL -A '$AUTHOR'"
CALL="$CALL -H '$PROJECT'"
CALL="$CALL -V '$VERSION'"
CALL="$CALL -R '$RELEASE'"
CALL="$CALL -o ${OUTDIR}/apidoc/sphinx"
CALL="$CALL -f -F "
CALL="$CALL $@"

#
bin_epyunit=bin/epyunit

DOCHTMLDIR=${OUTDIR}apidoc/sphinx/_build/
DOCHTML=${DOCHTMLDIR}html/index.html
cat <<EOF
#
# Create apidoc builder...
#
EOF
IFSO=$IFS
IFS=';'
FX=( ${FILEDIRS} )
IFS=$IFSO
for fx in ${FX[@]};do
	echo "CALL=<$CALL '$fx'>"
	eval $CALL "$fx"
done


# rst files
for d in docsrc/*.rst;do cat $d > ${OUTDIR}/apidoc/sphinx/${d##*/}; done

#
# static - literal data
#
# images
for d in docsrc/*.{png,jpg};do cp $d "${STATIC}"; done

# html
for d in docsrc/*.html;do cp $d "${STATIC}"; done

# txt
for d in docsrc/*.txt;do cp $d "${STATIC}"; done

# css
for d in docsrc/*.css;do cp $d "${STATIC}"; done

# sh
for d in bin/*.sh bin/*.py;do cp $d "${STATIC}"; done
#for d in utils/*.sh;do cp $d "${STATIC}"; done

cp ArtisticLicense20.html "${STATIC}"
cp licenses-amendments.txt "${STATIC}"

{
cat <<EOF

import sys,os
extensions.append('sphinx.ext.intersphinx.')
sys.path.insert(0, os.path.abspath('$PWD/..'))
sys.path.insert(0, os.path.abspath('$PWD'))

html_logo = "_static/epyunit-64x64.png"
#html_favicon = None

html_theme = "default"
#html_theme = "classic"
#html_theme = "pyramid"
#html_theme = "agogo"
#html_theme = "bizstyle"
html_theme_options = {
#    "rightsidebar": "true",
#    "relbarbgcolor": "black",

    "externalrefs": "true",
    "sidebarwidth": "290",
    "stickysidebar": "true",

#    "collapsiblesidebar": "true",

#    "footerbgcolor": "",
#    "footertextcolor": "",
#    "sidebarbgcolor": "",
#    "sidebarbtncolor": "",
#    "sidebartextcolor": "",
#    "sidebarlinkcolor": "",
#    "relbarbgcolor": "",
#    "relbartextcolor": "",
#    "relbarlinkcolor": "",
#    "bgcolor": "",
#    "textcolor": "",
#    "linkcolor": "",
#    "visitedlinkcolor": "",
#    "headbgcolor": "",
#    "headtextcolor": "",
#    "headlinkcolor": "",
#    "codebgcolor": "",
#    "codetextcolor": "",
#    "bodyfont": "",
#    "headfont": "",
}

# def setup(app):
#     app.add_stylesheet('custom.css')


EOF
} >> ${OUTDIR}/apidoc/sphinx/conf.py

# put the docs together
#
cat docsrc/index.rst                     > ${OUTDIR}/apidoc/sphinx/index.rst

{
cat <<EOF
Project data summary:

* PROJECT=${PROJECT}

* MISSION=${MISSION}

* AUTHOR=${AUTHOR}

* COPYRIGHT=${COPYRIGHT}

* LICENSE=${LICENSE}

* VERSION=${VERSION}

* RELEASE=${RELEASE}

* STATUS=${STATUS}

* NICKNAME=${NICKNAME}

  ${NICKNAME} see \`The second chain of Fenrir... <https://en.wikipedia.org/wiki/Dromi>\`_  

EOF
} >> ${OUTDIR}/apidoc/sphinx/index.rst 


CALL=" "
CALL="export SPHINXBUILD=sphinx-build; "
CALL="$CALL cd ${OUTDIR}/apidoc/sphinx;"
CALL="$CALL export PYTHONPATH=$PWD:$MYPATH:$PYTHONPATH;"
CALL="$CALL make html ;"
CALL="$CALL cd - "
cat <<EOF
#
# Build apidoc...
#
EOF
echo "CALL=<$CALL>"
eval $CALL

DOCDIR="${DOCDIR:-doc/en/html/man3/$PROJECT}"
if [ ! -e "${DOCDIR}" ];then
	mkdir -p "${DOCDIR}"
fi
echo

