import sys
sys.path.append(r'..')

from marketsim import orderbook, observable, timeserie, scheduler, veusz, registry, context, trader, orderbook

class Context(object):
    
    def __init__(self, world):
        
        self.world = world 
        self.book_A = orderbook.Local(tickSize=0.01, label="A")
        self.book_B = orderbook.Local(tickSize=0.01, label="B")
    
        self.graph = veusz.Graph
        self.price_graph = self.graph("Price")
        self.eff_graph = self.graph("efficiency")
        self.amount_graph = self.graph("amount")
        
        self.graphs = [self.price_graph, self.eff_graph, self.amount_graph]
         
        self.books = { 'Asset A' : self.book_A ,
                       'Asset B' : self.book_B  }
        
    def makeTrader(self, book, strategy, label, additional_ts = []):
        def trader_ts():
            thisTrader = trader.SASM_Proxy()
            return { observable.VolumeTraded(thisTrader) : self.amount_graph, 
                     observable.Efficiency(thisTrader)   : self.eff_graph }
        
        t = trader.SASM(book, strategies = strategy, label = label, timeseries = trader_ts())\
            if type(strategy) == list\
            else trader.SASM(book, strategy, label, timeseries = trader_ts())
            
        for (ts, graph) in additional_ts:
            t.addTimeSerie(ts, graph)
            
        return t
        
    def makeTrader_A(self, strategy, label, additional_ts = []):
        return self.makeTrader(self.book_A, strategy, label, additional_ts)
    
    def makeTrader_B(self, strategy, label, additional_ts = []):
        return self.makeTrader(self.book_B, strategy, label, additional_ts)
    
runTwoTimes = False
    
def run(name, constructor):
    with scheduler.create() as world:
        
        ctx = Context(world)
        traders = constructor(ctx)
        
        books = list(set([t.orderBook for t in traders]))        
        
        graphs = ctx.graphs
        
        def orderbook_ts():
            thisBook = orderbook.Proxy()
            askPrice = observable.AskPrice(thisBook)
            bidPrice = observable.BidPrice(thisBook)
            assetPrice = observable.Price(thisBook)
            avg = observable.avg
            return [timeserie.ToRecord(askPrice, ctx.price_graph),
                    timeserie.ToRecord(bidPrice, ctx.price_graph),
                    timeserie.ToRecord(assetPrice, ctx.price_graph), 
                    timeserie.ToRecord(avg(assetPrice, alpha=0.15), ctx.price_graph),
                    timeserie.ToRecord(avg(assetPrice, alpha=0.65), ctx.price_graph),
                    timeserie.ToRecord(avg(assetPrice, alpha=0.015), ctx.price_graph)]

        for b in books:
            b.timeseries = orderbook_ts()
        
        r = registry.create()
        root = registry.Simulation(traders, list(ctx.books.itervalues()), graphs)
        r.insert(root)
        r.pushAllReferences()
        context.Binder({'world' : world }).bind(root)
        
        world.workTill(500)
        
        veusz.render(name, graphs)
        
        world._reset()
        context.Resetter().apply(root)

        if runTwoTimes:
            world.workTill(500)
            veusz.render(name, graphs)
