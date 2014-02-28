class Source_Impl(object):

    @property
    def dereference(self):
        return self.x.source

class Alpha_Impl(object):

    @property
    def dereference(self):
        return self.x.alpha

class Timeframe_Impl(object):

    @property
    def dereference(self):
        return self.x.timeframe