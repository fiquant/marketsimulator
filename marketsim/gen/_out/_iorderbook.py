class IOrderBook(object):
    def TickSize(self):
        from marketsim.gen._out.orderbook._ticksize import TickSize
        return TickSize(self)
    
    def PairTrading(self, factor = None,book = None):
        from marketsim.gen._out.strategy.side._pairtrading import PairTrading
        return PairTrading(self,factor,book)
    
    def MidPrice(self):
        from marketsim.gen._out.orderbook._midprice import MidPrice
        return MidPrice(self)
    
    def Asks(self):
        from marketsim.gen._out.orderbook._asks import Asks
        return Asks(self)
    
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
    
    def Remote(self, link = None,timeseries = None):
        from marketsim.gen._out.orderbook._remote import Remote
        return Remote(self,link,timeseries)
    
    def NaiveCumulativePrice(self, depth = None):
        from marketsim.gen._out.orderbook._naivecumulativeprice import NaiveCumulativePrice
        return NaiveCumulativePrice(self,depth)
    
    def Spread(self):
        from marketsim.gen._out.orderbook._spread import Spread
        return Spread(self)
    
    pass
