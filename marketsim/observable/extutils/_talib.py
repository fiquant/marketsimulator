def Candlesticks(price_ts, volume_ts=None, freq='S'):
    """ Calculates a dictionary candlestick indicators
        that is used by the TA-lib (Technical Analysis library)
    """
    candlesticks = {'open': price_ts.resample(freq, how='first', fill_method='bfill'),
                    'close': price_ts.resample(freq, how='last', fill_method='bfill'),
                    'high': price_ts.resample(freq, how='max', fill_method='bfill'),
                    'low': price_ts.resample(freq, how='min', fill_method='bfill')}

    if volume_ts is not None:
        candlesticks['volume'] = volume_ts.resample(freq, how='sum')

    return candlesticks

