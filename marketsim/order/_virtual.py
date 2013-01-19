from marketsim import Event, Side, registry
from marketsim.types import *

class VirtualMarket(object):
    """ Used to evaluates price at which a market order of given volume would be executed
        Since this query might be computationally expensive and done asynchronously,
        we wrap function OrderQueue.evaluateOrderPrice by this class
        The result will returned in on_matched event with empty 'other' field
        TBD: we make use of on_matched machinery since that is supported in RemoteBook
        but i'm not sure that it is a good design decision  
    """
    def __init__(self, side, volume):
        self.volume = volume
        self.side = side
        self.on_matched = Event()
        self.on_charged = Event()
        
    def copyTo(self, dst):
        pass # we might copy here the total price
    
    def processIn(self, orderBook):
        def callback((price, volume_unmatched)):
            self.on_matched.fire(self, None, (price, self.volume - volume_unmatched))
            
        orderBook.evaluateOrderPriceAsync(self.side, self.volume, callback)

    @staticmethod
    def Buy(volume): return VirtualMarket(Side.Buy, volume)
    
    @staticmethod
    def Sell(volume): return VirtualMarket(Side.Sell, volume)
    
    @staticmethod
    @registry.expose
    @sig(args=(Side,), rv=function((Volume,), Order), label='VirtualMarket')
    def T(side): return lambda volume: VirtualMarket(side, volume)
