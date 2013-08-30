from marketsim import (request, trader, orderbook, event, _, Side, order, types, mathutils,
                       scheduler, ops, observable, registry, combine)

from marketsim.types import *
from _basic import Strategy
from _wrap import wrapper2
from marketsim.trader import TraderHistory, SingleProxy

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas.tools.plotting import lag_plot, autocorrelation_plot
from scipy import stats
import statsmodels.api as sm

# from marketsim.observable import MidPrice, DataStore, AskPrice, BidPrice
from marketsim.event import Every as Timer

import re
import inspect
def internals(cls):
    types_ = ("observable", "orderbook")
    source = inspect.getsource(cls.__init__)
    source = source.splitlines()
    _internals = []
    for line in source:
        if any([word in line for word in types_]):
            field_name = re.findall(r'self.([\w]+)', line)[0]
            _internals.append(field_name)
    cls._internals = _internals
    return cls

@internals
class Plotter(Strategy):

    def __init__(self, plot_freq=10):
        Strategy.__init__(self)

        self.book = orderbook.OfTrader()
        self.askprice = observable.AskPrice(self.book)
        self.bidprice = observable.BidPrice(self.book)
        self.store = observable.DataStore
        self.store.addSource(self.askprice, 'price')
        self.log = TraderHistory(SingleProxy())

        # plotting
        self._eventPlot = Timer(ops.constant(plot_freq))
        event.subscribe(self._eventPlot, _(self).plot, self)

        self.fig = plt.figure()
        plt.ion()
        plt.show()

    # _internals = ['book', 'log', 'askprice', 'store']

    def plot(self, dummy):
        self.fig.clear()
        price = self.store.data['price']
        price = price.resample('1S', how='mean')

        self.fig.add_subplot(211)
        price.plot()
        cycle, trend = sm.tsa.filters.hpfilter(price)
        trend.plot()

        self.fig.add_subplot(212)
        # cycle.plot()
        # cycle_mean = pd.rolling_mean(cycle, window=20, min_periods=0)
        # cycle_std = pd.rolling_std(cycle, window=20, min_periods=0)
        # upper = cycle_mean + 2*cycle_std
        # lower = cycle_mean - 2*cycle_std
        # upper.plot()
        # lower.plot()
        trend.diff().diff().plot()

        plt.draw()

@internals
class TrendNew(Strategy):
    def __init__(self):
        Strategy.__init__(self)
        self._eventGen = Timer(ops.constant(50))
        event.subscribe(self._eventGen, _(self)._wakeUp, self)

        self.book = orderbook.OfTrader()
        self.mid_price = observable.LastTradePrice(self.book)
        self.price = observable.ObservableHistory(self.mid_price)
        # event.subscribe(self.price, _(self)._wakeUp, self)

    def _wakeUp(self, *args, **kwargs):
        price_on_sec = self.price.resample('1S', how='mean', fill_method='bfill')
        mean_price = pd.rolling_mean(price_on_sec, window=20)
        mean_price.plot()
        plt.show()

from marketsim import parts

@internals
class TrendNew_(Strategy):

    def __init__(self):
        Strategy.__init__(self)
        self._eventGen = Timer(ops.constant(1))
        event.subscribe(self._eventGen, _(self)._wakeUp, self)

        self.book = orderbook.OfTrader()
        self.order_factory = order.factory.side.Market()

        self.midprice = observable.MidPrice(self.book)
        self.store = observable.DataStore
        self.store.addSource(self.midprice, 'price')

        self.log = TraderHistory(SingleProxy())

        self.invested = False

    #_internals = ['book', 'log', 'midprice', 'store']

    def _wakeUp(self, dummy):
        price = self.store.data['price']
        price = price.resample('1S', how='mean')

        if len(price) > 40:
            cycle, trend = sm.tsa.filters.hpfilter(price)
            print cycle[-1]
            if cycle[-1] < -10:
                buyOrder = self.order_factory(parts.side.Random())
                self._send(buyOrder)
                self.invested = True