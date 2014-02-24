def Iceberg(proto = None,lotSize = None): 
    from marketsim.gen._out._ifunction import IFunctionIObservableIOrderIFunctionSide
    from marketsim.gen._out._ifunction import IFunctionfloat
    from marketsim.gen._out.order._curried._side_iceberg import side_Iceberg_SideIObservableIOrderFloat as _order__curried_side_Iceberg_SideIObservableIOrderFloat
    from marketsim import rtti
    if proto is None or rtti.can_be_casted(proto, IFunctionIObservableIOrderIFunctionSide):
        if lotSize is None or rtti.can_be_casted(lotSize, IFunctionfloat):
            return _order__curried_side_Iceberg_SideIObservableIOrderFloat(proto,lotSize)
    raise Exception('Cannot find suitable overload for Iceberg('+str(proto) +':'+ str(type(proto))+','+str(lotSize) +':'+ str(type(lotSize))+')')
