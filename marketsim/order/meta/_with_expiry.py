from marketsim import request, combine, meta, types, _, registry, ops, context

from .. import _limit
from marketsim.types import *

import _meta

from marketsim.gen._intrinsic.order.meta.with_expiry import Order_Impl as WithExpiry
from marketsim.gen._out.order._WithExpiry import WithExpiry as Factory
from marketsim.gen._out.order._curried._side_WithExpiry import side_WithExpiry as Side_Factory
from marketsim.gen._out.order._curried._sideprice_WithExpiry import sideprice_WithExpiry as SidePrice_Factory

LimitOrderFactorySignature = meta.function((types.Side,), meta.function((types.Price, types.Volume), types.IOrder))

@registry.expose(['WithExpiry'])
class WithExpiryFactory(object):
    """ Limit-like order which is cancelled after given *delay*
    """
    
    def __init__(self, expirationDistr=ops.constant(10)):
        self.expirationDistr = expirationDistr
        
    _types = [LimitOrderFactorySignature]
        
    _properties = {'expirationDistr'  : meta.function((), types.TimeInterval)}
    
    def create(self, side, price, volume):
        return WithExpiry(_limit.Limit(side, price, volume), 
                          self.expirationDistr())
    
    def __call__(self, side):
        return _(self, side).create
