from marketsim import registry
from marketsim.gen._out.strategy.side._meanreversion import MeanReversion
@registry.expose(["-", "Book"])
class Book_strategysideMeanReversion(object):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.strategy.side._meanreversion import MeanReversion_FloatIOrderBook as _strategy_side_MeanReversion_FloatIOrderBook
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_strategy_side_MeanReversion_FloatIOrderBook())
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : MeanReversion
    }
    def __repr__(self):
        return "Book(%(x)s)" % self.__dict__
    
    @property
    def dereference(self):
        return self.x.book
    
from marketsim import registry
from marketsim.gen._out.strategy.side._fundamentalvalue import FundamentalValue
@registry.expose(["-", "Book"])
class Book_strategysideFundamentalValue(object):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.strategy.side._fundamentalvalue import FundamentalValue_FloatIOrderBook as _strategy_side_FundamentalValue_FloatIOrderBook
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_strategy_side_FundamentalValue_FloatIOrderBook())
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : FundamentalValue
    }
    def __repr__(self):
        return "Book(%(x)s)" % self.__dict__
    
    @property
    def dereference(self):
        return self.x.book
    
from marketsim import registry
from marketsim.gen._out.strategy.side._crossingaverages import CrossingAverages
@registry.expose(["-", "Book"])
class Book_strategysideCrossingAverages(object):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.strategy.side._crossingaverages import CrossingAverages_FloatFloatFloatIOrderBook as _strategy_side_CrossingAverages_FloatFloatFloatIOrderBook
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_strategy_side_CrossingAverages_FloatFloatFloatIOrderBook())
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : CrossingAverages
    }
    def __repr__(self):
        return "Book(%(x)s)" % self.__dict__
    
    @property
    def dereference(self):
        return self.x.book
    
from marketsim import registry
from marketsim.gen._out.strategy.side._pairtrading import PairTrading
@registry.expose(["-", "Book"])
class Book_strategysidePairTrading(object):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.strategy.side._pairtrading import PairTrading_IOrderBookFloatIOrderBook as _strategy_side_PairTrading_IOrderBookFloatIOrderBook
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_strategy_side_PairTrading_IOrderBookFloatIOrderBook())
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : PairTrading
    }
    def __repr__(self):
        return "Book(%(x)s)" % self.__dict__
    
    @property
    def dereference(self):
        return self.x.book
    
def Book(x = None): 
    from marketsim import rtti
    from marketsim.gen._out.strategy.side._meanreversion import MeanReversion
    from marketsim.gen._out.strategy.side._crossingaverages import CrossingAverages
    from marketsim.gen._out.strategy.side._fundamentalvalue import FundamentalValue
    from marketsim.gen._out.strategy.side._pairtrading import PairTrading
    if x is None or rtti.can_be_casted(x, MeanReversion):
        return Book_strategysideMeanReversion(x)
    if x is None or rtti.can_be_casted(x, FundamentalValue):
        return Book_strategysideFundamentalValue(x)
    if x is None or rtti.can_be_casted(x, CrossingAverages):
        return Book_strategysideCrossingAverages(x)
    if x is None or rtti.can_be_casted(x, PairTrading):
        return Book_strategysidePairTrading(x)
    raise Exception('Cannot find suitable overload for Book('+str(x) +':'+ str(type(x))+')')
