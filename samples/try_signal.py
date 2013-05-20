import sys
sys.path.append(r'..')

from marketsim import (signal, strategy, trader, orderbook, 
                       timeserie, scheduler, observable, veusz, mathutils)

from common import run

const = mathutils.constant

def Signal(graph, world, books):

    book_A = books['Asset A']

    price_graph = graph("Price")
    eff_graph = graph("efficiency")
    amount_graph = graph("amount")
     
    def trader_ts():
        thisTrader = trader.SASM_Proxy()
        return { observable.VolumeTraded(thisTrader) : amount_graph, 
                 observable.Efficiency(thisTrader)   : eff_graph }
    
    def orderbook_ts():
        thisBook = orderbook.Proxy()
        askPrice = observable.AskPrice(thisBook)
        bidPrice = observable.BidPrice(thisBook)
        assetPrice = observable.Price(thisBook)
        avg = observable.avg
        return [timeserie.ToRecord(askPrice, price_graph),
                timeserie.ToRecord(bidPrice, price_graph),
                timeserie.ToRecord(assetPrice, price_graph), 
                timeserie.ToRecord(avg(assetPrice, alpha=0.15), price_graph),
                timeserie.ToRecord(avg(assetPrice, alpha=0.65), price_graph),
                timeserie.ToRecord(avg(assetPrice, alpha=0.015), price_graph)]
       
    book_A.timeseries = orderbook_ts()
    
    lp_A = trader.SASM(book_A, 
                       strategy.LiquidityProvider(volumeDistr=const(2)),
                       "liquidity", 
                       timeseries = trader_ts())
    
    linear_signal = signal.RandomWalk(initialValue=20, 
                                      deltaDistr=const(-.1), 
                                      label="20-0.1t")
    
    signal_trader = trader.SASM(book_A, 
                                strategy.Signal(linear_signal), 
                                "signal", 
                                timeseries = trader_ts())

    signal_trader2 = trader.SASM(book_A, 
                                strategy.Signal2(linear_signal), 
                                "signal2", 
                                timeseries = trader_ts())
    
    signal_trader.addTimeSerie(linear_signal, amount_graph)
    
    signal_ex_trader = trader.SASM(book_A, 
                                   strategy.SignalEx(linear_signal), 
                                   "signal_ex", 
                                   timeseries = trader_ts())
        
    signal_ex_trader2 = trader.SASM(book_A, 
                                   strategy.SignalEx2(linear_signal), 
                                   "signal_ex 2", 
                                   timeseries = trader_ts())
        
    return [lp_A, signal_trader, signal_trader2, signal_ex_trader, signal_ex_trader2], [price_graph, eff_graph, amount_graph]

if __name__ == '__main__':
    run("signal_trader", Signal)