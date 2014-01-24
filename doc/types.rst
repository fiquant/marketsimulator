Types
=====

.. contents::
    :local:
    :depth: 2
    :backlinks: none

The strategy definition language aimes to introduce a strict static type system in order to prevent errors as soon as possible. Though this task isn't completely accomplished yet and sometimes the user has to do explicit downcasts,
the type system is evolutioning in order to avoid them.

Syntax
------

.. code-block :: scala

    Type ::= UnitType | SimpleType | TupleType | FunctionType

    UnitType ::= "()"

    SimpleType ::= QualifiedName

    TupleType ::= "(" Type ("," Type)+ ")"

    FunctionType ::= Type "=>" Type

    TypeDef ::= TypeAliasDef | InterfaceDef

    GenericArgs ::= "[" Ident ("," Ident)* "]"

    TypeAliasDef ::= "type" Ident GenericArgs? "=" Type

    InterfaceDef ::= "type" Ident GenericArgs? (":" Type ("," Type)*)?

Predefined types
----------------

* **Unit type**: ``()``

* **Simple type**: ``Float``, ``Int`` etc.

* **Tuple types**: ``(t1, t2, ... tn)`` where ``ti`` are other types (n >= 2 is implied, for n = 0 a unit type should be used, and for n = 1 a simple type should be used). In future it might be useful to consider unit type as a particular case of a tuple type.

* **Function types**: ``args_type => ret_type`` where ``arg_type`` may be a unit type, simple type, tuple type or another function type

Some simple types must be declared by the user and the following code must appear in a model description
(it is done for readability reasons in order to show what types are defined):

.. code-block :: scala

    type Any

    type Float
    type Int : Float
    type Boolean
    type String

    type Optional[T]
    type List[T]

Generic types
-------------

User defined types may have generic parameters that are used in their definition.
Contravariance rules are applied for function type arguments: ``T <: U`` implies ``U => X <: T => X``. For all other cases covariance is used: ``T <: U`` implies ``List[T] <: List[U]`` and ``T <: U`` implies ``() => T <: () => U``. (We use notation ``T <: U`` to show that type ``T`` can be casted to type ``U``)

Type aliases
------------

Type aliases behave like ``typedef`` in C++ and introduce a handy shortcut for another type. For example,

.. code-block :: scala

    type IFunction[T] = () => T

Alias for a type equals to it. It implies that in the following code

.. code-block :: scala

    def f() : () => Float
    def g() : IFunction[Float]

functions ``f`` and ``g`` have the same type.

User-defined types
------------------

A user may define own types. These types may inherit from other types:

.. code-block :: scala

    type IObservable[T] : IFunction[T], IEvent

In this sample type ``IObservable[Float]`` may be used in any place where ``IFunction[Float]`` or ``IEvent`` is expected (but not vice versa).

Special types
-------------

Type ``Any`` is an implicit super type for any type, i.e. any type casts to ``Any``. For example, ``IObservable[Float]`` casts to ``IObservable[Any]``.

Type ``Optional[T]`` appears at function declarations having default arguments. Any type ``T`` casts to ``Optional[T]``.

Lists can be constructed using following syntax: ``[e1,e2,...,en]`` where ``ei`` are some expressions and they have type ``List[T]`` where ``T`` is the bottommost type all ``ei`` can be casted to.

Type ``Nothing`` is the bottommost type so it can be casted to any type. For the moment it appears only when an empty list is declared so literal ``[]`` has type ``List[Nothing]`` and can be casted to ``List[T]`` for any ``T``.

