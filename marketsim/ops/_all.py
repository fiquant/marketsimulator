from marketsim import types, event


import collections

from marketsim.gen._out._icandlestick import ICandleStick

class CandleStick(collections.namedtuple("CandleStick", [
                                                     "open", "close",
                                                     "min", "max",
                                                     "mean", "stddev"
                                     ]), ICandleStick):

    pass
