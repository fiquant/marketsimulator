def Limit(signedVolume = None,price = None): 
    from marketsim import float
    from marketsim import IFunction
    from marketsim.gen._out.order._limitsigned import LimitSigned_FloatIFunctionFloat as _order_LimitSigned
    from marketsim import rtti
    if signedVolume is None or rtti.can_be_casted(signedVolume, IFunction[float]):
        if price is None or rtti.can_be_casted(price, IFunction[float]):
            return _order_LimitSigned(signedVolume,price)
    raise Exception("Cannot find suitable overload")
