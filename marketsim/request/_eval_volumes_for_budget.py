from marketsim import types, _

class EvalVolumesForBudget(object):
    
    def __init__(self, side, budget, callback):
        self.side = side
        self.budget = budget
        self.callback = callback
        
    def processIn(self, orderBook):
        orderBook.evaluateVolumesForBudget(self.side, self.budget, self.callback)

        
    