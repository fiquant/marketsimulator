def WithExpiry(expiry = None,proto = None): 
    from marketsim import IFunction
    from marketsim.gen._out.order._curried._price_withexpiry import price_WithExpiry_IFunctionFloatFloatIOrderGenerator as _order__curried_price_WithExpiry_IFunctionFloatFloatIOrderGenerator
    from marketsim import rtti
    from marketsim import float
    from marketsim import IOrderGenerator
    if expiry is None or rtti.can_be_casted(expiry, IFunction[float]):
        if proto is None or rtti.can_be_casted(proto, IFunction[IOrderGenerator,IFunction[float]]):
            return _order__curried_price_WithExpiry_IFunctionFloatFloatIOrderGenerator(expiry,proto)
    raise Exception('Cannot find suitable overload for WithExpiry('+str(expiry)+','+str(proto)+')')
