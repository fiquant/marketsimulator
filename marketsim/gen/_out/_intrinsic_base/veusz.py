class Graph_Base(object):
    def get_name(self):
        return self.__name
    
    def set_name(self, value):
        self.__name = value
    
    name = property(get_name, set_name)
