class BookBase(object):

    def __init__(self, bids, asks, tickSize=1, label=""):
        """ Initializes empty order book with given tick size
        """
        self._bids = bids
        self._asks = asks
        # queues indexed by their side
        self._queues = [0, 0]
        self._queues[self._bids.side.id] = self._bids
        self._queues[self._asks.side.id] = self._asks
        self._tickSize = tickSize
        self.label = label
        self._incomingOrders = None

    def queue(self, side):
        """ Returns queue of the given side
        """
        return self._queues[side.id]

    @property
    def tickSize(self):
        """ Returns the tick side
        """
        return self._tickSize

    def __str__(self):
        return type(self).__name__ + "(" + str(self._bids) + ", " + str(self._asks) + ")"

    def __repr__(self):
        return self.__str__()
    
    def cancelOrder(self, order):
        """ To be called when 'order' is cancelled
        """
        self.queue(order.side).cancelOrder(order)

    def process(self, order):
        """ Processes an order by calling its processIn method
        """
        if self._incomingOrders is None:
            self._incomingOrders = []
            order.processIn(self)
            idx = 0
            while idx < len(self._incomingOrders):
                self._incomingOrders[idx].processIn(self)
                idx += 1
            self._incomingOrders = None
        else:
            self._incomingOrders.append(order)
            
    def evaluateOrderPrice(self, side, volume):
        """ Evaluates price at which a market order of given 'side' 
            and having given 'volume' would be executed 
        """
        return self._queues[side.opposite.id].evaluateOrderPrice(volume)

    def evaluateOrderPriceAsync(self, side, volume, callback):
        callback(self.evaluateOrderPrice(side, volume))

    def processLimitOrder(self, order):
        """ Processes 'order' as limit order:
        If it is not matched completely, it stays at the order queue
        """
        if not self.processMarketOrder(order):
            self._queues[order.side.id].push(order)

    def processMarketOrder(self, order):
        """ Processes 'order' as market order:
        Iff it is not matched completely, returns False
        """
        return self._queues[order.side.opposite.id].matchWith(order)

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

    @property 
    def price(self):
        """ Returns middle arithmetic price if buy and sell sides are not empty,
        None otherwise 
        """
        return None if self.asks.empty or self.bids.empty \
                    else (self.asks.best.price + self.bids.best.price) / 2.0
                    
    @property
    def spread(self):
        """ Returns spread between sell and buy side if they are not empty,
        None otherwise
        """
        return None if self.asks.empty or self.bids.empty \
                    else self.asks.best.price - self.bids.best.price
