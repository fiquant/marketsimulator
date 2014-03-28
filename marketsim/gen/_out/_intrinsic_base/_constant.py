class Constant_Base(object):
    def get_x(self):
        return self._back_x
    
    def set_x(self, value):
        self._back_x = value
        self.on_x_set(value)
    
    x = property(get_x, set_x)
    def on_x_set(self, value):
        pass
    
class Null_Base(object):
    pass
class False_Base(object):
    pass
class True_Base(object):
    pass
