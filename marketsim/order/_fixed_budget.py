from marketsim import event, _, Event, combine, ops, types
from marketsim.types import *

from _limit_market import LimitMarket

class FixedBudget(object):
    
    def __init__(self, side, budget):
        self.side = side
        self.budget = budget
        self.on_matched = Event()
        self.on_cancelled = Event()
        self.on_charged = Event()
        
    def processIn(self, orderBook):
        orderBook.evaluateVolumesForBudget(self.side, self.budget, 
                                           _(self, orderBook)._onEvaluated)
        
    def _onEvaluated(self, orderBook, pvs):
        self._ordersSent = 0
        for p,v in pvs:
            order = LimitMarket(self.side, p, v)
            event.subscribe(order.on_matched, _(self)._onMatched, self, {}) 
            event.subscribe(order.on_cancelled, _(self)._onCancelled, self, {}) 
            event.subscribe(order.on_charged, self.on_charged.fire, self, {}) 
            orderBook.process(order)
            self._ordersSent += 1
            
    def __repr__(self):
        return 'FixedBudget(%s,%s)' % (self.side, self.budget)
            
    def _onMatched(self, order, other, (p,v)):
        self.budget -= p*v
        self.on_matched.fire(self, other, (p,v))
            
    def _onCancelled(self, order):
        self._ordersSent -= 1
        if self._ordersSent == 0:
            self.on_cancelled.fire(self)

class Factory(types.IOrderGenerator, combine.SideBudget):
    
    def __call__(self):
        params = combine.SideBudget.__call__(self)
        return FixedBudget(*params) if params is not None else None
