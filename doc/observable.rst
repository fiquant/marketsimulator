Functions and observables
=========================

Function 
	Object with overloaded ``__call__`` operator that accepts no arguments and returns a value of type ``T``.
	Further we will refer to the type of a function as ``() -> T`` or ``IFunction``.
	
Observable
	Function notifying listeners about its value changes. Only piecewise constant functions should be considered as observables. An arbitrary function can transformed into observable by means of ``observable.OnEveryDt(dt, func)``.

Conceptually observable might be defined as

.. code-block:: python 

	class IObservable[T] (IFunction[T], IEvent): ...
	
Basic observables
-----------------

- ``Constant[T]`` / ``None[T]`` represent typed constant value or ``None`` value

- ``Identity[T]`` function (note: its signature is ``T -> T`` and partial function application is to be explained)

- Arithmetic operations (``Sum``, ``Sub``, ``Product``, ``Div``, ``Mod``). If both arguments of the operation are observable the operation fires events about its value change and thus becomes an event itself. Functions overload operations ``+``, ``-``, ``*``, ``-``, ``%`` so they construct respective objects.  For example, 
  
  .. code-block :: python 
    
    (observable.AskPrice(orderbook) + observable.BidPrice()) / 2
    
  creates an observable that notifies about every change of the mid-price.

- Logic operations (``Equal[T]``, ``NotEqual[T]``, ``Less[T]``, ``Greater[T]``, ``GreaterEqual[T]``, ``LessEqual[T]``).  If both arguments of the operation are observable the operation fires events about its value change and thus becomes an event itself. Functions overload operations ``==``, ``!=``, ``>``, ``<``, ``<=`` so they construct respective objects. These operations inherit from ``IFunction[bool]``/``IObservable[bool]`` and have overloaded indexing operator that constructs ``Condition[T]`` object and it allows to write if-then-else expressions like:
  
  .. code-block:: python 
  
    # randomly chooses either Side.Buy or Side.Sell
    (mathutils.rnd.uniform(0.,1.) < 0.5)[ ops.constant(Side.Buy), ops.constant(Side.Sell) ]
  
- Functions from standard ``math`` module: ``Atan``, ``Pow`` etc

- Random distributions from ``random`` module: ``uniform``, ``lognormvariate``, ``expovariate`` etc.

- ``Derivative`` of a differentiable function
- ``Lagged``: returns function values with some lag

.. code-block:: haskell

	Max(x,y) ::= if x > y then x else y
	Min(x,y) ::= if x < y then x else y
	Sqr(x) ::= x*x

- ``Quotes``: downloads external historical data

There are also `statistics <statistics.rst>`_ related functions, functions of `orderbooks <orderbook.rst>`_ and of `traders <trader.rst>`_.

TODO: functions and observables with identical parameters should share their state
TODO: true topological sort should be done for event propagation in observables
