Order book
----------

For the moment, there are two kinds of order books: local and remote
ones. Local order books execute methods immediately but remote onces try
to simulate some delay between a trader and a market by means of message
passing (so they are asynchronous by their nature). These books try to
have the same interface in order that traders cannot tell the difference
between them.

The base class for the order books is:

::

    class orderbook._base.BookBase(object):
        def __init__(self, tickSize=1, label="")
        def queue(self, side)
        def tickSize(self)
        def process(self, order)
        def bids(self)
        def asks(self)
        def price(self)
        def spread(self)
        def evaluateOrderPriceAsync(self, side, volume, callback)

Methods , and give access to queues composing the order book. Methods
and return middle arithmetic price and spread if they are defined (i.e.
bids and asks are not empty). Orders are handled by an order book by
method. If method is called recursively (e.g. from a listener of event)
its order is put into an internal queue which is to be processed when
the current order processing is finished. This ensures that at every
moment of time only one order is processed. Method is used to compute
P&L of a market order of given side and volume without executing it.
Since this operation might be expensive to be computed locally in case
of a remote order book we return the result price asynchronously by
calling function given by parameter.

Local order book
----------------

Local order books extend the base order book by concrete order
processing implementation (methods , etc.) and allow user to define
functions computing transaction fees:

::

    class orderbook.Local(BookBase):
        """ Order book for a single asset in a market
        Maintains two order queues for orders of different sides
        """
        def __init__(self, tickSize=1, label="",
                     marketOrderFee = None,
                     limitOrderFee = None,
                     cancelOrderFee = None)

Order queue
-----------

Order queues can be accessed via , and methods of an order book and
provide following user interface:

::

    class orderbook._queue.Queue(object):
        def __init__(self, ...):
            # event to be called when the best order changes
            self.on_best_changed = Event()  
            # event (orderQueue, cancelledOrder) to be called when an order is cancelled
            self.on_order_cancelled = Event() 

        def book(self)
        def empty(self)
        def best(self)
        def withPricesBetterThan(self, limit)
        def volumeWithPriceBetterThan(self, limit)
        def sorted(self)
        def sortedPVs(self) 

The best order in a queue can be obtained by calling method provided
that the queue is not . Method enumerates orders having limit price
better or equal to . This function is used to obtain total volume of
orders that can be traded on price better or equal to the given one: .
Property enumerates orders in their limit price order. Property
enumerates aggregate volumes for each price in the queue in their order.

When the best order changes in a queue (a new order arrival or the best
order has matched), event listeners get notified.

Remote order book
-----------------

Remote order book ( class) represents an order book for a remote trader.
Remoteness means that there is some delay between moment when an order
is sent to a market and the moment when the order is received by the
market so it models latency in telecommunication networks. A remote book
constructor accepts a reference to an actual order book (or to another
remote order book) and a reference to a two-way communication channel.
Class implements a two-way telecommunication channel having different
latency functions in each direction (to market and from market). It also
ensures that messages are delivired to the recipient in the order they
were sent. Queues in a remote book are instances of class. This class is
connected to the real order queue and listens events thus keeping
information about the best order in the queue up-to-date. When a remote
order book receives an order, it is cloned and sent to the actual order
book via communication link. The remote order book gets subscribed to
the clone order’s events via downside link. It leads to that in some
moments of time the state of the original order and its clone are not
synchronised (and this is normal).
