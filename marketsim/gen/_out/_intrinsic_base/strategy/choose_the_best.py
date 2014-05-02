class ChooseTheBest_Base(object):
    def get_strategies(self):
        return self._back_strategies
    
    def set_strategies(self, value):
        self._back_strategies = value
        self.on_strategies_set(value)
    
    strategies = property(get_strategies, set_strategies)
    def on_strategies_set(self, value):
        pass
    
    def get_account(self):
        return self._back_account
    
    def set_account(self, value):
        self._back_account = value
        self.on_account_set(value)
    
    account = property(get_account, set_account)
    def on_account_set(self, value):
        pass
    
    def get_performance(self):
        return self._back_performance
    
    def set_performance(self, value):
        self._back_performance = value
        self.on_performance_set(value)
    
    performance = property(get_performance, set_performance)
    def on_performance_set(self, value):
        pass
    
    def bind_impl(self, ctx):
        pass
    
    def reset(self):
        pass
    
