from marketsim import types, meta, getLabel, Side

from _base import Base

class SingleAsset(Base, types.ISingleAssetTrader):
    """ Trader that trades only one asset 
    (should we consider a same asset on different markets as the same asset?)
    Maintains number of assets traded:
    positive if trader has bought more assets than sold them
    negative otherwise
    """

    def __init__(self, strategy, label=None, amount = 0, PnL=0, timeseries = []):
        Base.__init__(self, PnL, timeseries)
        self._amount = amount
        self.strategy = strategy
        self._label = label
        self.label = self._label
        self._alias = [self._label]
             
    def reset(self):
        self._amount = 0
        
    _properties = {'amount'     : float, 
                   'strategy'   : types.ISingleAssetStrategy}
    
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
        
    def _onOrderMatched_impl(self, order, other, (price, volume)):
        """ Called when a trader's 'order' is traded against 'other' order 
        at given 'price' and 'volume'
        Trader's amount and P&L is updated and listeners are notified about the trade   
        """
        self._amount += volume if order.side == Side.Buy else -volume
        Base._onOrderMatched_impl(self, order, other, (price, volume))
