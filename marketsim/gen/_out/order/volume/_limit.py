def Limit(side = None,price = None): 
    from marketsim import IFunction
    from marketsim import rtti
    from marketsim.gen._out.order._curried._volume_limit import volume_Limit_SideIFunctionFloat as _order__curried_volume_Limit
    from marketsim import float
    from marketsim import Side
    if side is None or rtti.can_be_casted(side, IFunction[Side]):
        if price is None or rtti.can_be_casted(price, IFunction[float]):
            return _order__curried_volume_Limit(side,price)
    raise Exception("Cannot find suitable overload")
