# generated with class generator.python.intrinsic_function$Import
from marketsim.gen._out._imultiassetstrategy import IMultiAssetStrategy
from marketsim import registry
from marketsim.gen._out._itrader import ITrader
from marketsim.gen._out._isingleassettrader import ISingleAssetTrader
from marketsim.gen._out._itimeserie import ITimeSerie
from marketsim import listOf
from marketsim.gen._intrinsic.trader.classes import MultiAsset_Impl
@registry.expose(["Trader", "MultiAsset"])
class MultiAsset_ListISingleAssetTraderIMultiAssetStrategyStringFloatListITimeSerie(ITrader,MultiAsset_Impl):
    """ **A trader that trades different assets**
    
      It can be considered as a composition of single asset traders and multi asset strategies
      At the moment there is no way to instruct a multi asset strategy to trade only on subset of the assets
    
    Parameters are:
    
    **traders**
    	 defines accounts for every asset to trade 
    
    **strategy**
    	 multi asset strategy run by the trader 
    
    **name**
    
    **PnL**
    	 current trader balance (number of money units that it owns) 
    
    **timeseries**
    	 defines what data should be gathered for the trader 
    """ 
    def __init__(self, traders = None, strategy = None, name = None, PnL = None, timeseries = None):
        from marketsim.gen._out.strategy._arbitrage import Arbitrage_ as _strategy_Arbitrage_
        from marketsim import deref_opt
        from marketsim import rtti
        self.traders = traders if traders is not None else []
        self.strategy = strategy if strategy is not None else deref_opt(_strategy_Arbitrage_())
        self.name = name if name is not None else "-trader-"
        self.PnL = PnL if PnL is not None else 0.0
        self.timeseries = timeseries if timeseries is not None else []
        rtti.check_fields(self)
        MultiAsset_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'traders' : listOf(ISingleAssetTrader),
        'strategy' : IMultiAssetStrategy,
        'name' : str,
        'PnL' : float,
        'timeseries' : listOf(ITimeSerie)
    }
    
    
    
    
    
    
    
    
    
    
    def __repr__(self):
        return "%(name)s" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        self.__dict__['_ctx_ex'] = ctx.updatedFrom(self)
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.bind_ex(self.__dict__['_ctx_ex'])
                else:
                    v.bind_ex(self.__dict__['_ctx_ex'])
        for x in self.traders: x.bind_ex(self._ctx_ex)
        self.strategy.bind_ex(self._ctx_ex)
        for x in self.timeseries: x.bind_ex(self._ctx_ex)
        self.bind_impl(self.__dict__['_ctx_ex'])
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
    def reset_ex(self, generation):
        if self.__dict__.get('_reset_generation_ex', -1) == generation: return
        self.__dict__['_reset_generation_ex'] = generation
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.reset_ex(generation)
                else:
                    v.reset_ex(generation)
        for x in self.traders: x.reset_ex(generation)
        self.strategy.reset_ex(generation)
        for x in self.timeseries: x.reset_ex(generation)
        self.reset()
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
def MultiAsset(traders = None,strategy = None,name = None,PnL = None,timeseries = None): 
    from marketsim import rtti
    from marketsim.gen._out._itimeserie import ITimeSerie
    from marketsim.gen._out._isingleassettrader import ISingleAssetTrader
    from marketsim import listOf
    from marketsim.gen._out._imultiassetstrategy import IMultiAssetStrategy
    if traders is None or rtti.can_be_casted(traders, listOf(ISingleAssetTrader)):
        if strategy is None or rtti.can_be_casted(strategy, IMultiAssetStrategy):
            if name is None or rtti.can_be_casted(name, str):
                if PnL is None or rtti.can_be_casted(PnL, float):
                    if timeseries is None or rtti.can_be_casted(timeseries, listOf(ITimeSerie)):
                        return MultiAsset_ListISingleAssetTraderIMultiAssetStrategyStringFloatListITimeSerie(traders,strategy,name,PnL,timeseries)
    raise Exception('Cannot find suitable overload for MultiAsset('+str(traders) +':'+ str(type(traders))+','+str(strategy) +':'+ str(type(strategy))+','+str(name) +':'+ str(type(name))+','+str(PnL) +':'+ str(type(PnL))+','+str(timeseries) +':'+ str(type(timeseries))+')')
