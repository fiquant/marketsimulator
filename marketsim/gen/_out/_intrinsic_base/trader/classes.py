class SingleAsset_Base(object):
    def get_orderBook(self):
        return self._back_orderBook
    
    def set_orderBook(self, value):
        self._back_orderBook = value
        self.on_orderBook_set(value)
    
    orderBook = property(get_orderBook, set_orderBook)
    def on_orderBook_set(self, value):
        pass
    
    def get_strategy(self):
        return self._back_strategy
    
    def set_strategy(self, value):
        self._back_strategy = value
        self.on_strategy_set(value)
    
    strategy = property(get_strategy, set_strategy)
    def on_strategy_set(self, value):
        pass
    
    def get_name(self):
        return self._back_name
    
    def set_name(self, value):
        self._back_name = value
        self.on_name_set(value)
    
    name = property(get_name, set_name)
    def on_name_set(self, value):
        pass
    
    def get_amount(self):
        return self._back_amount
    
    def set_amount(self, value):
        self._back_amount = value
        self.on_amount_set(value)
    
    amount = property(get_amount, set_amount)
    def on_amount_set(self, value):
        pass
    
    def get_PnL(self):
        return self._back_PnL
    
    def set_PnL(self, value):
        self._back_PnL = value
        self.on_PnL_set(value)
    
    PnL = property(get_PnL, set_PnL)
    def on_PnL_set(self, value):
        pass
    
    def get_timeseries(self):
        return self._back_timeseries
    
    def set_timeseries(self, value):
        self._back_timeseries = value
        self.on_timeseries_set(value)
    
    timeseries = property(get_timeseries, set_timeseries)
    def on_timeseries_set(self, value):
        pass
    
class MultiAsset_Base(object):
    def get_traders(self):
        return self._back_traders
    
    def set_traders(self, value):
        self._back_traders = value
        self.on_traders_set(value)
    
    traders = property(get_traders, set_traders)
    def on_traders_set(self, value):
        pass
    
    def get_strategy(self):
        return self._back_strategy
    
    def set_strategy(self, value):
        self._back_strategy = value
        self.on_strategy_set(value)
    
    strategy = property(get_strategy, set_strategy)
    def on_strategy_set(self, value):
        pass
    
    def get_name(self):
        return self._back_name
    
    def set_name(self, value):
        self._back_name = value
        self.on_name_set(value)
    
    name = property(get_name, set_name)
    def on_name_set(self, value):
        pass
    
    def get_PnL(self):
        return self._back_PnL
    
    def set_PnL(self, value):
        self._back_PnL = value
        self.on_PnL_set(value)
    
    PnL = property(get_PnL, set_PnL)
    def on_PnL_set(self, value):
        pass
    
    def get_timeseries(self):
        return self._back_timeseries
    
    def set_timeseries(self, value):
        self._back_timeseries = value
        self.on_timeseries_set(value)
    
    timeseries = property(get_timeseries, set_timeseries)
    def on_timeseries_set(self, value):
        pass
    
