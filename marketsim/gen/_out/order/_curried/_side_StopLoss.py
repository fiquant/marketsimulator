from marketsim import registry
from marketsim.gen._out._ifunction import IFunctionIObservableIOrderIFunctionSide
from marketsim.gen._out._ifunction import IFunctionfloat
@registry.expose(["Order", "StopLoss"])
class side_StopLoss_FloatSideIObservableIOrder(IFunctionIObservableIOrderIFunctionSide):
    """ 
      StopLoss order is initialised by an underlying order and a maximal acceptable loss factor.
      It keeps track of position and balance change induced by trades of the underlying order and
      if losses from keeping the position exceed certain limit (given by maximum loss factor),
      the meta order clears its position.
    """ 
    def __init__(self, maxloss = None, proto = None):
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.order._curried._side_limit import side_Limit_FloatFloat as _order__curried_side_Limit_FloatFloat
        from marketsim import rtti
        self.maxloss = maxloss if maxloss is not None else _constant_Float(0.1)
        self.proto = proto if proto is not None else _order__curried_side_Limit_FloatFloat()
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'maxloss' : IFunctionfloat,
        'proto' : IFunctionIObservableIOrderIFunctionSide
    }
    def __repr__(self):
        return "StopLoss(%(maxloss)s, %(proto)s)" % self.__dict__
    
    def __call__(self, side = None):
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out.order._stoploss import StopLoss
        side = side if side is not None else _side_Sell_()
        maxloss = self.maxloss
        proto = self.proto
        return StopLoss(maxloss, proto(side))
    
def side_StopLoss(maxloss = None,proto = None): 
    from marketsim.gen._out._ifunction import IFunctionfloat
    from marketsim.gen._out._ifunction import IFunctionIObservableIOrderIFunctionSide
    from marketsim import rtti
    if maxloss is None or rtti.can_be_casted(maxloss, IFunctionfloat):
        if proto is None or rtti.can_be_casted(proto, IFunctionIObservableIOrderIFunctionSide):
            return side_StopLoss_FloatSideIObservableIOrder(maxloss,proto)
    raise Exception('Cannot find suitable overload for side_StopLoss('+str(maxloss) +':'+ str(type(maxloss))+','+str(proto) +':'+ str(type(proto))+')')
