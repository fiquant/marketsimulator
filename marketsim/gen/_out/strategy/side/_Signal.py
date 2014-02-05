from marketsim import registry
from marketsim import Side
from marketsim import Side
from marketsim.ops._all import Observable
from marketsim import IFunction
from marketsim import float
from marketsim import float
from marketsim import context
@registry.expose(["Side function", "Signal"])
class Signal_Optional__IFunction__Float____Optional__Float_(Observable[Side]):
    """ 
    """ 
    def __init__(self, signal = None, threshold = None):
        from marketsim import Side
        from marketsim import Side
        from marketsim.ops._all import Observable
        from marketsim.gen._out._constant import constant as _constant
        from marketsim import rtti
        from marketsim import _
        from marketsim import event
        Observable[Side].__init__(self)
        self.signal = signal if signal is not None else _constant(0.0)
        self.threshold = threshold if threshold is not None else 0.7
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'signal' : IFunction[float],
        'threshold' : float
    }
    def __repr__(self):
        return "Signal(%(signal)s, %(threshold)s)" % self.__dict__
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    _internals = ['impl']
    def __call__(self, *args, **kwargs):
        return self.impl()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def getImpl(self):
        from marketsim.gen._out.ops._Condition_Side import Condition_Side as _ops_Condition_Side
        from marketsim.gen._out.ops._Greater import Greater as _ops_Greater
        from marketsim.gen._out._const import const as _const
        from marketsim.gen._out.side._Buy import Buy as _side_Buy
        from marketsim.gen._out.ops._Condition_Side import Condition_Side as _ops_Condition_Side
        from marketsim.gen._out.ops._Less import Less as _ops_Less
        from marketsim.gen._out._const import const as _const
        from marketsim.gen._out.side._Sell import Sell as _side_Sell
        from marketsim.gen._out.side._Nothing import Nothing as _side_Nothing
        return _ops_Condition_Side(_ops_Greater(self.signal,_const(self.threshold)),_side_Buy(),_ops_Condition_Side(_ops_Less(self.signal,_const((0-self.threshold))),_side_Sell(),_side_Nothing()))
    
Signal = Signal_Optional__IFunction__Float____Optional__Float_
