def WithExpiry(proto = None,expiry = None): 
    from marketsim.gen._out._ifunction._ifunctionifunctioniobservableiorderifunctionfloatifunctionfloat import IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim.gen._out.order._curried._volume_price_withexpiry import volume_price_WithExpiry_FloatFloatIObservableIOrderFloat as _order__curried_volume_price_WithExpiry_FloatFloatIObservableIOrderFloat
    from marketsim import rtti
    if proto is None or rtti.can_be_casted(proto, IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat):
        if expiry is None or rtti.can_be_casted(expiry, IFunctionfloat):
            return _order__curried_volume_price_WithExpiry_FloatFloatIObservableIOrderFloat(proto,expiry)
    raise Exception('Cannot find suitable overload for WithExpiry('+str(proto) +':'+ str(type(proto))+','+str(expiry) +':'+ str(type(expiry))+')')
