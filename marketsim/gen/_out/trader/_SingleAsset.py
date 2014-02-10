from marketsim import str
from marketsim.gen._intrinsic.trader.classes import _SingleAsset_Impl
from marketsim import ITimeSerie
from marketsim import ISingleAssetStrategy
from marketsim import IOrderBook
from marketsim import listOf
from marketsim import float

class SingleAsset_IOrderBookISingleAssetStrategyStringFloatFloatListITimeSerie(_SingleAsset_Impl):
    """ 
    """ 
    def __init__(self, orderBook , strategy = None, name = None, amount = None, PnL = None, timeseries = None):
        from marketsim.gen._out.strategy._noise import Noise as _strategy_Noise
        from marketsim import rtti
        self.orderBook = orderBook
        self.strategy = strategy if strategy is not None else _strategy_Noise()
        self.name = name if name is not None else "-trader-"
        self.amount = amount if amount is not None else 0.0
        self.PnL = PnL if PnL is not None else 0.0
        self.timeseries = timeseries if timeseries is not None else []
        rtti.check_fields(self)
        _SingleAsset_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'orderBook' : IOrderBook,
        'strategy' : ISingleAssetStrategy,
        'name' : str,
        'amount' : float,
        'PnL' : float,
        'timeseries' : listOf(ITimeSerie)
    }
    def __repr__(self):
        return "%(name)s" % self.__dict__
    
def SingleAsset(orderBook = None,strategy = None,name = None,amount = None,PnL = None,timeseries = None): 
    from marketsim import rtti
    from marketsim import float
    from marketsim import IOrderBook
    from marketsim import str
    from marketsim import listOf
    from marketsim import ISingleAssetStrategy
    from marketsim import ITimeSerie
    if orderBook is None or rtti.can_be_casted(orderBook, IOrderBook):
        if strategy is None or rtti.can_be_casted(strategy, ISingleAssetStrategy):
            if name is None or rtti.can_be_casted(name, str):
                if amount is None or rtti.can_be_casted(amount, float):
                    if PnL is None or rtti.can_be_casted(PnL, float):
                        if timeseries is None or rtti.can_be_casted(timeseries, listOf(ITimeSerie)):
                            return SingleAsset_IOrderBookISingleAssetStrategyStringFloatFloatListITimeSerie(orderBook,strategy,name,amount,PnL,timeseries)
    raise Exception("Cannot find suitable overload")
