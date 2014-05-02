# generated with class generator.python.intrinsic_function$Import
from marketsim.gen._intrinsic.veusz import CSV_Impl

class CSV_StringAnyAny(CSV_Impl):
    """ 
    """ 
    def __init__(self, directory , source , attributes ):
        from marketsim import rtti
        self.directory = directory
        self.source = source
        self.attributes = attributes
        rtti.check_fields(self)
        CSV_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'directory' : str,
        'source' : object,
        'attributes' : object
    }
    
    
    
    
    
    
    def __repr__(self):
        return "CSV(%(directory)s, %(source)s, %(attributes)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        self.__dict__['_ctx_ex'] = ctx.updatedFrom(self)
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.bind_ex(self.__dict__['_ctx_ex'])
                else:
                    v.bind_ex(self.__dict__['_ctx_ex'])
        self.source.bind_ex(self._ctx_ex)
        self.attributes.bind_ex(self._ctx_ex)
        self.bind_impl(self.__dict__['_ctx_ex'])
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
    def reset_ex(self, generation):
        if self.__dict__.get('_reset_generation_ex', -1) == generation: return
        self.__dict__['_reset_generation_ex'] = generation
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.reset_ex(generation)
                else:
                    v.reset_ex(generation)
        self.source.reset_ex(generation)
        self.attributes.reset_ex(generation)
        self.reset()
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
    def bind_impl(self, ctx):
        CSV_Impl.bind_impl(self, ctx)
    
    def reset(self):
        CSV_Impl.reset(self)
    
def CSV(directory = None,source = None,attributes = None): 
    from marketsim import rtti
    if directory is None or rtti.can_be_casted(directory, str):
        if source is None or rtti.can_be_casted(source, object):
            if attributes is None or rtti.can_be_casted(attributes, object):
                return CSV_StringAnyAny(directory,source,attributes)
    raise Exception('Cannot find suitable overload for CSV('+str(directory) +':'+ str(type(directory))+','+str(source) +':'+ str(type(source))+','+str(attributes) +':'+ str(type(attributes))+')')
