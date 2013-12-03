from marketsim import defs, _, ops, types, registry, orderbook

from _ewma import EWMA
from _computed import OnEveryDt
from _orderbook import MidPrice

import _wrap

class MACD(ops.Function[float]):
    
    def getImpl(self):
        return EWMA(self.source, 2./(self.fast+1)) - EWMA(self.source, 2./(self.slow+1))

    def __repr__(self):
        return self.label
    
    @property
    def label(self):
        return 'MACD_{%s}^{%s}(%s)' % (self.fast, self.slow, self.source.label)
    
_wrap.function(MACD, ['Statistics', 'MACD', 'Convergence/Divergence'], 
               """ Moving average convergence/divergence
               """, 
               [
                    ('source', 'MidPrice()', 'types.IObservable[float]'), 
                    ('fast',   '12',         'types.positive'),
                    ('slow',   '26',         'types.positive'),
               ], globals())    

class signal(ops.Function[float]):
    
    def getImpl(self):
        return EWMA(OnEveryDt(self.updateInterval, 
                              MACD(self.source, 
                                   self.fast, 
                                   self.slow)), 
                    2./(self.timeframe+1))

    def __repr__(self):
        return self.label

    @property
    def label(self):
        return 'Signal_{%s}(MACD_{%s}^{%s}(%s))' % (self.timeframe, 
                                                    self.fast, 
                                                    self.slow, 
                                                    self.source.label)
    
_wrap.function(signal, ['Statistics', 'MACD', 'Signal'], 
               """ Moving average convergence/divergence signal
               """, 
               [
                    ('source',          'MidPrice()',   'types.IObservable[float]'), 
                    ('fast',            '12',         'types.positive'),
                    ('slow',            '26',         'types.positive'),
                    ('timeframe',       '9',          'types.positive'),
                    ('updateInterval',  '1.',         'types.positive'),
               ], globals())    

class histogram(ops.Function[float]):
    
    def getDefinitions(self):
        return {
             'macd' : OnEveryDt(self.updateInterval, 
                                MACD(self.source, 
                                     self.fast, 
                                     self.slow))
        }
    
    def getImpl(self):
        return ops.Sub(_.macd, EWMA(_.macd, 2./(self.timeframe+1)))

    def __repr__(self):
        return self.label

    @property
    def label(self):
        return 'Histogram_{%s}(MACD_{%s}^{%s}(%s))' % (self.timeframe, 
                                                       self.fast, 
                                                       self.slow, 
                                                       self.source.label)
    
_wrap.function(histogram, ['Statistics', 'MACD', 'Histogram'], 
               """ Moving average convergence/divergence histogram
               """, 
               [
                    ('source',          'MidPrice()',   'types.IObservable[float]'), 
                    ('fast',            '12',         'types.positive'),
                    ('slow',            '26',         'types.positive'),
                    ('timeframe',       '9',          'types.positive'),
                    ('updateInterval',  '1.',         'types.positive'),
               ], globals())    

