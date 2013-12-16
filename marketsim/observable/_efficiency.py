from marketsim import (registry, orderbook, request, Side, getLabel,
                       meta, types, bind, event, _, ops)

import marketsim

from _trader import volume_traded, profit_and_loss

from _orderbook import LastTrade

def sign(x):
    return 1 if x > 0 else -1 if x < 0 else 0

@registry.expose(alias = ["Asset's", "Cumulative price"])
class CumulativePrice(ops.Observable[float]):

    def __init__(self, book = None, depth = None):

        super(CumulativePrice, self).__init__()

        self.book = book if book else orderbook.OfTrader()
        self.depth = depth if depth else volume_traded(marketsim.trader.SingleProxy())

        self.attributes = {}

        self.reset()
        event.subscribe(LastTrade(self.book), _(self)._update, self)
        event.subscribe(self.depth, _(self)._update, self)

    @property
    def digits(self):
        return self.book._digitsToShow

    def _callback(self, sign, (price, volume_unmatched)):
        if volume_unmatched == 0:
            self._current = sign*price
            self.fire(self)
        else: # don't know what to do for the moment
            self._current = None

    def _update(self, dummy = None):
        depth = self.depth()
        side = Side.Buy if depth < 0 else Side.Sell
        self.book.process(
                        request.EvalMarketOrder(side,
                                                abs(depth),
                                                _(self, -sign(depth))._callback))

    _properties = {
        'book' : types.IOrderBook,
        'depth': types.IObservable[float]
    }

    def reset(self):
        self._current = None

    @property
    def label(self):
        """ Returns indicator label
        """
        return "CumulativePrice_{"+getLabel(self.book)+"}"

    def __call__(self):
        return self._current


@registry.expose(alias = ["Trader's", "Efficiency"])
class Efficiency(ops.Observable[float]):
    """ Observes trader's balance as if was cleared (trader's balance if its position was cleared).
    Can be None if there is not enough assets on the market to clear the position.
    This observable is updated when trader position is changed 
    (which is not fair since the asset price change influences on this parameter also)
    """
    
    def __init__(self, trader = None):
        
        super(Efficiency, self).__init__()
        
        self._trader = trader if trader else marketsim.trader.SingleProxy()
        
        self.attributes = {}

        self.amount = volume_traded(trader)
        self.balance = profit_and_loss(trader)
        
        self.reset()
        event.subscribe(LastTrade(orderbook.OfTrader(trader)), _(self)._update, self)
        event.subscribe(self.amount, _(self)._update, self)

    _internal = ["amount"]
        
    @property
    def digits(self):
        return self._trader.orderBook._digitsToShow
    
    def _callback(self, sign, (price, volume_unmatched)): 
        if volume_unmatched == 0: 
            self._current = self.balance() - sign*price
            self.fire(self)
        else: # don't know what to do for the moment
            self._current = None

    def _update(self, dummy = None):
        amount = self.amount()
        side = Side.Buy if amount < 0 else Side.Sell
        self._trader.orderBook.process(
                        request.EvalMarketOrder(side, 
                                                abs(amount),
                                                _(self, -sign(amount))._callback))
    
        
    @property
    def trader(self):
        return self._trader
    
    @trader.setter
    def trader(self, value):
        self._trader = value    
        #self._event.switchTo(self._trader.on_traded)
            

    _properties = { 'trader' : types.IAccount }
    
        
    def reset(self):
        self._current = None

    @property
    def label(self):
        """ Returns indicator label
        """
        return "Efficiency_{"+getLabel(self._trader)+"}"
        
    def __call__(self):
        return self._current
