from marketsim import Side

class _Sell_Impl(object):

    def __call__(self):
        from marketsim.ops import constant
        return Side.Sell

class _Buy_Impl(object):

    def __call__(self):
        from marketsim.ops import constant
        return Side.Buy

class _None_Impl(object):

    def __call__(self):
        from marketsim.ops._all import _None
        return None