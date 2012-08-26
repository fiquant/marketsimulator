class Side:
    """ Enumeration representing trade side of an order
    TBD: Sell and Buy should be literals of some class for readability reasons
    """
    Sell = 0
    Buy = 1
    
    @staticmethod
    def opposite(side):
        """ Returns side opposite to 'side'
        """
        return 1 - side


class Event(object):
    """ Multicast event
    
    Keeps a set of callable listeners 
    """

    def __init__(self):
        self._listeners = set()
        
    def __iadd__(self, listener):
        """ Adds 'listener' to the listeners set
        """
        self._listeners.add(listener)
        return self
        
    def advise(self, listener):
        """ Adds 'listener' to the listeners set
        """
        self += listener
        
    def fire(self, *args):
        """ Calls all listeners passing *args to them
        """
        for x in self._listeners:
            x(*args)
                    
