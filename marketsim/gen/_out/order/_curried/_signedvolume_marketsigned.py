from marketsim import registry
from marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionfloat import IFunctionIObservableIOrder_from_IFunctionfloat
@registry.expose(["Order", "MarketSigned"])
class signedVolume_MarketSigned_(IFunctionIObservableIOrder_from_IFunctionfloat):
    """ **Factory creating market orders**
    
    
      Market order intructs buy or sell given volume immediately
    
    Parameters are:
    """ 
    def __init__(self):
        from marketsim import rtti
        
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        
    }
    
    def __repr__(self):
        return "MarketSigned" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bindEx(self, ctx):
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        setattr(self, '_processing_ex', True)
        
        delattr(self, '_processing_ex')
    
    def __call__(self, signedVolume = None):
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import deref_opt
        from marketsim.gen._out.order._marketsigned import MarketSigned
        signedVolume = signedVolume if signedVolume is not None else deref_opt(_constant_Float(1.0))
        
        return MarketSigned(signedVolume)
    
def signedVolume_MarketSigned(): 
    from marketsim import rtti
    return signedVolume_MarketSigned_()
    raise Exception('Cannot find suitable overload for signedVolume_MarketSigned('++')')
