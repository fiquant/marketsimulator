def WithExpiry(expiry = None,proto = None): 
    from marketsim.gen._out._ifunction import IFunctionfloat
    from marketsim.gen._out._ifunction import IFunctionIObservableIOrderIFunctionSide
    from marketsim.gen._out.order._curried._side_withexpiry import side_WithExpiry_FloatSideIObservableIOrder as _order__curried_side_WithExpiry_FloatSideIObservableIOrder
    from marketsim import rtti
    if expiry is None or rtti.can_be_casted(expiry, IFunctionfloat):
        if proto is None or rtti.can_be_casted(proto, IFunctionIObservableIOrderIFunctionSide):
            return _order__curried_side_WithExpiry_FloatSideIObservableIOrder(expiry,proto)
    raise Exception('Cannot find suitable overload for WithExpiry('+str(expiry) +':'+ str(type(expiry))+','+str(proto) +':'+ str(type(proto))+')')
