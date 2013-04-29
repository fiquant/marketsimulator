from marketsim import types, Event

class BookBase(types.IOrderBook):

    def __init__(self, bids, asks, label=""):
        """ Initializes empty order book with given tick size
        """
        self._bids = bids
        self._asks = asks
        # queues indexed by their side
        self._queues = [0, 0]
        self._queues[self._bids.side.id] = self._bids
        self._queues[self._asks.side.id] = self._asks
        self.label = label
        if label != "":
            self._alias = [label]
        self.on_price_changed = Event()
        self._bids.on_best_changed += self.on_price_changed
        self._asks.on_best_changed += self.on_price_changed
        self.reset()
        
    def reset(self):
        self._bids.reset()
        self._asks.reset()
        self._incomingOrders = None
        
    def queue(self, side):
        """ Returns queue of the given side
        """
        return self._queues[side.id]

    def __str__(self):
        return type(self).__name__ + "(" + str(self._bids) + ", " + str(self._asks) + ")"

    def __repr__(self):
        return self.__str__()
    
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
