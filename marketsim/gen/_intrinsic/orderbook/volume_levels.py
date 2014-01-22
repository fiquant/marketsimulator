from marketsim import Side, ops, IVolumeLevels, event
from marketsim.gen._out.side._Buy import Buy
from marketsim.gen._out.side._Sell import Sell

class VolumeLevels_Impl(ops.Observable[IVolumeLevels]):

    def __init__(self):
        ops.Observable[IVolumeLevels].__init__(self)
        event.subscribe(event.Every(ops.constant(1)), self.fire, self)

    @property
    def dataSource(self):
        return self

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
            'fillBelow' : repr(self.queue.side) == "Buy",
            'fillAbove' : repr(self.queue.side) == "Sell"
        }