from marketsim import Side
from marketsim.order._base import Base as Order
from marketsim.orderbook._base import BookBase as OrderBook
from marketsim.constraints import *
from marketsim.trader import SingleAsset as SingleAssetTrader
from marketsim.meta import *

Price = float #non_negative
Volume = float #non_negative
TimeInterval = float #non_negative


class UpdatableValue(object):    
    """
    Class implementing UpdatableValue concept should obey the following interface
    @property 
    def value(self) # Returns average value at the last update point 
    def at(self, t) # Returns value of the average at some time point t >= last update time
    def derivativeAt(self, t) # Returns derivative of the average at some time point t >= last update time
    def update(self, time, value)# Adds point (time, value) to calculate the average
    """
    pass

UpdatableValue._types = [UpdatableValue]
