from marketsim import request, _

import ioc
from .. import  limit

from _meta import *

class Order_Impl(Base):
    
    def __init__(self, side, budget):
        Base.__init__(self, None)
        self.side = side
        self.budget = budget

    def onOrderMatched(self, order, price, volume):
        self.budget -= price*volume
        Base.onOrderMatched(self, order, price, volume)
        
    def onOrderDisposed(self, order):
        self._ordersSent -= 1
        if self._ordersSent == 0:
            self.cancel()
        
    def startProcessing(self):
        self.orderBook.process(
                   request.EvalVolumesForBudget(
                                self.side, self.budget, 
                                _(self)._onEvaluated))
        
    def _onEvaluated(self, pvs):
        self._ordersSent = 0
        self._volumeUnmatched = sum([v for p,v in pvs])
        for p,v in pvs:
            self.send(ioc.Order_Impl(limit.Order_Impl(self.side, p, v)))
            self._ordersSent += 1
            
    def __repr__(self):
        return 'FixedBudget(%s,%s)' % (self.side, self.budget)
