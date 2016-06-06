"""Distribute 'epyunit', a generic unit test wrapper for commandline interfaces.

   Installs 'epyunit', adds/modifies the following helper features to standard
   'setuptools' options.

   Args:
      build_sphinx: Creates documentation for runtime system by Sphinx, html only.
         Calls 'callDocSphinx.sh'.
      build_epydoc: Creates documentation for runtime system by Epydoc, html only.
         Calls 'callDocEpydoc.sh'.

      test: Runs PyUnit tests by discovery.

      --no-install-required: Suppresses installation dependency checks, 
          requires appropriate PYTHONPATH.
      --offline: Sets online dependencies to offline, or ignores online
          dependencies.

      --exit: Exit 'setup.py'.

      --help-epyunit: Displays this help.

   Returns:
      Results for success in installed 'epyunit'.

   Raises:
      ffs.

"""
# priority is offline here - needs manual 'bootstrap', thus dropped ez_setup for now
# import ez_setup
# ez_setup.use_setuptools()

#import sys
#from polybori.plot import THEN

#
#*** common source header
#
__author__ = 'Arno-Can Uestuensoez'
__author_email__ = 'acue_sf2@sourceforge.net'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2015-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.10'
__uuid__='9de52399-7752-4633-9fdc-66c87a9200b8'


# some debug
if __debug__:
    __DEVELTEST__ = True

#
#***
#
import os,sys
from setuptools import setup #, find_packages
import fnmatch
import re


#
#*** ===>>> setup.py helper
#
def find_files(srcdir, *wildcards, **kw):
    """Assembles a list of package files for package_files.

        Args:
            srcdir: Source root.
            *wildcards: list of globs.
            **kw: Additional control of resolution:
                single_level: Flat only.
                subpath: Cut topmost path elemenr from listelements,
                    special for dictionaries.
                nopostfix: Drop filename postfix.
                packages: List packages only, else files.
                yield_folders:
        Returns:
            Results in an list.

        Raises:
            ffs.

    """
    def all_files(root, *patterns, **kw):
        ret=[]
        single_level = kw.get('single_level', False)
        subpath = kw.get('subpath', False)
        nopostfix = kw.get('nopostfix', True)
        packages = kw.get('packages', True)
        yield_folders = kw.get('yield_folders', True)

        for path, subdirs, files in os.walk(root):
            if yield_folders:
                files.extend(subdirs)
            files.sort( )

            if subpath:
                path=re.sub(r'^[^'+os.sep+']*'+os.sep, '',path)

            for name in files:
                if name in ('.gitignore', '.git', '.svn'):
                    continue

                for pattern in patterns:
                    if fnmatch.fnmatch(name, pattern):
                        if packages:
                            if not name == '__init__.py':
                                continue
                            ret.append(path)
                            continue
                        if nopostfix:
                            name=os.path.splitext(name)[0]

                        ret.append(os.path.join(path, name))

            if single_level:
                break
        return ret

    file_list = all_files(srcdir, *wildcards,**kw)
    return file_list

def usage():
    if __name__ == '__main__':
        import pydoc
        #FIXME: literally displayed '__main__'
        print pydoc.help(__name__)
    else:
        help(str(os.path.basename(sys.argv[0]).split('.')[0]))

#
#* shortcuts
#

exit_code = 0

# custom doc creation by sphinx-apidoc
if 'build_sphinx' in sys.argv:
    print "#---------------------------------------------------------"
    exit_code = os.system('./callDocSphinx.sh') # create apidoc
    print "#---------------------------------------------------------"
    print "Called/Finished callDocSphinx.sh => exit="+str(exit_code)
    sys.argv.remove('build_sphinx')

# custom doc creation by epydoc
if 'build_epydoc' in sys.argv:
    print "#---------------------------------------------------------"
    exit_code = os.system('./callDocEpydoc.sh') # create apidoc
    print "#---------------------------------------------------------"
    print "Called/Finished callDocEpydoc.sh => exit="+str(exit_code)
    sys.argv.remove('build_epydoc')

# call of complete test suite by 'discover'
if 'test' in sys.argv:
    print "#"
    exit_code = os.system('python -m unittest discover -s tests -p CallCase.py') # traverse tree
    print "#"
    print "Called/Finished PyUnit tests => exit="+str(exit_code)
    print "exit setup.py now: exit="+str(exit_code)
    sys.argv.remove('test')

# Intentional HACK: ignore (online) dependencies, mainly foreseen for developement
__no_install_requires = False
if '--no-install-requires' in sys.argv:
    __no_install_requires = True
    sys.argv.remove('--no-install-requires')

# Intentional HACK: offline only, mainly foreseen for developement
__offline = False
if '--offline' in sys.argv:
    __offline = True
    __no_install_requires = True
    sys.argv.remove('--offline')

# Execution failed - Error.
if exit_code != 0:
    sys.exit(exit_code)

# Help on addons.
if '--help-epyunit' in sys.argv:
    usage()
    sys.exit(0)

# Exit here.
if '--exit' in sys.argv:
    sys.exit(0)

# if epyunit-specials only
if len(sys.argv)==1:
    sys.exit(exit_code)

#
#*** <<<=== setup.py helper
#


#
#*** setup.py configuration
#
_name='epyunit'

_description=("The 'epyunit' package provides a wrapper for unit tests of commandline interfaces." 
              "The package could be used either from the comandline, or integrated into Eclipse "
              "with PyDev."
              )

# def read(fname):
#     return open(os.path.join(os.path.dirname(__file__), fname)).read()
_README = os.path.join(os.path.dirname(__file__), 'README')
_long_description = open(_README).read() + 'nn'

_platforms='any'

_classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: Free To Use But Restricted",
    "License :: OSI Approved :: Artistic License",
    "Natural Language :: English",
    "Operating System :: Microsoft :: Windows :: Windows 7",
    "Operating System :: OS Independent",
    "Operating System :: POSIX :: BSD :: OpenBSD",
    "Operating System :: POSIX :: Linux",
    "Operating System :: POSIX",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",    
    "Programming Language :: Python :: 2.7",    
    "Programming Language :: Unix Shell",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Utilities",
]

_keywords  = ' Python PyUnit PyDev Eclipse CLI command line'
_keywords += ' test unit unittest regression regressiontest fileobjects commandline'
_keywords += ' JSON json ujson'

_packages = ["epyunit"]
_scripts = ["bin/epyunit", ]

_package_data = {
    'epyunit': ['README','ArtisticLicense20.html', 'licenses-amendments.txt',
                'myscript.sh',
            ],
}

#_download_url="https://github.com/ArnoCan/epyunit/"
_download_url="https://sourceforge.net/projects/epyunit/files/"

_url='https://sourceforge.net/projects/epyunit/'

_install_requires=[
    'inspect',
    're',
    'sysobjects',
#    'termcolor'
]

_test_suite="tests.CallCase"

if __debug__:
    if __DEVELTEST__:
        print "#---------------------------------------------------------"
        print "packages="+str(_packages)
        print "#---------------------------------------------------------"
        print "package_data="+str(_package_data)
        print "#---------------------------------------------------------"



#
#*** ===>>> setup.py helper
#

# Intentional HACK: ignore (online) dependencies, mainly foreseen for developement
if __no_install_requires:
    print "#"
    print "# Changed to offline mode, ignore install dependencies completely."
    print "# Requires appropriate PYTHONPATH."
    print "# Ignored dependencies are:"
    print "#"
    for ir in _install_requires:
        print "#   "+str(ir)
    print "#"
    _install_requires=[]

#
#*** <<<=== setup.py helper
#


#
#*** do it now...
#
setup(name=_name,
      version=__version__,
      author=__author__,
      author_email=__author_email__,
      classifiers=_classifiers,
      description=_description,
      download_url=_download_url,
      install_requires=_install_requires,
      keywords=_keywords,
      license=__license__,
      long_description=_long_description,
      platforms=_platforms,
      url=_url,
      scripts=_scripts,
      packages=_packages,
      package_data=_package_data
)
