from marketsim import types, meta, getLabel, Side

from _base import Base

class SingleAsset(Base, types.ISingleAssetTrader):
    """ Trader that trades only one asset 
    (should we consider a same asset on different markets as the same asset?)
    Maintains number of assets traded:
    positive if trader has bought more assets than sold them
    negative otherwise
    """

    def __init__(self, strategy=None, label=None, strategies=[], amount = 0, PnL=0, timeseries = []):
        Base.__init__(self, PnL, timeseries)
        self._amount = amount
        self._strategies = []
        self._label = label if label else getLabel(self)
        self.label = self._label
        self._alias = [self._label]
        
        if strategy is not None:
            strategies = strategies + [strategy]

        for strategy in strategies:
            self.addStrategy(strategy)
            
    def reset(self):
        Base.reset(self)
        self._amount = 0
        
    def stop(self):
        Base.stop(self) 
        for strategy in self._strategies:
            strategy.stopRunning() 
        
    _properties = {'amount'     : float, 
                   'strategies' : meta.listOf(types.IStrategy)}
    
    @property
    def amount(self):
        """ Number of assets traded:
        positive if trader has bought more assets than sold them
        negative otherwise
        """
        return self._amount
    
    @amount.setter
    def amount(self, value):
        self._amount = value
        
    @property 
    def strategies(self):
        return self._strategies
    
    @strategies.setter
    def strategies(self, value):
        old = set(self._strategies)
        new = set(value)
        to_delete = old - new
        to_add = new - old
        for s in to_delete:
            self.removeStrategy(s)
        for s in to_add:
            self.addStrategy(s)
            
    def removeStrategy(self, strategy):
        strategy.dispose()
        self._strategies.remove(strategy)
    
    def addStrategy(self, strategy):
        self._strategies.append(strategy)        

    def _onOrderMatched_impl(self, order, other, (price, volume)):
        """ Called when a trader's 'order' is traded against 'other' order 
        at given 'price' and 'volume'
        Trader's amount and P&L is updated and listeners are notified about the trade   
        """
        self._amount += volume if order.side == Side.Buy else -volume
        Base._onOrderMatched_impl(self, order, other, (price, volume))
