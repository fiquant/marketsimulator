from marketsim import (trader, Side, event, order, orderbook, observable, order, 
                       request, registry, types, meta, _, ops, event)

from .._basic import Strategy
from .._wrap import wrapper2

from ..side import FundamentalValue

from marketsim.gen._out.strategy.account._Real import Real as Account

@registry.expose(alias=['actually traded'])
@meta.sig((types.ISingleAssetStrategy,), types.IAccount)
def account(strategy):
    return Account(strategy)