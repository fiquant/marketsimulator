class BreaksAtChanges_Base(object):
    @property
    def source(self):
        return self.__source
    
    @source.setter
    def source(self, value):
        self.__source = value
    
