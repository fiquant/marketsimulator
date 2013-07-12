from marketsim import _, defs, ops, order, orderbook, observable, registry

from _desired_position import DesiredPosition
    
@registry.expose(['Desired position', 'Bollinger linear'])
def Bollinger_linear(alpha                   = 0.15,
                     k                       = ops.constant(0.5),
                     orderFactory            = order.MarketFactory):
    
    thisBook = orderbook.OfTrader()
    
    return defs(DesiredPosition(
                        orderFactory = orderFactory, 
                        desiredPosition = observable.IndicatorBase(_.price, 
                                            ops.Sub(_.price, _.mean) / _.stddev * k)), 
                { 'price' : observable.MidPrice(thisBook),
                  'mean'  : observable.EWMA(_.price, alpha), 
                  'stddev': observable.StdDevEW(_.price, alpha) })
