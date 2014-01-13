from marketsim import (orderbook, event, Side, request, registry, types, meta, _, ops, event)

from .._basic import Strategy, Base
from .._wrap import wrapper2

from ..side import FundamentalValue

from marketsim.gen._out.strategy.account._VirtualMarket import VirtualMarket

@registry.expose(alias=['virtual market'])
@meta.sig((types.ISingleAssetStrategy,), types.IAccount)
def virtualMarket(strategy):
    return VirtualMarket(strategy)