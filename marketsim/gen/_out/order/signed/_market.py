def Market(signedVolume = None): 
    from marketsim import float
    from marketsim import IFunction
    from marketsim import rtti
    if signedVolume is None or rtti.can_be_casted(signedVolume, IFunction[float]):
        return MarketSigned_Float(signedVolume)
    raise Exception("Cannot find suitable overload")
