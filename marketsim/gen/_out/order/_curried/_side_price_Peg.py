from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import Side
from marketsim import registry
from marketsim import float
@registry.expose(["Order", "price_Peg"])
class side_price_Peg_SideFloatIOrderGenerator(IFunction[IFunction[IOrderGenerator,IFunction[float]],IFunction[Side]]):
    """ 
      A peg order is a particular case of the floating price order
      with the price better at one tick than the best price of the order queue.
      It implies that if several peg orders are sent to the same order queue
      they start to race until being matched against the counterparty orders.
    """ 
    def __init__(self, proto = None):
        from marketsim.gen._out.order._curried._side_price_limit import side_price_Limit_IFunctionFloat as _order__curried_side_price_Limit_IFunctionFloat
        from marketsim import rtti
        self.proto = proto if proto is not None else _order__curried_side_price_Limit_IFunctionFloat()
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : IFunction[IFunction[IOrderGenerator, IFunction[float]], IFunction[Side]]
    }
    def __repr__(self):
        return "price_Peg(%(proto)s)" % self.__dict__
    
    def __call__(self, side = None):
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out.order._curried._price_peg import price_Peg
        side = side if side is not None else _side_Sell_()
        proto = self.proto
        return price_Peg(proto(side))
    
def side_price_Peg(proto = None): 
    from marketsim import IFunction
    from marketsim import rtti
    from marketsim import float
    from marketsim import IOrderGenerator
    from marketsim import Side
    if proto is None or rtti.can_be_casted(proto, IFunction[IFunction[IOrderGenerator,IFunction[float]],IFunction[Side]]):
        return side_price_Peg_SideFloatIOrderGenerator(proto)
    raise Exception('Cannot find suitable overload for side_price_Peg('+str(proto)+')')
