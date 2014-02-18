def A(x = None,y = None): 
    from marketsim.gen._out._ifunction import IFunctionint
    from marketsim.gen._out._ifunction import IFunctionfloat
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, IFunctionint):
        if y is None or rtti.can_be_casted(y, IFunctionfloat):
            return A_IntFloat(x,y)
    raise Exception('Cannot find suitable overload for A('+str(x) +':'+ str(type(x))+','+str(y) +':'+ str(type(y))+')')
