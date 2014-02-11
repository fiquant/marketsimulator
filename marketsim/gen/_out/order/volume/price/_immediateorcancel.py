def ImmediateOrCancel(proto = None): 
    from marketsim import IFunction
    from marketsim import rtti
    from marketsim import float
    from marketsim import IOrderGenerator
    from marketsim.gen._out.order._curried._volume_price_immediateorcancel import volume_price_ImmediateOrCancel_FloatFloatIOrderGenerator as _order__curried_volume_price_ImmediateOrCancel
    if proto is None or rtti.can_be_casted(proto, IFunction[IFunction[IOrderGenerator,IFunction[float]],IFunction[float]]):
        return _order__curried_volume_price_ImmediateOrCancel(proto)
    raise Exception('Cannot find suitable overload for ImmediateOrCancel('+str(proto)+')')
