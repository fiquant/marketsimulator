class ILink(object):
    def TwoWayLink(self, down = None):
        from marketsim.gen._out.orderbook._twowaylink import TwoWayLink
        return TwoWayLink(self,down)
    
    pass
