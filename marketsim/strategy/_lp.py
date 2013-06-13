import random
from _basic import Strategy
from _one_side import OneSide
from _generic import Generic
from _array import Array
from _wrap import merge, wrapper, wrapper2
from _lp_side import LiquidityProviderSide, LiquidityProviderSideEx
from marketsim import order, orderbook, scheduler, mathutils, types, registry, bind, meta, trader
from marketsim.types import *

def merge_dict(d, **kwargs):
    ret = d.copy()
    for k in kwargs:
        ret[k] = kwargs[k]
    return ret


class _LiquidityProvider_Impl(Strategy):
    def __init__(self):
        Strategy.__init__(self)
        props = { k : getattr(self, k) for k in self._properties.iterkeys() }
        sp = merge_dict(props, side=Side.Sell)
        bp = merge_dict(props, side=Side.Buy) 
        self._sell = LiquidityProviderSide(**sp)
        self._buy = LiquidityProviderSide(**bp)

    _internals = ['_sell', '_buy']
        
        
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


@registry.expose(["Generic", 'LiquidityProvider'], args = ())
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

    r = Array([
            create(Side.Sell),
            create(Side.Buy)
        ])
    
    return r

