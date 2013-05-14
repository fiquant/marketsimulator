from marketsim import Side, registry, meta, types, bind
from _base import Base
from _limit import LimitFactory
from _cancel import Cancel
from marketsim.types import *

class AlwaysBest(Base):
    """ AlwaysBest is a virtual order that ensures that it has the best price in the order book. 
    It is implemented as a limit order which is cancelled 
    once the best price in the order queue has changed 
    and is sent again to the order book 
    with a price one tick better than the best price in the book.
    """
    
    def __init__(self, volume, 
                 side = Side.Sell, 
                 orderFactoryT = LimitFactory):
        
        Base.__init__(self, side, volume)

        self._factory = orderFactoryT(side)
        self._current = None
        
    def processIn(self, book):
        def onBestChanged(queue):
            if not queue.empty and queue.best != self._current:
                if self._current is not None:
                    book.process(Cancel(self._current))
                if not self.empty and not self.cancelled:
                    price = queue.best.price
                    tick = queue.book.tickSize
                    price += tick if self.side == Side.Buy else -tick
                    self._current = self._factory(price, self.volume)
                    self._current.on_matched += lambda my, other, pv: self.onMatchedWith(other, pv)
                    book.process(self._current)
        onBestChanged(book.queue(self.side))
        book.queue(self.side).on_best_changed += onBestChanged
    
@registry.expose(alias=['AlwaysBest'])
@sig(args=(Side,), rv=function((Price,), IOrder))
def AlwaysBestFactory(side):
    return bind.Construct(AlwaysBest, side)
         
AlwaysBestFactory.__doc__ = AlwaysBest.__doc__