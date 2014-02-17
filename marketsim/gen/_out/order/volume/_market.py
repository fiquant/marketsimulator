def Market(side = None): 
    from marketsim import IFunction
    from marketsim import Side
    from marketsim.gen._out.order._curried._volume_market import volume_Market_IFunctionSide as _order__curried_volume_Market_IFunctionSide
    from marketsim import rtti
    if side is None or rtti.can_be_casted(side, IFunction[Side]):
        return _order__curried_volume_Market_IFunctionSide(side)
    raise Exception('Cannot find suitable overload for Market('+str(side)+')')
