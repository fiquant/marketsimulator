from _basic import OneSide, Strategy
from _wrap import merge, wrapper
from marketsim import order, Side, scheduler, mathutils, types
from marketsim.mathutils.predicates import *


class _LiquidityProviderSide_Impl(OneSide):

    def __init__(self, trader, params):
        self._params = params
        self._orderFactory = params.orderFactoryT(params.side)
        self._queue = trader.book.queue(params.side)
        self._eventGen = scheduler.Timer(params.creationIntervalDistr)
        
        OneSide.__init__(self, trader)
        
    def _orderFunc(self):
        currentPrice = self._queue.best.price if not self._queue.empty else\
                       self._queue.lastPrice if self._queue.lastPrice is not None else\
                       self._params.defaultValue
        price = currentPrice * self._params.priceDistr()
        volume = int(self._params.volumeDistr())
        return (price, volume)
    
    def dispose(self):
        OneSide.dispose(self)
        self._eventGen.cancel()
        
exec wrapper("LiquidityProviderSide",
             [('side',                  'Side.Sell',                            'None'),
              ('orderFactoryT',         'order.Limit.T',                        'None'),
              ('defaultValue',          '100',                                  'non_negative'),
              ('creationIntervalDistr', 'mathutils.rnd.expovariate(1.)',        '() -> float'),
              ('priceDistr',            'mathutils.rnd.lognormvariate(0., .1)', '() -> float'),
              ('volumeDistr',           'mathutils.rnd.expovariate(1.)',        '() -> float')])
       
class _LiquidityProvider_Impl(Strategy):
    def __init__(self, trader, params):
        Strategy.__init__(self, trader)
        sp = merge(params, side=Side.Sell)
        bp = merge(params, side=Side.Buy) 
        self._sell = _LiquidityProviderSide_Impl(trader, sp)
        self._buy = _LiquidityProviderSide_Impl(trader, bp)
    
    def suspend(self, s):
        Strategy.suspend(self, s)
        self._sell.suspend(s)
        self._buy.suspend(s)
        
    @property
    def suspended(self):
        assert self._sell.suspended == self._suspended
        assert self._buy.suspended == self._suspended
        return Strategy.suspended(self)
    
    def dispose(self):
        self._sell.dispose()
        self._buy.dispose()

exec wrapper('LiquidityProvider',
            [('orderFactoryT',          'order.Limit.T',                        'None'),
             ('defaultValue',           '100',                                  'non_negative'),
             ('creationIntervalDistr',  'mathutils.rnd.expovariate(1.)',        '() -> float'),
             ('priceDistr',             'mathutils.rnd.lognormvariate(0., .1)', '() -> float'),
             ('volumeDistr',            'mathutils.rnd.expovariate(.1)',        '() -> float')])

class _Canceller_Impl(object):
    """ Randomly cancels created orders in specific moments of time    
    """

    def __init__(self, source, params):

        # orders created by trader
        self._elements = []

        # start listening its orders sent
        source.on_order_sent += self.process
        
        book = source.book

        def wakeUp(_):
            # if we have orders to cancel
            while self._elements <> []:
                # choose an order
                N = len(self._elements)
                idx = params.choiceFunc(N)
                e = self._elements[idx]
                # if the order is invalid
                if e.empty or e.cancelled:
                    # put the last order instead of it and repeat the procedure
                    if e <> self._elements[-1]:
                        self._elements[idx] = self._elements[-1]
                    # it converges since every time we pops an element from the queue
                    self._elements.pop()
                else:
                    # if order is valid, cancel it
                    book.process(order.Cancel(e))
                    return

        scheduler.Timer(params.cancellationIntervalDistr).advise(wakeUp)

    def process(self, order):
        """ Puts 'order' to future cancellation list
        """
        self._elements.append(order)

exec wrapper("Canceller",
             [('cancellationIntervalDistr', 'mathutils.rnd.expovariate(1.)',    '() -> float'),
              ('choiceFunc',                'lambda N: random.randint(0,N-1)',  'None')])
