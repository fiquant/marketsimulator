import sys
sys.path.append(r'../../..')

from marketsim import strategy, orderbook, trader, scheduler, observable, veusz, mathutils

with scheduler.create() as world:
    
    book_A = orderbook.Local(tickSize=0.01, label="A")
    
    price_graph = veusz.Graph("Price")
     
    assetPrice = observable.Price(book_A)
    price_graph.addTimeSerie(assetPrice)
    
    avg = observable.avg
    trend = observable.trend
    
    price_graph.addTimeSerie(avg(assetPrice))
    
    t_A = trader.SASM(book_A, strategy.LiquidityProvider(volumeDistr=lambda: 70))
    
    trader_200 = trader.SASM(book_A, 
                             strategy.FundamentalValue(fundamentalValue=lambda: 200., 
                                                            volumeDistr=lambda: 12),
                             "t200")
    
    trader_200_1=trader.SASM(book_A, 
                             strategy.FundamentalValue(fundamentalValue=lambda: 200., 
                                                            volumeDistr=lambda: 1), 
                             "t200_1")
    
    trader_200_2=trader.SASM(book_A, 
                             strategy.FundamentalValue(fundamentalValue=lambda: 200., 
                                                            volumeDistr=lambda: 1), 
                             "t200_2")
    
    trader_150 = trader.SASM(book_A, 
                             strategy.FundamentalValue(fundamentalValue=lambda: 150., 
                                                            volumeDistr=lambda: 1), 
                             "t150")
    
    meanreversion = trader.SASM(book_A, 
                                strategy.MeanReversion(volumeDistr=lambda:1), 
                                "mr_0_15")
    
    avg_plus = trader.SASM(book_A, 
                           strategy.TwoAverages(average1=mathutils.ewma(0.15),
                                                average2=mathutils.ewma(0.015),
                                                volumeDistr=lambda:1),
                           label="avg+")

    avg_minus= trader.SASM(book_A, 
                           strategy.TwoAverages(average1=mathutils.ewma(0.015),
                                                average2=mathutils.ewma(0.15),
                                                volumeDistr=lambda:1),
                           label="avg-")
    
#    def fv_virtual(fv):
#        return strategy.suspendIfNotEffective(\
#                    strategy.withEstimator(
#                            strategy.FundamentalValue, 
#                            trader = trader.SASM(book_A, "v"+str(fv)), 
#                            volumeDistr = lambda: 1,
#                            fundamentalValue=lambda: fv)).trader
#    
#    virtual_160 = fv_virtual(160.)
#    virtual_170 = fv_virtual(170.)
#    virtual_180 = fv_virtual(180.)
#    virtual_190 = fv_virtual(190.)
#    
#    def fv(x, trader):
#        return strategy.withEstimator(
#                    strategy.FundamentalValue, 
#                    trader = trader, 
#                    volumeDistr = lambda: 1,
#                    fundamentalValue=lambda: fv)
#    
#    best_trader = trader.SASM(book_A, "best")    
#    strategies = [fv(x, best_trader) for x in range(170, 190, 10)]
#    best = strategy.chooseTheBest(strategies)    
    
#    tf = strategy.suspendIfNotEffective(\
#            strategy.withEstimator(strategy.TrendFollower, 
#                                   trader = trader.SASM(book_A, label="TF"), 
#                                   average=mathutils.ewma(0.015), 
#                                   volumeDistr=lambda: 5)).trader
#    
#    tf_0_15 = strategy.suspendIfNotEffective(\
#                strategy.withEstimator(strategy.TrendFollower,
#                                       trader=trader.SASM(book_A, label="tf0.15"), 
#                                       average=mathutils.ewma(0.15),
#                                       volumeDistr=lambda: 1)).trader
#                                             
#    tf_0_015 = strategy.suspendIfNotEffective(\
#                strategy.withEstimator(strategy.TrendFollower,
#                                       trader=trader.SASM(book_A, label="tf0.015"), 
#                                       average=mathutils.ewma(0.015),
#                                       volumeDistr=lambda: 1)).trader
#    
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
    
    
    addToGraph([trader_150, trader_200, trader_200_1, trader_200_2, 
#                best_trader, 
#                tf, tf_0_15, tf_0_015, 
                meanreversion, avg_plus, avg_minus,
#                virtual_160, virtual_170, virtual_180, virtual_190
                ])
    
    world.workTill(1500)
    
    veusz.render("fv_trader", [price_graph, eff_graph, trend_graph, pnl_graph, volume_graph])
