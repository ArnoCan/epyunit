PROJECT='epyunit'
VERSION="0.1.8"
RELEASE="0.1.8"
NICKNAME="Dromi"
AUTHOR='Arno-Can Uestuensoez'
COPYRIGHT='Copyright (C) 2010,2011,2015-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez'
LICENSE='Artistic-License-2.0 + Forced-Fairplay-Constraints'
STATUS='pre-alpha'
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
#FILEDIRS="${INDIR}epyunit"
#FILEDIRS="$FILEDIRS ${INDIR}bin"
FILEDIRS="$FILEDIRS ${INDIR}UseCases"

#FILEDIRS="$FILEDIRS ${INDIR}UseCases/binaries/epyunit/epyunit4RDbg.py"


#FILEDIRS="$FILEDIRS ${INDIR}tests"
#FILEDIRS="$FILEDIRS ${INDIR}testdata"

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
#build=patches
bin_epyunit=bin/epyunit
#cp $bin_epyunit  ${bin_epyunit}.py

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

{
cat <<EOF

extensions.append('sphinx.ext.intersphinx.')
sys.path.insert(0, os.path.abspath('$PWD/..'))
sys.path.insert(0, os.path.abspath('$PWD'))

html_logo = "_static/epyunit-64x64.png"
#html_favicon = None

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
#     app.add_stylesheet('css/custom.css')


EOF
} >> ${OUTDIR}/apidoc/sphinx/conf.py
mkdir -p "${STATIC}/css/"
cp docsrc/custom.css "${STATIC}/css/custom.css"

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

#
cat docsrc/shortcuts.rst          > ${OUTDIR}/apidoc/sphinx/shortcuts.rst
cat docsrc/usecases.rst           > ${OUTDIR}/apidoc/sphinx/usecases.rst
cat docsrc/software_design.rst    > ${OUTDIR}/apidoc/sphinx/software_design.rst

cat docsrc/commandline_scripting.rst         > ${OUTDIR}/apidoc/sphinx/commandline_scripting.rst
cat docsrc/eclipse_integration.rst         > ${OUTDIR}/apidoc/sphinx/eclipse_integration.rst

cat docsrc/subprocessunit.rst > ${OUTDIR}/apidoc/sphinx/subprocessunit.rst
cat docsrc/systemcalls.rst > ${OUTDIR}/apidoc/sphinx/systemcalls.rst
cat docsrc/pydeverdbg.rst > ${OUTDIR}/apidoc/sphinx/pydeverdbg.rst
cat docsrc/rules_logic.rst > ${OUTDIR}/apidoc/sphinx/rules_logic.rst

cat docsrc/pydevd_integration.rst > ${OUTDIR}/apidoc/sphinx/pydevd_integration.rst
cat docsrc/myscript-sh.rst > ${OUTDIR}/apidoc/sphinx/myscript-sh.rst
cat docsrc/myscript.sh > ${OUTDIR}/apidoc/sphinx/myscript.sh
#
cat docsrc/commandline_tools.rst         > ${OUTDIR}/apidoc/sphinx/commandline_tools.rst
cat docsrc/pydeverdbg.rst                > ${OUTDIR}/apidoc/sphinx/pydeverdbg.rst
cat docsrc/epyunit.rst                   > ${OUTDIR}/apidoc/sphinx/epyunit.rst
cat docsrc/epyunit_cli.rst               > ${OUTDIR}/apidoc/sphinx/epyunit_cli.rst
cat docsrc/call_integration.rst          > ${OUTDIR}/apidoc/sphinx/call_integration.rst
cat docsrc/epyunit_example_cli.rst       > ${OUTDIR}/apidoc/sphinx/epyunit_example_cli.rst
cat docsrc/epyunit_example_eclipse_executable.rst   > ${OUTDIR}/apidoc/sphinx/epyunit_example_eclipse_executable.rst
cat docsrc/epyunit_example_eclipse_python.rst   > ${OUTDIR}/apidoc/sphinx/epyunit_example_eclipse_python.rst


#
# static - literal data
cat ArtisticLicense20.html > "${STATIC}/ArtisticLicense20.html"
cat licenses-amendments.txt > "${STATIC}/licenses-amendments.txt"
#
cp docsrc/epyunit-64x64.png "${STATIC}"

cp docsrc/remote-debug-basics.png "${STATIC}"

cp docsrc/pydev-remotedebugger1.png "${STATIC}"
cp docsrc/pydev-remotedebugger1b.png "${STATIC}"
cp docsrc/pydev-remotedebugger2.png "${STATIC}"
cp docsrc/pydev-remotedebugger3.png "${STATIC}"

#CALL="SPHINXOPTS= "
CALL=" "
#CALL="SPHINXBUILD=sphinx-build PYTHONPATH=$PYTHONPATH "
CALL="export SPHINXBUILD=sphinx-build; "
CALL="$CALL cd ${OUTDIR}/apidoc/sphinx;"
#CALL="$CALL export PYTHONPATH=$PYTHONPATH "
CALL="$CALL export PYTHONPATH=$PWD:$MYPATH:$PYTHONPATH;"
#CALL="$CALL export PYTHONPATH=$PYTHONPATH; "
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
cp -a "${DOCHTMLDIR}"/html/* "${DOCDIR}"
echo
echo "display with: firefox -P preview.simple ${DOCHTML}"
echo "display with: firefox -P preview.simple ${DOCDIR}/index.html"
echo
#rm ${bin_epyunit}.py
