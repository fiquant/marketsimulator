class VolumeLevelProxy_Base(object):
    def get_source(self):
        return self._back_source
    
    def set_source(self, value):
        self._back_source = value
        self.on_source_set(value)
    
    source = property(get_source, set_source)
    def on_source_set(self, value):
        pass
    
    def get_idx(self):
        return self._back_idx
    
    def set_idx(self, value):
        self._back_idx = value
        self.on_idx_set(value)
    
    idx = property(get_idx, set_idx)
    def on_idx_set(self, value):
        pass
    
    def bind_impl(self, ctx):
        pass
    
    def reset(self):
        pass
    
class CSV_Base(object):
    def get_directory(self):
        return self._back_directory
    
    def set_directory(self, value):
        self._back_directory = value
        self.on_directory_set(value)
    
    directory = property(get_directory, set_directory)
    def on_directory_set(self, value):
        pass
    
    def get_source(self):
        return self._back_source
    
    def set_source(self, value):
        self._back_source = value
        self.on_source_set(value)
    
    source = property(get_source, set_source)
    def on_source_set(self, value):
        pass
    
    def get_attributes(self):
        return self._back_attributes
    
    def set_attributes(self, value):
        self._back_attributes = value
        self.on_attributes_set(value)
    
    attributes = property(get_attributes, set_attributes)
    def on_attributes_set(self, value):
        pass
    
    def bind_impl(self, ctx):
        pass
    
    def reset(self):
        pass
    
class Graph_Base(object):
    def get_name(self):
        return self._back_name
    
    def set_name(self, value):
        self._back_name = value
        self.on_name_set(value)
    
    name = property(get_name, set_name)
    def on_name_set(self, value):
        pass
    
    def bind_impl(self, ctx):
        pass
    
    def reset(self):
        pass
    
