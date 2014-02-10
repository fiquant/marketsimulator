def ImmediateOrCancel(proto = None): 
    from marketsim import IFunction
    from marketsim import rtti
    from marketsim import float
    from marketsim import IOrderGenerator
    from marketsim import Side
    from marketsim.gen._out.order._curried._sidevolume_price_immediateorcancel import sidevolume_price_ImmediateOrCancel_SideFloatFloatIOrderGenerator as _order__curried_sidevolume_price_ImmediateOrCancel
    if proto is None or rtti.can_be_casted(proto, IFunction[IFunction[IOrderGenerator,IFunction[float]],IFunction[Side]
    ,IFunction[float]]):
        return _order__curried_sidevolume_price_ImmediateOrCancel(proto)
    raise Exception("Cannot find suitable overload")
