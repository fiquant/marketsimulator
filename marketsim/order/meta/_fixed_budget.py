from marketsim import registry, request, context, event, _, Event, combine, ops, types
from marketsim.types import *

import _ioc
from .. import  _limit

from _meta import *

class FixedBudget(Base):
    
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
            self.send(_ioc.Order(_limit.Order(self.side, p, v)))
            self._ordersSent += 1
            
    def __repr__(self):
        return 'FixedBudget(%s,%s)' % (self.side, self.budget)
            

@registry.expose(['FixedBudget'])    
class Factory(types.IOrderGenerator, combine.SideBudget):
    
    def bind(self, ctx):
        self._ctx = ctx.context.copy()
        
    def __call__(self):
        params = combine.SideBudget.__call__(self)
        return FixedBudget(*params) if params is not None else None

@registry.expose(['FixedBudget'])    
@sig((IFunction[Side],), IOrderGenerator)
class Side_Factory(object):
    
    def __init__(self, budget = ops.constant(200.)):
        self.budget = budget
        
    _properties = { 
        'budget'  : types.IFunction[float],
    }
    
    def __call__(self, side):
        return Factory(side, self.budget)
