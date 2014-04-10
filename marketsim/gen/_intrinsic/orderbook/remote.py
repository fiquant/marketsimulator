from marketsim import types, bind, _
from base import BookBase
from queue import BestPrice, LastTrade

from marketsim.gen._out._intrinsic_base.orderbook.remote import Remote_Base

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

    def bind_ex(self, ctx):
        self._bound_ex = True
        self.book.bind_ex(ctx)
        self._link.bind_ex(ctx)

        
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
    
class Remote_Impl(BookBase, Remote_Base):
    """ Represent an *orderbook* from point of view of a remote trader connected
    to the market by means of a *link* that introduces some latency in information propagation
    """
    
    def __init__(self):
        
        self.name = self.orderbook.label
        self._digitsToShow = self.orderbook._digitsToShow
        BookBase.__init__(self, # TODO: dependency tracking
                          Queue(self.orderbook.bids, self, self.link.down),
                          Queue(self.orderbook.asks, self, self.link.down))


    @property
    def _upLink(self):
        return self.link.up
    
    @property
    def _downLink(self):
        return self.link.down
    
    @property
    def tickSize(self):
        return self.orderbook.tickSize
        
    def _on_matched(self, order, price, volume):
        order.remote.copyTo(order)
        order.owner.onOrderMatched(order, price, volume)
        
    def _on_order_disposed(self, order):
        order.remote.copyTo(order)
        order.owner.onOrderDisposed(order)
        
    def onOrderMatched(self, order, price, volume):
        self._downLink.send(_(self, order, price, volume)._on_matched)
        
    def onOrderDisposed(self, order):
        self._downLink.send(_(self, order)._on_order_disposed)
    
    def onOrderCharged(self, price):
        self.owner.onOrderCharged(price)    
        
    def _remote(self, order):
        remote = order.clone()
        assert 'remote' not in dir(order)
        order.remote = remote
        remote.remote = order
        remote.owner = self
        return remote       
    
    def process(self, order):
        from marketsim.gen._out._iorder import IOrder
        if isinstance(order, IOrder):
            BookBase.process(self, order)
        else:
            #if 'callback' in dir(order):
            #    order.callback = _(self, order.callback)._sendToDownLink
            self._upLink.send(_(self.orderbook, order).process)
        
    def processMarketOrder(self, order):
        self._upLink.send(_(self.orderbook, self._remote(order)).processMarketOrder)
        
    def processLimitOrder(self, order):
        self._upLink.send(_(self.orderbook, self._remote(order)).processLimitOrder)
        
    def _sendToDownLink(self, callback, x):
        self._downLink.send(bind.Callable(callback, x))
