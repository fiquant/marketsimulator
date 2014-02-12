def WithExpiry(expiry = None,proto = None): 
    from marketsim import IFunction
    from marketsim import rtti
    from marketsim import float
    from marketsim import IOrderGenerator
    from marketsim import Side
    from marketsim.gen._out.order._curried._side_price_withexpiry import side_price_WithExpiry_IFunctionFloatSideFloatIOrderGenerator as _order__curried_side_price_WithExpiry_IFunctionFloatSideFloatIOrderGenerator
    if expiry is None or rtti.can_be_casted(expiry, IFunction[float]):
        if proto is None or rtti.can_be_casted(proto, IFunction[IFunction[IOrderGenerator,IFunction[float]],IFunction[Side]]):
            return _order__curried_side_price_WithExpiry_IFunctionFloatSideFloatIOrderGenerator(expiry,proto)
    raise Exception('Cannot find suitable overload for WithExpiry('+str(expiry)+','+str(proto)+')')
