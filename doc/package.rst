Packages
========

Packages are used to group type and function declarations and to introduce high level structure

Syntax:

.. code-block:: scala

    QualifiedName ::= Ident("." Ident)*

    Decorator ::= "@" (Annotation | Attribute)

    Annotation ::= QualifiedName "(" Expr ("," Expr)* ")"

    Attribute ::= Ident "=" Expr

    PackageDef ::= Decorator* "abstract"? "package" QualifiedName? ("extends" QualifiedName)*
                        ("{" MemberDef* "}") | MemberDef*

    MemberDef ::= PackageDef | FunctionDef | TypeDef

Packages are conceptually close to namespaces in C++ and to packages in Java and C#.

Package may have a composite name like X.Y.Z -- in this case declaration like

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

Members are accessed in a natural way. For example, function `f` can be accessed from package `X` as `Y.Z.f`.

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

