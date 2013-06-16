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
    
    def __init__(self, orderBook, strategy, label=None, amount=0, PnL=0, timeseries = []):
        self._orderBook = orderBook
        SingleAsset.__init__(self, strategy, label, amount, PnL, timeseries)
        
    _properties = {'orderBook' : types.IOrderBook}
    
    _internals = ['_orderBook']
            
    @property
    def book(self): # obsolete
        return self._orderBook
    
    @property
    def orderBook(self):
        return self._orderBook
    
    @property
    def orderBooks(self):
        return [self._orderBook]
    
    @property
    def _digitsToShow(self):
        return self._orderBook._digitsToShow
    
    @orderBook.setter
    def orderBook(self, newvalue):
        self._orderBook = newvalue
        
    def send(self, order):
        SingleAsset.send(self, self._orderBook, order)
