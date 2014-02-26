def ImmediateOrCancel(proto = None): 
    from marketsim.gen._out._ifunction._ifunctioniobservableiorderifunctionsideifunctionfloat import IFunctionIObservableIOrderIFunctionSideIFunctionfloat
    from marketsim.gen._out.order._curried._sidevolume_immediateorcancel import sidevolume_ImmediateOrCancel_SideFloatIObservableIOrder as _order__curried_sidevolume_ImmediateOrCancel_SideFloatIObservableIOrder
    from marketsim import rtti
    if proto is None or rtti.can_be_casted(proto, IFunctionIObservableIOrderIFunctionSideIFunctionfloat):
        return _order__curried_sidevolume_ImmediateOrCancel_SideFloatIObservableIOrder(proto)
    raise Exception('Cannot find suitable overload for ImmediateOrCancel('+str(proto) +':'+ str(type(proto))+')')
