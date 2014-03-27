class ChooseTheBest_Base(object):
    @property
    def strategies(self):
        return self.__strategies
    
    @strategies.setter
    def strategies(self, value):
        self.__strategies = value
    
    @property
    def account(self):
        return self.__account
    
    @account.setter
    def account(self, value):
        self.__account = value
    
    @property
    def performance(self):
        return self.__performance
    
    @performance.setter
    def performance(self, value):
        self.__performance = value
    
