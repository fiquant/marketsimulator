class MultiarmedBandit2_Base(object):
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
    
    def get_weight(self):
        return self._back_weight
    
    def set_weight(self, value):
        self._back_weight = value
        self.on_weight_set(value)
    
    weight = property(get_weight, set_weight)
    def on_weight_set(self, value):
        pass
    
    def get_normalizer(self):
        return self._back_normalizer
    
    def set_normalizer(self, value):
        self._back_normalizer = value
        self.on_normalizer_set(value)
    
    normalizer = property(get_normalizer, set_normalizer)
    def on_normalizer_set(self, value):
        pass
    
    def get_corrector(self):
        return self._back_corrector
    
    def set_corrector(self, value):
        self._back_corrector = value
        self.on_corrector_set(value)
    
    corrector = property(get_corrector, set_corrector)
    def on_corrector_set(self, value):
        pass
    
    def bind_impl(self, ctx):
        pass
    
    def reset(self):
        pass
    
