def StopLoss(maxloss = None,proto = None): 
    from marketsim import IFunction
    from marketsim import rtti
    from marketsim.gen._out.order._curried._sideprice_stoploss import sideprice_StopLoss_IFunctionFloatSideFloatIOrderGenerator as _order__curried_sideprice_StopLoss_IFunctionFloatSideFloatIOrderGenerator
    from marketsim import float
    from marketsim import IOrderGenerator
    from marketsim import Side
    if maxloss is None or rtti.can_be_casted(maxloss, IFunction[float]):
        if proto is None or rtti.can_be_casted(proto, IFunction[IOrderGenerator,IFunction[Side]
        ,IFunction[float]]):
            return _order__curried_sideprice_StopLoss_IFunctionFloatSideFloatIOrderGenerator(maxloss,proto)
    raise Exception('Cannot find suitable overload for StopLoss('+str(maxloss)+','+str(proto)+')')
