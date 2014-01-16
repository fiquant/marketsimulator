from marketsim import types, event, timeserie, event, _

ORDER_PROCESSING_TIME = 1e-8

from queue import LastTrade

from ..trader.classes import _Holder_Impl

class BookBase(types.IOrderBook, _Holder_Impl):

    def __init__(self, bids, asks):
        """ Initializes empty order book with given tick size
        """
        _Holder_Impl.__init__(self)
        self._bids = bids
        self._asks = asks
        # queues indexed by their side
        self._queues = [0, 0]
        self._queues[self._bids.side.id] = self._bids
        self._queues[self._asks.side.id] = self._asks
        if self.name != "":
            self._alias = [self.name]

        self.lastTrade = LastTrade()
        event.subscribe(self._asks.lastTrade, _(self.lastTrade)._retranslate, self)
        event.subscribe(self._bids.lastTrade, _(self.lastTrade)._retranslate, self)
        
        self.reset()
        
    def bind(self, ctx):
        self._scheduler = ctx.world
        
    _internals = ['_asks', '_bids']
        
    def updateContext(self, context):
        context.orderbook = self
        
    def reset(self):
        self._bids.reset()
        self._asks.reset()
        self._incomingOrders = []
        self._orderBeingProcessed = None
        
    def queue(self, side):
        """ Returns queue of the given side
        """
        return self._queues[side.id]

    def __str__(self):
        return type(self).__name__ + "(" + str(self._bids) + ", " + str(self._asks) + ")"

    def __repr__(self):
        return self.__str__()
    
    def _step(self):
        self._orderBeingProcessed.processIn(self)
        self._orderBeingProcessed = None
        if len(self._incomingOrders):
            self._orderBeingProcessed = self._incomingOrders.pop(0) 
            self._scheduler.scheduleAfter(ORDER_PROCESSING_TIME, _(self)._step)
    
    def process(self, order):
        """ Processes an order by calling its processIn method
        """
        if isinstance(order, types.IOrder):
            assert order.owner is not None
        if self._orderBeingProcessed is None:
            self._orderBeingProcessed = order
            self._scheduler.scheduleAfter(ORDER_PROCESSING_TIME, _(self)._step)            
        else:
            self._incomingOrders.append(order)

            
    @property
    def bids(self):
        """ Returns buy side order queue
        """
        return self._bids

    @property
    def asks(self):
        """ Returns sell side order queue
        """
        return self._asks
