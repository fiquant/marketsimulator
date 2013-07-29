from marketsim import (context, combine, Side, registry, meta, types, bind, 
                       event, _, ops, observable, orderbook)
from _base import Base
from _limit import LimitFactory, Limit
from _cancel import Cancel
from _mutable import Mutable
from marketsim.types import *

def AlwaysBest2(side, volume):
    
    book = orderbook.OfTrader()
    tickSize = observable.TickSize(book)
    askPrice = observable.AskPrice(book)
    bidPrice = observable.BidPrice(book)
    
    price = observable.MinEpsilon(askPrice, tickSize)\
                if side == Side.Sell else\
            observable.MaxEpsilon(bidPrice, tickSize)

    return Mutable(
                combine.SidePriceVolume(
                    ops.constant(side), 
                    price, 
                    ops.constant(volume)))
    
class Factory(types.IOrderGenerator, combine.SideVolume):
    
    def bind(self, ctx):
        self._ctx = ctx.context.copy()
        
    def __call__(self):
        params = combine.SideVolume.__call__(self)
        order = AlwaysBest2(*params) if params is not None else None
        if order is not None:
            context.bind(order, self._ctx)
        return order

class AlwaysBest(Base):
    """ AlwaysBest is a virtual order that ensures that it has the best price in the order book. 
    It is implemented as a limit order which is cancelled 
    once the best price in the order queue has changed 
    and is sent again to the order book 
    with a price one tick better than the best price in the book.
    """
    
    def __init__(self, side, volume):
        
        Base.__init__(self, side, volume)
        self._current = None
        
    def onOrderMatched(self, my, other, pv):
        Base.onMatchedWith(self, other, pv)
        if self._volume == 0:
            self._subscription.dispose()
            del self._subscription 
    
    def _onBestOrderChanged(self, queue):
        if not queue.empty and queue.best != self._current:
            if self._current is not None:
                self._orderSubscription.dispose()
                queue.book.process(Cancel(self._current))
                self._subscription.dispose()
                #print "cancelled"
            if not self.empty and not self.cancelled:
                price = queue.best.price
                tick = queue.book.tickSize
                price += tick if self.side == Side.Buy else -tick
                self._current = Limit(self.side, price, self.volume)
                self._orderSubscription = \
                    event.subscribe(self._current.on_matched, 
                                    _(self).onOrderMatched,
                                    self, {})
                queue.book.process(self._current)
                #print self.side, price
                handler = (event.GreaterThan \
                                if self.side == Side.Buy else \
                           event.LessThan)(price, (self)._onBestOrderChanged)
                self._subscription = event.subscribe(
                                        queue.bestPrice,
                                        handler,
                                        self, {})
                #print "queued"
        
    def processIn(self, book):
        self._onBestOrderChanged(book.queue(self.side))
