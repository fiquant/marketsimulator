class Last(object):
    """ Aggregates (folds) time-dependent data from *source* using given
        functional  *folder* (e.g. moving average) defined in derived class

    For example ::

        price_avg = EWMA(MidPrice(book_A), alpha = 0.15)

    creates a observable for a moving average with |alpha| = 0.15 of mid-price of asset *book_A*
    """

    def bind(self, context):
        self._scheduler = context.world

    def _update(self, _):
        self.update(self._scheduler.currentTime, self.source())

    def __call__(self):
        """ Returns value from the accumulator corresponding to the current time
        """
        return self.at(self._scheduler.currentTime)
