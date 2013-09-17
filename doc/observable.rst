Events, functions and observables
==================================

.. contents::
    :local:
    :depth: 2
    :backlinks: none

Events
------

**Events** in the simultator are conceptually close to events in C# or ``boost::signal`` in C++. Number of listeners can be subscribed for event notification using += operator and unsubscribed with -= operator. A listener should be a callable object that accepts a single argument - the source of the event (it allows not to store an event source in the listener and also use a single listener for several event sources at the same time). 

Event subscription
------------------

Since event subscription is often done at binding time and unadvising should be done at dispose time ``event.subscribe`` helper function was introduced to manage event subscription declaratively:  

.. code-block:: python

  class ProgressPrinter(object):
  
    def __init__(self):
      event.subscribe(event.Every(ops.constant(10)), # event source to subscribe to
                      _(self)._wakeUp,               # event listener
                      self)                          
      
    def _wakeUp(self, _):
      print '.'   # prints . every 10 units of time
      
Event helpers
-------------
      
``event.After`` and ``event.Every`` are used to represent a `single <scheduler.rst#generating-a-single-event>`_ and a `repeating  <scheduler.rst#generating-events-on-regular-basis>`_ action

``event.Array`` is used when several event sources are to be represented as a single event. For example,

.. code-block:: python

  event.Array([BestPrice(Asks(orderbook)), BestPrice(Bids(orderbook))])
  
fires an event once bid or ask of ``orderbook`` has changed.

Filtered events
---------------

Sometimes an event source (for example, price of an asset) has hundreds subscribers who check is the event source is less or greater than some value. In order to avoid excessive calls ``event.LessThan`` and ``event.GreaterThan`` classes are introduced. Event sources detect objects of these types and store them sorted in order to lookup relevant listeners very quickly. For example, 

.. code-block:: python 

  observable.MidPrice(orderbook) += event.LessThan(100, listener)
  
will call ``listener`` only if mid-price of the asset is less than 100.

Functions and observables
-------------------------

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

*TODO: functions and observables with identical parameters should share their state.*

*TODO: true topological sort should be done for event propagation in observables.*
