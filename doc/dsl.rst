Comments:

.. code-block:: fsharp

	// Comments are given either in C style or in 
	(* OCaml style *)

Types
=====

Primitive
---------

.. code-block:: fsharp

	type float;
	type int;
	type string; 
	type bool;

Pre-defined
-----------

.. code-block:: fsharp

    // strong typedefs 
    type Ticks = int in [0,+inf); 
    type Price = float in [0,+inf);
    type Volume = int in [0,+inf);
    type Time = float in [0,+inf);
    type TimeInterval = float in [0,+inf);

    // variant type
    type Side = Buy | Sell; 
    // later we may refer to these options as Side.Buy or Side.Sell

    // 
    type IFunction['a] = () -> 'a;
    // function returning values of type 'a
    
    // some functions may provide a way to calculate its derivative
    type IDifferentiable inherit IFunction[float]
    
    type IEvent; 
    // in Python it has methods +=, -= to subscribe/unsubcsribe listeners
    // listeners are callable objects with single parameter - source of the event
    
    type IObservable['a] inherit IFunction['a] inherit IEvent
    // observable is a function notifying about changes of its value 
    // (so every observable is a piecewise constant function)
    
    type IOrderQueue;
    type IOrderBook;
    
    type IOrder;
    type IRequest;
    
    type IOrderGenerator = () -> IOrder;
    
    type IStrategy;
    type ISingleAssetStrategy inherit IStrategy;
    
    type IAccount;
    type ITrader;
    
    type ISingleAssetTrader inherit ITrader inherit IAccount;
    
    type ICandleStick;
    type IVolumeLevels;
    
    type ITimeSerie['a];
    type IGraph;
    
    
    
    
    
