def ImmediateOrCancel(proto = None): 
    from marketsim import IFunction
    from marketsim import rtti
    from marketsim import float
    from marketsim import IOrderGenerator
    from marketsim.gen._out.order._curried._volume_immediateorcancel import volume_ImmediateOrCancel_FloatIOrderGenerator as _order__curried_volume_ImmediateOrCancel_FloatIOrderGenerator
    if proto is None or rtti.can_be_casted(proto, IFunction[IOrderGenerator,IFunction[float]]):
        return _order__curried_volume_ImmediateOrCancel_FloatIOrderGenerator(proto)
    raise Exception('Cannot find suitable overload for ImmediateOrCancel('+str(proto)+')')
