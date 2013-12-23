from marketsim import Side

class VolumeLevels_Impl(object):

    @property
    def volumes(self):
        return [self.volumeDelta * i for i in range(self.volumeCount)]

    def __call__(self):
        queue = self.queue
        return [price for (volume, price) in queue.getVolumePrices(self.volumes)]

    @property
    def digits(self):
        return self.queue._digitsToShow

    @property
    def attributes(self):
        return {
            'smooth':True,
            'volumeLevels' : True,
            'fillBelow' : self.queue.side == Side.Buy,
            'fillAbove' : self.queue.side == Side.Sell
        }