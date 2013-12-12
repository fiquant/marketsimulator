package observable.macd

def MACD(x = orderbook.MidPrice(), slow = 26.0, fast = 12.0)
    = EWMA(x, 2./(fast+1)) - EWMA(x, 2./(slow+1))

def Signal(x = orderbook.MidPrice(), slow = 26.0, fast = 12.0, timeframe = 9.0, step = 1.0)
    = EWMA(OnEveryDt(MACD(x, slow, fast), step),  2/(timeframe+1))

def Histogram(x = orderbook.MidPrice(), slow = 26.0, fast = 12.0, timeframe = 9.0, step = 1.0)
    = MACD(x,slow,fast) - Signal(x,slow, fast, timeframe, step)