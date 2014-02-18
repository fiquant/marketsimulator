def Limit(side = None,price = None): 
    from marketsim.gen._out._ifunction import IFunctionSide
    from marketsim.gen._out._ifunction import IFunctionfloat
    from marketsim.gen._out.order._curried._volume_limit import volume_Limit_SideFloat as _order__curried_volume_Limit_SideFloat
    from marketsim import rtti
    if side is None or rtti.can_be_casted(side, IFunctionSide):
        if price is None or rtti.can_be_casted(price, IFunctionfloat):
            return _order__curried_volume_Limit_SideFloat(side,price)
    raise Exception('Cannot find suitable overload for Limit('+str(side) +':'+ str(type(side))+','+str(price) +':'+ str(type(price))+')')
