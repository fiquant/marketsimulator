import random 
from marketsim import Event
from marketsim.scheduler import world

class RemoteQueue(object):
    
    def __init__(self, queue, book,
                 latency=lambda: 0.001*random.lognormvariate(0., 1.)):
        self._queue = queue
        self.book = book
        self._latency = latency
        self._best = queue.best
        queue.on_best_changed += self._onBestChanged
        self.on_best_changed = Event()
        self._lastT = 0
        
    @property
    def side(self):
        return self._queue.side
    
    @property
    def lastPrice(self):
        return self._best.price if self._best is not None else None
        
    def _onBestChanged(self, queue):
        best = queue.best
        def update():
            self._best = best
            self.on_best_changed.fire(self)
        # we ensure the right order of events
        t = world.currentTime + self._latency()
        if t < self._lastT:
            t = self._lastT
        self._lastT = t 
        world.schedule(t, update)
        
    @property 
    def best(self):
        return self._best
    
    @property
    def empty(self):
        return self._best is None
    
class RemoteBook(object):
    
    def __init__(self, book, 
                 latencyUp = lambda: 0.001 * random.lognormvariate(0.,1.), 
                 latencyDown = lambda: 0.001 * random.lognormvariate(0.,1.)):
        
        self._asks = RemoteQueue(book.asks, self, latencyDown)
        self._bids = RemoteQueue(book.bids, self, latencyDown)
        self._latencyUp = latencyUp
        self._latencyDown = latencyDown
        self._book = book
        
        self._queues = [0, 0]
        self._queues[self._bids.side] = self._bids
        self._queues[self._asks.side] = self._asks
        self._tickSize = book.tickSize
        self.label = book.label
        self._lastT = world.currentTime
        
        
    def queue(self, side):
        """ Returns queue of the given side
        """
        return self._queues[side]
    
    def process(self, order):
        t = world.currentTime + self._latencyUp()
        # we ensure that the orders will be processed in right order 
        if t < self._lastT:
            t = self._lastT
        self._lastT = t
        world.schedule(t, lambda: self._book.process(order))
        

    @property
    def tickSize(self):
        """ Returns the tick side
        """
        return self._tickSize
        
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
                    
        