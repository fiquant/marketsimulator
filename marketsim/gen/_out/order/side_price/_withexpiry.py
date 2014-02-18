def WithExpiry(expiry = None,proto = None): 
    from marketsim.gen._out._ifunction import IFunctionfloat
    from marketsim.gen._out._ifunction import IFunctionIObservableIOrderIFunctionSideIFunctionfloat
    from marketsim.gen._out.order._curried._sideprice_withexpiry import sideprice_WithExpiry_FloatSideFloatIObservableIOrder as _order__curried_sideprice_WithExpiry_FloatSideFloatIObservableIOrder
    from marketsim import rtti
    if expiry is None or rtti.can_be_casted(expiry, IFunctionfloat):
        if proto is None or rtti.can_be_casted(proto, IFunctionIObservableIOrderIFunctionSideIFunctionfloat):
            return _order__curried_sideprice_WithExpiry_FloatSideFloatIObservableIOrder(expiry,proto)
    raise Exception('Cannot find suitable overload for WithExpiry('+str(expiry) +':'+ str(type(expiry))+','+str(proto) +':'+ str(type(proto))+')')
