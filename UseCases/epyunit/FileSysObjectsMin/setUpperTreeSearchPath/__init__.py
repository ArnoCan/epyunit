"""Use-Cases 'FileSysObjectsMin.setUpperTreeSearchPath'

Create hierarchical search paths for basic variants.
The order simulates inheritance e.g. for superior
classes, data, and executables by grouping via
filesystem hierarchy.

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

  sys.path = [ 'A', ]

Call::

  setUpperTreeSearchPath( 'a/b/c/d', basename('a') )

After::

  sys.path = [ 'a/b/c/d', 'a/b/c', 'a/b', 'a', 'A', ]

"""