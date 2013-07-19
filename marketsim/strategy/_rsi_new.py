from marketsim import (registry, meta, bind, types, Side, mathutils, order,
                        Event, orderbook, event, observable, scheduler,  _)


from _enter_exit import EnterExit
from _wrap import wrapper2

class _RSInew_Impl(EnterExit):

    def __init__(self, threshold = 30):
        EnterExit.__init__(self)
        self.threshold = threshold
        self._rsi = observable.RSI(orderbook.OfTrader(), 10, 1./14)

    def bind(self, context):
        EnterExit.bind(self, context)


    def checkEnter(self):
        # if self._rsi is None:
        #     return

        if self._rsi is not None:
            print self._rsi()
        rsi = 50 # self._rsi()

        if rsi > 100 - self.threshold:
            self.sell()
        elif rsi < self.threshold:
            self.buy()

    def checkExit(self):
        rsi = self._rsi

        if rsi < self.threshold and self.sideEntered is Side.Sell:
            self.buy()
        elif rsi > 100 - self.threshold and self.sideEntered is Side.Buy:
            self.sell()

exec wrapper2("RSInew",
              """
              """,
              [])