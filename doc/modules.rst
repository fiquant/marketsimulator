Basic modules
--------------

Normally they return None if one of the operands is None

- Constant[T]/None[T] functions
- Identity function
- Arithmetic operations (+,-,*,/,%)
- Comparisons (<, <=, >, >=, ==, !=)
- Conditional branching (condition ? trueBranch : falseBranch)
- Math module functions (Exp, Pow, Log, Atan etc.)
- Random distrubutions (uniform, lognormvariate, expovariate etc.)
- Derivative of a differentiable function
- Quotes: downloads external historical data
- Lagged: returns function values with some lag
- CurrentTime: current model time

.. code-block::

	Max(x,y) ::= x > y ? x : y
	Min(x,y) ::= x < y ? x : y
	Sqr(x) ::= x*x


Statistics
----------

- average (Mean): cumulative (CMA), moving (MA), exponentially weighted (EWMA)
- variance (Variance): cumulative, moving, exponentially weighted
- moving minimum/maximum

Variances could be implemented via Mean but it looses precision 

.. code-block::

	Var(x) ::= Mean(Sqr(x)) - Sqr(Mean(x)) 

Standard deviation 

.. code-block::

	StdDev(x) ::= Sqrt(Variance(x))

Relative strength index

.. code-block::

	Ups(x, dt, alpha) ::= EWMA(max(0, x - Lagged(x, dt)), alpha)
	Downs(x, dt, alpha) ::= EWMA(max(0, Lagged(x, dt) - x), alpha)
	RSI(x, dt, alpha) ::= 100 - 100 / (1 + Ups(x,dt,alpha)/Downs(x,dt,alpha))

Moving average convergence/divergence

.. code-block::

	MACD(x, slow, fast) ::= EWMA(x, 2./(fast+1)) - EWMA(x, 2./(slow+1))
	MACD_signal(x, slow, fast, timeframe) ::= EWMA(MACD(x, slow, fast), 2/(timeframe+1))
	MACD_histogram(x, slow, fast, timeframe) ::= MACD(x,slow,fast) - MACD_signal(x,slow, fast, timeframe)

Bollinger bands

.. code-block::

	Bollinger_Hi(x) ::= Mean(x) + 2*StdDev(x)
	Bollinger_Lo(x) ::= Mean(x) - 2*StdDev(x)


Order book functions/observables
--------------------------------

- TickSize(orderbook)
- Asks(orderbook)/Bids(orderbook): return asks or bids queue of the orderbook
- BestPrice(orderqueue): current price
- LastTradePrice(orderqueue): price of the last trade
- LastTradeVolume(orderqueue): volume of the last trade
- PriceAtVolume(orderqueue, volume): price of order at the given depth
- CumulativePrice(volume): sum of the best order prices with volume less than given

Price of last trades weighted by their volumes

.. code-block::

    WeightedPrice(Q, alpha) ::= EWMA(LastTradePrice(Q)*LastTradeVolume(Q), alpha) / EWMA(LastTradeVolume(Q), alpha)
    
Mid-price

.. code-block::

    MidPrice(orderbook) ::= (BestPrice(Asks(orderbook)) + BestPrice(Bids(orderbook))) / 2
    
Spread

.. code-block::

    Spread(orderbook) ::= Asks(orderbook) - Bids(orderbook)
