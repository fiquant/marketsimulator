import statsmodels.api as sm
from marketsim import ops, event
import pandas as pd
import numpy as np
from .._dict import BufferedSeries


def OLS(data, window=20):
    """ Calculates ordinary least squares parameters for a given window
    """
    y = data.values[-window:]
    if len(y) == window:
        x = sm.add_constant(np.arange(len(y)))
        ols_model = sm.OLS(y, x, missing='drop', hasconst=True)
        ols_results = ols_model.fit()
        return ols_results.params
    else:
        return None
