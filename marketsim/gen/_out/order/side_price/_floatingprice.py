def FloatingPrice(floatingPrice = None,proto = None): 
    from marketsim import IFunction
    from marketsim.gen._out.order._curried._sideprice_floatingprice import sideprice_FloatingPrice_IObservableFloatSideFloatIOrderGenerator as _order__curried_sideprice_FloatingPrice_IObservableFloatSideFloatIOrderGenerator
    from marketsim import rtti
    from marketsim import IObservable
    from marketsim import float
    from marketsim import IOrderGenerator
    from marketsim import Side
    if floatingPrice is None or rtti.can_be_casted(floatingPrice, IObservable[float]):
        if proto is None or rtti.can_be_casted(proto, IFunction[IFunction[IOrderGenerator,IFunction[float]],IFunction[Side]]):
            return _order__curried_sideprice_FloatingPrice_IObservableFloatSideFloatIOrderGenerator(floatingPrice,proto)
    raise Exception('Cannot find suitable overload for FloatingPrice('+str(floatingPrice)+','+str(proto)+')')
