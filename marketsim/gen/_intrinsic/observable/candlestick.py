from marketsim import _, event, context

from marketsim.gen._out._constant import constant
from marketsim.ops._all import CandleStick

from marketsim.gen._out._intrinsic_base.observable.candlestick import CandleSticks_Base

class CandleSticks_Impl(CandleSticks_Base):

    def __init__(self):
        self._event = event.subscribe(self.source, _(self)._update, self)
        event.subscribe(event.Every(constant(self.timeframe)), _(self)._flush, self)
        self.reset()
        self._mean = self.source.Cumulative.Avg
        self._stddev = self.source.Cumulative.StdDev

    @property
    def attributes(self):
        return {}

    _internals = ["_mean", '_stddev']

    def reset(self):
        self._last = None
        self._open = None
        self._min = None
        self._max = None
        self._close = None

    def _flush(self, _):
        last = CandleStick(self._open, self._close,
                           self._min, self._max,
                           self._mean(), self._stddev()) \
                if self._open is not None else None
        self.reset()
        self._last = last
        self.fire(self)

    def _update(self, _):
        x = self.source()
        if x is not None:
            if self._open is None:
                self._open = x
                self._max = x
                self._min = x
                context.reset(self._mean)
                context.reset(self._stddev)
            if self._min > x: self._min = x
            if self._max < x: self._max = x
            self._close = x

    def __call__(self):
        return self._last