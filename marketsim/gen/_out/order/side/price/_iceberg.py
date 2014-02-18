def Iceberg(lotSize = None,proto = None): 
    from marketsim.gen._out._ifunction import IFunctionfloat
    from marketsim.gen._out._ifunction import IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide
    from marketsim.gen._out.order._curried._side_price_iceberg import side_price_Iceberg_FloatSideFloatIObservableIOrder as _order__curried_side_price_Iceberg_FloatSideFloatIObservableIOrder
    from marketsim import rtti
    if lotSize is None or rtti.can_be_casted(lotSize, IFunctionfloat):
        if proto is None or rtti.can_be_casted(proto, IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide):
            return _order__curried_side_price_Iceberg_FloatSideFloatIObservableIOrder(lotSize,proto)
    raise Exception('Cannot find suitable overload for Iceberg('+str(lotSize) +':'+ str(type(lotSize))+','+str(proto) +':'+ str(type(proto))+')')
