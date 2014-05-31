package marketsim.strategy.price

import marketsim.{OrderFactory, Ticks, Account}

class LiquidityProviderSide(account       : Account,
                            intervals     : () => Double,
                            prices        : () => Double,
                            price_factory : () => Ticks => OrderFactory)
{

}
