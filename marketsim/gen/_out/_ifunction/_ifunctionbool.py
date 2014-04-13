from marketsim.types import Function_impl
from marketsim.gen._out._ifunction._ifunctionobject import IFunctionobject
from marketsim import meta
#() => .Boolean
class IFunctionbool(Function_impl):
    _types = [meta.function((),bool)]
    _types.append(IFunctionobject)
    def And(self, y = None):
        from marketsim.gen._out.ops._and import And
        return And(self,y)
    
    def Or(self, y = None):
        from marketsim.gen._out.ops._or import Or
        return Or(self,y)
    
    def Condition(self, ifpart = None,elsepart = None):
        from marketsim.gen._out.ops._condition import Condition
        return Condition(self,ifpart,elsepart)
    
    pass



