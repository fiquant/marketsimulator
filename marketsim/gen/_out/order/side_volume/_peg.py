def Peg(proto = None): 
    from marketsim import IFunction
    from marketsim import rtti
    from marketsim import float
    from marketsim import IOrderGenerator
    from marketsim import Side
    from marketsim.gen._out.order._curried._sidevolume_peg import sidevolume_Peg_SideFloatFloatIOrderGenerator as _order__curried_sidevolume_Peg
    if proto is None or rtti.can_be_casted(proto, IFunction[IFunction[IOrderGenerator,IFunction[float]],IFunction[Side]
    ,IFunction[float]]):
        return _order__curried_sidevolume_Peg(proto)
    raise Exception("Cannot find suitable overload")
