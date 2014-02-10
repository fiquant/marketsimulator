def Peg(proto = None): 
    from marketsim import IFunction
    from marketsim import rtti
    from marketsim import float
    from marketsim import IOrderGenerator
    from marketsim.gen._out.order._curried._sideprice_peg import sideprice_Peg_SideFloatIOrderGenerator as _order__curried_sideprice_Peg
    from marketsim import Side
    if proto is None or rtti.can_be_casted(proto, IFunction[IFunction[IOrderGenerator,IFunction[float]],IFunction[Side]]):
        return _order__curried_sideprice_Peg(proto)
    raise Exception("Cannot find suitable overload")
