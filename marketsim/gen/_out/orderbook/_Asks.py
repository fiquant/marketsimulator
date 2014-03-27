from marketsim import registry
from marketsim.gen._out._iorderqueue import IOrderQueue
from marketsim.gen._intrinsic.orderbook.proxy import Asks_Impl
from marketsim.gen._out._iorderbook import IOrderBook
@registry.expose(["Asset", "Asks"])
class Asks_IOrderBook(IOrderQueue,Asks_Impl):
    """ 
    """ 
    def __init__(self, book = None):
        from marketsim.gen._out.orderbook._oftrader import OfTrader_IAccount as _orderbook_OfTrader_IAccount
        from marketsim import deref_opt
        from marketsim import rtti
        self.book = book if book is not None else deref_opt(_orderbook_OfTrader_IAccount())
        rtti.check_fields(self)
        Asks_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'book' : IOrderBook
    }
    
    
    def __repr__(self):
        return "Asks(%(book)s)" % { name : getattr(self, name) for name in self._properties.iterkeys() }
    
def Asks(book = None): 
    from marketsim.gen._out._iorderbook import IOrderBook
    from marketsim import rtti
    if book is None or rtti.can_be_casted(book, IOrderBook):
        return Asks_IOrderBook(book)
    raise Exception('Cannot find suitable overload for Asks('+str(book) +':'+ str(type(book))+')')
