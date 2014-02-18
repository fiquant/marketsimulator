def Limit(side = None,volume = None): 
    from marketsim.gen._out._ifunction import IFunctionSide
    from marketsim.gen._out._ifunction import IFunctionfloat
    from marketsim.gen._out.order._curried._price_limit import price_Limit_SideFloat as _order__curried_price_Limit_SideFloat
    from marketsim import rtti
    if side is None or rtti.can_be_casted(side, IFunctionSide):
        if volume is None or rtti.can_be_casted(volume, IFunctionfloat):
            return _order__curried_price_Limit_SideFloat(side,volume)
    raise Exception('Cannot find suitable overload for Limit('+str(side) +':'+ str(type(side))+','+str(volume) +':'+ str(type(volume))+')')
