def Limit(price = None,volume = None): 
    from marketsim import IFunction
    from marketsim import float
    from marketsim.gen._out.order._curried._side_limit import side_Limit_IFunctionFloatIFunctionFloat as _order__curried_side_Limit
    from marketsim import rtti
    if price is None or rtti.can_be_casted(price, IFunction[float]):
        if volume is None or rtti.can_be_casted(volume, IFunction[float]):
            return _order__curried_side_Limit(price,volume)
    raise Exception('Cannot find suitable overload for Limit('+str(price)+','+str(volume)+')')
