from marketsim.gen._out._ifunction._ifunctionobject import IFunctionobject
from marketsim import meta
#() => .Boolean
class IFunctionbool(object):
    _types = [meta.function((),bool)]
    _types.append(IFunctionobject)
    def Condition(self, ifpart = None,elsepart = None):
        from marketsim.gen._out.ops._condition import Condition
        return Condition(self,ifpart,elsepart)
    
    pass



