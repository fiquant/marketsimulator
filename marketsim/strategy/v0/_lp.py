import random
from .._basic import Strategy
from _one_side import OneSide
from .._array import Array
from _wrap import merge, wrapper2
from _lp_side import (LiquidityProviderSide)
from marketsim import (event, order, orderbook, scheduler, mathutils, defs, _,
                       types, registry, bind, meta, trader, ops)
from marketsim.types import *

def merge_dict(d, **kwargs):
    ret = d.copy()
    for k in kwargs:
        ret[k] = kwargs[k]
    return ret


class _LiquidityProvider_Impl(Strategy):
    def __init__(self):
        Strategy.__init__(self)
        props = dict([(k, getattr(self, k)) for k in self._properties.iterkeys() ])
        sp = merge_dict(props, side=Side.Sell)
        bp = merge_dict(props, side=Side.Buy) 
        self._sell = LiquidityProviderSide(**sp)
        self._buy = LiquidityProviderSide(**bp)
        event.subscribe(self._sell.on_order_created, _(self)._send, self)
        event.subscribe(self._buy.on_order_created, _(self)._send, self)
        

    _internals = ['_sell', '_buy']
        
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
