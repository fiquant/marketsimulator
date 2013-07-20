import marketsim
from marketsim import wrap, ops, types, event, _, flags

FunctionBase = types.Factory('FunctionBase', """(wrap.Base):
    _properties = {'impl' : (types.IFunction[%(T)s], flags.collapsed) }
""", globals())

ObservableBase = types.Factory('ObservableBase', """(wrap.Base):

    def __init__(self):
        wrap.Base.__init__(self)
        event.subscribe(self.impl, _(self).fire, self)
        
    _properties = {'impl' : (types.IObservable[%(T)s], flags.collapsed) }
""", globals())
        
 
def function(cls, alias, docstring, fields, ctx):
    wrap.generate("Function", cls, alias, docstring, fields, ctx)
    
def observable(cls, alias, docstring, fields, ctx):
    wrap.generate("Observable", cls, alias, docstring, fields, ctx)
