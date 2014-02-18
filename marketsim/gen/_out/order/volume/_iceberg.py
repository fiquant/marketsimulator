def Iceberg(lotSize = None,proto = None): 
    from marketsim.gen._out._ifunction import IFunctionfloat
    from marketsim.gen._out._ifunction import IFunctionIObservableIOrderIFunctionfloat
    from marketsim.gen._out.order._curried._volume_iceberg import volume_Iceberg_FloatFloatIObservableIOrder as _order__curried_volume_Iceberg_FloatFloatIObservableIOrder
    from marketsim import rtti
    if lotSize is None or rtti.can_be_casted(lotSize, IFunctionfloat):
        if proto is None or rtti.can_be_casted(proto, IFunctionIObservableIOrderIFunctionfloat):
            return _order__curried_volume_Iceberg_FloatFloatIObservableIOrder(lotSize,proto)
    raise Exception('Cannot find suitable overload for Iceberg('+str(lotSize) +':'+ str(type(lotSize))+','+str(proto) +':'+ str(type(proto))+')')
