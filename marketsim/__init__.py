class Side:
    Sell = 0
    Buy = 1
    
    @staticmethod
    def opposite(side):
        return 1 - side

class Event(object):

    def __init__(self):
        self._listeners = set()
        
    def __iadd__(self, listener):
        if listener is None:
            pass
        self._listeners.add(listener)
        return self
        
    def advise(self, listener):
        self += listener
        
    def fire(self, *what):
        for x in self._listeners:
            x(*what)
                    
