def _queue(book = None): 
    from marketsim import IOrderBook
    from marketsim.gen._out.orderbook._asks import Asks_IOrderBook as _orderbook_Asks
    from marketsim import rtti
    if book is None or rtti.can_be_casted(book, IOrderBook):
        return _orderbook_Asks(book)
    raise Exception("Cannot find suitable overload")
