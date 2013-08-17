from marketsim import event, _, types, meta, getLabel, Side

from _base import Base

class SingleAsset(Base, types.ISingleAssetTrader):
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

    def __init__(self, orderBook, strategy, label=None, amount = 0, PnL=0, timeseries = []):
        Base.__init__(self, PnL, timeseries)
        self._orderBook = orderBook
        self._amount = amount
        self._strategy = strategy
        self._subscription = event.subscribe(strategy.on_order_created, _(self).send, self)
        self._label = label
        self.label = self._label
        self._alias = [self._label]
        
    @property
    def strategy(self):
        return self._strategy
    
    @strategy.setter
    def strategy(self, value):
        self._subscription.switchTo(value.on_order_created)
        self._strategy = value
             
    def reset(self):
        self._amount = 0
        
    _properties = {'amount'     : float,
                   'strategy'   : types.ISingleAssetStrategy,
                   'orderBook'  : types.IOrderBook }
    
    _internals = ['_orderBook'] # hack in order to make it processed first
            
    
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
        
    def onOrderMatched(self, order, price, volume):
        """ Called when a trader's 'order' is traded against 'other' order 
        at given 'price' and 'volume'
        Trader's amount and P&L is updated and listeners are notified about the trade   
        """
        dVolume = volume if order.side == Side.Buy else -volume
        self._amount += dVolume
        Base.onOrderMatched(self, order, price, volume)
        

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
        Base.send(self, self._orderBook, order)
