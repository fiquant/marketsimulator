def ImmediateOrCancel(proto = None): 
    from marketsim.gen._out._ifunction._ifunctioniobservableiorderifunctionfloat import IFunctionIObservableIOrderIFunctionfloat
    from marketsim.gen._out.order._curried._price_immediateorcancel import price_ImmediateOrCancel_FloatIObservableIOrder as _order__curried_price_ImmediateOrCancel_FloatIObservableIOrder
    from marketsim import rtti
    if proto is None or rtti.can_be_casted(proto, IFunctionIObservableIOrderIFunctionfloat):
        return _order__curried_price_ImmediateOrCancel_FloatIObservableIOrder(proto)
    raise Exception('Cannot find suitable overload for ImmediateOrCancel('+str(proto) +':'+ str(type(proto))+')')
