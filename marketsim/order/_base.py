from marketsim import Event, types

class Base(types.IOrder):
    """ Base class for market and limit orders.
    Responsible for:
    - tracking order's volume
    - keeping order cancellation flag (does it needed for market orders???)
    - notifying order listeners about order matching
    TBD: split into Cancelable, HavingVolume base classes
    """

    def __init__(self, side, volume, owner = None, volumeFilled = 0):
        """ Initializes order by volume to trade
        """
        self._volumeUnmatched = volume
        self._volumeFilled = 0
        self._side = side
        self._cancelled = False
        self._owner = owner
        
    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self, value):
        self._owner = value
        
    @property
    def side(self):
        return self._side
        
    def copyTo(self, dst):
        dst._volumeUnmatched = self._volumeUnmatched
        dst._volumeFilled = self._volumeFilled
        dst._side = self._side
        dst._cancelled = self._cancelled
        
    def __str__(self):
        return "%s_%s[%d/%d]" % (type(self).__name__, self._side, self._volumeUnmatched, self.volumeTotal)

    def __repr__(self):
        return self.__str__()

    @property
    def volumeTotal(self):
        return self.volumeFilled + self.volumeUnmatched
    
    @property
    def volumeFilled(self):
        return self._volumeFilled

    @property
    def volumeUnmatched(self):
        """ Volume to trade
        """
        return self._volumeUnmatched

    @property
    def signedVolumeUnmatched(self):
        return self._side.makeVolumeSigned(self._volume)
    
    @property
    def empty(self):
        """ Volume is empty iff its volume is 0
        """
        return self.volumeUnmatched == 0

    @property
    def cancelled(self):
        """ Is order cancelled
        """
        return self._cancelled
    

    def cancel(self):
        """ Marks order as cancelled. Notifies the order book about it
        """
        if not self._cancelled:
            self._cancelled = True
            self.owner.onOrderDisposed(self)

    #--------------------------------- these methods are to be called by order book
            
    def charge(self, price): 
        self.owner.onOrderCharged(price)

    def onMatchedWith(self, price, volume):
        """ Called when the order is matched with another order
        price - price at which the match was done
        volume - volume of the match.
        In this method we correct order volume and P&L 
        and notify order listener about the match
        """
        self._volumeUnmatched -= volume
        self._volumeFilled += volume
        self.owner.onOrderMatched(self, price, volume)
        if self.empty:
            self.cancel()

    def __hash__(self):
        return id(self)
