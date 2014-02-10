def _queue(book = None): 
    from marketsim import IOrderBook
    from marketsim import rtti
    if book is None or rtti.can_be_casted(book, IOrderBook):
        return Asks_IOrderBook(book)
    raise Exception("Cannot find suitable overload")
