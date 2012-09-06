import random 
from marketsim import Event
from marketsim.order_queue import OrderBookBase
from marketsim.scheduler import world

class Link(object):
    """ Ensures that sending packets via a link preserves their order
    """
    
    def __init__(self, latency):
        """ Initializes the link with a latency function
        """
        self._latency = latency
        self._lastT = 0
        
    def send(self, func):
        """ "Sends" data via link.
        After latency() moments of time 'func' will be called
        If there is another function that is scheduled for later time 
        we adjust action time of 'func' in order to preserve their order 
        """
        t = world.currentTime + self._latency()
        if t < self._lastT:
            t = self._lastT
        self._lastT = t 
        world.schedule(t, func)

class TwoWayLink(object):
    
    def __init__(self, 
                 latencyUp = lambda: 0.001 * random.lognormvariate(0.,1.), 
                 latencyDown = lambda: 0.001 * random.lognormvariate(0.,1.)):
        
        self.up = Link(latencyUp)
        self.down = Link(latencyDown)

class RemoteQueue(object):
    
    def __init__(self, queue, book, link):
        self._queue = queue
        self.book = book
        self._link = link
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
        self._link.send(update)
        
    @property 
    def best(self):
        return self._best
    
    @property
    def empty(self):
        return self._best is None
    
class RemoteBook(OrderBookBase):
    
    def __init__(self, book, twowaylink):
        
        OrderBookBase.__init__(self, 
                               RemoteQueue(book.bids, self, twowaylink.down), 
                               RemoteQueue(book.asks, self, twowaylink.down), 
                               book.tickSize, 
                               book.label)
        
        self._upLink = twowaylink.up
        self._downLink = twowaylink.down
        self._book = book
        
    def _remote(self, order):
        remote = order.clone()
        assert 'remote' not in dir(order)
        order.remote = remote
        def on_matched(*args):
            remote.copyTo(order)
            order.on_matched.fire(*args)
        remote.on_matched += lambda *args: self._downLink.send(lambda: on_matched(*args))
        return remote
        
        
        
    def processMarketOrder(self, order):
        self._upLink.send(lambda: self._book.processMarketOrder(self._remote(order)))
        
    def processLimitOrder(self, order):
        self._upLink.send(lambda: self._book.processLimitOrder(self._remote(order)))

    def cancelOrder(self, order):
        self._upLink.send(lambda: self._book.cancelOrder(order.remote))
