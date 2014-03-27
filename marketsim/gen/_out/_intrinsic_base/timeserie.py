class ToRecord_Base(object):
    def get_source(self):
        return self.__source
    
    def set_source(self, value):
        self.__source = value
    
    source = property(get_source, set_source)
    def get_graph(self):
        return self.__graph
    
    def set_graph(self, value):
        self.__graph = value
    
    graph = property(get_graph, set_graph)
    def get__digitsToShow(self):
        return self.___digitsToShow
    
    def set__digitsToShow(self, value):
        self.___digitsToShow = value
    
    _digitsToShow = property(get__digitsToShow, set__digitsToShow)
    def get__smooth(self):
        return self.___smooth
    
    def set__smooth(self, value):
        self.___smooth = value
    
    _smooth = property(get__smooth, set__smooth)
class VolumeLevels_Base(object):
    def get_source(self):
        return self.__source
    
    def set_source(self, value):
        self.__source = value
    
    source = property(get_source, set_source)
    def get_graph(self):
        return self.__graph
    
    def set_graph(self, value):
        self.__graph = value
    
    graph = property(get_graph, set_graph)
    def get__digitsToShow(self):
        return self.___digitsToShow
    
    def set__digitsToShow(self, value):
        self.___digitsToShow = value
    
    _digitsToShow = property(get__digitsToShow, set__digitsToShow)
    def get__smooth(self):
        return self.___smooth
    
    def set__smooth(self, value):
        self.___smooth = value
    
    _smooth = property(get__smooth, set__smooth)
    def get__volumes(self):
        return self.___volumes
    
    def set__volumes(self, value):
        self.___volumes = value
    
    _volumes = property(get__volumes, set__volumes)
    def get__isBuy(self):
        return self.___isBuy
    
    def set__isBuy(self, value):
        self.___isBuy = value
    
    _isBuy = property(get__isBuy, set__isBuy)
