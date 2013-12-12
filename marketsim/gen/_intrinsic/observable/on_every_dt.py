from marketsim import event, types, ops

class IndicatorBase(ops.Observable[float]):
    """ Observable that stores some scalar value and knows how to update it

    * **Source of data** -- function that provides data
    * **Events when to act** -- events when to act
    """
    def __init__(self):
        ops.Observable[float].__init__(self)
        self._alias = ['_details', 'indicator base']

    @property
    def label(self):
        return self._dataSource.label

    _properties = [
        ('eventSource' , types.IEvent) ,
        ('dataSource'  , types.IFunction[float])
    ]

    @property
    def eventSource(self):
        return self._subscription.event

    @eventSource.setter
    def eventSource(self, value):
        self._subscription.event = value

    @property
    def digits(self):
        return self._dataSource.digits if 'digits' in dir(self._dataSource) else 4

    @property
    def dataSource(self):
        return self._dataSource

    @dataSource.setter
    def dataSource(self, value):
        self._dataSource = value

    def schedule(self):
        self.reset()

    def __call__(self):
        """ Returns current value
        """
        return self._dataSource()

class _OnEveryDt_Impl(IndicatorBase):
    """ Creates an indicator that is updated regularly
    interval - constant interval between updates
    source - function to obtain indicator value
    """
    def __init__(self):
        self.attributes = {'smooth':True}
        self._dataSource = self.x
        IndicatorBase.__init__(self)
        self._subscription = event.subscribe(event.Every(ops.constant(self.dt)), self.fire, self)
