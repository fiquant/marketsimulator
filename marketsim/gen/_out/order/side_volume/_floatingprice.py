def FloatingPrice(floatingPrice = None,proto = None): 
    from marketsim.gen._out._iobservable import IObservablefloat
    from marketsim.gen._out._ifunction import IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat
    from marketsim.gen._out.order._curried._sidevolume_floatingprice import sidevolume_FloatingPrice_IObservableFloatSideFloatFloatIObservableIOrder as _order__curried_sidevolume_FloatingPrice_IObservableFloatSideFloatFloatIObservableIOrder
    from marketsim import rtti
    if floatingPrice is None or rtti.can_be_casted(floatingPrice, IObservablefloat):
        if proto is None or rtti.can_be_casted(proto, IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat):
            return _order__curried_sidevolume_FloatingPrice_IObservableFloatSideFloatFloatIObservableIOrder(floatingPrice,proto)
    raise Exception('Cannot find suitable overload for FloatingPrice('+str(floatingPrice) +':'+ str(type(floatingPrice))+','+str(proto) +':'+ str(type(proto))+')')
