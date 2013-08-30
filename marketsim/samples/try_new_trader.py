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


@expose("Two Markets", __name__, only_veusz=True)
def TwoMarkets(ctx):
    exchange = create_exchange(books=[ctx.book_A, ctx.book_B])

    return [

        ctx.makeTrader_A(strategy.MarketData(), "marketdataA"),

        ctx.makeTrader_B(strategy.MarketData(), "marketdataB"),

        ctx.makeTrader_A(strategy.Noise(), "noiseA"),

        ctx.makeTrader_B(strategy.Noise(), "noiseB"),

        trader.Trader(exchange, strategy.v0.OrderbookStrategy())
    ]