from marketsim import types

from _sa import SingleAsset

class SingleAssetSingleMarket(SingleAsset):
    """ A trader that trades a single asset on a single market.
    
        Parameters:
        
        **orderBook**
            order book for the asset being traded
            
        **strategies**
            array of strategies run by the trader
            
        **amount** 
            current position of the trader (number of assets that it owns)
            
        **PnL**
            current trader balance (number of money units that it owns)
    """
    
    def __init__(self, orderBook, strategy=None, label=None, strategies=[], amount=0, PnL=0):
        self._orderBook = orderBook
        SingleAsset.__init__(self, strategy, label, strategies, amount, PnL)
        
    _properties = {'orderBook' : types.IOrderBook}
            
    @property
    def book(self): # obsolete
        return self._orderBook
    
    @property
    def orderBook(self):
        return self._orderBook
    
    @orderBook.setter
    def orderBook(self, newvalue):
        self.stop()
        self._orderBook = newvalue
        self.run()
        
    def send(self, order):
        SingleAsset.send(self, self._orderBook, order)
