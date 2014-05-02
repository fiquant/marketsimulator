def LimitSigned(price = None): 
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim.gen._out.order._curried._signedvolume_limitsigned import signedVolume_LimitSigned_Float as _order__curried_signedVolume_LimitSigned_Float
    from marketsim import rtti
    if price is None or rtti.can_be_casted(price, IFunctionfloat):
        return _order__curried_signedVolume_LimitSigned_Float(price)
    raise Exception('Cannot find suitable overload for LimitSigned('+str(price) +':'+ str(type(price))+')')
