import sys
sys.path.append(r'../..')

from marketsim import (order, parts, signal, strategy, trader, orderbook, 
                       event, timeserie,  observable, veusz, mathutils, ops)

const = ops.constant

from common import expose

@expose("Multiarmed-Bandit", __name__)
def MultiarmedBandit(ctx):

    ctx.volumeStep = 30
        
    demo = ctx.addGraph('demo')
    myVolume = lambda: [(observable.VolumeTraded(), demo)]
    myAverage = lambda alpha: [(observable.avg(observable.MidPrice(orderbook.OfTrader()), alpha), demo)]
    
    def fv(x):
        return  strategy.FundamentalValue(
                    event.Every(ops.constant(1.)),
                    order.factory.side.Market(volume = const(1.)),
                    fundamentalValue = const(x))
                                        
    xs = range(100, 300, 50) + range(160, 190, 10)
    def strategies():
        return map(fv, xs)
    
    def fv_traders():
        return [ctx.makeTrader_A(fv(x), "fv" + str(x), myVolume()) for x in xs]
        
    return [
        ctx.makeTrader_A(strategy.LiquidityProvider(
            orderFactory = order.factory.sideprice.Limit(volume=ops.constant(45))),
                         "liquidity"),
            
        ctx.makeTrader_A(        
                strategy.FundamentalValue(
                    event.Every(ops.constant(1.)),
                    order.factory.side.Market(volume = const(12.)),
                    fundamentalValue = const(200)),
                'fv 12-200'), 

        ctx.makeTrader_A(strategy.MultiarmedBandit(
                                    strategies(), 
                                    strategy.adaptive.virtualMarket(),
                                    strategy.adaptive.weight.efficiencyTrend()),
                         'virt trend',
                         myVolume()),

        ctx.makeTrader_A(strategy.MultiarmedBandit(
                                    strategies(), 
                                    strategy.adaptive.account(),
                                    strategy.adaptive.weight.efficiencyTrend()),
                         'real trend',
                         myVolume()),

        ctx.makeTrader_A(strategy.MultiarmedBandit(
                                    strategies(), 
                                    strategy.adaptive.virtualMarket(),
                                    strategy.adaptive.weight.efficiency()),
                         'virt efficiency',
                         myVolume()),

        ctx.makeTrader_A(strategy.MultiarmedBandit(
                                    strategies(), 
                                    strategy.adaptive.account(),
                                    strategy.adaptive.weight.efficiency()),
                         'real efficiency',
                         myVolume()),

        ctx.makeTrader_A(strategy.MultiarmedBandit(
                                    strategies(),
                                    strategy.adaptive.virtualMarket(),
                                    strategy.adaptive.weight.score(),
                                    strategy.adaptive.weight.atanpow()),
                         'virt score',
                         myVolume()),

        ctx.makeTrader_A(strategy.MultiarmedBandit(
                                    strategies(),
                                    strategy.adaptive.account(),
                                    strategy.adaptive.weight.score(),
                                    strategy.adaptive.weight.clamp0()),
                         'real score',
                         myVolume()),

        ctx.makeTrader_A(strategy.MultiarmedBandit(
                                    strategies(), 
                                    strategy.adaptive.virtualMarket(),
                                    strategy.adaptive.weight.efficiencyTrend(),
                                    strategy.adaptive.weight.identityF(),
                                    strategy.adaptive.weight.chooseTheBest()),
                         'virt best',
                         myVolume()),

        ctx.makeTrader_A(strategy.MultiarmedBandit(
                                    strategies(), 
                                    strategy.adaptive.account(),
                                    strategy.adaptive.weight.unit(),
                                    strategy.adaptive.weight.identityF()),
                         'uniform',
                         myVolume()),

    ] + fv_traders()
