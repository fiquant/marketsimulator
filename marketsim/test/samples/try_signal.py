import sys
sys.path.append(r'../../..')

from marketsim import signal, strategy, trader, orderbook, scheduler, observable, veusz

with scheduler.create() as world:
    
    book_A = orderbook.Local(tickSize=0.01, label="A")
    
    price_graph = veusz.Graph("Price")
     
    assetPrice = observable.Price(book_A)
    
    avg = observable.avg
    
    
    lp_A = strategy.LiquidityProvider(trader.SASM(book_A), volumeDistr=lambda:1).trader
    signal = signal.RandomWalk(initialValue=20, deltaDistr=lambda: -.1, label="signal")
    trader = strategy.Signal(trader.SASM(book_A, "signal"), signal).trader
    
    price_graph += [assetPrice,
                    avg(assetPrice),
                    signal,
                    observable.VolumeTraded(trader)]
    
    eff_graph = veusz.Graph("efficiency")
    eff_graph += [observable.Efficiency(trader),
                  observable.PnL(trader)]
    
    world.workTill(500)
    
    veusz.render("signal_trader", [price_graph, eff_graph])
    
