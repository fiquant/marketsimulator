def Iceberg(proto = None,lotSize = None): 
    from marketsim.gen._out._ifunction._ifunctioniobservableiorderifunctionsideifunctionfloat import IFunctionIObservableIOrderIFunctionSideIFunctionfloat
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim.gen._out.order._curried._sidevolume_iceberg import sidevolume_Iceberg_SideFloatIObservableIOrderFloat as _order__curried_sidevolume_Iceberg_SideFloatIObservableIOrderFloat
    from marketsim import rtti
    if proto is None or rtti.can_be_casted(proto, IFunctionIObservableIOrderIFunctionSideIFunctionfloat):
        if lotSize is None or rtti.can_be_casted(lotSize, IFunctionfloat):
            return _order__curried_sidevolume_Iceberg_SideFloatIObservableIOrderFloat(proto,lotSize)
    raise Exception('Cannot find suitable overload for Iceberg('+str(proto) +':'+ str(type(proto))+','+str(lotSize) +':'+ str(type(lotSize))+')')
