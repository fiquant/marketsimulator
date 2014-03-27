class MultiarmedBandit2_Base(object):
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
    def weight(self):
        return self.__weight
    
    @weight.setter
    def weight(self, value):
        self.__weight = value
    
    @property
    def normalizer(self):
        return self.__normalizer
    
    @normalizer.setter
    def normalizer(self, value):
        self.__normalizer = value
    
    @property
    def corrector(self):
        return self.__corrector
    
    @corrector.setter
    def corrector(self, value):
        self.__corrector = value
    
