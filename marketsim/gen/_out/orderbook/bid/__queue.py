def _queue(book = None): 
    from marketsim.gen._out._iorderbook import IOrderBook
    from marketsim.gen._out.orderbook._bids import Bids_IOrderBook as _orderbook_Bids_IOrderBook
    from marketsim import rtti
    if book is None or rtti.can_be_casted(book, IOrderBook):
        return _orderbook_Bids_IOrderBook(book)
    raise Exception('Cannot find suitable overload for _queue('+str(book) +':'+ str(type(book))+')')
