def Limit(signedVolume = None,price = None): 
    from marketsim import float
    from marketsim import IFunction
    from marketsim import rtti
    if signedVolume is None or rtti.can_be_casted(signedVolume, IFunction[float]):
        if price is None or rtti.can_be_casted(price, IFunction[float]):
            return LimitSigned_FloatIFunctionFloat(signedVolume,price)
    raise Exception("Cannot find suitable overload")
