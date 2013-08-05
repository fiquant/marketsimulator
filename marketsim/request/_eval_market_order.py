from marketsim import types, _

class EvalMarketOrder(types.IRequest):
    
    def __init__(self, side, volume, callback):
        self.side = side
        self.volume = volume
        self.callback = callback
        
    def processIn(self, orderBook):
        orderBook.evaluateOrderPriceAsync(self.side, self.volume, self.callback)

        
    