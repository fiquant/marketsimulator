def Peg(proto = None): 
    from marketsim import IFunction
    from marketsim import rtti
    from marketsim import float
    from marketsim import IOrderGenerator
    from marketsim.gen._out.order._curried._price_peg import price_Peg_FloatIOrderGenerator as _order__curried_price_Peg_FloatIOrderGenerator
    if proto is None or rtti.can_be_casted(proto, IFunction[IOrderGenerator,IFunction[float]]):
        return _order__curried_price_Peg_FloatIOrderGenerator(proto)
    raise Exception('Cannot find suitable overload for Peg('+str(proto)+')')
