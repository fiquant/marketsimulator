import sys
sys.path.append(r'../..')

from marketsim import (order, parts, signal, strategy, trader, orderbook, 
                       timeserie, scheduler, observable, veusz, mathutils, ops)

const = ops.constant

from common import expose

@expose("Multiarmed-Bandit", __name__)
def MultiarmedBandit(ctx):

    ctx.volumeStep = 30
        
    demo = ctx.addGraph('demo')
    myVolume = lambda: [(observable.VolumeTraded(), demo)]
    myAverage = lambda alpha: [(observable.avg(observable.MidPrice(orderbook.OfTrader()), alpha), demo)]
    
    def fv(x):
        return strategy.Generic(
                    order.factory.Market(
                        side = parts.side.FundamentalValue(ops.constant(x)),
                        volume = const(1.)),
                    scheduler.Timer(const(1.)))
        
    xs = range(100, 300, 50) + range(160, 190, 10)
    def strategies():
        return map(fv, xs)
    
    def fv_traders():
        return [ctx.makeTrader_A(fv(x), "fv" + str(x), myVolume()) for x in xs]
        
    return [
        ctx.makeTrader_A(strategy.v0.LiquidityProvider(volumeDistr=const(45)),
                         "liquidity"),
            
        ctx.makeTrader_A(        
                strategy.Generic(
                    order.factory.Market(
                        side = parts.side.FundamentalValue(ops.constant(200)),
                        volume = const(12.)),
                    scheduler.Timer(const(1.))),
                'fv 12-200'), 

        ctx.makeTrader_A(strategy.MultiarmedBandit(
                                    strategies(), 
                                    strategy.adaptive.virtualMarket,
                                    strategy.adaptive.weight.efficiencyTrend), 
                         'virt trend',
                         myVolume()),

        ctx.makeTrader_A(strategy.MultiarmedBandit(
                                    strategies(), 
                                    strategy.adaptive.account,
                                    strategy.adaptive.weight.efficiencyTrend), 
                         'real trend',
                         myVolume()),

        ctx.makeTrader_A(strategy.MultiarmedBandit(
                                    strategies(), 
                                    strategy.adaptive.virtualMarket,
                                    strategy.adaptive.weight.efficiency), 
                         'virt efficiency',
                         myVolume()),

        ctx.makeTrader_A(strategy.MultiarmedBandit(
                                    strategies(), 
                                    strategy.adaptive.account,
                                    strategy.adaptive.weight.efficiency), 
                         'real efficiency',
                         myVolume()),

        ctx.makeTrader_A(strategy.MultiarmedBandit(
                                    strategies(), 
                                    strategy.adaptive.virtualMarket,
                                    strategy.adaptive.weight.score, 
                                    strategy.adaptive.weight.identity), 
                         'virt score',
                         myVolume()),

        ctx.makeTrader_A(strategy.MultiarmedBandit(
                                    strategies(), 
                                    strategy.adaptive.account,
                                    strategy.adaptive.weight.score, 
                                    strategy.adaptive.weight.identity), 
                         'real score',
                         myVolume()),

        ctx.makeTrader_A(strategy.MultiarmedBandit(
                                    strategies(), 
                                    strategy.adaptive.virtualMarket,
                                    strategy.adaptive.weight.efficiencyTrend, 
                                    strategy.adaptive.weight.identity, 
                                    strategy.adaptive.weight.chooseTheBest), 
                         'virt best',
                         myVolume()),

        ctx.makeTrader_A(strategy.MultiarmedBandit(
                                    strategies(), 
                                    strategy.adaptive.account,
                                    strategy.adaptive.weight.unit,
                                    strategy.adaptive.weight.identity), 
                         'uniform',
                         myVolume()),

    ] + fv_traders()
