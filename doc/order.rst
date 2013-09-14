Elementary orders, their factories and requests
===============================================

.. contents::
    :local:
    :depth: 2
    :backlinks: none
    
Traders send orders to a market. There are two basic kinds of orders:

- **Market orders**	ask to buy or sell some asset at any price.

- **Limit orders** ask to buy or sell some asset at price better than some limit price. If a limit order is not competely fulfilled it remains in an order book waiting to be matched with another order.

An order book processes market and limit orders but keeps persistently only limit ones. Limit orders can be cancelled by sending cancel request. 

From trader point of view there can be other order types like `Iceberg <metaorder.rst#iceberg-order>`_ order but from order book perspective it is just a sequence of basic orders and requests. They will be considered at `meta orders <metaorder.rst>`_ section.

Besides basic orders there are also requests: order cancellation request, request to estimate market impact of a trade etc. Their interface differs a lot from orders' interface that's why they are put into a separate group.

Market and limit orders
-------------------------

Market and limit orders (and some meta orders) derive from a common base class that provides some basic functionality: 
- matched/unmatched volume management
- storing cancellation flag
- keeping a reference to the order's owner  

It has following interface:

.. code-block:: python 

    class order.Base(object):

        @property
        def volumeFilled(self)
        
        @property
        def volumeUnmatched(self)	
        
        @property
        def volumeTotal(self):
            return self.volumeFilled + self.volumeUnmatched
        	
        @property
        def empty(self):
            return self.volumeUnmatched == 0
        
        @property
        def side(self)
        
        @property
        def cancelled(self)
        
        def cancel(self)
        
        # owner who issued the order (trader, metaorder or proxy orderbook)
        # it will be notified about order's events	    
        @property
        def owner(self)
		
Classes ``order.Market`` and ``order.Limit`` derive from this class and define method ``processIn(orderbook)`` which defines how the order should be processed in an orderbook. 

When the order is matched against another order it calls ``onMatchedWith`` method of ``owner`` passing volume and price at which the trade was done.

If an order is cancelled or gets completely matched ``onOrderDisposed`` method of the ``owner`` is called. 

Limit order defines also accessors to its price:

.. code-block:: python 

    class order.Limit(order.Base):
    
    	@property
    	def price(self)
    
    	# Returns "signed" price of the order:
    	#	positive if the order is on sell side
    	#	negative if the order is on buy side
    	@property
    	def signedPrice(self)

Order factories
---------------

Usually a user in the simulator specify a kind of orders to create by choosing appropriate *order factory*.

Order factories are initialized by functions calculating parameters of order to create. For example,

.. code-block:: python 

    class order.factory.Market(types.IOrderFactory):
	
        def __init__(self, side, volume):
            self.side = side
            self.volume = volume
        	
        _properties = {
            'side'   : IFunction[Side],
            'volume' : IFunction[Volume]
        }
        	
        def __call__(self):
            side = self.side()
            if side is None: return None
            
            volume = self.volume()
            if volume is None: return None
            
            return order.Market(side, volume)
		
If some parameters of an order to create depend on other parameters, a special factory is provided. For example, 

.. code-block:: python 

    class order.factory.SignedMarket(types.IOrderFactory):
    
    	def __init__(self, signedvolume):
            self.signedvolume = signedvolume
    	
    	_properties = {
            'signedvolume' : IFunction[int]
    	}
    		
    	def __call__(self):
            signedvolume = self.signedvolume()
            if signedvolume in [None, 0]: return None
            
            return order.Market(signedvolume > 0 ? Side.Buy : Side.Sell, 
                                abs(signedvolume))

Sometimes order factories are constructed in several stages: for example, some parameters of the factory are defined by a trading strategy and the rest is defined by user.

In order to support these use cases order factories have also a curried form. For example, ``order.factory.volume.Market`` has type ``(() -> Volume) -> IOrderGenerator`` and ``order.factory.side_price.Limit`` has type ``(() -> Side) -> (() -> Price) -> IOrderGenerator``.

Requests
--------

Requests query some information about an order book or instructs to do something.

- ``request.Cancel(order)`` instructs an order book to cancel the ``order``

- ``request.EvalMarketOrder(side, volume)`` calculates cumulative price and volume of trades induced by a market order with given ``side`` and ``volume``.

- ``request.EvalVolumesForBudget(side, budget)`` calculates a sequence of prices and volumes of best orders in the order book with total price less or equal to ``budget``.

These requests also have ``callback`` parameter used to pass results of the request (so it is a continuation passing style, CPS).

