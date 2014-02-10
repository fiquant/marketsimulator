def FloatingPrice(floatingPrice = None,proto = None): 
    from marketsim import IFunction
    from marketsim import rtti
    from marketsim import IObservable
    from marketsim import float
    from marketsim import IOrderGenerator
    from marketsim.gen._out.order._curried._sidevolume_price_floatingprice import sidevolume_price_FloatingPrice_IObservableFloatSideFloatFloatIOrderGenerator as _order__curried_sidevolume_price_FloatingPrice
    from marketsim import Side
    if floatingPrice is None or rtti.can_be_casted(floatingPrice, IObservable[float]):
        if proto is None or rtti.can_be_casted(proto, IFunction[IFunction[IOrderGenerator,IFunction[float]],IFunction[Side]
        ,IFunction[float]]):
            return _order__curried_sidevolume_price_FloatingPrice(floatingPrice,proto)
    raise Exception("Cannot find suitable overload")
