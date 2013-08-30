

class ExchangeBase(dict):
    # TODO: what if there are more possibilities of trading an asset?
    # currently the exchange associates an asset with an order book

    def __init__(self, label="Exchange"):
        super(ExchangeBase, self).__init__()
        self._label = label

    def get_label(self):
        return self._label

    def assets(self):
        return self.keys()

    def books(self):
        return self.values()

    label = property(get_label)