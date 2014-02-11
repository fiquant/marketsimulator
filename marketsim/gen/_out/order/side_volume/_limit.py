def Limit(price = None): 
    from marketsim import IFunction
    from marketsim import float
    from marketsim.gen._out.order._curried._sidevolume_limit import sidevolume_Limit_IFunctionFloat as _order__curried_sidevolume_Limit
    from marketsim import rtti
    if price is None or rtti.can_be_casted(price, IFunction[float]):
        return _order__curried_sidevolume_Limit(price)
    raise Exception('Cannot find suitable overload for Limit('+str(price)+')')
