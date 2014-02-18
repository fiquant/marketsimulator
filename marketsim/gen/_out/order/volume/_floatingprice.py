def FloatingPrice(floatingPrice = None,proto = None): 
    from marketsim.gen._out._iobservable import IObservablefloat
    from marketsim.gen._out._ifunction import IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat
    from marketsim.gen._out.order._curried._volume_floatingprice import volume_FloatingPrice_IObservableFloatFloatFloatIObservableIOrder as _order__curried_volume_FloatingPrice_IObservableFloatFloatFloatIObservableIOrder
    from marketsim import rtti
    if floatingPrice is None or rtti.can_be_casted(floatingPrice, IObservablefloat):
        if proto is None or rtti.can_be_casted(proto, IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat):
            return _order__curried_volume_FloatingPrice_IObservableFloatFloatFloatIObservableIOrder(floatingPrice,proto)
    raise Exception('Cannot find suitable overload for FloatingPrice('+str(floatingPrice) +':'+ str(type(floatingPrice))+','+str(proto) +':'+ str(type(proto))+')')
