from marketsim import Side

class OrderBase(object):

   def __init__(self, volume):
      self._volume = volume
      self._cancelled = False
      self._PnL = 0
      self.on_matched = set()

   def __str__(self):
      return type(self).__name__ + "(volume=" + str(self.volume) + ", P&L="+str(self.PnL)+")"

   def __repr__(self):
      return self.__str__()

   @property
   def volume(self):
      return self._volume

   @property
   def empty(self):
      return self.volume == 0

   @property
   def cancelled(self):
      return self._cancelled

   def cancel(self):
      self._cancelled = True

   def notifyOnMatched(self, other, (price, volume)):
      for x in self.on_matched:
          x(self, other, (price, volume))


   """
   Called on order matching
   other - other order
   price - price at which the match was done
   volume - volume of the match
   """
   def onMatchedWith(self, other, (price,volume)):
      self._volume -= volume
      self._PnL += volume * price
      self.notifyOnMatched(other, (price, volume))


class LimitOrderBase(OrderBase):

   def __init__(self, price, volume):
      OrderBase.__init__(self, volume)
      self._price = price

   def __str__(self):
      return type(self).__name__ + "(Price=" + str(self.price) + ", volume=" + str(self.volume) + ", P&L="+str(self.PnL)+")"

   def processIn(self, orderBook):
      orderBook.processLimitOrder(self)

   @property
   def price(self):
      return self._price

   @price.setter
   def price(self, value):
      self._price = value

   """
   Matches the order with another one
   Returns True iff this order is completely matched
   """
   def matchWith(self, other):
      if other.canBeMatched(self):
         v = min(self.volume, other.volume)
         assert v > 0
         p = self.price
         self.onMatchedWith(other, (p,v))
         other.onMatchedWith(self, (p,v))
      return self.empty

class BuySideOrderBase(object):

   # Returns P&L for the order
   # negative for buy orders
   @property
   def PnL(self):
      return -self._PnL

   side = Side.Buy

class SellSideOrderBase(object):

   # Returns P&L for the order
   # positive for sell orders
   @property
   def PnL(self):
      return +self._PnL

   side = Side.Sell

class MarketOrderBase(OrderBase):

   def __init__(self, volume):
      OrderBase.__init__(self, volume)

   def processIn(self, orderBook):
      orderBook.processMarketOrder(self)

   def canBeMatched(self, other):
       assert other.side == Side.opposite(self.side)
       return True

class MarketOrderBuy(MarketOrderBase, BuySideOrderBase):

   def __init__(self, volume):
      MarketOrderBase.__init__(self, volume)

class MarketOrderSell(MarketOrderBase, SellSideOrderBase):

   def __init__(self, volume):
      MarketOrderBase.__init__(self, volume)

def MarketOrderT(side):
    return MarketOrderSell if side==Side.Sell else MarketOrderBuy

class LimitOrderBuy(LimitOrderBase, BuySideOrderBase):

   def __init__(self, price, volume):
      LimitOrderBase.__init__(self, price, volume)

   def canBeMatched(self, other):
      assert other.side == Side.Sell
      return self.price >= other.price


class LimitOrderSell(LimitOrderBase, SellSideOrderBase):

   def __init__(self, price, volume):
      LimitOrderBase.__init__(self, price, volume)

   def canBeMatched(self, other):
      assert other.side == Side.Buy
      return self.price <= other.price

def LimitOrderT(side):
    return LimitOrderSell if side==Side.Sell else LimitOrderBuy

