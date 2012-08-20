class HistoryCheckerBase(object):
    def __init__(self):
        self._history = []
        self._delta = []

    def append(self, value):
        self._delta.append(value)

    def checkDelta(self, other):
        res = other == self._delta
        self._history.extend(self._delta)
        self._delta = []
        return res

    @property
    def history(self):
        return self._history + self._delta

class OrderQueueHistoryChecker(HistoryCheckerBase):

    def append(self, queue):
        HistoryCheckerBase.append(self, (queue.best.price, queue.best.volume) if not queue.empty else None)

class TraderHistoryChecker(HistoryCheckerBase):

    def append(self, trader):
        HistoryCheckerBase.append(self, (trader.PnL, trader.amount))
