def ImmediateOrCancel(proto = None): 
    from marketsim.gen._out._ifunction import IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat
    from marketsim.gen._out.order._curried._sidevolume_price_immediateorcancel import sidevolume_price_ImmediateOrCancel_SideFloatFloatIObservableIOrder as _order__curried_sidevolume_price_ImmediateOrCancel_SideFloatFloatIObservableIOrder
    from marketsim import rtti
    if proto is None or rtti.can_be_casted(proto, IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat):
        return _order__curried_sidevolume_price_ImmediateOrCancel_SideFloatFloatIObservableIOrder(proto)
    raise Exception('Cannot find suitable overload for ImmediateOrCancel('+str(proto) +':'+ str(type(proto))+')')
