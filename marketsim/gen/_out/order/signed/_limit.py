def Limit(signedVolume = None,price = None): 
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim.gen._out.order._limitsigned import LimitSigned_FloatFloat as _order_LimitSigned_FloatFloat
    from marketsim import rtti
    if signedVolume is None or rtti.can_be_casted(signedVolume, IFunctionfloat):
        if price is None or rtti.can_be_casted(price, IFunctionfloat):
            return _order_LimitSigned_FloatFloat(signedVolume,price)
    raise Exception('Cannot find suitable overload for Limit('+str(signedVolume) +':'+ str(type(signedVolume))+','+str(price) +':'+ str(type(price))+')')
