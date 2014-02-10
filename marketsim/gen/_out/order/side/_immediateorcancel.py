def ImmediateOrCancel(proto = None): 
    from marketsim import IFunction
    from marketsim import rtti
    from marketsim import IOrderGenerator
    from marketsim import Side
    from marketsim.gen._out.order._curried._side_immediateorcancel import side_ImmediateOrCancel_SideIOrderGenerator as _order__curried_side_ImmediateOrCancel
    if proto is None or rtti.can_be_casted(proto, IFunction[IOrderGenerator,IFunction[Side]]):
        return _order__curried_side_ImmediateOrCancel(proto)
    raise Exception("Cannot find suitable overload")
