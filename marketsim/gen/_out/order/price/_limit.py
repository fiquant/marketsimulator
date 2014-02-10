def Limit(side = None,volume = None): 
    from marketsim import IFunction
    from marketsim import rtti
    from marketsim import float
    from marketsim import Side
    from marketsim.gen._out.order._curried._price_limit import price_Limit_SideIFunctionFloat as _order__curried_price_Limit
    if side is None or rtti.can_be_casted(side, IFunction[Side]):
        if volume is None or rtti.can_be_casted(volume, IFunction[float]):
            return _order__curried_price_Limit(side,volume)
    raise Exception("Cannot find suitable overload")
