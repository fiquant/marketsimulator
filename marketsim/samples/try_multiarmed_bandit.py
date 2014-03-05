import sys
sys.path.append(r'../..')

from marketsim._pub import (order, strategy, trader, orderbook, event, observable, math, constant, const)

from common import expose

@expose("Multiarmed-Bandit", __name__)
def MultiarmedBandit(ctx):

    ctx.volumeStep = 30

    slow_alpha = 0.015
    fast_alpha = 0.15

    linear_signal = math.RandomWalk(initialValue=200,
                                      deltaDistr=constant(-1),
                                      name="200-t")

    demo = ctx.addGraph('demo')
    myVolume = lambda: [(trader.Position(), demo)]
    myAverage = lambda alpha: [(orderbook.OfTrader().MidPrice.EW(alpha).Avg.OnEveryDt(1), demo)]

    def cross(alpha1, alpha2):
        return strategy.side.CrossingAverages(alpha1, alpha2)\
                            .Strategy(event.Every(constant(1.)),
                                      order.side.Market(volume = constant(1.)))

    def strategies():
        return [cross(slow_alpha, fast_alpha), cross(fast_alpha, slow_alpha)]

    return [
        ctx.makeTrader_A(
            strategy.price.LiquidityProvider()
                    .Strategy(orderFactory = order.side_price.Limit(volume=constant(45))),
                         "liquidity"),

        ctx.makeTrader_A(strategy.side.Signal(linear_signal)
                                      .Strategy(event.Every(constant(1.)),
                                                order.side.Market(volume = constant(20))),
                        "signal",
                        [(linear_signal, ctx.amount_graph)]),

        ctx.makeTrader_A(cross(slow_alpha, fast_alpha),
                        'avg+',
                        myAverage(slow_alpha) + myAverage(fast_alpha) + myVolume()),

        ctx.makeTrader_A(cross(fast_alpha, slow_alpha),
                         'avg-',
                         myVolume()),

        ctx.makeTrader_A(strategy.MultiArmedBandit(
                                    strategies(),
                                    strategy.account.virtualMarket(),
                                    strategy.weight.efficiencyTrend()),
                         'virt trend',
                         myVolume()),

        ctx.makeTrader_A(strategy.MultiArmedBandit(
                                    strategies(),
                                    strategy.account.real(),
                                    strategy.weight.efficiencyTrend()),
                         'real trend',
                         myVolume()),

        ctx.makeTrader_A(strategy.MultiArmedBandit(
                                    strategies(),
                                    strategy.account.virtualMarket(),
                                    strategy.weight.efficiency()),
                         'virt efficiency',
                         myVolume()),

        ctx.makeTrader_A(strategy.MultiArmedBandit(
                                    strategies(),
                                    strategy.account.real(),
                                    strategy.weight.efficiency()),
                         'real efficiency',
                         myVolume()),

        ctx.makeTrader_A(strategy.MultiArmedBandit(
                                    strategies(),
                                    strategy.account.virtualMarket(),
                                    strategy.weight.score(),
                                    strategy.weight.atanPow()),
                         'virt score',
                         myVolume()),

        ctx.makeTrader_A(strategy.MultiArmedBandit(
                                    strategies(),
                                    strategy.account.real(),
                                    strategy.weight.score(),
                                    strategy.weight.clamp0()),
                         'real score',
                         myVolume()),

        ctx.makeTrader_A(strategy.MultiArmedBandit(
                                    strategies(),
                                    strategy.account.virtualMarket(),
                                    strategy.weight.efficiencyTrend(),
                                    strategy.weight.identityF(),
                                    strategy.weight.chooseTheBest()),
                         'virt best',
                         myVolume()),

        ctx.makeTrader_A(strategy.MultiArmedBandit(
                                    strategies(),
                                    strategy.account.real(),
                                    strategy.weight.unit(),
                                    strategy.weight.identityF()),
                         'uniform',
                         myVolume()),
    ]
    #
    #ctx.volumeStep = 30
    #
    #demo = ctx.addGraph('demo')
    #myVolume = lambda: [(trader.Position(), demo)]
    #
    #def fv(x):
    #    return  strategy.side.FundamentalValue(const(x)).Strategy(
    #                event.Every(constant(1.)),
    #                order.side.Market(volume = constant(1.)))
    #
    #xs = range(100, 200, 25)
    #def strategies():
    #    return map(fv, xs)
    #
    #def fv_traders():
    #    return [ctx.makeTrader_A(fv(x), "fv" + str(x), myVolume()) for x in xs]
    #
    #return [
    #    ctx.makeTrader_A(strategy.price.LiquidityProvider().Strategy(
    #        orderFactory = order.side_price.Limit(const(30))
    #                            .sideprice_WithExpiry(const(300))),
    #                     "liquidity"),
    #
    #    ctx.makeTrader_A(
    #            strategy.side.FundamentalValue(const(150)).Strategy(
    #                event.Every(constant(1.)),
    #                order.side.Market(volume = constant(10.))),
    #            'fv 12-200'),
    #
    #    ctx.makeTrader_A(strategy.MultiArmedBandit(
    #                                strategies(),
    #                                strategy.account.virtualMarket(),
    #                                strategy.weight.efficiencyTrend()),
    #                     'virt trend',
    #                     myVolume()),
    #
    #    ctx.makeTrader_A(strategy.MultiArmedBandit(
    #                                strategies(),
    #                                strategy.account.real(),
    #                                strategy.weight.efficiencyTrend()),
    #                     'real trend',
    #                     myVolume()),
    #
    #    ctx.makeTrader_A(strategy.MultiArmedBandit(
    #                                strategies(),
    #                                strategy.account.virtualMarket(),
    #                                strategy.weight.efficiency()),
    #                     'virt efficiency',
    #                     myVolume()),
    #
    #    ctx.makeTrader_A(strategy.MultiArmedBandit(
    #                                strategies(),
    #                                strategy.account.real(),
    #                                strategy.weight.efficiency()),
    #                     'real efficiency',
    #                     myVolume()),
    #
    #    ctx.makeTrader_A(strategy.MultiArmedBandit(
    #                                strategies(),
    #                                strategy.account.virtualMarket(),
    #                                strategy.weight.score(),
    #                                strategy.weight.atanPow()),
    #                     'virt score',
    #                     myVolume()),
    #
    #    ctx.makeTrader_A(strategy.MultiArmedBandit(
    #                                strategies(),
    #                                strategy.account.real(),
    #                                strategy.weight.score(),
    #                                strategy.weight.clamp0()),
    #                     'real score',
    #                     myVolume()),
    #
    #    ctx.makeTrader_A(strategy.MultiArmedBandit(
    #                                strategies(),
    #                                strategy.account.virtualMarket(),
    #                                strategy.weight.efficiencyTrend(),
    #                                strategy.weight.identityF(),
    #                                strategy.weight.chooseTheBest()),
    #                     'virt best',
    #                     myVolume()),
    #
    #    ctx.makeTrader_A(strategy.MultiArmedBandit(
    #                                strategies(),
    #                                strategy.account.real(),
    #                                strategy.weight.unit(),
    #                                strategy.weight.identityF()),
    #                     'uniform',
    #                     myVolume()),
    #
    #] + fv_traders()
