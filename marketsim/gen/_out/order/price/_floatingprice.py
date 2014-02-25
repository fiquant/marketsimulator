def FloatingPrice(proto = None,floatingPrice = None): 
    from marketsim.gen._out._ifunction import IFunctionIObservableIOrderIFunctionfloat
    from marketsim.gen._out._iobservable import IObservablefloat
    from marketsim.gen._out.order._curried._price_floatingprice import price_FloatingPrice_FloatIObservableIOrderIObservableFloat as _order__curried_price_FloatingPrice_FloatIObservableIOrderIObservableFloat
    from marketsim import rtti
    if proto is None or rtti.can_be_casted(proto, IFunctionIObservableIOrderIFunctionfloat):
        if floatingPrice is None or rtti.can_be_casted(floatingPrice, IObservablefloat):
            return _order__curried_price_FloatingPrice_FloatIObservableIOrderIObservableFloat(proto,floatingPrice)
    raise Exception('Cannot find suitable overload for FloatingPrice('+str(proto) +':'+ str(type(proto))+','+str(floatingPrice) +':'+ str(type(floatingPrice))+')')
