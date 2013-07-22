from marketsim import (registry, meta, bind, types, Side, mathutils, order,
                        Event, orderbook, event, scheduler, observable, defs ,  _)
from marketsim.types import *
import marketsim

from _basic import Strategy
from _wrap import wrapper2

class _EnterExit_Impl(Strategy):

    def __init__(self):
        """
        """
        Strategy.__init__(self)
        self._entered = False
        self._enteredMatched = False
        self._priceEntered = 0
        self._enterTime = None
        self.sideEntered = None


    def bind(self, context):
        Strategy.bind(self, context)
        self._book = orderbook.OfTrader(self._trader)
        event.subscribe(self.eventGen, _(self).check, self, {})


    def check(self, _):
        if self._book.price is None:
            return

        if not self._entered:
            self.checkEnter()

        if self._enteredMatched:
            self.checkExit()

    def checkEnter(self):
        pass

    def checkExit(self):
        pass

    def order(self, side, volume, price=None):
        if price is None:
            orderToSend = marketsim.order.Market(side, volume)
        else:
            orderToSend = marketsim.order.Limit(side, price, volume)

        # send order
        self._event = event.subscribe(orderToSend.on_matched, self.onMatched, self, {})
        self._trader.send(orderToSend)

        if not self._entered:
            self._entered = True

        if self.sideEntered is None:
            self.sideEntered = side

    def onMatched(self, order, other, (price, volume)):
        if self._entered and order.volume == 0:
            if not self._enteredMatched:
                self._enteredMatched = True
                self._priceEntered = price
                self._volumeEntered = volume
                self._enterTime = self._scheduler.currentTime
            else:
                self._entered = False
                self._enteredMatched = False
                self.sideEntered = None
                print "bought at ", self._priceEntered, "and sold at", price

    def buy(self, volume=1, price=None):
        self.order(Side.Buy, volume, price)

    def sell(self, volume=1, price=None):
        self.order(Side.Sell, volume, price)

    @property
    def holdingTime(self):
        return self._scheduler.currentTime - self.enterTime

    @property
    def enterTime(self):
        return self._scheduler.currentTime if self._enterTime is None else self._enterTime


exec wrapper2("EnterExit",
             """
             """,
             [('eventGen', 'None', 'Event')], register = False)


class testObservable(Event):

    def __init__(self):
        Event.__init__(self)

    def bind(self, context):
        self._scheduler = context.world
        self._trader = context.trader

    def


@registry.expose(["EnterExit", "RSIter"], args=())
def RSIter():


    return EnterExit(eventGen = scheduler.Timer(mathutils.constant(1)))

