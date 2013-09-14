Meta orders 
===========

Meta orders look like normal orders from trader's point of view (so they can be easily interchanged with limit and market orders) but from order book's point of view it is a sequence of elementary orders and requests. This behaviour is achieved by overriding ``processIn`` method.

It should be noted that border between a strategy and a meta order is quite blur: some strategies can be implemented as meta orders and vice versa.

Meta orders can be combined in quite wide range. For example, 

.. code-block:: python

    order.factory.side.WithExpiry(ops.constant(10.),
        order.factory.side.Iceberg(ops.constant(1),
            order.factory.side.Peg(
                order.factory.side_price.Limit(ops.constant(10)))
                
creates limit orders of volume 10 split into lots of size 1 with price set to the best price of the order queue. These orders are cancelled after 10 units of time.


creates limit orders with volume 10, price is taken as the best price (Peg order), sends them in portions of ``lotSize = 1`` and cancels them after ``expiry = 10`` units of time.


Iceberg order
-------------

Iceberg order is initialized by an underlying order and a lot size. It sends consequently pieces of the underlying order of size equal or less to the lot size thus maximum lot size volume is visible at the market at any moment.


Immediate-or-Cancel (IoC) order 
-------------------------------

This order sends the underlying order to the market and immediately sends a cancel request for it. It allows to combine market and limit order behaviour: the order is either executed immediately at price equal or better than given one either it is cancelled (and consequently never stored in the order queue).

.. code-block :: python 

	class ImmediateOrCancel(_meta.OwnsSingleOrder):
	    
	    def processIn(self, orderBook):
	        self.send(self.proto)
	        self.orderBook.process(request.Cancel(self.proto))


With expiry order
-----------------

It can viewed as a version of Immediate-or-Cancel order where the cancel request is sent after some time interval.

.. code-block :: python 

	class WithExpiry(_meta.OwnsSingleOrder):

	    def processIn(self, orderBook):
	        self.send(self.proto)
	        self.world.scheduleAfter(
	        	self._delay, _(self.orderBook, 
	                           request.Cancel(self.proto)).process)


Stoploss order 
--------------

This order is initialised by an underlying order and a maximal acceptable loss factor.
It keeps track of position and balance change induced by trades of the underlying order and if losses from keeping the position goes above certain limit (given by maximum loss factor), the meta order clears its position.

Fixed budget order
------------------

It acts like a market order but the volume is implicitly given by a budget available for trades. Internally first it sends ``request.EvalVolumesForBudget`` in order to estimate volumes and prices of orders to sent and then sends a sequence of ``order.ImmediateOrCancel`` to be sure that budget not greater than given is used.

.. code-block:: python

	class FixedBudget(_meta.Base):

	    def processIn(self, orderBook):
	        self.orderBook.process(
	                   request.EvalVolumesForBudget(
	                                self.side, self.budget, 
	                                _(self)._onEvaluated))
	        
	    def _onEvaluated(self, pvs):
	        self._volumeUnmatched = sum([v for p,v in pvs])
	        for p,v in pvs:
	            self.send(_ioc.Order(_limit.Order(self.side, p, v)))


Floating price order
--------------------

.. code-block:: python 

	class FloatingPrice(_meta.OwnSingleOrder):
	
	    def _update(self, _):	# called when price needs to be changed
	        if self.active:		# if order is not cancelled
	            self._dispose() # cancel previous order
	            price = self._priceFunc()	# calculate new price
	            if price is not None:		# if defined 
	            	# send a new order with given price and unmatched volume
	                self.send(self.proto.With(price = price,  
	                                          volume = self.volumeUnmatched))
	            else:
	                self.send(None)


This order is initialized by an order having a price and an observable that generate new prices. When the observable value changes the order is cancelled and a new order with new price is created and sent to the order book.

Peg order
---------

A peg order is a case of the floating price order with price better at one tick than the best price of the order queue. It implies that if several peg orders are sent to the same order queue they start to race until being matched against the counterparty orders.

.. code-block:: python 
	
	def Peg(order):
	    """ Peg is a virtual order that ensures that it has the best price in the order book. 
	    It is implemented as a limit order which is cancelled 
	    once the best price in the order queue has changed 
	    and is sent again to the order book 
	    with a price one tick better than the best price in the book.
	    """
	
	    side = order.side
	    book = orderbook.OfTrader()
	    tickSize = observable.TickSize(book)
	    askPrice = observable.AskPrice(book)
	    bidPrice = observable.BidPrice(book)
	    
	    price = observable.MinEpsilon(askPrice, tickSize)\
	                if side == Side.Sell else\
	            observable.MaxEpsilon(bidPrice, tickSize)
	
	    return FloatingPrice(order, price)
