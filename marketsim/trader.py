import random
from marketsim.scheduler import Timer, world
from marketsim import Side, getLabel
from marketsim.order import *
from marketsim.indicator import AssetPrice, ewma, Fold, derivative
import math

class TraderBase(object):
    """ Base class for traders.
    Responsible for bookkeeping P&L of the trader and 
    maintaining on_order_sent and on_traded events
    """

    def __init__(self):
        # P&L is the minus sum of money spent for the trades done
        # if a trader sells P&L increases
        # if a trader buys P&L falls
        self._PnL = 0
        # event to be fired when an order has been sent
        self.on_order_sent = Event()
        # event to be fired when a trader's is traded
        self.on_traded = Event()

    def _onOrderMatched(self, order, other, (price, volume)):
        """ Called when a trader's 'order' is traded against 'other' order 
        at given 'price' and 'volume'
        Trader's P&L is updated and listeners are notified about the trade   
        """
        pv = price * volume
        self._PnL += pv if order.side == Side.Sell else -pv
        
        self.on_traded.fire(self)

    @property
    def PnL(self):
        """ Returns traders's P&L
        """
        return self._PnL
    
    def _makeSubscribedTo(self, order):
        """ Makes trader subscribed to 'order' on_matched event
        before sending it to the order book
        Returns the order itself 
        """
        order.on_matched += self._onOrderMatched
        return order

    def send(self, book, order):
        """ Sends 'order' to 'book'
        After having the order sent notifies listeners about it 
        """
        book.process(self._makeSubscribedTo(order))
        self.on_order_sent.fire(order)        

        
class SingleAssetTrader(TraderBase):
    """ Trader that trades only one asset 
    (should we consider a same asset on different markets as the same asset?)
    Maintains number of assets traded:
    positive if trader has bought more assets than sold them
    negative otherwise
    """

    def __init__(self):
        TraderBase.__init__(self)
        self._amount = 0

    def _onOrderMatched(self, order, other, (price, volume)):
        """ Called when a trader's 'order' is traded against 'other' order 
        at given 'price' and 'volume'
        Trader's amount and P&L is updated and listeners are notified about the trade   
        """
        self._amount += volume if order.side == Side.Buy else -volume
        TraderBase._onOrderMatched(self, order, other, (price,volume))
        
    @property
    def amount(self):
        """ Number of assets traded:
        positive if trader has bought more assets than sold them
        negative otherwise
        """
        return self._amount
    
class SingleAssetSingleMarketTrader(SingleAssetTrader):
    
    def __init__(self, orderBook, label=None):
        SingleAssetTrader.__init__(self)
        self._orderBook = orderBook
        self._label = label if label else getLabel(self)
        self.label = self._label
        
    @property
    def book(self): # obsolete
        return self._orderBook
    
    @property
    def orderBook(self):
        return self._orderBook
    
#    @property
#    def label(self):
#        return self._label
    
    def send(self, order):
        SingleAssetTrader.send(self, self._orderBook, order)
        
SASM_Trader = SingleAssetSingleMarketTrader 

class SingleAssetMultipleMarketTrader(SingleAssetTrader):
    
    def __init__(self, orderBooks, label=None):
        SingleAssetTrader.__init__(self)
        self._orderBooks = orderBooks
        self._label = label if label else getLabel(self)
        
    @property
    def orderBooks(self):
        return self._orderBooks