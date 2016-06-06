"""Use-Cases 'FileSysObjectsMin.findRelPathInUpperTree'

Find a matching relative filepathname in upper directory
tree. 

**Example**::

  a
  |-- A.txt
  `-- b
      |-- B.txt
      `-- c
          |-- C.txt
          `-- d
              `-- D.txt


Before::

  'C.txt'

Call::

   findRelPathInUpperTree( 'C.txt' )

After::

  'a/b/c/C.txt'

"""