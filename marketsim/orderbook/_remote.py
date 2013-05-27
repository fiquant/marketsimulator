from marketsim import Event, registry, remote, types, bind
from _base import BookBase

class Queue(object):
    
    def __init__(self, queue, book, link):
        self._queue = queue
        self.book = book
        self._link = link
        self._onBestChanged = bind.Method(self, '_onBestChanged_impl')
        queue.on_best_changed += self._onBestChanged
        self.on_best_changed = Event()
        self.reset()
        
    def reset(self):
        self._best = self._queue.best
        self._lastT = 0
        
    @property
    def side(self):
        return self._queue.side
    
    @property
    def lastPrice(self):
        return self._best.price if self._best is not None else None
        
    def _update_impl(self, best):
        self._best = best
        self.on_best_changed.fire(self)

    def _onBestChanged_impl(self, queue):
        best = queue.best
        self._link.send(bind.Method(self, '_update_impl', best))
        
    @property 
    def best(self):
        return self._best
    
    @property
    def empty(self):
        return self._best is None
    
class Remote(BookBase):
    """ Represent an *orderbook* from point of view of a remote trader connected
    to the market by means of a *link* that introduces some latency in information propagation
    """
    
    def __init__(self, orderbook, link):
        
        BookBase.__init__(self, # TODO: dependency tracking
                          Queue(orderbook.bids, self, link.down), 
                          Queue(orderbook.asks, self, link.down), 
                          orderbook.label)
        
        self.link = link
        self._book = orderbook
        
    @property
    def _upLink(self):
        return self.link.up
    
    @property
    def _downLink(self):
        return self.link.down
        
    @property
    def orderbook(self):
        return self._book
    
    @orderbook.setter
    def orderbook(self, value):
        self._book = value
        
    _properties = { 'link'      : remote.TwoWayLink,
                    'orderbook' : types.IOrderBook }
        
    def _on_matched_impl(self, order, *args):
        order.remote.copyTo(order)
        order.on_matched.fire(*args)
        
    def _send_to_downlink(self, order, *args):
        self._downLink.send(bind.Method(self, '_on_matched_impl', order, *args))

    def _remote(self, order):
        remote = order.clone()
        assert 'remote' not in dir(order)
        order.remote = remote
        remote.on_matched += bind.Method(self, '_send_to_downlink', order)
        return remote       
        
        
    def processMarketOrder(self, order):
        self._upLink.send(bind.Method(self._book, 'processMarketOrder', self._remote(order)))
        
    def processLimitOrder(self, order):
        self._upLink.send(bind.Method(self._book, 'processLimitOrder', self._remote(order)))

    def cancelOrder(self, order):
        self._upLink.send(bind.Method(self._book, 'cancelOrder', order.remote))
        
    def evaluateOrderPriceAsync(self, side, volume, callback):
        self._upLink.send(
            bind.Method(self._book, 'evaluateOrderPriceAsync', side, volume, 
                bind.Method(self._downLink, 'send', bind.Callable(callback, x))))
        
