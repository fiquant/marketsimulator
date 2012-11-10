class SellSide(object):
    
    id = 0
    
    @property
    def opposite(self):
        return Side.Buy

    @staticmethod
    def better(x, y):
        """ Returns True iff signed price 'x' is more attractive than signed price 'y'
        """
        return x < y
    
    @staticmethod
    def makePriceSigned(price):
        """ Leaves price of something on sell side positive
        """
        return +price
    
class BuySide(object):
    
    id = 1

    @property
    def opposite(self):
        return Side.Sell
    
    @staticmethod
    def better(x, y):
        """ Returns True iff signed price 'x' is more attractive than signed price 'y'
        """
        return x > y
    
    @staticmethod
    def makePriceSigned(price):
        """ Makes price of something on buy side negative
        """
        return -price
    

class Side:
    """ Enumeration representing trade side of an order
    """
    Sell = SellSide()
    Buy = BuySide()
    
    @staticmethod
    def byId(x):
        return Side.Buy if x else Side.Sell  
    


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

def getLabel(x):
    """ Returns a printable label for x
    We try to access 'label' field of the object 
    If it doesn't exists, we return the object id string
    TBD: add label field to all classes  
    """
    return x.label if 'label' in dir(x) else "#"+str(id(x))
                    
