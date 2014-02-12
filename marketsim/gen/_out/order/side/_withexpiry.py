def WithExpiry(expiry = None,proto = None): 
    from marketsim import IFunction
    from marketsim.gen._out.order._curried._side_withexpiry import side_WithExpiry_IFunctionFloatSideIOrderGenerator as _order__curried_side_WithExpiry_IFunctionFloatSideIOrderGenerator
    from marketsim import rtti
    from marketsim import float
    from marketsim import IOrderGenerator
    from marketsim import Side
    if expiry is None or rtti.can_be_casted(expiry, IFunction[float]):
        if proto is None or rtti.can_be_casted(proto, IFunction[IOrderGenerator,IFunction[Side]]):
            return _order__curried_side_WithExpiry_IFunctionFloatSideIOrderGenerator(expiry,proto)
    raise Exception('Cannot find suitable overload for WithExpiry('+str(expiry)+','+str(proto)+')')
