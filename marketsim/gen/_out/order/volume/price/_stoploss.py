def StopLoss(maxloss = None,proto = None): 
    from marketsim import IFunction
    from marketsim import float
    from marketsim import IOrderGenerator
    from marketsim import rtti
    if maxloss is None or rtti.can_be_casted(maxloss, IFunction[float]):
        if proto is None or rtti.can_be_casted(proto, IFunction[IFunction[IOrderGenerator,IFunction[float]],IFunction[float]]):
            return price_StopLoss_IFunctionFloatFloatIOrderGenerator(maxloss,proto)
    raise Exception("Cannot find suitable overload")
