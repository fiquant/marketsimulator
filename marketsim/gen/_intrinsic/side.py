from marketsim import Side

class _Sell_Impl(object):

    def __call__(self):
        return Side.Sell

class _Buy_Impl(object):

    def __call__(self):
        return Side.Buy

class _None_Impl(object):

    def __call__(self):
        return None