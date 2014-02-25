def FloatingPrice(proto = None,floatingPrice = None): 
    from marketsim.gen._out._ifunction import IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide
    from marketsim.gen._out._iobservable import IObservablefloat
    from marketsim.gen._out.order._curried._side_price_floatingprice import side_price_FloatingPrice_SideFloatIObservableIOrderIObservableFloat as _order__curried_side_price_FloatingPrice_SideFloatIObservableIOrderIObservableFloat
    from marketsim import rtti
    if proto is None or rtti.can_be_casted(proto, IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide):
        if floatingPrice is None or rtti.can_be_casted(floatingPrice, IObservablefloat):
            return _order__curried_side_price_FloatingPrice_SideFloatIObservableIOrderIObservableFloat(proto,floatingPrice)
    raise Exception('Cannot find suitable overload for FloatingPrice('+str(proto) +':'+ str(type(proto))+','+str(floatingPrice) +':'+ str(type(floatingPrice))+')')
