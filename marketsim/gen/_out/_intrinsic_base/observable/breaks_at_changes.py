class BreaksAtChanges_Base(object):
    def get_source(self):
        return self.__source
    
    def set_source(self, value):
        self.__source = value
    
    source = property(get_source, set_source)
