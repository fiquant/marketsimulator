def StopLoss(maxloss = None,proto = None): 
    from marketsim import IFunction
    from marketsim import rtti
    from marketsim import float
    from marketsim import IOrderGenerator
    from marketsim.gen._out.order._curried._volume_stoploss import volume_StopLoss_IFunctionFloatFloatIOrderGenerator as _order__curried_volume_StopLoss
    if maxloss is None or rtti.can_be_casted(maxloss, IFunction[float]):
        if proto is None or rtti.can_be_casted(proto, IFunction[IOrderGenerator,IFunction[float]]):
            return _order__curried_volume_StopLoss(maxloss,proto)
    raise Exception("Cannot find suitable overload")
