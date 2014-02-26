def Market(side = None): 
    from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
    from marketsim.gen._out.order._curried._volume_market import volume_Market_Side as _order__curried_volume_Market_Side
    from marketsim import rtti
    if side is None or rtti.can_be_casted(side, IFunctionSide):
        return _order__curried_volume_Market_Side(side)
    raise Exception('Cannot find suitable overload for Market('+str(side) +':'+ str(type(side))+')')
