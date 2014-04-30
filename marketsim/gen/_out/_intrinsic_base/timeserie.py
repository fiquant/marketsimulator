class ToRecord_Base(object):
    def get_source(self):
        return self._back_source
    
    def set_source(self, value):
        self._back_source = value
        self.on_source_set(value)
    
    source = property(get_source, set_source)
    def on_source_set(self, value):
        pass
    
    def get_graph(self):
        return self._back_graph
    
    def set_graph(self, value):
        self._back_graph = value
        self.on_graph_set(value)
    
    graph = property(get_graph, set_graph)
    def on_graph_set(self, value):
        pass
    
    def get__digitsToShow(self):
        return self._back__digitsToShow
    
    def set__digitsToShow(self, value):
        self._back__digitsToShow = value
        self.on__digitsToShow_set(value)
    
    _digitsToShow = property(get__digitsToShow, set__digitsToShow)
    def on__digitsToShow_set(self, value):
        pass
    
    def get__smooth(self):
        return self._back__smooth
    
    def set__smooth(self, value):
        self._back__smooth = value
        self.on__smooth_set(value)
    
    _smooth = property(get__smooth, set__smooth)
    def on__smooth_set(self, value):
        pass
    
    def bind_impl(self, ctx):
        pass
    
    def reset(self):
        pass
    
class VolumeLevels_Base(object):
    def get_source(self):
        return self._back_source
    
    def set_source(self, value):
        self._back_source = value
        self.on_source_set(value)
    
    source = property(get_source, set_source)
    def on_source_set(self, value):
        pass
    
    def get_graph(self):
        return self._back_graph
    
    def set_graph(self, value):
        self._back_graph = value
        self.on_graph_set(value)
    
    graph = property(get_graph, set_graph)
    def on_graph_set(self, value):
        pass
    
    def get__digitsToShow(self):
        return self._back__digitsToShow
    
    def set__digitsToShow(self, value):
        self._back__digitsToShow = value
        self.on__digitsToShow_set(value)
    
    _digitsToShow = property(get__digitsToShow, set__digitsToShow)
    def on__digitsToShow_set(self, value):
        pass
    
    def get__smooth(self):
        return self._back__smooth
    
    def set__smooth(self, value):
        self._back__smooth = value
        self.on__smooth_set(value)
    
    _smooth = property(get__smooth, set__smooth)
    def on__smooth_set(self, value):
        pass
    
    def get__volumes(self):
        return self._back__volumes
    
    def set__volumes(self, value):
        self._back__volumes = value
        self.on__volumes_set(value)
    
    _volumes = property(get__volumes, set__volumes)
    def on__volumes_set(self, value):
        pass
    
    def get__isBuy(self):
        return self._back__isBuy
    
    def set__isBuy(self, value):
        self._back__isBuy = value
        self.on__isBuy_set(value)
    
    _isBuy = property(get__isBuy, set__isBuy)
    def on__isBuy_set(self, value):
        pass
    
    def bind_impl(self, ctx):
        pass
    
    def reset(self):
        pass
    
