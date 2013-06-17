import sys
sys.path.append(r'..')

from marketsim import strategy, order, orderbook, trader, scheduler

with scheduler.create() as world:
    
    book = orderbook.Local()
    
    trader = trader.SingleAsset(book, 
                         strategy.TrendFollower(creationIntervalDistr=lambda: 1, 
                                                volumeDistr=lambda: 1))
    
    for x in range(90, 100):
        book.process(order.Limit.Buy(x, 1))
        
    for x in range(101, 111):
        book.process(order.Limit.Sell(x, 1))
        
    assert trader.amount == 0
    assert trader.PnL == 0
    
    world.workTill(0.9)
    
    book.process(order.Limit.Buy(101,2))
    
    assert book.asks.best.price == 102
    assert book.price == 101.5
    
    world.workTill(1.1)
    
    assert book.asks.best.price == 103
    assert book.price == 102
    
    assert trader.amount == 1
    assert trader.PnL == -102
    
    book.process(order.Limit.Sell(95,10))
    assert book.asks.best.price == 95
    assert book.bids.best.price == 94
        
    world.workTill(2.1)
    
    assert book.bids.best.price == 93
    assert trader.amount == 0
    assert trader.PnL == -102 +94
