def ImmediateOrCancel(proto = None): 
    from marketsim.gen._out._ifunction import IFunctionIObservableIOrderIFunctionSideIFunctionfloat
    from marketsim.gen._out.order._curried._sideprice_immediateorcancel import sideprice_ImmediateOrCancel_SideFloatIObservableIOrder as _order__curried_sideprice_ImmediateOrCancel_SideFloatIObservableIOrder
    from marketsim import rtti
    if proto is None or rtti.can_be_casted(proto, IFunctionIObservableIOrderIFunctionSideIFunctionfloat):
        return _order__curried_sideprice_ImmediateOrCancel_SideFloatIObservableIOrder(proto)
    raise Exception('Cannot find suitable overload for ImmediateOrCancel('+str(proto) +':'+ str(type(proto))+')')
