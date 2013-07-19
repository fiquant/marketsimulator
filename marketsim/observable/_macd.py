from marketsim import defs, _, ops

from _ewma import EWMA
from _computed import OnEveryDt

def MACD(source, fast = 2./13, slow = 2./27):
    return EWMA(source, fast) - EWMA(source, slow)

def signal(source, fast = 2./13, slow = 2./27, timeframe = 2./10, updateInteval = 1.):
    return EWMA(OnEveryDt(updateInteval, MACD(source, fast, slow)), timeframe)

def histogram(source, fast = 2./13, slow = 2./27, timeframe = 2./10, updateInteval = 1.):
    return defs(ops.Sub(_.macd, EWMA(_.macd, timeframe)),
              {
                 'macd' : OnEveryDt(updateInteval, MACD(source, fast, slow))
              })
    