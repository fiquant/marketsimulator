from marketsim import ops, types, event, Side, _, Event

def correct_volume(x):
    return None if x is None or abs(x) < 1 else int(x)
    
def correct_price(x):
    return x
    
def correct_budget(x):
    return x
    
def correct_side(x):
    return x

class SideVolume(ops.Observable[types.SideVolume]): 
    
    def __init__(self, 
                 side = ops.constant(Side.Sell), 
                 volume = ops.constant(1.)):
        ops.Observable[types.SideVolume].__init__(self)
        self.side = side 
        self.volume = volume
        if isinstance(side, Event):
            event.subscribe(side, _(self).fire, self)
        if isinstance(volume, Event):
            event.subscribe(volume, _(self).fire, self)
            
    def __call__(self):
        side = correct_side(self.side())
        if side is None:
            return None
        volume = correct_volume(self.volume())
        if volume is None:
            return None
        
        return (side, volume)
                    
    _properties = {
        'side'     : types.IFunction[Side],
        'volume'   : types.IFunction[float],
    }

class SignedVolume(ops.Observable[types.SideVolume]): 
    
    def __init__(self, 
                 signedVolume = ops.constant(1.)):
        ops.Observable[types.SideVolume].__init__(self)
        self.signedVolume = signedVolume
        if isinstance(signedVolume, Event):
            event.subscribe(signedVolume, _(self).fire, self)
            
    
            
    def __call__(self):
        signedVolume = correct_volume(self.signedVolume())
        if signedVolume is None:
            return None
        side = Side.Buy if signedVolume > 0 else Side.Sell
        return (side, abs(signedVolume))
                    
    _properties = {
        'signedVolume'   : types.IFunction[float],
    }

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
        side = correct_side(self.side())
        if side is None:
            return None
        price = correct_price(self.price())
        if price is None:
            return None
        volume = correct_volume(self.volume())
        if volume is None:
            return None
        
        return (side, price, volume)
                    
    _properties = {
        'side'     : types.IFunction[Side],
        'price'    : types.IFunction[float],
        'volume'   : types.IFunction[float],
    }

class SideBudget(ops.Observable[types.SideBudget]): 
    
    def __init__(self, 
                 side = ops.constant(Side.Sell), 
                 budget = ops.constant(200.)):
        ops.Observable[types.SideBudget].__init__(self)
        self.side = side 
        self.budget = budget
        if isinstance(side, Event):
            event.subscribe(side, _(self).fire, self)
        if isinstance(budget, Event):
            event.subscribe(budget, _(self).fire, self)
            
    def __call__(self):
        side = correct_side(self.side())
        if side is None:
            return None
        budget = correct_budget(self.budget())
        if budget is None:
            return None
        
        return (side, budget)
                    
    _properties = {
        'side'     : types.IFunction[Side],
        'budget'   : types.IFunction[float],
    }

