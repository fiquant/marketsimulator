import random
from _basic import OneSide, Strategy, Generic
from _wrap import merge, wrapper, wrapper2
from marketsim import order, orderbook, scheduler, mathutils, types, registry, bind, meta
from marketsim.types import *

class _LiquidityProviderSide_Impl(OneSide):
    
    @property
    def _orderFactory(self):
        return self.orderFactoryT(self.side)
    
    @property
    def _eventGen(self):
        return scheduler.Timer(self.creationIntervalDistr, self._scheduler)
        
    def _orderFunc(self):
        queue = self._trader.book.queue(self.side)
        currentPrice = queue.best.price if not queue.empty else\
                       queue.lastPrice if queue.lastPrice is not None else\
                       self.defaultValue
        price = currentPrice * self.priceDistr()
        volume = int(self.volumeDistr())
        return (price, volume)
    
    def dispose(self):
        OneSide.dispose(self)
        self._eventGen.cancel()

exec wrapper2("LiquidityProviderSide",
             """ Liquidity provider for one side has followng parameters:

                 |side|
                     side of orders to create (default: Side.Sell)
                     
                 |orderFactory| 
                     order factory function (default: order.Limit.T)
                     
                 |initialValue| 
                     initial price which is taken if orderBook is empty (default: 100)
                     
                 |creationIntervalDistr|
                     defines intervals of time between order creation 
                     (default: exponential distribution with |lambda| = 1)
                     
                 |priceDistr|
                     defines multipliers for current asset price when price of
                     order to create is calculated (default: log normal distribution with 
                     |mu| = 0 and |sigma| = 0.1)
                     
                 |volumeDistr| 
                     defines volumes of orders to create 
                     (default: exponential distribution with |lambda| = 1)

                 It wakes up in moments of time given by *creationIntervalDistr*, checks
                 the last best price of orders in the corresponding queue, takes *initialValue*
                 if it is empty, multiplies it by a value taken from *priceDistr* to obtain price
                 of the order to create, calculates order volume using *volumeDistr*, creates
                 an order via *orderFactoryT(side)* and tells the trader to send it.
             """,
             [('side',                  'Side.Sell',                            'Side'),
              ('orderFactoryT',         'order.LimitFactory',                   'Side -> (Price, Volume) -> IOrder'),
              ('defaultValue',          '100',                                  'Price'),
              ('creationIntervalDistr', 'mathutils.rnd.expovariate(1.)',        '() -> TimeInterval'),
              ('priceDistr',            'mathutils.rnd.lognormvariate(0., .1)', '() -> float'),
              ('volumeDistr',           'mathutils.rnd.expovariate(1.)',        '() -> Volume')])


class ConstantSide(object):
    """ Constant function always returning given *side*. 
    
    Note: We need it since our type system doesn't support for the moment generic
    Constant: () -> 'a
    """
    
    def __init__(self, side = Side.Sell):
        self.side = side
        self._alias = ['Constant side']
        
    _properties = { 'side' : Side }
    _types = [ meta.function((), Side) ]
        
    def __call__(self):
        return self.side
    
class SafeSidePrice(object):
    """ Returns the best price of the given by *orderBook* and *side* order queue, 
        if there is no orders in the queue returns the price of the last trade and
        if there were no trades returns *defaultValue*.
    """
    
    def __init__(self, orderBook, side, defaultValue):
        self.orderBook = orderBook
        self.side = side
        self.defaultValue = defaultValue
        self._alias = ["Asset's", 'Safe order queue price']
        
    _properties = { 'orderBook'     : IOrderBook, 
                    'side'          : Side, 
                    'defaultValue'  : float }
    
    _types = [meta.function((), Price)]
        
    def __call__(self):
        queue = self.orderBook.queue(self.side)
        return queue.best.price if not queue.empty else\
               queue.lastPrice if queue.lastPrice is not None else\
               self.defaultValue

def LiquidityProviderSideEx(side                    = Side.Sell, 
                            orderFactory            = order.LimitFactory, 
                            defaultValue            = 100., 
                            creationIntervalDistr   = mathutils.rnd.expovariate(1.), 
                            priceDistr              = mathutils.rnd.lognormvariate(0., .1), 
                            volumeDistr             = mathutils.rnd.expovariate(1.)):
       
    orderBook = orderbook.OfTrader()
    r = Generic(eventGen    = scheduler.Timer(creationIntervalDistr),
                volumeFunc  = volumeDistr, 
                sideFunc    = ConstantSide(side),
                orderFactory= order.AdaptLimit(orderFactory,
                                               mathutils.product( 
                                                  SafeSidePrice(orderBook, side, defaultValue), 
                                                  priceDistr)))
    
    r._alias = ["Generic", 'LiquidityProviderSide']
    
    return r
        

def merge_dict(d, **kwargs):
    ret = d.copy()
    for k in kwargs:
        ret[k] = kwargs[k]
    return ret


class _LiquidityProvider_Impl(Strategy):
    def __init__(self):
        Strategy.__init__(self, None)
        props = { k : getattr(self, k) for k in self._properties.iterkeys() }
        sp = merge_dict(props, side=Side.Sell)
        bp = merge_dict(props, side=Side.Buy) 
        self._sell = LiquidityProviderSide(**sp)
        self._buy = LiquidityProviderSide(**bp)

    def bind(self, context):
        context.bind(self._sell)
        context.bind(self._buy)
        
    def reset(self):
        self._sell.reset()
        self._buy.reset()
    
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

exec wrapper2('LiquidityProvider',
             """ Liquidity provider is a combination of two LiquidityProviderSide traders 
                 with the same parameters but different trading sides. 
                 
                 It has followng parameters:

                 |orderFactory| 
                     order factory function (default: order.Limit.T)
                     
                 |initialValue| 
                     initial price which is taken if orderBook is empty (default: 100)
                     
                 |creationIntervalDistr|
                     defines intervals of time between order creation 
                     (default: exponential distribution with |lambda| = 1)
                     
                 |priceDistr|
                     defines multipliers for current asset price when price of
                     order to create is calculated (default: log normal distribution with 
                     |mu| = 0 and |sigma| = 0.1)
                     
                 |volumeDistr| 
                     defines volumes of orders to create 
                     (default: exponential distribution with |lambda| = 1)
            """,  
            [('orderFactoryT',          'order.LimitFactory',                   'Side -> (Price, Volume) -> IOrder'),
             ('defaultValue',           '100',                                  'Price'),
             ('creationIntervalDistr',  'mathutils.rnd.expovariate(1.)',        '() -> TimeInterval'),
             ('priceDistr',             'mathutils.rnd.lognormvariate(0., .1)', '() -> float'),
             ('volumeDistr',            'mathutils.rnd.expovariate(.1)',        '() -> Volume')])

class _StrategyArray_Impl(Strategy):
    
    def __init__(self):
        Strategy.__init__(self, None)
            
    def bind(self, context):
        self._trader = context.trader

    def reset(self):
        for s in self.strategies:
            s.reset()
    
    def dispose(self):
        for s in self.strategies:
            s.dispose()

    def suspend(self, flag):
        Strategy.suspend(self, flag)
        for s in self.strategies:
            s.suspend(flag)

    @property
    def suspended(self):
        for s in self.strategies:
            assert s.suspended == self._suspended
        return Strategy.suspended(self)
    
exec wrapper2('StrategyArray', "", [('strategies', '[LiquidityProvider()]', 'meta.listOf(IStrategy)')])

def LiquidityProviderEx    (orderFactory            = order.LimitFactory, 
                            defaultValue            = 100., 
                            creationIntervalDistr   = mathutils.rnd.expovariate(1.), 
                            priceDistr              = mathutils.rnd.lognormvariate(0., .1), 
                            volumeDistr             = mathutils.rnd.expovariate(1.)):

    orderBook = orderbook.OfTrader()

    def create(side):
        return LiquidityProviderSideEx(side, 
                                       orderFactory, 
                                       defaultValue, 
                                       creationIntervalDistr, 
                                       priceDistr, 
                                       volumeDistr)

    r = StrategyArray([
            create(Side.Sell),
            create(Side.Buy)
        ])
    
    r._alias = ["Generic", 'LiquidityProvider']
    
    return r

class _Canceller_Impl(object):
    """ Randomly cancels created orders in specific moments of time    
    """
    
    def choiceFunc(self, N):
        return random.randint(0, N-1)

    def _wakeUp_impl(self, _):
        # if we have orders to cancel
        while self._elements <> []:
            # choose an order
            N = len(self._elements)
            idx = self.choiceFunc(N)
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
                self._book.process(order.Cancel(e))
                return

    def __init__(self):

        # orders created by trader
        self._elements = []
        self.wakeUp = bind.Method(self, '_wakeUp_impl')
    
    def bind(self, context):
        trader = context.trader
        # start listening its orders sent
        trader.on_order_sent += bind.Method(self, 'process')
        self._book = orderbook.OfTrader(trader)
        self._eventGen = scheduler.Timer(self.cancellationIntervalDistr, context.world)
        self._eventGen += self.wakeUp
        
    def dispose(self):
        self._eventGen -= self.wakeUp
        
    def reset(self):
        self._eventGen.schedule()

    def process(self, order):
        """ Puts 'order' to future cancellation list
        """
        self._elements.append(order)

exec wrapper2("Canceller",
             "",
             [('cancellationIntervalDistr', 'mathutils.rnd.expovariate(1.)',    '() -> TimeInterval')])
