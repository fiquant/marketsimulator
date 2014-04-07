def Limit(price = None,volume = None): 
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim.gen._out.order._curried._side_limit import side_Limit_FloatFloat as _order__curried_side_Limit_FloatFloat
    from marketsim import rtti
    if price is None or rtti.can_be_casted(price, IFunctionfloat):
        if volume is None or rtti.can_be_casted(volume, IFunctionfloat):
            return _order__curried_side_Limit_FloatFloat(price,volume)
    raise Exception('Cannot find suitable overload for Limit('+str(price) +':'+ str(type(price))+','+str(volume) +':'+ str(type(volume))+')')
