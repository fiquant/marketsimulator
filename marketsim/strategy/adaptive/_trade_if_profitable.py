from marketsim import (trader, Event, order, orderbook, scheduler, observable, order, 
                       request, registry, types, meta, _, ops, event)

from marketsim.types import *

from .._basic import Strategy
from .._wrap import wrapper2

from .. import v0
from ..side import FundamentalValue
from _suspendable import Suspendable
from _virtual_market import VirtualMarket
import weight

class TradeIfProfitable(types.ISingleAssetStrategy):
    
    def getImpl(self):
        efficiency = self.evaluator(VirtualMarket(self.inner))
        return Suspendable(self.inner, efficiency >= 0)
    
from .. import _wrap

_wrap.strategy(TradeIfProfitable, ['Adaptive', 'Trade-if-profitable'], 
             """ 
             """,
             [
              ('inner', 'FundamentalValue()', 'ISingleAssetStrategy'),
              ('evaluator', 'weight.efficiencyTrend', 'types.IAccount -> types.IFunction[float]')
             ], 
             globals())
