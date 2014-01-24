Types
=====

.. contents::
    :local:
    :depth: 2
    :backlinks: none

The strategy definition language aimes to introduce a strict static type system in order to prevent errors as soon as possible.
Though this task isn't completely accomplished and sometimes the user has to do explicit downcasts,
the type system is evolutioning in order to avoid them.

Predefined types
----------------

* **Unit type**: ``()``

* **Simple type**: ``Float``, ``Int`` etc.

* **Tuple types**: ``(t1, t2, ... tn)`` where ``ti`` are other types
(n >= 2 is implied, for n = 0 a unit type should be used, and for n = 1 a simple type should be used)

* **Function types**: ``args_type => ret_type`` where ``arg_type`` usually a unit type, simple type, tuple type or another function type

