from marketsim import trader, strategy, order, orderbook, scheduler

world = scheduler.create()
        
book_A = orderbook.Local()
book_B = orderbook.Local()

trader = strategy.Arbitrage(trader.SAMM([book_A, book_B])).trader

b_120 = order.Limit.Buy(120,10)
b_110 = order.Limit.Buy(110,10)
book_B.bids.push(b_120)
world.advance(1)
book_B.bids.push(b_110)
world.advance(1)

s_100 = order.Limit.Sell(100,5)
book_A.process(s_100)
world.advance(1)
assert s_100.volume == 0
assert s_100.PnL == 100*5
assert trader.PnL == 20*5

assert book_B.bids.best.volume == 5
assert book_B.bids.best.PnL == -120*5

s_90 = order.Limit.Sell(90,10)
book_A.process(s_90)
world.advance(1)
assert trader.PnL == 20*5 + 5*(120-90) + 5*(110-90)

assert s_90.volume == 0
assert s_90.PnL == 90*10

assert book_B.bids.best.volume == 5
assert book_B.bids.best.PnL == -110*5
assert b_120.volume == 0
assert b_120.PnL == -120*10

assert b_110.volume == 5
assert b_110.PnL == -110*5

s_95 = order.Limit.Sell(95,10)
book_A.process(s_95)
world.advance(1)
assert trader.PnL == 20*5 + 5*(120-90) + 5*(110-90) + 5*(110-95)
assert s_95.volume == 5
assert s_95.PnL == 95*5

assert b_110.volume == 0
assert b_110.PnL == -110*10

world.reset()
