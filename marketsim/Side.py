class _SellSide(object):
    """ Tag class representing the sell side 
    """
    
    id = 0
    
    @property
    def opposite(self):
        return Buy

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
    
class _BuySide(object):
    
    id = 1

    @property
    def opposite(self):
        return Sell
    
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
    

Sell = _SellSide()
Buy = _BuySide()

def byId(x):
    return Buy if x else Sell  
