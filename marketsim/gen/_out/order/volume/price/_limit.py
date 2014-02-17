def Limit(side = None): 
    from marketsim import IFunction
    from marketsim import Side
    from marketsim.gen._out.order._curried._volume_price_limit import volume_price_Limit_IFunctionSide as _order__curried_volume_price_Limit_IFunctionSide
    from marketsim import rtti
    if side is None or rtti.can_be_casted(side, IFunction[Side]):
        return _order__curried_volume_price_Limit_IFunctionSide(side)
    raise Exception('Cannot find suitable overload for Limit('+str(side)+')')
