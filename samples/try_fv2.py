import sys
sys.path.append(r'..')

from marketsim import (strategy, trader, orderbook, 
                       scheduler, observable, veusz, registry)

with scheduler.create() as world:
    
    book_A = orderbook.Local(tickSize=0.01, label="A")
    
    price_graph = veusz.Graph("Price")
     
    assetPrice = observable.Price(book_A)
    
    avg = observable.avg
    
    
    lp_A = trader.SASM(book_A, strategy = strategy.LiquidityProvider(volumeDistr=lambda:1))
    trader = trader.SASM(book_A, strategy.FundamentalValue(fundamentalValue = lambda: world.currentTime), "fv_200")
    
    price_graph += [assetPrice,
                    avg(assetPrice)]
    
    eff_graph = veusz.Graph("efficiency")
    eff_graph += [observable.Efficiency(trader),
                  observable.PnL(trader)]
    
    world.workTill(500)
    
    veusz.render("fv_200_trader", [price_graph, eff_graph])
    
