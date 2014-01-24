Packages
========

.. contents::
    :local:
    :depth: 2
    :backlinks: none

Packages are used to group type and function declarations and to introduce high level structure. They are conceptually close to namespaces in C++ and to packages in Java and C#.


Syntax
------

.. code-block:: scala

    QualifiedName ::= Ident("." Ident)*

    Decorator ::= "@" (Annotation | Attribute)

    Annotation ::= QualifiedName "(" Expr ("," Expr)* ")"

    Attribute ::= Ident "=" Expr

    PackageDef ::= Decorator* "abstract"? "package" QualifiedName? ("extends" QualifiedName)*
                        ("{" MemberDef* "}") | MemberDef*

    MemberDef ::= PackageDef | FunctionDef | TypeDef

Composite names
---------------

Package may have a composite name like ``X.Y.Z`` -- in this case declaration like

.. code-block:: scala

    package X.Y.Z {
        def f() = //...
        // ...
    }

is a shortcut for

.. code-block:: scala

    package X {
        package Y {
            package Z {
                def f() = //...
                // ...
            }
        }
    }

Members are accessed in a natural way. For example, function ``f`` can be accessed from package ``X`` as ``Y.Z.f``.

Attribute inheritance
---------------------

Members of a package inherit its attributes

.. code-block:: scala

    @X = "A"
    @Y = "B"
    package N
    {
        @X = "C"
        package M
        {
            def g()
        }
    }

is equivalent to

.. code-block:: scala

    @X = "A"
    @Y = "B"
    package N
    {
        @X = "C"
        package M
        {
            @X = "C"
            @Y = "B"
            def g()
        }
    }

Anonymous packages
------------------

Sometimes packages serve only to assign attributes to a number of members. In these cases package name can be omitted

.. code-block:: scala

    package N
    {
        @X = "C"
        package
        {
            def f()
            def g()
            def h()
        }
    }

is equivalent to

.. code-block:: scala

    package N
    {
        @X = "C"
        def f()

        @X = "C"
        def g()

        @X = "C"
        def h()
    }

Braceless package body
----------------------

Braces may be omitted. In this case the rest of the file is treated as inner members of the package

.. code-block:: scala

    package N
    package M
    def g()
    package L
    def f()

is equivalent to

.. code-block:: scala

    package N {
        package M {
        def g()
            package L {
            def f()
    }}}
    
Abstract packages
-----------------

If no typing and no code generation should be done for a package, it should be marked as ``abstract``. Normally these packages are used only code reuse through package inheritance 

Package inheritance
-------------------

If package ``D`` derives from package ``B`` it inherits all his members literally (so it can be considered as a vary particular case of C++ macros). Multiple package inheritance is allowed. For example, 

.. code-block:: scala

    abstract package B1 
    {
        def f() = u() // note that u isn't defined at all
        def g() = u() 
    }
    
    abstract package B2
    {
        def f() = v() // note that v defined at D 
    }
    
    package D extends B1 extends B2
    {
       def g() = v() 
       def v() = // ...  
    }
    
is equivalent to 

.. code-block:: scala

    package D 
    {
       def f() = v()  // inherited from B2
       def g() = v()  // overrides B1.g
       def v() = // ...  
    }

    



