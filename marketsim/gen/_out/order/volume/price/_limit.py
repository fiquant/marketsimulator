def Limit(side = None): 
    from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
    from marketsim.gen._out.order._curried._volume_price_limit import volume_price_Limit_Side as _order__curried_volume_price_Limit_Side
    from marketsim import rtti
    if side is None or rtti.can_be_casted(side, IFunctionSide):
        return _order__curried_volume_price_Limit_Side(side)
    raise Exception('Cannot find suitable overload for Limit('+str(side) +':'+ str(type(side))+')')
