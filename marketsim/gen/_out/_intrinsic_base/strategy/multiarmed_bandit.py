class MultiarmedBandit2_Base(object):
    def get_strategies(self):
        return self.__strategies
    
    def set_strategies(self, value):
        self.__strategies = value
    
    strategies = property(get_strategies, set_strategies)
    def get_account(self):
        return self.__account
    
    def set_account(self, value):
        self.__account = value
    
    account = property(get_account, set_account)
    def get_weight(self):
        return self.__weight
    
    def set_weight(self, value):
        self.__weight = value
    
    weight = property(get_weight, set_weight)
    def get_normalizer(self):
        return self.__normalizer
    
    def set_normalizer(self, value):
        self.__normalizer = value
    
    normalizer = property(get_normalizer, set_normalizer)
    def get_corrector(self):
        return self.__corrector
    
    def set_corrector(self, value):
        self.__corrector = value
    
    corrector = property(get_corrector, set_corrector)
