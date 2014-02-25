def FloatingPrice(proto = None,floatingPrice = None): 
    from marketsim.gen._out._ifunction import IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat
    from marketsim.gen._out._iobservable import IObservablefloat
    from marketsim.gen._out.order._curried._sidevolume_floatingprice import sidevolume_FloatingPrice_SideFloatFloatIObservableIOrderIObservableFloat as _order__curried_sidevolume_FloatingPrice_SideFloatFloatIObservableIOrderIObservableFloat
    from marketsim import rtti
    if proto is None or rtti.can_be_casted(proto, IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat):
        if floatingPrice is None or rtti.can_be_casted(floatingPrice, IObservablefloat):
            return _order__curried_sidevolume_FloatingPrice_SideFloatFloatIObservableIOrderIObservableFloat(proto,floatingPrice)
    raise Exception('Cannot find suitable overload for FloatingPrice('+str(proto) +':'+ str(type(proto))+','+str(floatingPrice) +':'+ str(type(floatingPrice))+')')
