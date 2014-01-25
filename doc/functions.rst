Functions
=========

.. contents::
    :local:
    :depth: 2
    :backlinks: none

Syntax
------

.. code-block:: scala

    QualifiedName ::= Ident("." Ident)*

    Decorator ::= "@" (Annotation | Attribute)

    Annotation ::= QualifiedName "(" Expr ("," Expr)* ")"

    Attribute ::= Ident "=" Expr

    Parameter ::= Ident (":" Type)? ("=" Expr)?

    FunctionDef ::= Decorator* "def" Ident "(" Parameter? ("," Parameter)* ")" (":" Type)? ("=" Expr)?

Functions as simulation modules
-------------------------------

Functions in Strategy Definition Language correspond to simple and compound modules in a simulation model. Functions have parameters which are used to generate module fields. Every parameter has an unique name, type and an optional default value. Parameter type tells what kind of values may be assigned to this field. 

Simple modules represent some functionality which is considered as elemental and they are implemented in target language (like Python). Functions for simple modules (intrinsic functions) don't have body but they must be decorated by an annotation (e.g. ``@python.intrinsic("_Class_Impl")``) telling where Python implementation should be taken from.  

Compound modules are compositions of other modules and can be completely generated from a high level description at Strategy Definition Language. Functions that describe them must have a body defining how they are composed.

Functions are assigned types and these types allows modules to be used as parameters for other modules.

Type inference
--------------

Function parameter types usually are infered from type of their initializer and thus may be omitted. If a parameter doesn't have a default value, its type should be specified explicitely.

Return type of function can be inferred automatically if function has body and thus omitted but must be specified explicitely otherwise.

There are two ways to specify return type of a function: after a colon (":") a full return type is specified and
after an arrow ("=>") a return type of a function to be returned is given (this syntax is introduced for brevity). For example,

.. code-block :: scala

    def f() => Float

is equivalent to

.. code-block :: scala

    def f() : () => Float

Note that in some rare cases (generating curried versions of functions) the current compiler implementation imposes restriction that parameter type must be specified explicitly even if there is a default parameter (curried functions are injected into code at before typing stage where type information is not disponible).

