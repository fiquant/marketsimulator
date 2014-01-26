Functions
=========

.. contents::
    :local:
    :depth: 2
    :backlinks: none

Syntax
------

.. code-block:: scala

    QualifiedName ::= Ident("." Ident)*

    Decorator ::= "@" (Annotation | Attribute)

    Annotation ::= QualifiedName "(" Expr ("," Expr)* ")"

    Attribute ::= Ident "=" Expr

    Parameter ::= Ident (":" Type)? ("=" Expr)?

    FunctionDef ::= Decorator* "def" Ident "(" Parameter? ("," Parameter)* ")" (":" Type)? ("=" Expr)?

Functions as simulation modules
-------------------------------

Functions in Strategy Definition Language correspond to simple and compound modules in a simulation model. Functions have parameters which are used to generate module fields. Every parameter has an unique name, type and an optional default value. Parameter type tells what kind of values may be assigned to this field. 

Simple modules represent some functionality which is considered as elemental and they are implemented in target language (like Python). Functions for simple modules (intrinsic functions) don't have body but they must be decorated by an annotation (e.g. ``@python.intrinsic("_Class_Impl")``) telling where Python implementation should be taken from.  

Compound modules are compositions of other modules and can be completely generated from a high level description at Strategy Definition Language. Functions that describe them must have a body defining how they are composed.

Functions are assigned types and these types allows modules to be used as parameters for other modules.

Type inference
--------------

Function parameter types usually are infered from type of their initializer and thus may be omitted. If a parameter doesn't have a default value, its type should be specified explicitely.

Return type of function can be inferred automatically if function has body and thus omitted but must be specified explicitely otherwise.

There are two ways to specify return type of a function: after a colon (":") a full return type is specified and
after an arrow ("=>") a return type of a function to be returned is given (this syntax is introduced for brevity). For example,

.. code-block :: scala

    def f() => Float

is equivalent to

.. code-block :: scala

    def f() : () => Float

Note that in some rare cases (generating partial functions) the current compiler implementation imposes restriction that parameter type must be specified explicitly even if there is a default parameter (curried functions are injected into code at before typing stage where type information is not disponible).

Order factories
---------------

Order factories are parametrized by functions calculating various parameters of orders to create. For example, 

.. code-block :: scala

    /**
     *  Factory creating limit orders
     *
     *  Limit orders ask to buy or sell some asset at price better than some limit price.
     *  If a limit order is not competely fulfilled
     *  it remains in an order book waiting to be matched with another order.
     */
    @python.order.factory("order.limit.Order_Impl")
    def Limit(/** function defining side of orders to create */
              side      = side.Sell(),
              /** function defining price of orders to create */
              price     = constant(100.),
              /** function defining volume of orders to create */
              volume    = constant(1.)) : IOrderGenerator

Usually trading strategies define only subset of these parameters. For example ``LiquidityProvider`` calculates side and price of orders to create but tells nothing about what volume orders should be created with. Hence it should be parametrized by a function that creates an order factory provided side and price functions:

.. code-block :: scala

    /**
     * Liquidity provider for one side
     */
    def LiquidityProviderSide(
                /** Event source making the strategy to wake up*/
                eventGen     = event.Every(math.random.expovariate(1.)),
                /** order factory function*/
                orderFactory = order.side_price.Limit(), // has type (() => Side, () => Price) => IOrderGenerator
                /** side of orders to create */
                side         = .side.Sell(),
                /** initial price which is taken if orderBook is empty */
                initialValue = 100.0,
                /** defines multipliers for current asset price when price of
                    order to create is calculated*/
                priceDistr   = math.random.lognormvariate(0., .1))

        =   Generic(
                orderFactory(   // partial function application
                    side,
                    price.LiquidityProvider(
                        side,
                        initialValue,
                        priceDistr)),
                eventGen)

Partial order factories are generated automatically once a function is annotated by ``@python.order.factory`` annotation. At the moment it generates partial functions for following arguments:

.. code-block :: scala

    signedVolume => IOrderGenerator
    Price => IOrderGenerator
    Volume => IOrderGenerator
    (Side, Price) => IOrderGenerator
    (Side, Volume) => IOrderGenerator
    Side => Price => IOrderGenerator
    Volume => Price => IOrderGenerator
    (Side, Volume) => Price => IOrderGenerator

If an order factory doesn't have some parameter (e.g. ``order.Market`` doesn't have ``price``) a partial function for this parameter is not generated. 

Meta order factories have ``proto`` parameter which refers to the underlying order factory. Partial meta order factories accept corresponding partial underlying order factory:

.. code-block :: scala

    // NB! This code is generated automatically at before typing stage
    /** Factory creating StopLoss orders
     *
     *  StopLoss order is initialised by an underlying order and a maximal acceptable loss factor.
     *  It keeps track of position and balance change induced by trades of the underlying order and
     *  if losses from keeping the position exceed certain limit (given by maximum loss factor),
     *  the meta order clears its position.
     */
    
    @python.order.factory.on_proto("price_StopLoss")
    def side_price_StopLoss(/** maximal acceptable loss factor */ 
                            maxloss : Optional[.IFunction[.Float]] = .constant(0.1),
                            /** underlying orders to create */ 
                            proto : Optional[(() => .Side) => ((() => .Float) => .IOrderGenerator)] 
                               = .order._curried.side_price_Limit()
                            ) : (() => .Side) => ((() => .Float) => .IOrderGenerator)

Partial order factory for arguments ``(X,Y) => Z => Factory`` can be accessed as ``.order.X_Y.Z.Factory``.

For example, function taking pair ``(side, volume)`` and returning function ``price => order.Limit(side, price, volume)`` can be accessed as ``.order.side_volume.price.Limit``.

Partial functions
-----------------

Sometimes it is useful to have a partially applied function. For example, ``strategy.MultiAssetTrader`` is parametrized by a function that maps trader's "performance" to weights for random strategy selection procedure (in the following code it is named ``normalizer``).

.. code-block :: scala

    /**
     * A composite strategy initialized with an array of strategies.
     * In some moments of time the efficiency of the strategies is evaluated
     * These efficiencies are mapped into weights using *weight* and *normilizer*
     * functions per every strategy and *corrector* for the whole collection of weights
     * These weights are used to choose randomly a strategy to run for the next quant of time.
     * All other strategies are suspended
     */
    @python.intrinsic("strategy.multiarmed_bandit._MultiarmedBandit2_Impl")
    def MultiArmedBandit(
            /** original strategies that can be suspended */
            strategies = [Noise()],
            /** function creating a virtual account used for estimate efficiency of the strategy itself */
            account    = account.inner.inner_VirtualMarket(),
            /** function estimating is the strategy efficient or not */
            weight     = weight.trader.trader_EfficiencyTrend(),
            /** function that maps trader efficiency to its weight that will be used for random choice */
            normalizer = weight.f.f_AtanPow(),
            /** given array of strategy weights corrects them.
              * for example it may set to 0 all weights except the maximal one */
            corrector  = weight.array.array_IdentityL()) : ISingleAssetStrategy

This parameter has default value ``(f : Float => Float) => Atan(Pow(1.002, f))`` which is a partial application of function

.. code-block :: scala

    /**
     *  scaling function = atan(base^f(x))
     */
    @curried("f")
    def AtanPow(
        /** function to scale */
        f : Optional[IFunction[Float]] = constant(),
        /** base for power function */
        base = 1.002) : IFunction[Float]

        = math.Atan(math.Pow(constant(base), f))

by parameter ``f``. Unfortunately, explicit request to generate a partial function (``@curried("f")``) is required since it might be used directly from a Python code. At the moment partial functions can be generated only over a single parameter. Function ``.pkg.F`` partially applied by parameter ``x`` can be accessed as ``.pkg.x.x_F``.
