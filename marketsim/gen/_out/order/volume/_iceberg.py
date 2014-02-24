def Iceberg(proto = None,lotSize = None): 
    from marketsim.gen._out._ifunction import IFunctionIObservableIOrderIFunctionfloat
    from marketsim.gen._out._ifunction import IFunctionfloat
    from marketsim.gen._out.order._curried._volume_iceberg import volume_Iceberg_FloatIObservableIOrderFloat as _order__curried_volume_Iceberg_FloatIObservableIOrderFloat
    from marketsim import rtti
    if proto is None or rtti.can_be_casted(proto, IFunctionIObservableIOrderIFunctionfloat):
        if lotSize is None or rtti.can_be_casted(lotSize, IFunctionfloat):
            return _order__curried_volume_Iceberg_FloatIObservableIOrderFloat(proto,lotSize)
    raise Exception('Cannot find suitable overload for Iceberg('+str(proto) +':'+ str(type(proto))+','+str(lotSize) +':'+ str(type(lotSize))+')')
