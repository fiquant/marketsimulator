def Limit(volume = None): 
    from marketsim import IFunction
    from marketsim import float
    from marketsim.gen._out.order._curried._side_price_limit import side_price_Limit_IFunctionFloat as _order__curried_side_price_Limit
    from marketsim import rtti
    if volume is None or rtti.can_be_casted(volume, IFunction[float]):
        return _order__curried_side_price_Limit(volume)
    raise Exception("Cannot find suitable overload")
