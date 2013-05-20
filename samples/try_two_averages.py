import sys
sys.path.append(r'..')

from marketsim import (signal, strategy, trader, orderbook, 
                       timeserie, scheduler, observable, veusz, mathutils)

from common import run

const = mathutils.constant

def TwoAverages(graph, world, books):

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
                       strategy.LiquidityProvider(volumeDistr=const(10)),
                       "liquidity", 
                       timeseries = trader_ts())
    
    linear_signal = signal.RandomWalk(initialValue=200, deltaDistr=const(-1), label="200-t")
    
    signal_trader = trader.SASM(book_A, 
                                strategy.Signal(linear_signal, 
                                                volumeDistr=const(3)), 
                                "signal", 
                                timeseries = trader_ts())
    
    signal_trader.addTimeSerie(linear_signal, amount_graph)
    
    slow = mathutils.ewma(alpha = 0.015)
    fast = mathutils.ewma(alpha = 0.15)
    
    avg_plus = trader.SASM(book_A, 
                           strategy.TwoAverages(average1 = slow, 
                                                average2 = fast), 
                           'avg+', 
                           timeseries = trader_ts())
    
    avg_minus = trader.SASM(book_A, 
                            strategy.TwoAverages(average1 = fast, 
                                                 average2 = slow), 
                            'avg-', 
                            timeseries = trader_ts())

    avg_plus2 = trader.SASM(book_A, 
                           strategy.TwoAverages2(average1 = slow, 
                                                average2 = fast), 
                           'avg2+', 
                           timeseries = trader_ts())
    
    avg_minus2 = trader.SASM(book_A, 
                            strategy.TwoAverages2(average1 = fast, 
                                                 average2 = slow), 
                            'avg2-', 
                            timeseries = trader_ts())

    avg_ex_plus = trader.SASM(book_A, 
                              strategy.TwoAveragesEx(average1 = slow, 
                                                     average2 = fast), 
                              'avg_ex+', 
                              timeseries = trader_ts())
    
    avg_ex_minus = trader.SASM(book_A, 
                               strategy.TwoAveragesEx(average1 = fast, 
                                                      average2 = slow), 
                               'avg_ex-', 
                               timeseries = trader_ts())
        
    avg_ex_plus2 = trader.SASM(book_A, 
                              strategy.TwoAveragesEx2(average1 = slow, 
                                                     average2 = fast), 
                              'avg_ex+ 2', 
                              timeseries = trader_ts())
    
    avg_ex_minus2 = trader.SASM(book_A, 
                               strategy.TwoAveragesEx2(average1 = fast, 
                                                      average2 = slow), 
                               'avg_ex- 2', 
                               timeseries = trader_ts())
        
    return [lp_A, signal_trader, avg_plus, avg_minus, avg_plus2, avg_minus2, avg_ex_plus, avg_ex_minus, avg_ex_plus2, avg_ex_minus2], [price_graph, eff_graph, amount_graph]

if __name__ == '__main__':
    run("two_averages", TwoAverages)