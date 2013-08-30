
from asset import *

class Position(object):
    def __init__(self):
        self._amount = 0
        self._pending = 0


class Portfolio(dict):
    def __init__(self):
        super(Portfolio, self).__init__()
