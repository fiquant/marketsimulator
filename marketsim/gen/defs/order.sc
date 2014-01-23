@category = "Order"
package order
{
    // Order factory is a callable object that creates orders
    // It is often handy to have order factories in curried form
    // factories in curried form are generated on the fly and put into inner packages of this package
    // Curried form x => (y,z) => Factory can be accessed as x.y_z.Factory
    // For example,
    //      .order.side_volume.price.Limit
    //  refers to curried function (side, volume) => price => .order.Limit(side, price, volume)

    /**
     *  Factory creating market orders
     *
     *  Market order intructs buy or sell given volume immediately
     */
    @python.order.factory("order.market.Order_Impl")
    def Market(/** function defining side of orders to create */
               side     = side.Sell(),
               /** function defining volume of orders to create */
               volume   = constant(1.)) : IOrderGenerator

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

    /**
     *  Factory creating fixed budget orders
     *
     *  Fixed budget order acts like a market order
     *  but the volume is implicitly given by a budget available for trades.
     *  Internally first it sends request.EvalVolumesForBudget
     *  to estimate volumes and prices of orders to sent and
     *  then sends a sequence of order.ImmediateOrCancel to be sure that
     *  cumulative price of trades to be done won't exceed the given budget.
     */
    @python.order.factory("order.meta.fixed_budget.Order_Impl")
    def FixedBudget(/** function defining side of orders to create */
                    side    = side.Sell(),
                    /** function defining budget on which it may send orders at one time */
                    budget  = constant(1000.)) : IOrderGenerator

    /**
     *  Factory creating Immediate-Or-Cancel orders
     *
     *  Immediate-Or-Cancel order sends an underlying order to the market and
     *  immediately sends a cancel request for it.
     *  It allows to combine market and limit order behaviour:
     *  the order is either executed immediately
     *  at price equal or better than given one
     *  either it is cancelled (and consequently never stored in the order queue).
     */
    @python.order.factory("order.meta.ioc.Order_Impl")
    def ImmediateOrCancel(/** factory for underlying orders */
                          proto     = Limit()) : IOrderGenerator

    /**
     *  Factory creating StopLoss orders
     *
     *  StopLoss order is initialised by an underlying order and a maximal acceptable loss factor.
     *  It keeps track of position and balance change induced by trades of the underlying order and
     *  if losses from keeping the position exceed certain limit (given by maximum loss factor),
     *  the meta order clears its position.
     */
    @python.order.factory("order.meta.stoploss.Order_Impl")
    def StopLoss(/** maximal acceptable loss factor */
                 maxloss = constant(0.1),
                 /** underlying orders to create */
                 proto = Limit()) : IOrderGenerator

    /**
     * Factory creating WithExpiry orders
     *
     * WithExpiry orders can be viewed as ImmediateOrCancel orders
     * where cancel order is sent not immediately but after some delay
     */
    @python.order.factory("order.meta.with_expiry.Order_Impl")
    def WithExpiry(/** expiration period for orders */
                   expiry   = constant(10.),
                   /** underlying orders to create */
                   proto    = Limit()) : IOrderGenerator

    /**
     *  Factory creating iceberg orders
     *
     *  Iceberg order is initialized by an underlying order and a lot size.
     *  It sends consequently pieces of the underlying order of size equal or less to the lot size
     *  thus maximum lot size volume is visible at the market at any moment.
     */
    @python.order.factory("order.meta.iceberg.Order_Impl")
    def Iceberg(/** maximal size of order to send */
                lotSize = constant(10.),
                /** underlying orders to create */
                proto   = Limit()) : IOrderGenerator

    /**
     *  Factory creating orders with floating price
     *
     *  Floating price order is initialized by an order having a price and an observable that generates new prices.
     *  When the observable value changes the order is cancelled and
     *  a new order with new price is created and sent to the order book.
     */
    @python.order.factory("order.meta.floating_price.Factory_Impl")
    def FloatingPrice(/** observable defining price of orders to create */
                      floatingPrice = const(10.),
                      /** underlying orders to create */
                      proto = price.Limit()) : IOrderGenerator

    /**
     *  Factory creating Peg orders
     *
     *  A peg order is a particular case of the floating price order
     *  with the price better at one tick than the best price of the order queue.
     *  It implies that if several peg orders are sent to the same order queue
     *  they start to race until being matched against the counterparty orders.
     */
    @python.order.factory("order.meta.peg.Factory_Impl")
    def Peg(proto = price.Limit()) : IOrderGenerator
}