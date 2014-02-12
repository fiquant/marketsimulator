def StopLoss(maxloss = None,proto = None): 
    from marketsim import IFunction
    from marketsim import rtti
    from marketsim import float
    from marketsim import IOrderGenerator
    from marketsim.gen._out.order._curried._side_stoploss import side_StopLoss_IFunctionFloatSideIOrderGenerator as _order__curried_side_StopLoss_IFunctionFloatSideIOrderGenerator
    from marketsim import Side
    if maxloss is None or rtti.can_be_casted(maxloss, IFunction[float]):
        if proto is None or rtti.can_be_casted(proto, IFunction[IOrderGenerator,IFunction[Side]]):
            return _order__curried_side_StopLoss_IFunctionFloatSideIOrderGenerator(maxloss,proto)
    raise Exception('Cannot find suitable overload for StopLoss('+str(maxloss)+','+str(proto)+')')
