from marketsim.gen._intrinsic.trader.classes import _SingleAsset_Impl
from marketsim import IOrderBook
from marketsim import ISingleAssetStrategy
from marketsim import listOf
from marketsim import ITimeSerie

class SingleAsset(_SingleAsset_Impl):
    """ 
    """ 
    def __init__(self, orderBook , strategy = None, name = None, amount = None, PnL = None, timeseries = None):
        from marketsim.gen._out.strategy._Noise import Noise as _strategy_Noise
        self.orderBook = orderBook
        self.strategy = strategy if strategy is not None else _strategy_Noise()
        self.name = name if name is not None else "-trader-"
        self.amount = amount if amount is not None else 0.0
        self.PnL = PnL if PnL is not None else 0.0
        self.timeseries = timeseries if timeseries is not None else []
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
    
