class Div_Base(object):
    def get_x(self):
        return self._back_x
    
    def set_x(self, value):
        self._back_x = value
        self.on_x_set(value)
    
    x = property(get_x, set_x)
    def on_x_set(self, value):
        pass
    
    def get_y(self):
        return self._back_y
    
    def set_y(self, value):
        self._back_y = value
        self.on_y_set(value)
    
    y = property(get_y, set_y)
    def on_y_set(self, value):
        pass
    
class NotEqual_Base(object):
    def get_x(self):
        return self._back_x
    
    def set_x(self, value):
        self._back_x = value
        self.on_x_set(value)
    
    x = property(get_x, set_x)
    def on_x_set(self, value):
        pass
    
    def get_y(self):
        return self._back_y
    
    def set_y(self, value):
        self._back_y = value
        self.on_y_set(value)
    
    y = property(get_y, set_y)
    def on_y_set(self, value):
        pass
    
class LessEqual_Base(object):
    def get_x(self):
        return self._back_x
    
    def set_x(self, value):
        self._back_x = value
        self.on_x_set(value)
    
    x = property(get_x, set_x)
    def on_x_set(self, value):
        pass
    
    def get_y(self):
        return self._back_y
    
    def set_y(self, value):
        self._back_y = value
        self.on_y_set(value)
    
    y = property(get_y, set_y)
    def on_y_set(self, value):
        pass
    
class GreaterEqual_Base(object):
    def get_x(self):
        return self._back_x
    
    def set_x(self, value):
        self._back_x = value
        self.on_x_set(value)
    
    x = property(get_x, set_x)
    def on_x_set(self, value):
        pass
    
    def get_y(self):
        return self._back_y
    
    def set_y(self, value):
        self._back_y = value
        self.on_y_set(value)
    
    y = property(get_y, set_y)
    def on_y_set(self, value):
        pass
    
class Negate_Base(object):
    def get_x(self):
        return self._back_x
    
    def set_x(self, value):
        self._back_x = value
        self.on_x_set(value)
    
    x = property(get_x, set_x)
    def on_x_set(self, value):
        pass
    
class Less_Base(object):
    def get_x(self):
        return self._back_x
    
    def set_x(self, value):
        self._back_x = value
        self.on_x_set(value)
    
    x = property(get_x, set_x)
    def on_x_set(self, value):
        pass
    
    def get_y(self):
        return self._back_y
    
    def set_y(self, value):
        self._back_y = value
        self.on_y_set(value)
    
    y = property(get_y, set_y)
    def on_y_set(self, value):
        pass
    
class Sub_Base(object):
    def get_x(self):
        return self._back_x
    
    def set_x(self, value):
        self._back_x = value
        self.on_x_set(value)
    
    x = property(get_x, set_x)
    def on_x_set(self, value):
        pass
    
    def get_y(self):
        return self._back_y
    
    def set_y(self, value):
        self._back_y = value
        self.on_y_set(value)
    
    y = property(get_y, set_y)
    def on_y_set(self, value):
        pass
    
class Add_Base(object):
    def get_x(self):
        return self._back_x
    
    def set_x(self, value):
        self._back_x = value
        self.on_x_set(value)
    
    x = property(get_x, set_x)
    def on_x_set(self, value):
        pass
    
    def get_y(self):
        return self._back_y
    
    def set_y(self, value):
        self._back_y = value
        self.on_y_set(value)
    
    y = property(get_y, set_y)
    def on_y_set(self, value):
        pass
    
class Greater_Base(object):
    def get_x(self):
        return self._back_x
    
    def set_x(self, value):
        self._back_x = value
        self.on_x_set(value)
    
    x = property(get_x, set_x)
    def on_x_set(self, value):
        pass
    
    def get_y(self):
        return self._back_y
    
    def set_y(self, value):
        self._back_y = value
        self.on_y_set(value)
    
    y = property(get_y, set_y)
    def on_y_set(self, value):
        pass
    
class Condition_Base(object):
    def get_cond(self):
        return self._back_cond
    
    def set_cond(self, value):
        self._back_cond = value
        self.on_cond_set(value)
    
    cond = property(get_cond, set_cond)
    def on_cond_set(self, value):
        pass
    
    def get_ifpart(self):
        return self._back_ifpart
    
    def set_ifpart(self, value):
        self._back_ifpart = value
        self.on_ifpart_set(value)
    
    ifpart = property(get_ifpart, set_ifpart)
    def on_ifpart_set(self, value):
        pass
    
    def get_elsepart(self):
        return self._back_elsepart
    
    def set_elsepart(self, value):
        self._back_elsepart = value
        self.on_elsepart_set(value)
    
    elsepart = property(get_elsepart, set_elsepart)
    def on_elsepart_set(self, value):
        pass
    
class Equal_Base(object):
    def get_x(self):
        return self._back_x
    
    def set_x(self, value):
        self._back_x = value
        self.on_x_set(value)
    
    x = property(get_x, set_x)
    def on_x_set(self, value):
        pass
    
    def get_y(self):
        return self._back_y
    
    def set_y(self, value):
        self._back_y = value
        self.on_y_set(value)
    
    y = property(get_y, set_y)
    def on_y_set(self, value):
        pass
    
class Mul_Base(object):
    def get_x(self):
        return self._back_x
    
    def set_x(self, value):
        self._back_x = value
        self.on_x_set(value)
    
    x = property(get_x, set_x)
    def on_x_set(self, value):
        pass
    
    def get_y(self):
        return self._back_y
    
    def set_y(self, value):
        self._back_y = value
        self.on_y_set(value)
    
    y = property(get_y, set_y)
    def on_y_set(self, value):
        pass
    
