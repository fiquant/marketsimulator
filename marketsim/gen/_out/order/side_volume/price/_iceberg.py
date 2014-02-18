def Iceberg(lotSize = None,proto = None): 
    from marketsim.gen._out._ifunction import IFunctionfloat
    from marketsim.gen._out._ifunction import IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat
    from marketsim.gen._out.order._curried._sidevolume_price_iceberg import sidevolume_price_Iceberg_FloatSideFloatFloatIObservableIOrder as _order__curried_sidevolume_price_Iceberg_FloatSideFloatFloatIObservableIOrder
    from marketsim import rtti
    if lotSize is None or rtti.can_be_casted(lotSize, IFunctionfloat):
        if proto is None or rtti.can_be_casted(proto, IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat):
            return _order__curried_sidevolume_price_Iceberg_FloatSideFloatFloatIObservableIOrder(lotSize,proto)
    raise Exception('Cannot find suitable overload for Iceberg('+str(lotSize) +':'+ str(type(lotSize))+','+str(proto) +':'+ str(type(proto))+')')
