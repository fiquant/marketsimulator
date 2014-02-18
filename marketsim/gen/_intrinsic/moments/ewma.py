import math
from marketsim import types, registry, ops, registry, event, _, getLabel

from marketsim.gen._intrinsic.observable import fold
from marketsim.gen._out.observable._oneverydt import OnEveryDt


class EWMA_Impl(fold.Last):
    """ Exponentially weighted moving average
    """

    def __init__(self):
        """ Initializes EWMA with \alpha = alpha
        """
        from marketsim.gen._out._ievent import IEvent
        if not isinstance(self.source, IEvent):
            self.source = OnEveryDt(1, self.source)

        self._event = event.subscribe(self.source, _(self)._update, self)

        self.reset()

    def reset(self):
        self._avg = None
        self._lastValue = None
        self._lastTime = None

    @property
    def attributes(self):
        return {}

    def bind(self, context):
        self._scheduler = context.world

    def at(self, t):
        """ Returns value of the average at some time point t >= last update time
        Returns None if no data has come
        """
        return \
            self._avg + (self._lastValue - self._avg)*(1 - (1 - self.alpha)**( t - self._lastTime)) \
            if self._avg is not None else None

    def derivative(self):
        return self.derivativeAt(self._scheduler.currentTime)

    def derivativeAt(self, t):
        """ Returns derivative of the average at some time point t >= last update time
        Returns None if no data has come
        """
        if self._avg is None:
            return None
        dt = t - self._lastTime
        return  -(self._lastValue - self._avg)*math.log(1 - self.alpha)*(1 - self.alpha)**dt

    def update(self, time, value):
        """ Adds point (time, value) to calculate the average
        """
        if value is not None:
            self._avg = self.at(time) if self._avg is not None else value
            self._lastValue = value
            self._lastTime = time
