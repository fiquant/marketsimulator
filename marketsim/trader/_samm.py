from marketsim import types, meta

from _sa import SingleAsset

class SingleAssetMultipleMarket(SingleAsset):
    
    def __init__(self, orderBooks, strategy, label=None, timeseries=[]):
        self._orderBooks = orderBooks
        SingleAsset.__init__(self, strategy, label, timeseries = timeseries)
        
    _properties = { 'orderBooks' : meta.listOf(types.IOrderBook) }
        
    @property
    def orderBooks(self):
        return self._orderBooks
