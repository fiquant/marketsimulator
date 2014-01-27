Using the compiler
==================

The compiler is invoked automatically once one of files at ``marketsim/gen`` directory (except those ones who reside at ``.output``, ``.idea``, ``project``, ``target``, ``_out``, ``_intrinsic``) becomes newer than ``marketsil/gen/.timestamp`` file. It implies that all changes in strategy definition files and in the compiler itself incur regeneration of Python code.

The compiler processes all strategy definitions files that reside at ``marketsim/gen/defs`` directory (in future ability to tell the compiler what files should be processed will be added).

The result of the compilation is put into ``marketsim/gen/_out`` and ``marketsim/_pub`` directories. For every function with full name like ``pkgA.pkgB.F`` actual implementation is generated as class ``F`` in file ``marketsim/gen/_out/pkgA/pkgB/_F.py``. This generated implementation is not for direct use but alias ``pkgA.pkgB.F`` generated into package ``marketsim._pub`` should be used instead.

For debug puproses the following intermediate files are dumped:

* raw and pretty-printed representation of input files are put into directory ``marketsim/gen/.parsed``
* raw and pretty-printed representation of all input files after building name tables is put into ``marketsim/gen/.output/names.*``
* pretty-printed representation of all input files after typing is put into ``marketsim/gen/.output/typed.sc``

Pretty-printed representation is reparsed and compared with the original in order to make sure that parsing is a reverse operation for pretty-printing.
