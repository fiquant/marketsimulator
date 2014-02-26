from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionifunctioniobservableiorderifunctionfloatifunctionsideifunctionfloat import IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
@registry.expose(["Order", "price_StopLoss"])
class sidevolume_price_StopLoss_SideFloatFloatIObservableIOrderFloat(IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat):
    """ 
      StopLoss order is initialised by an underlying order and a maximal acceptable loss factor.
      It keeps track of position and balance change induced by trades of the underlying order and
      if losses from keeping the position exceed certain limit (given by maximum loss factor),
      the meta order clears its position.
    """ 
    def __init__(self, proto = None, maxloss = None):
        from marketsim.gen._out.order._curried._sidevolume_price_limit import sidevolume_price_Limit_ as _order__curried_sidevolume_price_Limit_
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import rtti
        self.proto = proto if proto is not None else _order__curried_sidevolume_price_Limit_()
        self.maxloss = maxloss if maxloss is not None else _constant_Float(0.1)
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat,
        'maxloss' : IFunctionfloat
    }
    def __repr__(self):
        return "price_StopLoss(%(proto)s, %(maxloss)s)" % self.__dict__
    
    def __call__(self, side = None,volume = None):
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.order._curried._price_stoploss import price_StopLoss
        side = side if side is not None else _side_Sell_()
        volume = volume if volume is not None else _constant_Float(1.0)
        proto = self.proto
        maxloss = self.maxloss
        return price_StopLoss(proto(side,volume), maxloss)
    
def sidevolume_price_StopLoss(proto = None,maxloss = None): 
    from marketsim.gen._out._ifunction._ifunctionifunctioniobservableiorderifunctionfloatifunctionsideifunctionfloat import IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim import rtti
    if proto is None or rtti.can_be_casted(proto, IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat):
        if maxloss is None or rtti.can_be_casted(maxloss, IFunctionfloat):
            return sidevolume_price_StopLoss_SideFloatFloatIObservableIOrderFloat(proto,maxloss)
    raise Exception('Cannot find suitable overload for sidevolume_price_StopLoss('+str(proto) +':'+ str(type(proto))+','+str(maxloss) +':'+ str(type(maxloss))+')')
