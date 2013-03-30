import sys
sys.path.append(r'..')

from marketsim import (strategy, trader, orderbook, order,
                       scheduler, observable, veusz, registry)

with scheduler.create() as world:
    
    book_A = orderbook.Local(tickSize=0.01, label="A")
    
    price_graph = veusz.Graph("Price")
     
    assetPrice = observable.Price(book_A)
    
    avg = observable.avg
    
    
    lp_A = trader.SASM(book_A, 
                       strategy.LiquidityProvider(
                            volumeDistr=lambda:1,
                            orderFactoryT=order.WithExpiryFactory(
                                expirationDistr=lambda: 10)))
    noise_trader = trader.SASM(book_A, strategy.Noise(), "noise")
    
    price_graph += [assetPrice,
                    avg(assetPrice)]
    
    eff_graph = veusz.Graph("efficiency")
    eff_graph += [observable.Efficiency(noise_trader),
                  observable.PnL(noise_trader)]
    
    for t in [lp_A, noise_trader]: t.run()
    
    world.workTill(500)
    
    veusz.render("noise_trader", [price_graph, eff_graph])
    
