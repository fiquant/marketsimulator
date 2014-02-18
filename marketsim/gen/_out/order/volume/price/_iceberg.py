def Iceberg(lotSize = None,proto = None): 
    from marketsim.gen._out._ifunction import IFunctionfloat
    from marketsim.gen._out._ifunction import IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat
    from marketsim.gen._out.order._curried._volume_price_iceberg import volume_price_Iceberg_FloatFloatFloatIObservableIOrder as _order__curried_volume_price_Iceberg_FloatFloatFloatIObservableIOrder
    from marketsim import rtti
    if lotSize is None or rtti.can_be_casted(lotSize, IFunctionfloat):
        if proto is None or rtti.can_be_casted(proto, IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat):
            return _order__curried_volume_price_Iceberg_FloatFloatFloatIObservableIOrder(lotSize,proto)
    raise Exception('Cannot find suitable overload for Iceberg('+str(lotSize) +':'+ str(type(lotSize))+','+str(proto) +':'+ str(type(proto))+')')
