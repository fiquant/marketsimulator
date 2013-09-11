
Market representation
==========================

.. contents::
    :local:
    :depth: 2
    :backlinks: none

Order book
    Order book represents a single asset traded in some market. Same asset traded in different markets would have been represented by different order books. An order book stores unfulfilled limit orders sent for this asset in two order queues, one for each trade sides (Asks for sell orders and Bids for buy orders).

Order queue
    Order queues are organized in a way to extract quickly the best order and to place a new order inside. In order to achieve this a heap based implementation is used. (A bucket based implementation might be also used).

Ticks
    Order books support a notion of a tick size: all limit orders stored in the book should have prices that are multipliers of the chosen tick size. If an order has a limit price not divisible by the tick size it is rounded to the closest 'weaker' tick ('floored' for buy orders and 'ceiled' for sell orders). In future all prices will be stored as integers in ticks.

Market order
    Market orders are processed by an order book in the following way: if there are unfulfilled limit orders at the opposite trade side, the market order is matched against them till either it is fulfilled or there are no more unfilled limit orders. Price for the trade is taken as the limit order limit price. Limit orders are matched in order of their price (ascending for sell orders and descending for buy orders). If two orders have the same price, it is garanteed that the elder order will be matched first.

Limit order
    Limit orders firstly processed exactly as market orders. If a limit order is not filled completely it is stored in a corresponding order queue.

Order processing time
    Orders and requests are processed by an order book in serialized way. It implies that, for example, if a meta order sends another order it is garanteed that the latter will be processed only after the meta order is completely processed. ``ORDER_PROCESSING_TIME`` defines how much time every order or request should be processed (in future, it might be replaced by a function)

Transaction costs
    There is a notion of transaction costs: if a user wants to define functions computing transaction fees for market, limit and cancel orders she should pass functions of form ``(anOrder, orderBook) --> Price`` to the order book constructor.  If ``Price`` is negative, the trader gains some money on this transaction. If the functions are given,  once an order is processed by an order book, method ``order.charge(price)`` is called. The default implementation for the method delegates it to ``trader.charge(price)`` where ``trader`` is a trader associated with the ``order``. 


Order book
----------

For the moment, there are two kinds of order books: local and remote ones. Local order books execute their methods immediately but remote onces try to simulate some delay between a trader and a market by means of message passing (so they are asynchronous by their nature). These books try to have the same interface in order that traders couldn't tell the difference between them.

The base class for the order books is:

.. code-block:: python

    class orderbook.BookBase(object):
        def __init__(self, tickSize=1, label="")
        def tickSize(self)
        def process(self, orderOrRequest)
        def bids(self)
        def asks(self)

Local order book
----------------

Local order books extend the base order book by concrete order processing implementation (methods ``processLimitOrder``, ``cancelOrder``, etc.) and allow user to define functions computing transaction fees:

.. code-block :: python 

    class orderbook.Local(BookBase):
        """ Order book for a single asset in a market
        Maintains two order queues for orders of different sides
        """
        def __init__(self, tickSize=1, label="",
                     marketOrderFee = None,
                     limitOrderFee = None,
                     cancelOrderFee = None)

    def cancelOrder(self, order)
    
    # Evaluates price at which a market order of given 'side' and having given 'volume' would be executed
    def evaluateOrderPrice(self, side, volume)

    def evaluateOrderPriceAsync(self, side, volume, callback):
        callback(self.evaluateOrderPrice(side, volume))

    # returns list of (price, volume) of trades that might be done for given 'budget'
    def evaluateVolumesForBudget(self, side, budget, callback)
        
    def processLimitOrder(self, order)
    def processMarketOrder(self, order)

Order queue
-----------

Order queues can be accessed via ``queue``, ``asks`` and ``bids`` methods of an order book and
provide following user interface:

.. code-block :: python

    class orderbook.Queue(object):
        def __init__(self, ...):
            self.lastTrade = LastTrade() # observable updating after each trade
            self.bestPrice = BestPrice(self) # observable with price of the best order

        # Enumerates orders in order of their price 
        # Enumeration best M orders requires O(MlogM) operations
        @property
        def sorted(self)

        # Enumerates (price, volume) cumulative volumes for every price in the queue        
        @property             
        def sortedPVs(self)

        # Evaluates price for a potential market order with given 'volume'
        # Returns pair (price, volume_unmatched) where 'volume_unmatched' may be positive
        # if there is not enough volume in the order queue  
        # Complexity of the operation: O(MlogM) where M - number of orders involved       
        def evaluateOrderPrice(self, volume)

        # Returns prices of the order at depths given by 'volumes'
        def getVolumePrices(self, volumes)

        # Enumerates orders with price better than or equal to 'limit'
        def withPricesBetterThan(self, limit, idx=0)
    
        # Returns total volume of orders having price better than or equal to 'limit'        
        def volumeWithPriceBetterThan(self, limit)

        # Returns (price, volume) for limit orders to be placed 
        # in order to buy or sell assets on total *budget*
        def pvsForFixedBudget(self, budget)

Remote order book
-----------------

Remote order book (``orderbook.Remote`` class) represents an order book for a remote trader. Remoteness means that there is some delay between moment when an order is sent to a market and the moment when the order is received by the market so it models latency in telecommunication networks. A remote book constructor accepts a reference to an actual order book (or to another remote order book) and a reference to a two-way communication channel. 

Class ``remote.TwoWayLink`` implements a two-way telecommunication channel having different latency functions in each direction (to market and from market). It also ensures that messages are delivired to the recipient in the order they were sent. 

Queues in a remote book are instances of ``orderbook._remote.Queue`` class. This class is connected to the real order queue and listens ``bestPrice`` events thus keeping information about the best order in the queue up-to-date. 
When a remote order book receives an order, it is cloned and sent to the actual order book via a communication link. The remote order book gets subscribed to the clone order's events via downside link. It leads to that in some moments of time the state of the original order and its clone are not synchronised (and this is normal).

In future a mechanism to query underlying order book capabilities (for example, can it process meta orders by himself) will be introduced thus allowing to model meta order processing at client/broker/market side.
