from marketsim import _, defs, ops, order, orderbook, observable, registry, types
from marketsim.types import *

from _desired_position import DesiredPosition

import _wrap

class Bollinger_linear(types.ISingleAssetStrategy):

    def getDefinitions(self):
        return  { 'price' : observable.MidPrice(orderbook.OfTrader()),
                  'mean'  : observable.EWMA(_.price, self.alpha), 
                  'stddev': observable.StdDevEW(_.price, self.alpha) }
            
    def getImpl(self):
        return DesiredPosition(
                        orderFactory = self.orderFactory, 
                        desiredPosition = observable.IndicatorBase(_.price, 
                                            ops.Sub(_.price, _.mean) / _.stddev * self.k))
        
_wrap.strategy(Bollinger_linear, ['Desired position', 'Bollinger linear'], 
               """
               """, 
               [
                  ('alpha',        '0.15',                'non_negative'), 
                  ('k',            'ops.constant(+0.5)',  'IFunction[float]'), 
                  ('orderFactory', 'order.MarketFactory', 'Side -> Volume -> IOrder'),
               ], globals())
