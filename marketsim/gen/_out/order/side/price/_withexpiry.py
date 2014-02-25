def WithExpiry(proto = None,expiry = None): 
    from marketsim.gen._out._ifunction import IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide
    from marketsim.gen._out._ifunction import IFunctionfloat
    from marketsim.gen._out.order._curried._side_price_withexpiry import side_price_WithExpiry_SideFloatIObservableIOrderFloat as _order__curried_side_price_WithExpiry_SideFloatIObservableIOrderFloat
    from marketsim import rtti
    if proto is None or rtti.can_be_casted(proto, IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide):
        if expiry is None or rtti.can_be_casted(expiry, IFunctionfloat):
            return _order__curried_side_price_WithExpiry_SideFloatIObservableIOrderFloat(proto,expiry)
    raise Exception('Cannot find suitable overload for WithExpiry('+str(proto) +':'+ str(type(proto))+','+str(expiry) +':'+ str(type(expiry))+')')
