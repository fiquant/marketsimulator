def Limit(volume = None): 
    from marketsim import IFunction
    from marketsim import float
    from marketsim.gen._out.order._curried._sideprice_limit import sideprice_Limit_IFunctionFloat as _order__curried_sideprice_Limit_IFunctionFloat
    from marketsim import rtti
    if volume is None or rtti.can_be_casted(volume, IFunction[float]):
        return _order__curried_sideprice_Limit_IFunctionFloat(volume)
    raise Exception('Cannot find suitable overload for Limit('+str(volume)+')')
