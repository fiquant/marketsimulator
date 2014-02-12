def ImmediateOrCancel(proto = None): 
    from marketsim import IFunction
    from marketsim import rtti
    from marketsim import float
    from marketsim import IOrderGenerator
    from marketsim.gen._out.order._curried._side_price_immediateorcancel import side_price_ImmediateOrCancel_SideFloatIOrderGenerator as _order__curried_side_price_ImmediateOrCancel_SideFloatIOrderGenerator
    from marketsim import Side
    if proto is None or rtti.can_be_casted(proto, IFunction[IFunction[IOrderGenerator,IFunction[float]],IFunction[Side]]):
        return _order__curried_side_price_ImmediateOrCancel_SideFloatIOrderGenerator(proto)
    raise Exception('Cannot find suitable overload for ImmediateOrCancel('+str(proto)+')')
