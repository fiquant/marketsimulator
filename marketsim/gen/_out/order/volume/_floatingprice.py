def FloatingPrice(floatingPrice = None,proto = None): 
    from marketsim import IFunction
    from marketsim import rtti
    from marketsim import IObservable
    from marketsim import float
    from marketsim import IOrderGenerator
    from marketsim.gen._out.order._curried._volume_floatingprice import volume_FloatingPrice_IObservableFloatFloatFloatIOrderGenerator as _order__curried_volume_FloatingPrice_IObservableFloatFloatFloatIOrderGenerator
    if floatingPrice is None or rtti.can_be_casted(floatingPrice, IObservable[float]):
        if proto is None or rtti.can_be_casted(proto, IFunction[IFunction[IOrderGenerator,IFunction[float]],IFunction[float]]):
            return _order__curried_volume_FloatingPrice_IObservableFloatFloatFloatIOrderGenerator(floatingPrice,proto)
    raise Exception('Cannot find suitable overload for FloatingPrice('+str(floatingPrice)+','+str(proto)+')')
