import sys
sys.path.append(r'../..')

from marketsim import (signal, strategy, orderbook, mathutils, 
                       Side, types, ops, defs, _)
from marketsim import observable as obs
from common import expose, Constant

class DesiredVolumeBase(obs.IndicatorBaseT[float]):
    def __init__(self, source):
        from marketsim import scheduler
        timer = scheduler.Timer(ops.constant(1))
        IndicatorBase.__init__(self, timer, source, {'smooth': True})
        self._position = 0

    @property
    def label(self):
        return "volume based on " + self._dataSource.label

    @property
    def val(self):
        return self._dataSource()

    def __call__(self):
        volume = self.getVolume() if self._dataSource is not None else None
        self.updatePosition(volume, self.val)
        return self._position

    def getVolume(self):
        return 0

    def updatePosition(self, volume, val):
        self._position = volume if volume is not None else self._position

class BuyLowSellHighVolume(DesiredVolumeBase):

    def __init__(self, source, LO=30, HI=70):
        DesiredVolumeBase.__init__(self, source)
        self._lo = LO
        self._hi = HI
        self._brokenLO = False
        self._brokenHI = False

    @property
    def HI(self):
        return self._hi

    @property
    def LO(self):
        return self._lo

    @property
    def breakHI(self):
        if self.val > self.HI:
            if not self._brokenHI:
                self._brokenHI = True
                return True
            else:
                return False
        else:
            self._brokenHI = False
            return False

    @property
    def breakLO(self):
        if self.val < self.LO:
            if not self._brokenLO:
                self._brokenLO = True
                return True
            else:
                return False
        else:
            self._brokenLO = False
            return False

    def getVolume(self):
        volume = None
        if self.breakHI:
            volume = -1
        elif self.breakLO:
            volume = 1

        return volume


# class _observable_label(ops.identity):
#
#     def __init__(self, target, label, orderbook, timeframe):
#         ops.identity.__init__(self, target)
#         self._orderbook = orderbook
#         self._timeframe = timeframe
#         self._label = label
#
#     @property
#     def label(self):
#         return self._label + "_{" + self._orderbook.label + "}^{" + str(self._timeframe) + "}"



@expose("Desired position", __name__, only_veusz=True)
def DesiredPosition(ctx):

    const = ops.constant

    book = orderbook.OfTrader()

    # Values to observe
    asks = obs.BidPrice(book)
    bids = obs.AskPrice(book)
    price = obs.MidPrice(book)


    rsi_signal = BuyLowSellHighVolume(obs.RSI(book, 10, 1./14))

    def indicator(sources, f=(lambda x: x), window=1, name=None):
        return obs.OnEveryDt(1, obs.aggregate(sources, f, window, name))


    # Max Price
    def MaxMinPrice(price, window=20):
        MaxPrice = indicator(price, max, window, name="MaxPrice"+str(window))
        MinPrice = indicator(price, min, window, name="MinPrice"+str(window))
        return [MaxPrice, MinPrice]

    # Bid-Ask spread
    def BidAskSpread(bids, asks):
        return [indicator([bids, asks], lambda (bid, ask): bid-ask, name="BidAskspread")]

    # Moving Average
    def MovingAverageSpread(price):
        MA = lambda p, n: sum(p[-n:])/len(p[-n:])
        MAspread_f = lambda p: MA(p, 10) - MA(p, 20)
        MAspread = indicator(price, MAspread_f, window=20, name="MAspread")
        return [MAspread]

    # Exponential Moving Average
    def EWMASpread(price):
        EWMA = lambda alpha: (lambda p: reduce(lambda x, y: x + (y-x)*alpha, p, 0))
        EWMA_fast = EWMA(0.15)
        EWMA_slow = EWMA(0.015)
        EWMAspread_f = lambda p: EWMA_fast(p) - EWMA_slow(p)
        EWMA_spread = indicator(price, EWMAspread_f, window=20, name="EWMAspread")
        return [EWMA_spread]

    # Relative Strength Index
    def RSI(price):
        EWMA = lambda alpha: (lambda p: reduce(lambda x, y: x + (y-x)*alpha, p, 0))
        up = lambda p: [max(0, x-y) for x, y in zip(p[1:], p[:-1])]
        down = lambda p: [max(0, y-x) for x, y in zip(p[1:], p[:-1])]
        up_ewma = lambda p: EWMA(1./14)(up(p))
        down_ewma = lambda p: EWMA(1./14)(down(p))
        rs = lambda p: up_ewma(p) / down_ewma(p) if down_ewma(p) > 0 else 0
        rsi = lambda p: 100 - 100./(1+rs(p))
        RSI_value = indicator(price, rsi, window=30, name="RSI")
        return [RSI_value]

    # Bollinger Bands
    def BollingerBands(price):
        from math import sqrt
        MA = lambda p, n: sum(p[-n:])/len(p[-n:])
        ma = obs.aggregate(price, lambda p: MA(p, 20), window=20, name="MA20")
        std_dev = obs.aggregate([price, ma], lambda x: sqrt(sum([(v[1]-v[0])**2 for v in x])/len(x)), name="MA20sd", window=20)
        STDhi = indicator([ma, std_dev], lambda (m, s): m + 2*s, name="bollingerHI")
        STDmi = indicator(ma, name="bollingerMI")
        STDlo = indicator([ma, std_dev], lambda (m, s): m - 2*s, name="bollingerLO")
        return [STDhi, STDmi, STDlo]

    # MACD
    def MACD(price):
        EWMA = lambda alpha: (lambda p: reduce(lambda x, y: x + (y-x)*alpha, p, 0))
        ewma12 = obs.aggregate(price, EWMA(2./13), window=12, name="EWMA12")
        ewma26 = obs.aggregate(price, EWMA(2./27), window=26, name="EWMA26")
        macd_signal = obs.aggregate([ewma12, ewma26], lambda (x, y): x-y, name="MACDsignal")
        macd_line = obs.OnEveryDt(1, macd_signal)
        signal_line = indicator(macd_signal, EWMA(2./10), window=9, name="signal_line")
        MACD = [macd_line, signal_line]
        return MACD

    observables = BollingerBands(price) + RSI(price) + MACD(price) + MaxMinPrice(price)

    charts = [(o, ctx.price_graph) for o in observables]


    return [
        ctx.makeTrader_A(strategy.LiquidityProvider(volumeDistr=const(4)), "liquidity"),
        
        ctx.makeTrader_A(strategy.DesiredPosition(rsi_signal), "desired_position",
                         [(rsi_signal, ctx.amount_graph)] + charts)
    ]    
