from marketsim.order import OrderBase

class Volume(object):
    def __init__(self, v):
        self._volume = v

    hasPrice = False

    @property
    def packed(self):
        return self._volume,

class PriceVolume(object):

    def __init__(self, p, v):
        self._price = p
        self._volume = v

    hasPrice = True

    @property
    def packed(self):
        return self._price, self._volume

def unpack(args):
    return PriceVolume(*args) if len(args) == 2 else Volume(*args)

class IcebergOrder(OrderBase):

    def __init__(self, volumeLimit, orderFactory, *args):
        self._args = unpack(args)
        OrderBase.__init__(self, self._args._volume)
        self._volumeLimit = volumeLimit
        self._orderFactory = orderFactory
        self._current = None

    @property
    def price(self):  # NB! defined only for limit orders
        assert self._args.hasPrice
        return self._args._price

    def onMatchedWith(self, other, pv):
        self.notifyOnMatched(other, pv)
        if self._current.empty:
            self._PnL += self._current.PnL
            self.tryToResend()

    def cancel(self):
        OrderBase.cancel(self)
        if self._current:
            self._current.cancel()

    @property
    def PnL(self):
        return self._PnL + (self._current.PnL if self._current else 0)

    @property
    def volume(self):
        return self._volume + (self._current.volume if self._current else 0)

    def tryToResend(self):
        if self._volume > 0:
            v = min(self._volumeLimit, self._volume)
            self._args._volume = v
            self._volume -= v
            self._current = self._orderFactory(*self._args.packed)
            self._current.on_matched.add(lambda myOrder, otherOrder, pv: self.onMatchedWith(otherOrder, pv))
            self._book.process(self._current)
        else:
            self._current = None

    def processIn(self, book):
        self._book = book
        self.tryToResend()

def iceberg(volumeLimit, orderFactory):
    def inner(*args):
        return IcebergOrder(volumeLimit, orderFactory, *args)
    return inner