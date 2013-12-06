from marketsim import types, context

# TODO: inheritance like:
#        Proxy -> ITraderOpt
#        SingleAsset -> ITrader -> ITraderOpt

def aux(name):
    return name[0:2] == "__" or name == '_processing'

class Base(object):

    def __init__(self):
        
        self.__dict__['_impl'] = None
        
    def _bind(self, impl):
        assert self._impl is  None
        self.__dict__['_impl'] = impl
        
    def __getattr__(self, name):
        if not aux(name) and self._impl:
            return getattr(self._impl, name)
        else:
            raise AttributeError
        
    def __setattr__(self, name, value):
        if not aux(name) and self._impl:
            setattr(self._impl, name, value)
        else:
            self.__dict__[name] = value
            
    def __delattr__(self, name):
        if not aux(name) and self._impl:
            del self._impl.name 
        else:
            del self.__dict__[name]
        
    
    def _new_property_changed_listener_added(self, propname):
        pass
                
    _properties = {}
        
class SingleProxyBase(Base, types.ISingleAssetTrader):
    
    def __init__(self):
        Base.__init__(self)
        self.__dict__['_alias'] = ["$(Trader)"]
            
class MultiProxy(Base, types.ITrader):
    
    def __init__(self):
        Base.__init__(self)
        self.__dict__['_alias'] = ['$(MultiTrader)']
        
    def bind(self, context):
        self._bind(context.trader)

from marketsim.gen._out.observable.trader._SingleProxy import SingleProxy

#class SingleProxy(SingleProxyBase):
#
#    def bind(self, ctx):
#        self._bind(ctx.trader)
            
class ParentProxy(SingleProxyBase):
    
    def bind(self, ctx):
        self._bind(ctx.parentTrader)
        