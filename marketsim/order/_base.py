from marketsim import Event

class Base(object):
    """ Base class for market and limit orders.
    Responsible for:
    - tracking order's volume
    - tracking order's P&L
    - keeping order cancellation flag (does it needed for market orders???)
    - notifying order listeners about order matching
    TBD: split into Cancelable, HavingVolume base classes
    """

    def __init__(self, side, volume):
        """ Initializes order by volume to trade
        """
        self._volume = volume
        self._side = side
        self._cancelled = False
        self._PnL = 0
        # TODO: these events should be replaces by a reference to the trader
        # but in that case we'll have to introduce proxy classes for
        # remote book and virtual orders but it is ok
        self.on_matched = Event()
        self.on_charged = Event()
        
    @property
    def side(self):
        return self._side
        
    def copyTo(self, dst):
        dst._volume = self._volume
        dst._side = self._side
        dst._PnL = self._PnL
        dst._cancelled = self._cancelled

    def __str__(self):
        return type(self).__name__ + "("+self._side+", volume=" + str(self.volume) + ", P&L="+str(self.PnL)+")"

    def __repr__(self):
        return self.__str__()

    @property
    def volume(self):
        """ Volume to trade
        """
        return self._volume
    
    @property 
    def PnL(self):
        """ P&L of the order. 
        positive, if it is a sell side order
        negative, if it is a buy side order
        """
        return self.side.makePriceSigned(self._PnL)

    @property
    def empty(self):
        """ Volume is empty iff its volume is 0
        """
        return self.volume == 0

    @property
    def cancelled(self):
        """ Is order cancelled
        """
        return self._cancelled
    

    def cancel(self):
        """ Marks order as cancelled. Notifies the order book about it
        """
        self._cancelled = True

    #--------------------------------- these methods are to be called by order book
            
    def charge(self, price): 
        self.on_charged.fire(price)

    def onMatchedWith(self, other, (price,volume)):
        """ Called when the order is matched with another order
        other - other order
        price - price at which the match was done
        volume - volume of the match.
        In this method we correct order volume and P&L 
        and notify order listener about the match
        """
        self._volume -= volume
        self._PnL += volume * price
        #print "OrderMatched:", self, other, (price, volume)
        self.on_matched.fire(self, other, (price, volume))
