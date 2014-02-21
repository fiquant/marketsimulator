class IOrderBook(object):
    def WeightedPrice(self, alpha = None):
        from marketsim.gen._out.orderbook.bid._weightedprice import WeightedPrice
        return WeightedPrice(self,alpha)
    
    @property
    def TickSize(self):
        from marketsim.gen._out.orderbook._ticksize import TickSize
        return TickSize(self)
    
    @property
    def MidPrice(self):
        from marketsim.gen._out.orderbook._midprice import MidPrice
        return MidPrice(self)
    
    @property
    def Asks(self):
        from marketsim.gen._out.orderbook._asks import Asks
        return Asks(self)
    
    @property
    def LastTradeVolume(self):
        from marketsim.gen._out.orderbook.bid._lasttradevolume import LastTradeVolume
        return LastTradeVolume(self)
    
    @property
    def Price(self):
        from marketsim.gen._out.orderbook.bid._price import Price
        return Price(self)
    
    @property
    def Bids(self):
        from marketsim.gen._out.orderbook._bids import Bids
        return Bids(self)
    
    def RSI(self, timeframe = None,alpha = None):
        from marketsim.gen._out.math._rsi import RSI
        return RSI(self,timeframe,alpha)
    
    def Queue(self, side = None):
        from marketsim.gen._out.orderbook._queue import Queue
        return Queue(self,side)
    
    def CumulativePrice(self, depth = None):
        from marketsim.gen._out.orderbook._cumulativeprice import CumulativePrice
        return CumulativePrice(self,depth)
    
    @property
    def LastPrice(self):
        from marketsim.gen._out.orderbook.bid._lastprice import LastPrice
        return LastPrice(self)
    
    def Remote(self, link = None,timeseries = None):
        from marketsim.gen._out.orderbook._remote import Remote
        return Remote(self,link,timeseries)
    
    def NaiveCumulativePrice(self, depth = None):
        from marketsim.gen._out.orderbook._naivecumulativeprice import NaiveCumulativePrice
        return NaiveCumulativePrice(self,depth)
    
    @property
    def Spread(self):
        from marketsim.gen._out.orderbook._spread import Spread
        return Spread(self)
    
    @property
    def LastTradePrice(self):
        from marketsim.gen._out.orderbook.bid._lasttradeprice import LastTradePrice
        return LastTradePrice(self)
    
    pass
