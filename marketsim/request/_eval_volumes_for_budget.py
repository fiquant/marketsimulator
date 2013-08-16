from marketsim import types, _

class EvalVolumesForBudget(types.IRequest):
    
    def __init__(self, side, budget, callback):
        # callback((PnL, volume_unmatched)) will be called
        self.side = side
        self.budget = budget
        self.callback = callback
        
    def processIn(self, orderBook):
        orderBook.evaluateVolumesForBudget(self.side, self.budget, self.callback)

        
    