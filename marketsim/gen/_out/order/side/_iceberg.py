def Iceberg(lotSize = None,proto = None): 
    from marketsim.gen._out._ifunction import IFunctionfloat
    from marketsim.gen._out._ifunction import IFunctionIObservableIOrderIFunctionSide
    from marketsim.gen._out.order._curried._side_iceberg import side_Iceberg_FloatSideIObservableIOrder as _order__curried_side_Iceberg_FloatSideIObservableIOrder
    from marketsim import rtti
    if lotSize is None or rtti.can_be_casted(lotSize, IFunctionfloat):
        if proto is None or rtti.can_be_casted(proto, IFunctionIObservableIOrderIFunctionSide):
            return _order__curried_side_Iceberg_FloatSideIObservableIOrder(lotSize,proto)
    raise Exception('Cannot find suitable overload for Iceberg('+str(lotSize) +':'+ str(type(lotSize))+','+str(proto) +':'+ str(type(proto))+')')
