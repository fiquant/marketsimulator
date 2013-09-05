import sys
sys.path.append(r'../..')

from marketsim import strategy, ops, trader
from marketsim.asset import StockBase as Stock
from marketsim.exchange import ExchangeBase as StockExchange

from common import expose



def create_exchange(books=[]):
    assets_with_books = {Stock(label=book.label): book for book in books}
    exchange = StockExchange(label="Exchange")
    exchange.update(assets_with_books)
    return exchange

def multi_level(ctx, max_delta = 5):
    return [ctx.makeTrader_A(strategy.MarketData(delta=k, volume = k*k),
                             "m{0}".format(k)) for k in xrange(max_delta)]

@expose("Two Markets", __name__, only_veusz=True)
def TwoMarkets(ctx):
    exchange = create_exchange(books=[ctx.book_A, ctx.book_B])

    return [

        ctx.makeTrader_B(strategy.MarketData(), "marketdataB"),

        ctx.makeTrader_A(strategy.Noise(), "noiseA"),

        ctx.makeTrader_B(strategy.Noise(), "noiseB"),

        # trader.Trader(exchange, strategy.v0.OrderbookStrategy()),
        trader.Trader(exchange, strategy.v0.TrendFollow())
    ] + multi_level(ctx, 2)