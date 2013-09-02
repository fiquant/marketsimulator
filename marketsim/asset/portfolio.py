
from asset import *

# TODO: change to take into account more complex positions

class Position(object):
    def __init__(self):
        self._amount = 0
        self._pending = 0


class PortfolioBase(dict):
    def __init__(self):
        super(PortfolioBase, self).__init__()


class Portfolio(PortfolioBase):
    def __init__(self):
        super(Portfolio, self).__init__()
        self._main_cash_account = None

    def get_cash_account(self):
        return self._main_cash_account

    def set_cash_account(self, cash_account):
        if isinstance(CashBase, cash_account):
            self._main_cash_account = cash_account
        else:
            raise TypeError("Trying to set non-cash account")

    cash_account = property(get_cash_account, set_cash_account)
