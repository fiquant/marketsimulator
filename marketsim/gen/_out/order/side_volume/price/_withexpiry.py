def WithExpiry(expiry = None,proto = None): 
    from marketsim.gen._out._ifunction import IFunctionfloat
    from marketsim.gen._out._ifunction import IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat
    from marketsim.gen._out.order._curried._sidevolume_price_withexpiry import sidevolume_price_WithExpiry_FloatSideFloatFloatIObservableIOrder as _order__curried_sidevolume_price_WithExpiry_FloatSideFloatFloatIObservableIOrder
    from marketsim import rtti
    if expiry is None or rtti.can_be_casted(expiry, IFunctionfloat):
        if proto is None or rtti.can_be_casted(proto, IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat):
            return _order__curried_sidevolume_price_WithExpiry_FloatSideFloatFloatIObservableIOrder(expiry,proto)
    raise Exception('Cannot find suitable overload for WithExpiry('+str(expiry) +':'+ str(type(expiry))+','+str(proto) +':'+ str(type(proto))+')')
