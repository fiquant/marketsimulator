class IOrderQueue(object):
    def SafeSidePrice(self, defaultValue = None):
        from marketsim.gen._out.orderbook._safesideprice import SafeSidePrice
        return SafeSidePrice(self,defaultValue)
    
    def WeightedPrice(self, alpha = None):
        from marketsim.gen._out.orderbook._weightedprice import WeightedPrice
        return WeightedPrice(self,alpha)
    
    @property
    def LastTradeVolume(self):
        from marketsim.gen._out.orderbook._lasttradevolume import LastTradeVolume
        return LastTradeVolume(self)
    
    @property
    def BestPrice(self):
        from marketsim.gen._out.orderbook._bestprice import BestPrice
        return BestPrice(self)
    
    def VolumeLevels(self, volumeDelta = None,volumeCount = None):
        from marketsim.gen._out.orderbook._volumelevels import VolumeLevels
        return VolumeLevels(self,volumeDelta,volumeCount)
    
    @property
    def LastPrice(self):
        from marketsim.gen._out.orderbook._lastprice import LastPrice
        return LastPrice(self)
    
    @property
    def LastTradePrice(self):
        from marketsim.gen._out.orderbook._lasttradeprice import LastTradePrice
        return LastTradePrice(self)
    
    pass
