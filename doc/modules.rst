**Table of Contents**


.. contents::
    :local:
    :depth: 1
    :backlinks: none
    
Compound modules are shown in notation of a special domain specific language (to be developed)

.. code-block::

	MACD(x, slow, fast) ::= EWMA(x, 2./(fast+1)) - EWMA(x, 2./(slow+1))

Currently they are implemented using a Python subset:

.. code-block:: python

	class MACD(ops.Function[float]):
	    
	    def getImpl(self):
	        return EWMA(self.source, 2./(self.fast+1)) - EWMA(self.source, 2./(self.slow+1))
	    
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


Order book functions and observables
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

Trader functions and observables
-------------------------------------

- Position(trader)
- Balance(trader)
- PendingVolume(trader): cumulative volume of orders sent by the trader but haven't been matched

.. code-block::

    Efficiency(trader) ::= Balance(trader) + CumulativePrice(Orderbook(trader), Position(trader))
    EfficiencyTrend(trader, alpha) ::= Derivative(EWMA(Efficiency(trader), alpha))

Strategy parts
--------------

Price for a liquidity provider

.. code-block::
    
    NotNone(x, default) ::= x == None ? default : x
    LiquidityProviderPrice(orderqueue, priceDistr, defaultValue) ::=
        priceDistr * (NotNone(BestPrice(orderqueue), 
                         NotNone(LastTradePrice(orderqueue), 
                             defaultValue))
                             
Side for a noise strategy

.. code-block::

    NoiseSide() ::= uniform(0,1) > 0.5 ? Side.Sell : Side.Buy
    
    
Side for a signal value strategy

.. code-block::

    SignalSide(x, threshold) ::= x > threshold ? Side.Buy : -x > threshold ? Side.Sell : None 
    
Side for a trend follower

.. code-block::

    TrendFollowerSide(price, alpha) ::= SignalSide(Derivative(EWMA(price, alpha)), 0)
    
Side for crossing averages strategy

.. code-block::

    TwoAveragesSide(price, alpha1, alpha2) ::= SignalSide(EWMA(price, alpha1) - EWMA(price, alpha2), 0)

Side for fundamental value strategy

.. code-block::

    FundamentalValueSide(orderbook, fv) ::= BestPrice(Asks(orderbook)) < fv ? Side.Buy : 
                                            BestPrice(Bids(orderbook)) > fv ? Side.Sell :
                                            None

Side for mean reverting strategy

.. code-block::

    MeanReverting(orderbook, alpha) ::= FundamentalValueSide(orderbook, EWMA(MidPrice(orderbook), alpha))

Signed volume for a desired position strategy

.. code-block::

    DesiredPositionVolume(x, trader) ::= x - (Position(trader) + PendingVolume(trader))
    
Signed volume for a RSI strategy

.. code-block::

    RSI_Volume(trader, alpha, k, lag) ::= 
        price = MidPrice(Orderbook(trader)) in 
        DesiredPositionVolume(k * (50 - RSI(price, lag, alpha)), trader)
        
Signed volume for Bollinger band strategy

.. code-block::

    BollingerVolume(trader, alpha, k) ::= 
        price = MidPrice(Orderbook(trader)) in 
        DesiredPositionVolume((price - EWMA(price, alpha)) / StdDevEW(price, alpha) * k, trader)

Order factories
---------------

Base orders:
- Market order 
- Limit order 

Meta orders:
- Iceberg(lotSize, orderFactory) creates an order using orderFactory and sends it
  consequetively splitting on portions of lotSize
- FloatingPrice(priceFunc, orderFactory) creates an order with price controlled by priceFunc
- Peg(orderFactory) creates an order that tries to keep its price the best.
					Implemented via FloatingPrice and Maximum/Minimum
- ImmediateOrCancel(orderFactory) creates a (limit-like) order with a cancellation request
- WithExpiry(expiry, orderFactory) creates limit-like orders that are cancelled after expiry
- StopLoss(maxLoss, orderFactory) sends an order and if losses from keeping its
	position are too high liquidates it
	
Strategies
----------

- Generic(eventGen, orderFactory) wakes up at moments of time given by eventGen
	and asks orderFactory to create an order
- Array(strategies) aggregates an array of strategies
- Suspendable(strategy, predicate) passes orders issued by strategy only if predicate is true
