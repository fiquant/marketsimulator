from marketsim import getLabel, Event, Side, meta, types, Method

class Base(object):
    """ Base class for traders.
    Responsible for bookkeeping P&L of the trader and 
    maintaining on_order_sent and on_traded events
    """

    def __init__(self, PnL = 0):
        # P&L is the minus sum of money spent for the trades done
        # if a trader sells P&L increases
        # if a trader buys P&L falls
        self._PnL = PnL
        # event to be fired when an order has been sent
        self.on_order_sent = Event()
        # event to be fired when a trader's is traded
        self.on_traded = Event()
        self._running = False
        self.charge = Method(self, '_charge_impl')
        self._onOrderMatched = Method(self, '_onOrderMatched_impl')
        self.reset()
        
    @property
    def running(self):
        return self._running
    
    def run(self):
        assert not self._running
        self._running = True
    
    def stop(self):
        assert self._running
        self._running = False
        
    def reset(self):   
        self._PnL = 0 
        
    _properties = {'PnL' : float}
    
    @property
    def PnL(self):
        return self._PnL
    
    @PnL.setter
    def PnL(self, value):
        self._PnL = value
        
    def _charge_impl(self, price):
        self._PnL -= price

    def _onOrderMatched_impl(self, order, other, (price, volume)):
        """ Called when a trader's 'order' is traded against 'other' order 
        at given 'price' and 'volume'
        Trader's P&L is updated and listeners are notified about the trade   
        """
        pv = price * volume
        self._PnL += pv if order.side == Side.Sell else -pv
        
        self.on_traded.fire(self)

    def _makeSubscribedTo(self, order):
        """ Makes trader subscribed to 'order' on_matched event
        before sending it to the order book
        Returns the order itself 
        """
        order.on_matched += self._onOrderMatched
        order.on_charged += self.charge
        return order

    def send(self, book, order):
        """ Sends 'order' to 'book'
        After having the order sent notifies listeners about it 
        """
        book.process(self._makeSubscribedTo(order))
        self.on_order_sent.fire(order)        

        
class SingleAsset(Base, types.ISingleAssetTrader):
    """ Trader that trades only one asset 
    (should we consider a same asset on different markets as the same asset?)
    Maintains number of assets traded:
    positive if trader has bought more assets than sold them
    negative otherwise
    """

    def __init__(self, strategy=None, label=None, strategies=[], amount = 0, PnL=0):
        Base.__init__(self, PnL)
        self._amount = amount
        self._strategies = []
        self._label = label if label else getLabel(self)
        self.label = self._label
        self._alias = self._label
        
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
            
    def run(self):
        Base.run(self)
        for strategy in self._strategies:
            strategy.runAt(self)
            
    def removeStrategy(self, strategy):
        if not self.running:
            strategy.stopRunning()
        self._strategies.remove(strategy)
    
    def addStrategy(self, strategy):
        if self.running:
            strategy.runAt(self)
        self._strategies.append(strategy)        

    def _onOrderMatched_impl(self, order, other, (price, volume)):
        """ Called when a trader's 'order' is traded against 'other' order 
        at given 'price' and 'volume'
        Trader's amount and P&L is updated and listeners are notified about the trade   
        """
        self._amount += volume if order.side == Side.Buy else -volume
        Base._onOrderMatched_impl(self, order, other, (price, volume))
        
class SingleAssetSingleMarket(SingleAsset):
    
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
        
class SingleAssetMultipleMarket(SingleAsset):
    
    def __init__(self, orderBooks, strategy=None, label=None, strategies=[]):
        self._orderBooks = orderBooks
        SingleAsset.__init__(self, strategy, label, strategies)
        
    _properties = { 'orderBooks' : meta.listOf(types.IOrderBook) }
        
    @property
    def orderBooks(self):
        return self._orderBooks
    
SASM = SingleAssetSingleMarket 
SAMM = SingleAssetMultipleMarket    

class Collection(object):
    
    _properties = { 'traders': meta.listOf(types.ISingleAssetTrader) }
    
    def __init__(self, traders):
        self.traders = traders

