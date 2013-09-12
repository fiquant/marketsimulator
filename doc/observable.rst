Functions and observables
=========================

Function 
	Object with overloaded ``__call__`` operator that accepts no arguments and returns a value of type ``T``.
	Further we will refer to the type of a function as ``() -> T`` or ``IFunction``.
	
Observable
	Function notifying listeners about its value changes. 
	Only piecewise constant functions should be considered as observables. 
	An arbitrary function can transformed into observable by means of ``observable.OnEveryDt``.

.. code-block:: python 

	class IObservable[T] (IFunction[T], IEvent): ...
	
Basic observables
-----------------

- ``Constant[T]`` / ``None[T]`` represent typed constant value or ``None`` value

- ``Identity[T]`` function (note: its signature is ``T -> T``)

- Arithmetic operations (``Sum``, ``Sub``, ``Product``, ``Div``, ``Mod``).
  If both arguments of the operation are observable the operation fires events about its value change and thus becomes an event itself.
  Functions have operations ``+``, ``-``, ``*``, ``-``, ``%`` returning respective objects
  For example, 
  
  .. code-block :: python 
    
    (observable.AskPrice(orderbook) + observable.BidPrice()) / 2
    
  creates an observable that notifies about every mid-price change

- Logic operations (``Equal[T]``, ``NotEqual[T]``, ``Less[T]``, ``Greater[T]`` etc)
  If both arguments of the operation are observable the operation fires events about its value change and thus becomes an event itself.
  Functions have operations ``==``, ``!=``, ``>``, ``<``, ``<=`` returning functions/observables with value type ``bool``. 
  The latter has an indexing operator overloaded which creates ``Condition[T]`` object and it allows to write expressions like:
  
  .. code-block:: python 
  
    (mathutils.rnd.uniform(0.,1.) < 0.5)[   ops.constant(Side.Buy), 
						                    ops.constant(Side.Sell)  ]
  

