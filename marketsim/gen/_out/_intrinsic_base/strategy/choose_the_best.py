class ChooseTheBest_Base(object):
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
    def get_performance(self):
        return self.__performance
    
    def set_performance(self, value):
        self.__performance = value
    
    performance = property(get_performance, set_performance)
