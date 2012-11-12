from marketsim import Side
from _base import Base
from _limit import Limit
from _cancel import Cancel

class AlwaysBest(Base):
    
    def __init__(self, volume, 
                 side = Side.Sell, 
                 orderFactoryT = Limit.T):
        
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
