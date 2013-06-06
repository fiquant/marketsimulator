from marketsim import bind, Event, getLabel, Side, scheduler, types, meta, mathutils, registry, trader

class IndicatorBase(types.IObservable):
    """ Observable that stores some scalar value and knows how to update it
    
    * **Source of data** -- function that provides data
    * **Events when to act** -- events when to act
    """
    def __init__(self, eventSources, dataSource, attributes = {}):
        """ Initializes indicator
        eventSources -- sequence of events to be subscribed to 
        dataSource -- function to be called in order to obtain the value
        label -- indicator label to be shown, for example, on a graph
        attributes -- a dictionary of attributes to be associated with the indicator
        """
        
        super(IndicatorBase, self).__init__()
        self.attributes = attributes
        self._eventSources = []
        self.eventSources = eventSources
        self._dataSource = dataSource
        
    @property    
    def label(self):
        return self._dataSource.label
    
    _properties = [ ('dataSource'  , meta.function((), float)),
                    ('eventSources' , meta.listOf(Event)) ]
    
    @property
    def eventSources(self):
        return self._eventSources
    
    @eventSources.setter
    def eventSources(self, value):
        for es in self._eventSources:
            es -= self.fire
        self._eventSources = value
        for es in self._eventSources:
            es += self.fire
            
    @property
    def digits(self):
        return self._dataSource.digits if 'digits' in dir(self._dataSource) else 4
    
    @property
    def dataSource(self):
        return self._dataSource
    
    @dataSource.setter
    def dataSource(self, value):
        self._dataSource = value
    
    def schedule(self):
        self.reset()
                
    def __call__(self):
        """ Returns current value
        """
        return self._dataSource()

class rough_balance(object):
    """ Approximation for trader's cleared balance. :: 
    
        Rb(trader) = Balance(trader) + VolumeTraded(trader)*MidPrice(Asset(trader))
    
    (so, bigger the trader position worse the approximation).
    """
    
    def __init__(self, trader):
        self.trader = trader
        
    _types = [meta.function((), float)]
    
    def __call__(self):
        return self.trader.PnL + self.trader.amount*self.trader.book.price if self.trader.book.price else 0
   
    @property
    def digits(self):
        return self.trader.orderBook._digitsToShow
    
    @property
    def label(self):
        return "InstEfficiency_{" + getLabel(self.trader) + "}"
    
    _properties = { 'trader' : types.ISingleAssetTrader }


class OnTraded(Event):
    """ Multicast event that is fired once a trade is done by *trader*
    """

    def __init__(self, trader):
        Event.__init__(self)
        self.trader = trader
        self.trader.on_traded += self.fire
        
    _properties = { 'trader' : types.ISingleAssetTrader }
    
    
def InstEfficiency(trader):
    """ Creates an indicator bound to rough estimation of a trader's balance if cleared
    """
    
    return IndicatorBase([OnTraded(trader)], 
                         rough_balance(trader))

class profit_and_loss(object):
    """ Returns balance of the given *trader*
    """
    
    def __init__(self, trader):
        self.trader = trader
        self._alias = ["Trader's", "Balance"]
        
    @property
    def label(self):
        return "P&L_{" + getLabel(self.trader) + "}"
    
    @property
    def digits(self):
        return self.trader.orderBook._digitsToShow
    
    
    def __call__(self):
        return self.trader.PnL
    
    _properties = { 'trader' : types.ISingleAssetTrader }
    
def PnL(trader):
    
    return IndicatorBase([OnTraded(trader)], profit_and_loss(trader))

class mid_price(object):
    """ Returns middle price in the given *orderbook*
    """
    
    def __init__(self, orderbook):
        self.orderbook = orderbook
        self._alias = ["Asset's", "Mid-price"]
        
    _types = [meta.function((), float)]
    
    def __call__(self):
        return self.orderbook.price

    @property
    def digits(self):
        return self.orderbook._digitsToShow
    
    @property
    def label(self):
        return "Price_{" + getLabel(self.orderbook) + "}"
    
    _properties = { 'orderbook' : types.IOrderBook }
    
class OnPriceChanged(Event):
    """ Event that is fired once mid-price in the *orderbook* has changed
    """
    
    def __init__(self, orderbook):
        Event.__init__(self)
        self.orderbook = orderbook
        self.orderbook.on_price_changed += self.fire
        
    _properties = { 'orderbook' : types.IOrderBook }
    
def Price(book):
    """ Creates an indicator bound to the middle price of an asset
    """   
    return IndicatorBase(\
        [OnPriceChanged(book)], 
        mid_price(book))
    
class OnSideBestChanged(Event):
    """ Event that is fired once a *side* price in the *orderbook* has changed
    """
    
    def __init__(self, orderbook, side):
        Event.__init__(self)
        self.orderbook = orderbook
        self.side = side
        
    def bind(self, context): # TODO: we should subscribe to orderbook and side changed events
        self.orderbook.queue(self.side).on_best_changed += self.fire
        
    _properties = { 'orderbook' : types.IOrderBook, 
                    'side'      : types.Side }
    
class cross_spread(object):
    
    def __init__(self, book_A, book_B):
        self.book_A = book_A
        self.book_B = book_B
        
    def __call__(self):
        asks = self.book_A.asks
        bids = self.book_B.bids
        return asks.best.price - bids.best.price if not asks.empty and not bids.empty else None
    
    @property
    def label(self):
        return "Price("+self.book_A.asks.label+") - Price("+self.book_B.bids.label+")"
    
def CrossSpread(book_A, book_B):
    """ Returns indicator bound to difference between ask of book_A and bid of book_B
    """
    asks = book_A.asks
    bids = book_B.bids
    return IndicatorBase(\
        [asks.on_best_changed, bids.on_best_changed], 
         cross_spread(book_A, book_B))

class volume_traded(object):
    """ Returns trader's position (i.e. number of assets traded)
    """
    
    def __init__(self, trader):
        self.trader = trader
        self._alias = ["Trader's", "Position"]
        
    _types = [meta.function((), float)]
    
    def __call__(self):
        return self.trader.amount
    
    @property
    def digits(self):
        return 0
    
    @property
    def label(self):
        return "Amount_{" + getLabel(self.trader) + "}"
    
    _properties = { 'trader' : types.ISingleAssetTrader }

    
def VolumeTraded(aTrader = None):
    """ Returns an indicator bound to trader's position 
    """
    if aTrader is None:
        aTrader = trader.SASM_Proxy()
        
    return IndicatorBase(\
        [OnTraded(aTrader)], 
        volume_traded(aTrader))
    
class side_price(object):
    """ Returns *orderbook* *side* price 
    """
    
    def __init__(self, orderbook, side):
        self.orderbook = orderbook
        self.side = side
        self._alias = ["Asset's", "Side price"]
        
    _types = [meta.function((), float)]
    
    def __call__(self):
        queue = self.orderbook.queue(self.side)
        return queue.best.price if not queue.empty else None
    
    @property
    def digits(self):
        return self.orderbook._digitsToShow
    
    @property
    def label(self):
        return "Price("+self.orderbook.queue(self.side).label+")" 
    
    _properties = { 'orderbook' : types.IOrderBook, 
                    'side'      : types.Side }
    
class price_at_volume(object):

    def __init__(self, orderbook, side, volumeAt):
        self.orderbook = orderbook
        self.side = side
        self.volumeAt = volumeAt
        self._alias = ["Asset's", "Price at Volume"]
        
    _types = [meta.function((), float)]
    
    def __call__(self):
        queue = self.orderbook.queue(self.side)
        for (volume, price) in queue.getVolumePrices([self.volumeAt]):
            return price
        return None
    
    @property
    def digits(self):
        return self.orderbook._digitsToShow
    
    @property
    def label(self):
        return "PriceAtVolume_{"+str(self.volumeAt)+"}("+self.orderbook.queue(self.side).label+")" 
    
    _properties = { 'orderbook' : types.IOrderBook, 
                    'side'      : types.Side, 
                    'volumeAt'  : float }

class volume_levels(object):
    
    def __init__(self, orderbook, side, volumeDelta, volumeCount):
        self.orderbook = orderbook
        self.side = side
        self.volumeDelta = volumeDelta
        self.volumeCount = volumeCount
        self._alias = ["Asset's", "Volume levels"]
    
    @property    
    def volumes(self):
        return [self.volumeDelta * i for i in range(self.volumeCount)]
        
    _types = [meta.function((), float)] # should be () -> meta.listOf(float)
    
    def __call__(self):
        queue = self.orderbook.queue(self.side)
        return [price for (volume, price) in queue.getVolumePrices(self.volumes)]
    
    @property
    def digits(self):
        return self.orderbook._digitsToShow
    
    @property
    def label(self):
        return "VolumeLevels("+self.orderbook.queue(self.side).label+")" 
    
    _properties = { 'orderbook'     : types.IOrderBook, 
                    'side'          : types.Side, 
                    'volumeDelta'   : float,
                    'volumeCount'   : int  }
    
    

def BestPrice(book, side, label):
    """ Creates an indicator bound to the price of the best order in a queue
    book - asset order book
    side - side of the queue
    label - label prefix
    """
    
    return IndicatorBase(\
        [OnSideBestChanged(book, side)], 
        side_price(book, side))
    
def BidPrice(book):
    """ Creates an indicator bound to the bid price of the asset
    book - asset order book
    """
    return BestPrice(book, Side.Buy, "BidPrice ")

def AskPrice(book):
    """ Creates an indicator bound to the ask price of the asset
    book - asset order book
    """
    return BestPrice(book, Side.Sell, "AskPrice ")

def OnEveryDt(interval, source):
    """ Creates an indicator that is updated regularly
    interval - constant interval between updates
    source - function to obtain indicator value
    """
    
    return IndicatorBase([scheduler.Timer(mathutils.constant(interval))],
                         source, 
                         {'smooth':True})

def PriceAtVolume(interval, orderbook, side, volume):

    return IndicatorBase([scheduler.Timer(mathutils.constant(interval))],
                         price_at_volume(orderbook, side, volume), 
                         {'smooth':True, 'fillBelow' : side == Side.Buy, 'fillAbove' : side == Side.Sell})

def VolumeLevels(interval, orderbook, side, volumeDelta, volumeCount):

    return IndicatorBase([scheduler.Timer(mathutils.constant(interval))],
                         volume_levels(orderbook, side, volumeDelta, volumeCount), 
                         {'smooth':True, 'volumeLevels' : True, 
                          'fillBelow' : side == Side.Buy, 'fillAbove' : side == Side.Sell})
    