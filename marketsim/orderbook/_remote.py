from marketsim import Event
from _base import BookBase

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
    
class Remote(BookBase):
    
    def __init__(self, book, twowaylink):
        
        BookBase.__init__(self, 
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
        
    def evaluateOrderPriceAsync(self, side, volume, callback):
        self._upLink.send(
            lambda: self._book.evaluateOrderPriceAsync(side, volume, 
                lambda x: self._downLink.send(lambda: callback(x))))
