def Iceberg(proto = None,lotSize = None): 
    from marketsim.gen._out._ifunction import IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide
    from marketsim.gen._out._ifunction import IFunctionfloat
    from marketsim.gen._out.order._curried._side_price_iceberg import side_price_Iceberg_SideFloatIObservableIOrderFloat as _order__curried_side_price_Iceberg_SideFloatIObservableIOrderFloat
    from marketsim import rtti
    if proto is None or rtti.can_be_casted(proto, IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide):
        if lotSize is None or rtti.can_be_casted(lotSize, IFunctionfloat):
            return _order__curried_side_price_Iceberg_SideFloatIObservableIOrderFloat(proto,lotSize)
    raise Exception('Cannot find suitable overload for Iceberg('+str(proto) +':'+ str(type(proto))+','+str(lotSize) +':'+ str(type(lotSize))+')')
