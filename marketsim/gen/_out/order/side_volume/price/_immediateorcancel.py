def ImmediateOrCancel(proto = None): 
    from marketsim.gen._out._ifunction._ifunctionifunctioniobservableiorder_from_ifunctionfloat_from_ifunctionsideifunctionfloat import IFunctionIFunctionIObservableIOrder_from_IFunctionfloat_from_IFunctionSideIFunctionfloat
    from marketsim.gen._out.order._curried._sidevolume_price_immediateorcancel import sidevolume_price_ImmediateOrCancel_SideFloatFloatIObservableIOrder as _order__curried_sidevolume_price_ImmediateOrCancel_SideFloatFloatIObservableIOrder
    from marketsim import rtti
    if proto is None or rtti.can_be_casted(proto, IFunctionIFunctionIObservableIOrder_from_IFunctionfloat_from_IFunctionSideIFunctionfloat):
        return _order__curried_sidevolume_price_ImmediateOrCancel_SideFloatFloatIObservableIOrder(proto)
    raise Exception('Cannot find suitable overload for ImmediateOrCancel('+str(proto) +':'+ str(type(proto))+')')
