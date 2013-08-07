from marketsim import Event, types

class HasVolumeBase(object):

	def __str__(self):
		return "[%d/%d]" % (self.volumeUnmatched, self.volumeTotal)

	@property
	def volumeTotal(self):
		return self.volumeFilled + self.volumeUnmatched

	@property
	def signedVolumeUnmatched(self):
		return self.side.makeVolumeSigned(self.volumeUnmatched)
		
	@property
	def empty(self):
		""" Volume is empty iff its volume is 0
		"""
		return self.volumeUnmatched == 0

	def onMatchedWith(self, price, volume):
		""" Called when the order is matched with another order
		price - price at which the match was done
		volume - volume of the match.
		In this method we correct order volume and P&L 
		and notify order listener about the match
		"""
		self.owner.onOrderMatched(self, price, volume)
		if self.empty:
			self.cancel()
	

class HasVolume(HasVolumeBase):

	def __init__(self, volume, volumeFilled = 0):
		self._volumeUnmatched = volume
		self._volumeFilled = 0
				
	def copyTo(self, dst):
		dst._volumeUnmatched = self._volumeUnmatched
		dst._volumeFilled = self._volumeFilled
		
	@property
	def volumeFilled(self):
		return self._volumeFilled

	@property
	def volumeUnmatched(self):
		""" Volume to trade
		"""
		return self._volumeUnmatched

	def onMatchedWith(self, price, volume):
		""" Called when the order is matched with another order
		price - price at which the match was done
		volume - volume of the match.
		In this method we correct order volume and P&L 
		and notify order listener about the match
		"""
		self._volumeUnmatched -= volume
		self._volumeFilled += volume
		HasVolumeBase.onMatchedWith(self, price, volume)
			
class HasPrice(object):
	
	def __init__(self, price):
		self._price = price
		
	def copyTo(self, dst):
		dst._price = self._price
		
	@property
	def signedPrice(self):
		""" Returns "signed" price of the order:
		positive if the order is on sell side
		negative if the order is on buy side 
		"""
		return self.side.makePriceSigned(self._price)

	@property
	def price(self):
		""" Limit price of the order
		"""
		return self._price
	
	def __str__(self):
		return str(self._price)
	
	@price.setter
	def price(self, value):
		""" When an order is put into an oredr book, 
		its price might be corrected with respect to order tick size
		this function is used to notify the order about the new corrected price
		"""
		self._price = value

		
			
class HasSide(object):
	
	def __init__(self, side):
		self._side = side
		
	@property
	def side(self):
		return self._side
	
	def copyTo(self, dst):
		dst._side = self._side
		
	def __str__(self):
		return str(self._side)
	
class Cancellable(object):
	
	def __init__(self):
		self._cancelled = False

	@property
	def cancelled(self):
		""" Is order cancelled
		"""
		return self._cancelled
	

	def cancel(self):
		""" Marks order as cancelled. 
		"""
		if not self._cancelled:
			self._cancelled = True
			self.owner.onOrderDisposed(self)
			
	def copyTo(self, dst):
		dst._cancelled = self._cancelled

class Default(types.IOrder):

    def __init__(self, owner = None):
    	if not hasattr(self, 'owner'):
        	self._owner = owner
        
    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self, value):
        self._owner = value
            
    def charge(self, price): 
        self.owner.onOrderCharged(price)

    def __hash__(self):
        return id(self)


class Base(Default, HasSide, HasVolume, Cancellable):
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
        HasSide.__init__(self, side)
        HasVolume.__init__(self, volume, volumeFilled)
        Cancellable.__init__(self)
        Default.__init__(self, owner)
        
    def copyTo(self, dst):
    	HasSide.copyTo(self, dst)
    	HasVolume.copyTo(self, dst)
        Cancellable.copyTo(self, dst)
        
    def __str__(self):
        return "%s_%s[%s]" % (type(self).__name__, HasSide.__str__(self), HasVolume.__str__(self))
