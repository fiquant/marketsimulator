class AssetBase(object):
    """ Asset class defining behavior of tradeable assets
    """
    def __init__(self, label):
        super(AssetBase, self).__init__()
        self._label = label

    def __hash__(self):
        return hash(self._label)

    def __repr__(self):
        return self._label


class CashBase(AssetBase):
    def __init__(self, label):
        super(CashBase, self).__init__(label)


class BondBase(AssetBase):
    def __init__(self, label):
        super(BondBase, self).__init__(label)


class StockBase(AssetBase):
    def __init__(self, label):
        super(StockBase, self).__init__(label)

