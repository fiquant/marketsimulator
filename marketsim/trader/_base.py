from marketsim import event, _, Side, types, meta, timeserie, context

from _history import TraderHistory

class Base(timeserie.Holder):
    """ Base class for traders.
    Responsible for bookkeeping P&L of the trader and 
    maintaining on_order_sent and on_traded events
    """

    def __init__(self, PnL = 0, timeseries = []):
        timeserie.Holder.__init__(self, timeseries)
        # P&L is the minus sum of money spent for the trades done
        # if a trader sells P&L increases
        # if a trader buys P&L falls
        self._PnL = PnL
        # event to be fired when an order has been sent
        self.on_order_sent = event.Event()
        # event to be fired when an order issued by the trader has been matched
        self.on_order_matched = event.Event()
        # event to be fired when an order issued by the trader has been cancelled
        self.on_order_disposed = event.Event()
        # event to be fired when a trader's is traded; to be removed
        self.on_traded = event.Event()
        self.reset()
        
    def updateContext(self, context):
        context.trader = self
        context.orderProcessor = self
        
    def bind(self, ctx):
        self._ctx = ctx.context.copy()
                
    def reset(self):   
        self._PnL = 0

    _properties = {'PnL'        : float }
    
    @property
    def PnL(self):
        return self._PnL
    
    @PnL.setter
    def PnL(self, value):
        self._PnL = value
        
    def _charge(self, price):
        self._PnL -= price

    def onOrderMatched(self, order, price, volume):
        """ Called when a trader's 'order' is traded against 'other' order 
        at given 'price' and 'volume'
        Trader's P&L is updated and listeners are notified about the trade   
        """
        pv = price * volume
        self._PnL += pv if order.side == Side.Sell else -pv
        
        self.on_order_matched.fire(self, order, price, volume)
        self.on_traded.fire(self)
        
    def onOrderDisposed(self, order):
        self.on_order_disposed.fire(self, order)

    def _makeSubscribedTo(self, order):
        """ Makes trader subscribed to 'order' on_matched event
        before sending it to the order book
        Returns the order itself 
        """
        order.owner = self
        return order

    def send(self, book, order):
        """ Sends 'order' to 'book'
        After having the order sent notifies listeners about it 
        """
        context.bind(order, self._ctx)
        if isinstance(order, types.IOrder):
            order = self._makeSubscribedTo(order)
        book.process(order)
        if isinstance(order, types.IOrder):
            self.on_order_sent.fire(order)        
