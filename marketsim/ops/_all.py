from marketsim import types, event
import marketsim
from marketsim.gen._out._iobservable import IObservable

Observable = types.Factory('Observable', '''(IObservable[%(T)s], event.Conditional_Impl):''', globals())

Observable[int]._types.append(IObservable[float])
Observable[int]._types.append(IObservable[object])
Observable[float]._types.append(IObservable[object])

import collections

from marketsim.gen._out._icandlestick import ICandleStick

class CandleStick(collections.namedtuple("CandleStick", [
                                                     "open", "close",
                                                     "min", "max",
                                                     "mean", "stddev"
                                     ]), ICandleStick):

    pass
