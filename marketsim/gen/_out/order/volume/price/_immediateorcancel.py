def ImmediateOrCancel(proto = None): 
    from marketsim.gen._out._ifunction._ifunctionifunctioniobservableiorderifunctionfloatifunctionfloat import IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat
    from marketsim.gen._out.order._curried._volume_price_immediateorcancel import volume_price_ImmediateOrCancel_FloatFloatIObservableIOrder as _order__curried_volume_price_ImmediateOrCancel_FloatFloatIObservableIOrder
    from marketsim import rtti
    if proto is None or rtti.can_be_casted(proto, IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat):
        return _order__curried_volume_price_ImmediateOrCancel_FloatFloatIObservableIOrder(proto)
    raise Exception('Cannot find suitable overload for ImmediateOrCancel('+str(proto) +':'+ str(type(proto))+')')
