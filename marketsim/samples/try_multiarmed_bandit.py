import sys
sys.path.append(r'../..')

from marketsim._pub import (order, strategy, trader, orderbook, event, observable, math, constant, const)

from common import expose

@expose("Multiarmed-Bandit", __name__)
def MultiarmedBandit(ctx):

    ctx.volumeStep = 30
        
    demo = ctx.addGraph('demo')
    myVolume = lambda: [(trader.Position(), demo)]

    def fv(x):
        return  strategy.FundamentalValue(
                    event.Every(constant(1.)),
                    order.side.Market(volume = constant(1.)),
                    fundamentalValue = const(x))
                                        
    xs = range(100, 300, 50) + range(160, 190, 10)
    def strategies():
        return map(fv, xs)
    
    def fv_traders():
        return [ctx.makeTrader_A(fv(x), "fv" + str(x), myVolume()) for x in xs]
        
    return [
        ctx.makeTrader_A(strategy.LiquidityProvider(
            orderFactory = order.side_price.Limit(volume=constant(45))),
                         "liquidity"),
            
        ctx.makeTrader_A(        
                strategy.FundamentalValue(
                    event.Every(constant(1.)),
                    order.side.Market(volume = constant(12.)),
                    fundamentalValue = const(200)),
                'fv 12-200'), 

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

    ] + fv_traders()
