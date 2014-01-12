from marketsim import event, combine, ops, registry, meta, types, bind
from marketsim.types import *
from _base import *

from marketsim.gen._intrinsic.order.market import Order_Impl as Market

Order = Market

from marketsim.gen._out.order._Market import Market as Factory
from marketsim.gen._out.order._MarketSigned import MarketSigned as FactorySigned
from marketsim.gen._out.order._curried._side_Market import side_Market as Side_Factory
from marketsim.gen._out.order._curried._volume_Market import volume_Market as Volume_Factory

@registry.expose(['Market'])
@sig((IFunction[SignedVolume],), IOrderGenerator)
class SignedVolume_Factory(object):
    
    def __call__(self, signedVolume):
        return FactorySigned(signedVolume)


@registry.expose(alias=['Market'])
@sig(args=(Side,), rv=function((Volume,), IOrder))
def MarketFactory(side):
    return bind.Construct(Market, side)
    
MarketFactory.__doc__ = Market.__doc__