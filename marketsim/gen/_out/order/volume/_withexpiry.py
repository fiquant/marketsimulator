def WithExpiry(expiry = None,proto = None): 
    from marketsim.gen._out.order._curried._volume_withexpiry import volume_WithExpiry_IFunctionFloatFloatIOrderGenerator as _order__curried_volume_WithExpiry
    from marketsim import IFunction
    from marketsim import rtti
    from marketsim import float
    from marketsim import IOrderGenerator
    if expiry is None or rtti.can_be_casted(expiry, IFunction[float]):
        if proto is None or rtti.can_be_casted(proto, IFunction[IOrderGenerator,IFunction[float]]):
            return _order__curried_volume_WithExpiry(expiry,proto)
    raise Exception('Cannot find suitable overload for WithExpiry('+str(expiry)+','+str(proto)+')')
