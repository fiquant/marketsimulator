def WithExpiry(expiry = None,proto = None): 
    from marketsim.gen._out._ifunction import IFunctionfloat
    from marketsim.gen._out._ifunction import IFunctionIObservableIOrderIFunctionfloat
    from marketsim.gen._out.order._curried._volume_withexpiry import volume_WithExpiry_FloatFloatIObservableIOrder as _order__curried_volume_WithExpiry_FloatFloatIObservableIOrder
    from marketsim import rtti
    if expiry is None or rtti.can_be_casted(expiry, IFunctionfloat):
        if proto is None or rtti.can_be_casted(proto, IFunctionIObservableIOrderIFunctionfloat):
            return _order__curried_volume_WithExpiry_FloatFloatIObservableIOrder(expiry,proto)
    raise Exception('Cannot find suitable overload for WithExpiry('+str(expiry) +':'+ str(type(expiry))+','+str(proto) +':'+ str(type(proto))+')')
