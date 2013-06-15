from marketsim import meta, types, event
from _base import Base

class MultiAsset(Base, types.ITrader):
    
    def __init__(self, traders = [], strategy = None, PnL = 0, label = None, timeseries = []):
        Base.__init__(self, PnL, timeseries)
        self._traders = []
        self.traders = traders
        self.strategy = strategy
        self._label = label if label else getLabel(self)
        self.label = self._label
        self._alias = [self._label]
        
    _properties = { 'traders' : meta.listOf(types.ISingleAssetTrader),
                    'strategy': types.IMultiAssetStrategy }
    
    @property
    def traders(self):
        return self._traders
    
    @traders.setter
    def traders(self, newTraders):
        for t in self._traders:
            t.on_traded -= self.on_traded.fire
        self._traders = newTraders
        for t in self._traders:
            t.on_traded += self.on_traded.fire
            
    def dispose(self):
        for t in self._traders:
            t.on_traded -= self.on_traded.fire
        
    @property
    def orderBooks(self):
        return [t.orderBook for t in self._traders]
        
    @property
    def PnL(self):
        return sum([t.PnL for t in self._traders])

    @PnL.setter
    def PnL(self, value):
        assert value == self.PnL, 'cannot change balance of a multi asset trader'