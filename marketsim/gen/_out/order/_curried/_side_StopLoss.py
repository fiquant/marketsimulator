from marketsim import registry
from marketsim.gen._out._ifunction._ifunctioniobservableiorderifunctionside import IFunctionIObservableIOrderIFunctionSide
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
@registry.expose(["Order", "StopLoss"])
class side_StopLoss_SideIObservableIOrderFloat(IFunctionIObservableIOrderIFunctionSide):
    """ 
      StopLoss order is initialised by an underlying order and a maximal acceptable loss factor.
      It keeps track of position and balance change induced by trades of the underlying order and
      if losses from keeping the position exceed certain limit (given by maximum loss factor),
      the meta order clears its position.
    """ 
    def __init__(self, proto = None, maxloss = None):
        from marketsim.gen._out.order._curried._side_limit import side_Limit_FloatFloat as _order__curried_side_Limit_FloatFloat
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import rtti
        self.proto = proto if proto is not None else _order__curried_side_Limit_FloatFloat()
        self.maxloss = maxloss if maxloss is not None else _constant_Float(0.1)
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : IFunctionIObservableIOrderIFunctionSide,
        'maxloss' : IFunctionfloat
    }
    def __repr__(self):
        return "StopLoss(%(proto)s, %(maxloss)s)" % self.__dict__
    
    def __call__(self, side = None):
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out.order._stoploss import StopLoss
        side = side if side is not None else _side_Sell_()
        proto = self.proto
        maxloss = self.maxloss
        return StopLoss(proto(side), maxloss)
    
def side_StopLoss(proto = None,maxloss = None): 
    from marketsim.gen._out._ifunction._ifunctioniobservableiorderifunctionside import IFunctionIObservableIOrderIFunctionSide
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim import rtti
    if proto is None or rtti.can_be_casted(proto, IFunctionIObservableIOrderIFunctionSide):
        if maxloss is None or rtti.can_be_casted(maxloss, IFunctionfloat):
            return side_StopLoss_SideIObservableIOrderFloat(proto,maxloss)
    raise Exception('Cannot find suitable overload for side_StopLoss('+str(proto) +':'+ str(type(proto))+','+str(maxloss) +':'+ str(type(maxloss))+')')
