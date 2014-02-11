def Peg(proto = None): 
    from marketsim import IFunction
    from marketsim import rtti
    from marketsim import float
    from marketsim import IOrderGenerator
    from marketsim import Side
    from marketsim.gen._out.order._curried._side_peg import side_Peg_SideFloatIOrderGenerator as _order__curried_side_Peg
    if proto is None or rtti.can_be_casted(proto, IFunction[IFunction[IOrderGenerator,IFunction[float]],IFunction[Side]]):
        return _order__curried_side_Peg(proto)
    raise Exception('Cannot find suitable overload for Peg('+str(proto)+')')
