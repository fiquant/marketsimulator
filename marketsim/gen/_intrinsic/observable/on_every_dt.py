from marketsim import event

class IndicatorBase(object):
    """ Observable that stores some scalar value and knows how to update it

    * **Source of data** -- function that provides data
    * **Events when to act** -- events when to act
    """
    def __init__(self):
        self._alias = ['_details', 'indicator base']

    @property
    def label(self):
        return self._dataSource.label

    @property
    def digits(self):
        return self._dataSource.digits if 'digits' in dir(self._dataSource) else 4

    def schedule(self):
        self.reset()

    def __call__(self):
        """ Returns current value
        """
        return self._dataSource()

from marketsim.gen._out._constant import constant

class _OnEveryDt_Impl(IndicatorBase):
    """ Creates an indicator that is updated regularly
    interval - constant interval between updates
    source - function to obtain indicator value
    """
    def __init__(self):
        self.attributes = {'smooth':True}
        self._dataSource = self.x
        IndicatorBase.__init__(self)
        self._subscription = event.subscribe(event.Every(constant(self.dt)), self.fire, self)

class _Observable_Impl(object):
    """ Creates an indicator that is updated regularly
    interval - constant interval between updates
    source - function to obtain indicator value
    """
    def __init__(self):
        self._dataSource = self.x
        self._subscription = event.subscribe(self.x, self.fire, self)

    def schedule(self):
        self.reset()

    def __call__(self):
        """ Returns current value
        """
        return self._dataSource()

class _ObservableSide_Impl(object):
    """ Creates an indicator that is updated regularly
    interval - constant interval between updates
    source - function to obtain indicator value
    """
    def __init__(self):
        self._dataSource = self.x
        self._subscription = event.subscribe(self.x, self.fire, self)

    def schedule(self):
        self.reset()

    def __call__(self):
        """ Returns current value
        """
        return self._dataSource()
