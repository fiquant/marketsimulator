from marketsim import meta
class IFunctionbool(object):
    _types = [meta.function((),bool)]
    def Condition(self, ifpart = None,elsepart = None):
        from marketsim.gen._out.ops._condition import Condition
        return Condition(self,ifpart,elsepart)
    
    pass



