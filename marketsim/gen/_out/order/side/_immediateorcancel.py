def ImmediateOrCancel(proto = None): 
    from marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionside import IFunctionIObservableIOrder_from_IFunctionSide
    from marketsim.gen._out.order._curried._side_immediateorcancel import side_ImmediateOrCancel_SideIObservableIOrder as _order__curried_side_ImmediateOrCancel_SideIObservableIOrder
    from marketsim import rtti
    if proto is None or rtti.can_be_casted(proto, IFunctionIObservableIOrder_from_IFunctionSide):
        return _order__curried_side_ImmediateOrCancel_SideIObservableIOrder(proto)
    raise Exception('Cannot find suitable overload for ImmediateOrCancel('+str(proto) +':'+ str(type(proto))+')')
