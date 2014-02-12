def ImmediateOrCancel(proto = None): 
    from marketsim import IFunction
    from marketsim import rtti
    from marketsim import float
    from marketsim import IOrderGenerator
    from marketsim.gen._out.order._curried._sidevolume_price_immediateorcancel import sidevolume_price_ImmediateOrCancel_SideFloatFloatIOrderGenerator as _order__curried_sidevolume_price_ImmediateOrCancel_SideFloatFloatIOrderGenerator
    from marketsim import Side
    if proto is None or rtti.can_be_casted(proto, IFunction[IFunction[IOrderGenerator,IFunction[float]],IFunction[Side]
    ,IFunction[float]]):
        return _order__curried_sidevolume_price_ImmediateOrCancel_SideFloatFloatIOrderGenerator(proto)
    raise Exception('Cannot find suitable overload for ImmediateOrCancel('+str(proto)+')')
