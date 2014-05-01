class Event_Base(object):
    pass
    def bind_impl(self, ctx):
        pass
    
    def reset(self):
        pass
    
class After_Base(object):
    def get_delay(self):
        return self._back_delay
    
    def set_delay(self, value):
        self._back_delay = value
        self.on_delay_set(value)
    
    delay = property(get_delay, set_delay)
    def on_delay_set(self, value):
        pass
    
    def bind_impl(self, ctx):
        pass
    
    def reset(self):
        pass
    
class Subscription_Base(object):
    def get_event(self):
        return self._back_event
    
    def set_event(self, value):
        self._back_event = value
        self.on_event_set(value)
    
    event = property(get_event, set_event)
    def on_event_set(self, value):
        pass
    
    def get_listener(self):
        return self._back_listener
    
    def set_listener(self, value):
        self._back_listener = value
        self.on_listener_set(value)
    
    listener = property(get_listener, set_listener)
    def on_listener_set(self, value):
        pass
    
    def bind_impl(self, ctx):
        pass
    
    def reset(self):
        pass
    
class GreaterThan_Base(object):
    def get_bound(self):
        return self._back_bound
    
    def set_bound(self, value):
        self._back_bound = value
        self.on_bound_set(value)
    
    bound = property(get_bound, set_bound)
    def on_bound_set(self, value):
        pass
    
    def get_target(self):
        return self._back_target
    
    def set_target(self, value):
        self._back_target = value
        self.on_target_set(value)
    
    target = property(get_target, set_target)
    def on_target_set(self, value):
        pass
    
    def bind_impl(self, ctx):
        pass
    
    def reset(self):
        pass
    
class Every_Base(object):
    def get_intervalFunc(self):
        return self._back_intervalFunc
    
    def set_intervalFunc(self, value):
        self._back_intervalFunc = value
        self.on_intervalFunc_set(value)
    
    intervalFunc = property(get_intervalFunc, set_intervalFunc)
    def on_intervalFunc_set(self, value):
        pass
    
    def bind_impl(self, ctx):
        pass
    
    def reset(self):
        pass
    
class CurrentTime_Base(object):
    pass
    def bind_impl(self, ctx):
        pass
    
    def reset(self):
        pass
    
class LessThan_Base(object):
    def get_bound(self):
        return self._back_bound
    
    def set_bound(self, value):
        self._back_bound = value
        self.on_bound_set(value)
    
    bound = property(get_bound, set_bound)
    def on_bound_set(self, value):
        pass
    
    def get_target(self):
        return self._back_target
    
    def set_target(self, value):
        self._back_target = value
        self.on_target_set(value)
    
    target = property(get_target, set_target)
    def on_target_set(self, value):
        pass
    
    def bind_impl(self, ctx):
        pass
    
    def reset(self):
        pass
    
