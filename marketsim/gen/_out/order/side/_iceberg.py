def Iceberg(proto = None,lotSize = None): 
    from marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionside import IFunctionIObservableIOrder_from_IFunctionSide
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim.gen._out.order._curried._side_iceberg import side_Iceberg_SideIObservableIOrderFloat as _order__curried_side_Iceberg_SideIObservableIOrderFloat
    from marketsim import rtti
    if proto is None or rtti.can_be_casted(proto, IFunctionIObservableIOrder_from_IFunctionSide):
        if lotSize is None or rtti.can_be_casted(lotSize, IFunctionfloat):
            return _order__curried_side_Iceberg_SideIObservableIOrderFloat(proto,lotSize)
    raise Exception('Cannot find suitable overload for Iceberg('+str(proto) +':'+ str(type(proto))+','+str(lotSize) +':'+ str(type(lotSize))+')')
