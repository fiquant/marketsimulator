from marketsim.gen._out._side import Side

class Sell_Impl(object):

    def __call__(self):
        return Side.Sell

class Buy_Impl(object):

    def __call__(self):
        return Side.Buy

class None_Impl(object):

    def __call__(self):
        return None