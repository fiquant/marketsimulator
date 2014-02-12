def ImmediateOrCancel(proto = None): 
    from marketsim import IFunction
    from marketsim import rtti
    from marketsim import IOrderGenerator
    from marketsim.gen._out.order._curried._side_immediateorcancel import side_ImmediateOrCancel_SideIOrderGenerator as _order__curried_side_ImmediateOrCancel_SideIOrderGenerator
    from marketsim import Side
    if proto is None or rtti.can_be_casted(proto, IFunction[IOrderGenerator,IFunction[Side]]):
        return _order__curried_side_ImmediateOrCancel_SideIOrderGenerator(proto)
    raise Exception('Cannot find suitable overload for ImmediateOrCancel('+str(proto)+')')
