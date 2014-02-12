def FloatingPrice(floatingPrice = None,proto = None): 
    from marketsim import IFunction
    from marketsim import rtti
    from marketsim import IObservable
    from marketsim import float
    from marketsim import IOrderGenerator
    from marketsim import Side
    from marketsim.gen._out.order._curried._sidevolume_floatingprice import sidevolume_FloatingPrice_IObservableFloatSideFloatFloatIOrderGenerator as _order__curried_sidevolume_FloatingPrice_IObservableFloatSideFloatFloatIOrderGenerator
    if floatingPrice is None or rtti.can_be_casted(floatingPrice, IObservable[float]):
        if proto is None or rtti.can_be_casted(proto, IFunction[IFunction[IOrderGenerator,IFunction[float]],IFunction[Side]
        ,IFunction[float]]):
            return _order__curried_sidevolume_FloatingPrice_IObservableFloatSideFloatFloatIOrderGenerator(floatingPrice,proto)
    raise Exception('Cannot find suitable overload for FloatingPrice('+str(floatingPrice)+','+str(proto)+')')
