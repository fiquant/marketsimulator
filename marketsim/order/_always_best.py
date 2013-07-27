from marketsim import Side, registry, meta, types, bind, event, _, ops
from _base import Base
from _limit import LimitFactory, Limit
from _cancel import Cancel
from marketsim.types import *

class MaxEpsilon(ops.Observable[float]):
    """ Observable that fires if underlying source value becomes greater previous maximum plus some epsilon
    """
    
    def __init__(self, source, epsilon):
        ops.Observable[float].__init__(self)
        self.source = source
        self.epsilon = epsilon
        
    _properties = { 'source' : types.IObservable[float], 
                    'epsilon': types.IFunction[float] }
        
    def _subscribe(self):
        self.value = self.source()
        self._handler = _(self)._fire
        if self.value is not None:
            self._handler = event.GreaterThan(self.value + self.epsilon(), self._handler)
        self.source += self._handler
        
    def bind(self, ctx):
        self._subscribe()
        
    def __call__(self):
        return self.value
        
    def _fire(self, dummy):
        if self.source() is not None:
            self.source -= self._handler
            self._subscribe()
            self.fire(dummy)
        
    @property
    def label(self):
        return "Max^{" + self.source.label + "}_{\epsilon}"
    
    @property
    def attributes(self):
        return {}
        
        

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
