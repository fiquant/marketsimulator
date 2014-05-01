# generated with class generator.python.intrinsic_function$Import
from marketsim.gen._out._isingleassettrader import ISingleAssetTrader
from marketsim.gen._out._itimeserie import ITimeSerie
from marketsim.gen._out._iorderbook import IOrderBook
from marketsim.gen._intrinsic.trader.classes import SingleAsset_Impl
from marketsim import listOf
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy

class SingleAsset_IOrderBookISingleAssetStrategyStringFloatFloatListITimeSerie(ISingleAssetTrader,SingleAsset_Impl):
    """ **A trader that trades a single asset on a single market**
    
    
    Parameters are:
    
    **orderBook**
    	 order book for the asset being traded 
    
    **strategy**
    	 strategy run by the trader 
    
    **name**
    
    **amount**
    	 current position of the trader (number of assets that it owns) 
    
    **PnL**
    	 current trader balance (number of money units that it owns) 
    
    **timeseries**
    	 defines what data should be gathered for the trader 
    """ 
    def __init__(self, orderBook , strategy = None, name = None, amount = None, PnL = None, timeseries = None):
        from marketsim.gen._out.strategy._empty import Empty_ as _strategy_Empty_
        from marketsim import deref_opt
        from marketsim import rtti
        self.orderBook = orderBook
        self.strategy = strategy if strategy is not None else deref_opt(_strategy_Empty_())
        self.name = name if name is not None else "-trader-"
        self.amount = amount if amount is not None else 0.0
        self.PnL = PnL if PnL is not None else 0.0
        self.timeseries = timeseries if timeseries is not None else []
        rtti.check_fields(self)
        SingleAsset_Impl.__init__(self)
    
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
        self.orderBook.bind_ex(self._ctx_ex)
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
        self.orderBook.reset_ex(generation)
        self.strategy.reset_ex(generation)
        for x in self.timeseries: x.reset_ex(generation)
        self.reset()
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
    def bind_impl(self, ctx):
        SingleAsset_Impl.bind_impl(self, ctx)
    
    def reset(self):
        SingleAsset_Impl.reset(self)
    
def SingleAsset(orderBook = None,strategy = None,name = None,amount = None,PnL = None,timeseries = None): 
    from marketsim import rtti
    from marketsim.gen._out._itimeserie import ITimeSerie
    from marketsim.gen._out._iorderbook import IOrderBook
    from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
    from marketsim import listOf
    if orderBook is None or rtti.can_be_casted(orderBook, IOrderBook):
        if strategy is None or rtti.can_be_casted(strategy, ISingleAssetStrategy):
            if name is None or rtti.can_be_casted(name, str):
                if amount is None or rtti.can_be_casted(amount, float):
                    if PnL is None or rtti.can_be_casted(PnL, float):
                        if timeseries is None or rtti.can_be_casted(timeseries, listOf(ITimeSerie)):
                            return SingleAsset_IOrderBookISingleAssetStrategyStringFloatFloatListITimeSerie(orderBook,strategy,name,amount,PnL,timeseries)
    raise Exception('Cannot find suitable overload for SingleAsset('+str(orderBook) +':'+ str(type(orderBook))+','+str(strategy) +':'+ str(type(strategy))+','+str(name) +':'+ str(type(name))+','+str(amount) +':'+ str(type(amount))+','+str(PnL) +':'+ str(type(PnL))+','+str(timeseries) +':'+ str(type(timeseries))+')')
