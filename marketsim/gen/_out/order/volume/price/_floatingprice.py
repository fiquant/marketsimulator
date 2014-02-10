def FloatingPrice(floatingPrice = None,proto = None): 
    from marketsim import IFunction
    from marketsim import rtti
    from marketsim.gen._out.order._curried._volume_price_floatingprice import volume_price_FloatingPrice_IObservableFloatFloatFloatIOrderGenerator as _order__curried_volume_price_FloatingPrice
    from marketsim import IObservable
    from marketsim import float
    from marketsim import IOrderGenerator
    if floatingPrice is None or rtti.can_be_casted(floatingPrice, IObservable[float]):
        if proto is None or rtti.can_be_casted(proto, IFunction[IFunction[IOrderGenerator,IFunction[float]],IFunction[float]]):
            return _order__curried_volume_price_FloatingPrice(floatingPrice,proto)
    raise Exception("Cannot find suitable overload")
