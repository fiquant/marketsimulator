Simple strategies
=================

.. contents::
    :local:
    :depth: 2
    :backlinks: none
    
``Generic(eventGen, orderFactory)`` wakes up at moments of time given by ``eventGen`` and asks ``orderFactory`` to create an order.

For example, a crossing averages strategy that sends market orders with exponentially distributed volume sizes in even intervals of time could be written as:

.. code-block:: python

    strategy.Generic(event.Every(constant(1.)),
            order.factory.Market(
                side = parts.side.TwoAverages(
                                    MidPrice(orderbook.OfTrader()), 
                                    alpha1, alpha2),
                volume = rnd.Expovariate(1.)
           ))

There are also handy specialisations of this generic strategy. Usually they accept parameters defining strategy logic and an order factory in a curried form.

Liquidity provider strategy
---------------------------

Liquidity provider strategy is an array of two strategies providing liquidity for each side of trade over the asset. Every liquidity provider side wakes up at moments of time given by ``eventGen``, calculates a base price of the asset (it is taken as price of the best order in the queue, if none, price of the last trade is taken, if none we take some default value). Then an order with price equal to the base price is multiplied by a value taken from ``priceDistr`` and volume is taken from ``volumeDistr`` is created.
  
.. code-block:: haskell
    
    NotNone(x, defaultValue) ::= 
        if x == None then defaultValue else x
        
    price.LiquidityProviderSide(orderqueue, priceDistr, defaultValue) ::=
        priceDistr * (NotNone(BestPrice(orderqueue), 
                         NotNone(LastTradePrice(orderqueue), 
                             defaultValue))
  
    strategy.LiquidityProviderSide(eventGen, orderFactory, side, priceDistr, defaultValue) ::=
            orderbook = orderbook.OfTrader() in
            strategy.Generic(eventGen, 
                             orderFactory(ops.constant(side), 
                                          price.LiquidityProviderSide(
                                            orderbook.queue(side),
                                            priceDistr, 
                                            defaultValue)))
    						 			    
    strategy.LiquidityProvider(eventGen, orderFactory, priceDistr, defaultValue) ::=
    	strategy.Array([
    		strategy.LiquidityProviderSide(eventGen, orderFactory, Side.Sell, priceDistr, defaultValue),
    		strategy.LiquidityProviderSide(eventGen, orderFactory, Side.Buy,  priceDistr, defaultValue),
    	])    						 			    
		
Noise strategy
--------------

Noise strategy wakes up at moments of time given by ``eventGen`` and chooses randomly trade side. 

.. code-block:: haskell

    side.Random() ::= 
        if uniform(0,1) > 0.5 then Side.Sell else Side.Buy
    
    strategy.Noise(eventGen, orderFactory) ::= 
    	strategy.Generic(eventGen, orderFactory(side.Random()))
    
Signal strategy
---------------

Signal strategy listens to some discrete ``signal`` and when the signal becomes more than some ``threshold`` the strategy starts to buy. When the signal  gets lower than ``-threshold`` the strategy starts to sell.  

.. code-block:: haskell

    side.Signal(x, threshold) ::= 
        if  x > threshold then Side.Buy else 
        if -x > threshold then Side.Sell else
        None 
    
    strategy.Signal(eventGen, orderFactory, signal, threshold) ::= 
    	strategy.Generic(eventGen, orderFactory(
    	    side.Signal(signal, threshold)))
												
.. image:: Figures/web/signal.png

Trend follower
--------------

Trend follower can be considered as a sort of a signal strategy where the ``signal`` is a trend of the asset's price. Under trend we understand the first derivative of some moving average. If the derivative is positive, the trader buys; if the derivative is negative, it sells. Since a moving average is a continuously changing signal, we check its derivative at moments of time given by ``eventGen``.  

.. code-block:: haskell

    side.TrendFollower(price, alpha) ::= 
        side.Signal(Derivative(EWMA(price, alpha)), 0)
    
    strategy.TrendFollower(eventGen, orderFactory, alpha) ::= 
    	strategy.Generic(eventGen, orderFactory(
    		side.TrendFollower(observable.MidPrice(), alpha)))

.. image:: Figures/web/trendfollower.png

Crossing averages strategy
--------------------------

Crossing averages strategy can be considered as a sort of a signal strategy where the ``signal`` is a difference between two moving averages of the asset's price. 

.. code-block:: haskell

    side.TwoAverages(price, alpha1, alpha2) ::= 
        side.Signal(EWMA(price, alpha1) - EWMA(price, alpha2), 0)

	strategy.TwoAverages(eventGen, orderFactory, alpha1, alpha2) ::= 
		strategy.Generic(eventGen, orderFactory(
			side.TwoAverages(observable.MidPrice(), alpha1, alpha2)))
			
.. image:: Figures/web/twoaverages.png

Fundamental value strategy
--------------------------

Fundamental value strategy believes that an asset should cost some specific price (``fundamental value``) and if current asset price is lower than the fundamental value it starts to buy the asset and if the price is higher than the fundamental value it starts to sell the asset. 

.. code-block:: haskell

    side.FundamentalValue(orderbook, fv) ::= 
        if BestPrice(Asks(orderbook)) < fv then Side.Buy else 
        if BestPrice(Bids(orderbook)) > fv then Side.Sell else
        None
                                             
    strategy.FundamentalValue(eventGen, orderFactory, fv) ::= 
		strategy.Generic(eventGen, orderFactory(
			side.FundamentalValue(orderbook.OfTrader(), fv)))
			
.. image:: Figures/web/fundamentalvalue.png

Mean reverting strategy
-----------------------

Mean reverting strategy is a kind of a fundamental value strategy with ``fundamentalValue`` equal to a moving average of the asset's price.

.. code-block:: haskell

    side.MeanReverting(orderbook, alpha) ::= 
        side.FundamentalValue(orderbook, EWMA(MidPrice(orderbook), alpha))
    											
    strategy.MeanReverting(eventGen, orderFactory, alpha) ::=
        strategy.Generic(eventGen, orderFactory, 
            side.MeanReverting(orderbook.OfTrader(), alpha))

.. image:: Figures/web/meanreversion.png

Dependency trading strategy
---------------------------

Dependent price strategy believes that the fair price of an asset ``A`` is completely correlated with price of another asset ``B`` and the following relation should be held: ``Price(A) = k*Price(B)``, where ``k`` is some factor. It may be considered as a variety of a fundamental value strategy. 

.. code-block:: haskell

    side.Dependency(orderbook, otherOrderbook, factor) ::= 
    	side.FundamentalValue(orderbook, MidPrice(otherOrderbook) * factor)
    	
    strategy.Dependency(eventGen, orderFactory, otherOrderBook, factor) ::=
    	strategy.Generic(eventGen, orderFactory(
    		side.Dependency(orderbook.OfTrader(), otherOrderBook, factor)))

.. image:: Figures/web/dependency.png

Desired position strategies
---------------------------

These strategies keep track of the trader's position (actual position + pending orders volume) and if ``desiredVolume`` changes it creates orders in order to cover the gap between the current and the desired position.

.. code-block:: haskell

	signed_volume.DesiredPosition(trader, desiredPosition) ::=
		desiredPosition - VolumeTraded(trader) - VolumePending(trader)
		
Bollinger bands strategy
------------------------

Bollinger band strategy believes that a trader should take a position equal to the difference between the current asset price and its average divided on its standard deviation (and scaled by some ``factor``).

.. code-block:: haskell

    signed_volume.BollingerBands(alpha, k) ::= 
        trader = thisTrader(),
        price  = MidPrice(orderbook.OfTrader(trader)),
        mean   = EWMA(price, alpha), 
        stddev = StdDevEW(price, alpha) in 
        
        signed_volume.DesiredPosition(trader, (price - mean) / stddev * k)
		
Relative Strength Index strategy
--------------------------------

Relative Strength Index strategy believes that a trader should take a position equal to deviation of its relative strength index from 50 scaled by some ``factor``.

.. code-block:: haskell

    signed_volume.RSI(alpha, k, timeframe) ::=
        trader = thisTrader()
        rsi = RSI(orderbook.OfTrader(trader), timeframe, alpha) in 
        signed_volume.DesiredPosition(trader, OnEveryDt(1, (50 - rsi) * k))

Market data strategy
--------------------

This strategy allows to drive the asset price based on historical market data by creating large volume orders for the given price.  Every time step of 1 in the simulation corresponds to a 1 day in the market data. At each time step the previous Limit Buy/Sell orders are cancelled and new ones are created based on the next price of the market data.

It is implemented as a strategy that wakes up once and create a composition of iceberg and floating price orders. The floating price is equal to the current quote plus/minus some delta and the iceberg order breaks an 'infinite' limit order into small lots.

.. code-block:: python 

    class MarketData(types.ISingleAssetStrategy):
        
        def getImpl(self):
            quotes = observable.Quote(self.ticker, self.start, self.end) # TODO: should be in definitions
            return strategy.Array([
                strategy.Generic(
                    order.factory.Iceberg(
                        const(self.volume),
                        order.factory.FloatingPrice(
                            ops.constant(sign*self.delta) + quotes,
                            order.factory.price.Limit(
                                side = const(side),
                                volume = const(self.volume * 1000000)))),
                    event.After(ops.constant(0)))\
                    for side, sign in {Side.Buy : -1, Side.Sell : 1}.iteritems()
                ])

