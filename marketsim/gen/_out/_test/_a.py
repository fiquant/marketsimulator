def A(x = None): 
    from marketsim.gen._out._ifunction._ifunctiont import IFunctionT
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, IFunctionT):
        return A__testtypesT(x)
    raise Exception('Cannot find suitable overload for A('+str(x) +':'+ str(type(x))+')')
