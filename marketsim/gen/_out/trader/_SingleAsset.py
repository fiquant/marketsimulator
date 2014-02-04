from marketsim.gen._intrinsic.trader.classes import _SingleAsset_Impl
from marketsim import IOrderBook
from marketsim import ISingleAssetStrategy
from marketsim import str
from marketsim import float
from marketsim import float
from marketsim import ITimeSerie
from marketsim import listOf

class SingleAsset__IOrderBook__Optional__ISingleAssetStrategy___Optional__String___Optional__Float___Optional__Float___Optional_List__ITimeSerie__(_SingleAsset_Impl):
    """ 
    """ 
    def __init__(self, orderBook , strategy = None, name = None, amount = None, PnL = None, timeseries = None):
        from marketsim.gen._out.strategy._Noise import Noise as _strategy_Noise
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
    
SingleAsset = SingleAsset__IOrderBook__Optional__ISingleAssetStrategy___Optional__String___Optional__Float___Optional__Float___Optional_List__ITimeSerie__
