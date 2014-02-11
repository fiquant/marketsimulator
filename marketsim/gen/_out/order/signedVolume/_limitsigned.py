def LimitSigned(price = None): 
    from marketsim import IFunction
    from marketsim import float
    from marketsim.gen._out.order._curried._signedvolume_limitsigned import signedVolume_LimitSigned_IFunctionFloat as _order__curried_signedVolume_LimitSigned
    from marketsim import rtti
    if price is None or rtti.can_be_casted(price, IFunction[float]):
        return _order__curried_signedVolume_LimitSigned(price)
    raise Exception('Cannot find suitable overload for LimitSigned('+str(price)+')')
