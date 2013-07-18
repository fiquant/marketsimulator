from marketsim import event, registry, remote, types, bind, _
from _base import BookBase
from _queue import BestPrice, LastTrade

class Queue(object):
    
    def __init__(self, queue, book, link):
        self._queue = queue
        self.book = book
        self._link = link
        queue.bestPrice += _(self)._onBestChanged
        self.bestPrice = BestPrice(self)
        self.lastTrade = LastTrade()
        queue.lastTrade += _(self)._onTraded
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
        
    def _update(self, best):
        self._best = best
        self.bestPrice.fire(self)
        
    def _onTraded(self, value):
        self._link.send(_(self.lastTrade, value).set)

    def _onBestChanged(self, queue):
        best = queue.best
        self._link.send(_(self, best)._update)
        
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
        self._digitsToShow = self._book._digitsToShow
        
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
        
    def _on_matched(self, order, *args):
        order.remote.copyTo(order)
        order.on_matched.fire(*args)
        
    def _on_cancelled(self, order, *args):
        order.remote.copyTo(order)
        order.on_cancelled.fire(order)
        
    def _send_to_downlink(self, order, *args):
        self._downLink.send(_(self, order, *args)._on_matched)

    def _send_to_downlink_cancelled(self, order, *args):
        self._downLink.send(_(self, order, *args)._on_cancelled)

    def _remote(self, order):
        remote = order.clone()
        assert 'remote' not in dir(order)
        order.remote = remote
        remote.on_matched += _(self, order)._send_to_downlink
        remote.on_cancelled += _(self, order)._send_to_downlink_cancelled
        return remote       
        
    def processMarketOrder(self, order):
        self._upLink.send(_(self._book, self._remote(order)).processMarketOrder)
        
    def processLimitOrder(self, order):
        self._upLink.send(_(self._book, self._remote(order)).processLimitOrder)

    def cancelOrder(self, order):
        self._upLink.send(_(self._book, order.remote).cancelOrder)
        
    def _sendToDownLink(self, callback, x):
        self._downLink.send(bind.Callable(callback, x))
        
    def evaluateOrderPriceAsync(self, side, volume, callback):
        self._upLink.send(
            _(self._book, side, volume, _(self, callback)._sendToDownLink)
                .evaluateOrderPriceAsync)
        
