def StopLoss(maxloss = None,proto = None): 
    from marketsim import IFunction
    from marketsim import rtti
    from marketsim.gen._out.order._curried._price_stoploss import price_StopLoss_IFunctionFloatFloatIOrderGenerator as _order__curried_price_StopLoss
    from marketsim import float
    from marketsim import IOrderGenerator
    if maxloss is None or rtti.can_be_casted(maxloss, IFunction[float]):
        if proto is None or rtti.can_be_casted(proto, IFunction[IOrderGenerator,IFunction[float]]):
            return _order__curried_price_StopLoss(maxloss,proto)
    raise Exception("Cannot find suitable overload")
