def Peg(proto = None): 
    from marketsim import IFunction
    from marketsim import rtti
    from marketsim import float
    from marketsim import IOrderGenerator
    from marketsim.gen._out.order._curried._sidevolume_price_peg import sidevolume_price_Peg_SideFloatFloatIOrderGenerator as _order__curried_sidevolume_price_Peg
    from marketsim import Side
    if proto is None or rtti.can_be_casted(proto, IFunction[IFunction[IOrderGenerator,IFunction[float]],IFunction[Side]
    ,IFunction[float]]):
        return _order__curried_sidevolume_price_Peg(proto)
    raise Exception('Cannot find suitable overload for Peg('+str(proto)+')')
