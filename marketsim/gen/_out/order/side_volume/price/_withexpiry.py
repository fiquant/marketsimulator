def WithExpiry(expiry = None,proto = None): 
    from marketsim import IFunction
    from marketsim import rtti
    from marketsim.gen._out.order._curried._sidevolume_price_withexpiry import sidevolume_price_WithExpiry_IFunctionFloatSideFloatFloatIOrderGenerator as _order__curried_sidevolume_price_WithExpiry_IFunctionFloatSideFloatFloatIOrderGenerator
    from marketsim import float
    from marketsim import IOrderGenerator
    from marketsim import Side
    if expiry is None or rtti.can_be_casted(expiry, IFunction[float]):
        if proto is None or rtti.can_be_casted(proto, IFunction[IFunction[IOrderGenerator,IFunction[float]],IFunction[Side]
        ,IFunction[float]]):
            return _order__curried_sidevolume_price_WithExpiry_IFunctionFloatSideFloatFloatIOrderGenerator(expiry,proto)
    raise Exception('Cannot find suitable overload for WithExpiry('+str(expiry)+','+str(proto)+')')
