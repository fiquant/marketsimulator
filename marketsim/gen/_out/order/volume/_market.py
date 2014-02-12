def Market(side = None): 
    from marketsim import Side
    from marketsim import IFunction
    from marketsim.gen._out.order._curried._volume_market import volume_Market_Side as _order__curried_volume_Market_Side
    from marketsim import rtti
    if side is None or rtti.can_be_casted(side, IFunction[Side]):
        return _order__curried_volume_Market_Side(side)
    raise Exception('Cannot find suitable overload for Market('+str(side)+')')
