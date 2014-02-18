def ImmediateOrCancel(proto = None): 
    from marketsim.gen._out._ifunction import IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide
    from marketsim.gen._out.order._curried._side_price_immediateorcancel import side_price_ImmediateOrCancel_SideFloatIObservableIOrder as _order__curried_side_price_ImmediateOrCancel_SideFloatIObservableIOrder
    from marketsim import rtti
    if proto is None or rtti.can_be_casted(proto, IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide):
        return _order__curried_side_price_ImmediateOrCancel_SideFloatIObservableIOrder(proto)
    raise Exception('Cannot find suitable overload for ImmediateOrCancel('+str(proto) +':'+ str(type(proto))+')')
