import sys
sys.path.append(r'..')

from marketsim import strategy, orderbook, trader, scheduler, observable, veusz, mathutils, registry

const = mathutils.constant

with scheduler.create() as world:
    
    book_A = orderbook.Local(tickSize=0.01, label="A")
    
    price_graph = veusz.Graph("Price")
     
    assetPrice = observable.Price(book_A)
    price_graph.addTimeSerie(assetPrice)
    
    avg = observable.avg
    trend = observable.trend
    
    price_graph.addTimeSerie(avg(assetPrice))
    
    t_A = trader.SASM(book_A, strategy.LiquidityProvider(volumeDistr=const(70.)))
    
    c_200 = const(200.)
    
    fv_200_12 = strategy.FundamentalValue(fundamentalValue=c_200, volumeDistr=const(12))
    
    trader_200 = trader.SASM(book_A, fv_200_12, "t200")
    
    fv_200 = fv_200_12.With(volumeDistr = const(1.))
     
    trader_200_1=trader.SASM(book_A, fv_200, "t200_1")    
    trader_200_2=trader.SASM(book_A, fv_200, "t200_2")
    
    trader_150 = trader.SASM(book_A, 
                             strategy.FundamentalValue(fundamentalValue=const(150.), 
                                                            volumeDistr=const(1.)), 
                             "t150")
    
    meanreversion = trader.SASM(book_A, 
                                strategy.MeanReversion(volumeDistr=const(1.)), 
                                "mr_0_15")
    
    avg_plus = trader.SASM(book_A, 
                           strategy.TwoAverages(average1=mathutils.ewma(0.15),
                                                average2=mathutils.ewma(0.015),
                                                volumeDistr=const(1.)),
                           label="avg+")

    avg_minus= trader.SASM(book_A, 
                           strategy.TwoAverages(average1=mathutils.ewma(0.015),
                                                average2=mathutils.ewma(0.15),
                                                volumeDistr=const(1.)),
                           label="avg-")
    
    v_fv200 = trader.SASM(book_A, 
                          strategy.tradeIfProfitable(fv_200), 
                          "v_fv200")
    def s_fv(fv):
        return strategy.tradeIfProfitable(fv_200.With(fundamentalValue=const(fv)))

    def fv_virtual(fv):
        return trader.SASM(book_A, s_fv(fv), "v"+str(fv))
        
    
    virtual_160 = fv_virtual(160.)
    virtual_170 = fv_virtual(170.)
    virtual_180 = fv_virtual(180.)
    virtual_190 = fv_virtual(190.)
    
    best = trader.SASM(book_A, 
                       strategy.chooseTheBestEx([s_fv(160.), 
                                                 s_fv(170.), 
                                                 s_fv(180.), 
                                                 s_fv(190.),]), 
                       "best")
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
    
    traders = [trader_150, trader_200, trader_200_1, trader_200_2, 
                best, 
#                tf, tf_0_15, tf_0_015, 
                meanreversion, avg_plus, avg_minus, v_fv200,
                virtual_160, virtual_170, virtual_180, virtual_190
               ]
    
    addToGraph(traders)
    
    for t in traders + [t_A]:
        registry.instance.insert(t)
    
    for k,v in registry.instance.dumpall().iteritems():
        print k, v
        
    fv_200 = trader_200.strategies[0]
        
    c = registry.instance.createFromMeta(registry.instance.getUniqueId(), 
                                         ['marketsim.mathutils.constant', {'value': '50.0'}])
    
    world.workTill(500)

    registry.instance.setAttr(fv_200._id, 'fundamentalValue', c)
    
    world.advance(500)

    registry.instance.setAttr(fv_200.fundamentalValue._id, 'value', '200.')

    world.advance(500)
    
    veusz.render("fv_trader", [price_graph, eff_graph, trend_graph, pnl_graph, volume_graph])
