from marketsim import strategy, orderbook, trader, scheduler, observable, veusz,\
    mathutils

world = scheduler.create()

book_A = orderbook.Local(tickSize=0.01, label="A")

price_graph = veusz.Graph("Price")
 
assetPrice = observable.Price(book_A)
price_graph.addTimeSerie(assetPrice)

avg = observable.avg
trend = observable.trend

price_graph.addTimeSerie(avg(assetPrice))

lp_A = strategy.LiquidityProvider(trader.SASM(book_A), volumeDistr=lambda: 70).trader

trader_200 = strategy.FundamentalValue(trader.SASM(book_A, "t200"), fundamentalValue=lambda: 200., volumeDistr=lambda: 12).trader
trader_200_1 = strategy.FundamentalValue(trader.SASM(book_A, "t200_1"), fundamentalValue=lambda: 200., volumeDistr=lambda: 1).trader
trader_200_2 = strategy.FundamentalValue(trader.SASM(book_A, "t200_2"), fundamentalValue=lambda: 200., volumeDistr=lambda: 1).trader

trader_150 = strategy.FundamentalValue(trader.SASM(book_A, "t150"), fundamentalValue=lambda: 150., volumeDistr=lambda: 1).trader

def fv_virtual(fv):
    return strategy.suspendIfNotEffective(\
                strategy.withEstimator(
                        strategy.FundamentalValue, 
                        trader = trader.SASM(book_A, "v"+str(fv)), 
                        volumeDistr = lambda: 1,
                        fundamentalValue=lambda: fv)).trader

virtual_160 = fv_virtual(160.)
virtual_170 = fv_virtual(170.)
virtual_180 = fv_virtual(180.)
virtual_190 = fv_virtual(190.)

def fv(x, trader):
    return strategy.withEstimator(
                strategy.FundamentalValue, 
                trader = trader, 
                volumeDistr = lambda: 1,
                fundamentalValue=lambda: fv)

best_trader = trader.SASM(book_A, "best")    
strategies = [fv(x, best_trader) for x in range(170, 190, 10)]
best = strategy.chooseTheBest(strategies)    

#tf = strategy.suspendIfNotEffective(\
#        strategy.withEstimator(strategy.TrendFollower, 
#                               trader = trader.SASM(book_A, "TF"), 
#                               average=mathutils.ewma(0.015), 
#                               volumeDistr=lambda: 5)).trader
#
#tf_0_15 = strategy.suspendIfNotEffective(\
#            strategy.withEstimator(strategy.TrendFollower,
#                                   trader=trader.SASM(book_A, "tf0.15"), 
#                                   average=mathutils.ewma(0.15),
#                                   volumeDistr=lambda: 1)).trader
#                                         
#tf_0_015 = strategy.suspendIfNotEffective(\
#            strategy.withEstimator(strategy.TrendFollower,
#                                   trader=trader.SASM(book_A, "tf0.015"), 
#                                   average=mathutils.ewma(0.015),
#                                   volumeDistr=lambda: 1)).trader

eff_graph = veusz.Graph("efficiency")
trend_graph = veusz.Graph("efficiency trend")
pnl_graph = veusz.Graph("P&L")
volume_graph = veusz.Graph("volume")

def addToGraph(traders):
    for t in traders:
        e = observable.Efficiency(t)
        #eff_graph.addTimeSerie(e)
        #eff_graph.addTimeSerie(InstEfficiency(t))
        eff_graph.addTimeSerie(avg(e))
        trend_graph.addTimeSerie(trend(e))
        #trend_graph.addTimeSerie(trend(InstEfficiency(t)))
        pnl_graph.addTimeSerie(observable.PnL(t))
        volume_graph.addTimeSerie(observable.VolumeTraded(t))


addToGraph([trader_150, trader_200, best_trader, trader_200_1, trader_200_2,
            virtual_160, virtual_170, virtual_180, virtual_190])

world.workTill(1500)

veusz.render("fv_trader", [price_graph, eff_graph, trend_graph, pnl_graph, volume_graph])
