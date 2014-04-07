def Limit(volume = None): 
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim.gen._out.order._curried._side_price_limit import side_price_Limit_Float as _order__curried_side_price_Limit_Float
    from marketsim import rtti
    if volume is None or rtti.can_be_casted(volume, IFunctionfloat):
        return _order__curried_side_price_Limit_Float(volume)
    raise Exception('Cannot find suitable overload for Limit('+str(volume) +':'+ str(type(volume))+')')
