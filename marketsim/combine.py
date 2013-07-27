from marketsim import ops, types, event, Side, _, Event

class SidePriceVolume(ops.Observable[types.SidePriceVolume]): 
    
    def __init__(self, side, price, volume):
        ops.Observable[types.SidePriceVolume].__init__(self)
        self.side = side 
        self.price = price 
        self.volume = volume
        if isinstance(side, Event):
            event.subscribe(side, _(self).fire, self)
        if isinstance(price, Event):
            event.subscribe(price, _(self).fire, self)
        if isinstance(volume, Event):
            event.subscribe(volume, _(self).fire, self)
            
    def __call__(self):
        side = self.side()
        if side is None:
            return None
        price = self.price()
        if price is None:
            return None
        volume = self.volume()
        if volume is None:
            return None
        
        return (side, price, volume)
                    
    _properties = {
        'side' : types.IFunction[Side],
        'price': types.IFunction[float],
        'volume':types.IFunction[float],
    }
