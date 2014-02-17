def Limit(side = None,price = None): 
    from marketsim import IFunction
    from marketsim import rtti
    from marketsim import float
    from marketsim import Side
    from marketsim.gen._out.order._curried._volume_limit import volume_Limit_IFunctionSideIFunctionFloat as _order__curried_volume_Limit_IFunctionSideIFunctionFloat
    if side is None or rtti.can_be_casted(side, IFunction[Side]):
        if price is None or rtti.can_be_casted(price, IFunction[float]):
            return _order__curried_volume_Limit_IFunctionSideIFunctionFloat(side,price)
    raise Exception('Cannot find suitable overload for Limit('+str(side)+','+str(price)+')')
