from marketsim import types, Event, context

# TODO: inheritance like:
#        Proxy -> ITraderOpt
#        SingleAsset -> ITrader -> ITraderOpt

class Base(object):

    def __init__(self):
        
        self._impl = None
        
    def _bind(self, impl):
        assert self._impl is  None
        self._impl = impl
        
    def __getattr__(self, name):
        if name[0:2] != "__" and self._impl:
            return getattr(self._impl, name)
        else:
            raise AttributeError
    
    def _new_property_changed_listener_added(self, propname):
        pass
                
    _properties = {}
        
class SASM_ProxyBase(Base, types.ISingleAssetTrader):
    
    def __init__(self):
        Base.__init__(self)
        self._alias = ["$(Trader)"]
            
class MultiProxy(Base, types.ITrader):
    
    def __init__(self):
        Base.__init__(self)
        self._alias = ['$(MultiTrader)']
        
    def bind(self, context):
        self._bind(context.trader)

class SASM_Proxy(SASM_ProxyBase):

    def bind(self, ctx):
        self._bind(ctx.trader)
            
class SASM_ParentProxy(SASM_ProxyBase):
    
    def bind(self, ctx):
        self._bind(ctx.parentTrader)
        