from marketsim.gen._out._side import Side

from marketsim.gen._out._intrinsic_base.side import Sell_Base, Buy_Base, None_Base

class Sell_Impl(Sell_Base):

    def __call__(self):
        return Side.Sell

class Buy_Impl(Buy_Base):

    def __call__(self):
        return Side.Buy

class None_Impl(None_Base):

    def __call__(self):
        return None