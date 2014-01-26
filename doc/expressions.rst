Expressions
===========

.. contents::
    :local:
    :depth: 2
    :backlinks: none

Syntax
------

.. code-block:: scala

    Expr ::= Expr ":" Type                                      // cast to a weaker type
           | "if" Expr "then" Expr "else" Expr                  // conditional
           | Expr ("+" | "-" | "*" | "/") Expr                  // aritmethic binary expression
           | "-" Expr                                           // unary minus
           | Expr ("and" | "or") Expr                           // logic binary expression
           | "not" Expr                                         // logic negation
           | Expr ("<" | "<=" | ">" | ">=" | "==" | "<>")  Expr // comparison expression
           | "(" Expr ")"
           | Expr "(" (Expr ("," Expr)*)? ")"                   // function application
           | QualifiedName                                      // reference to a name, local or global

Float type unification and implicit conversions
-----------------------------------------------

At the moment some implicit conversions are hardcoded in the compiler. The rules following are applied in order:

1. If arguments of an operation can be casted to ``IObservable[Float]``, then expression type is ``IObservable[Float]``

2. If arguments of an operation can be casted to ``IFunction[Float]``, then expression type is ``IFunction[Float]``

3. If arguments of an operation can be casted to ``Float``, then expression type is ``Float``

4. If one argument of a function can be casted to ``IFunction[Float]`` and another one to ``Float``, an implicit conversion to ``IFunction[Float]`` is applied for the latter one (by injecting a call to ``constant(x)`` function).

In future, once generic and implicit functions are introduced, there won't be any need in these hardcoded rules.

We will refer to type obtained by appling these rules to expressions ``e1`` and ``e2`` as ``unifyFloat(e1, e2)``. Under *float-like type* we will understand a type that can be casted either to ``Float`` or to ``() => Float``

Expression typechecking
-----------------------

``e : T`` has type ``T`` and is valid iff ``decltype(e) castsTo T``

``if c then e1 else e2`` has type ``unifyFloat(e1,e2)`` and is valid iff ``c`` can be casted to ``() => Boolean`` and ``e1`` and ``e2`` have float-like types.

``e1 op e2`` where ``op`` is arithmetic operation symbol has type ``unifyFloat(e1,e2)`` and is valid iff ``e1`` and ``e2`` have float-like types.

``-e`` has the same type as ``e`` and valid iff ``e`` has a float-like type.

``e1 op e2`` where ``op`` is logic operation symbol has type ``() => Boolean`` and is valid iff ``e1`` and ``e2`` casts to ``() => Boolean``.

``not e`` has the type as ``() => Boolean`` and valid iff ``e`` has type ``() => Boolean``

``e1 op e2`` where ``op`` is comparison symbol has type ``() => Boolean`` and is valid iff ``e1`` and ``e2`` casts to ``() => Float``.

``f(e1,e2...en)`` has type ``ret_type(f)`` and valid if all passed arguments can be casted to corresponding parameter types and ``n`` is not less than obligatory argument count for ``f``. Function overloading is to be implemented.

