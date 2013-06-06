import sys
sys.path.append(r'..')

from marketsim import (orderbook, observable, timeserie, scheduler, veusz, registry, 
                       context, trader, orderbook, Side)

class Context(object):
    
    def __init__(self, world):
        
        self.world = world 
        self.book_A = orderbook.Local(tickSize=0.01, label="A")
        self.book_B = orderbook.Local(tickSize=0.01, label="B")
    
        self.graph = veusz.Graph
        self.price_graph = self.graph("Price")
        self.eff_graph = self.graph("efficiency")
        self.amount_graph = self.graph("amount")
        
        self.graphs = [
                       self.price_graph, 
                       self.eff_graph, 
                       self.amount_graph
                       ]
         
        self.books = { 'Asset A' : self.book_A ,
                       'Asset B' : self.book_B  }
        
    def addGraph(self, name):
        graph = self.graph(name)
        self.graphs.append(graph)
        return graph

        
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
    
runTwoTimes = True
    
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
            return [
                    timeserie.ToRecord(askPrice, ctx.price_graph),
                    timeserie.ToRecord(bidPrice, ctx.price_graph),
                    timeserie.ToRecord(assetPrice, ctx.price_graph), 
                    timeserie.ToRecord(avg(assetPrice, alpha=0.15), ctx.price_graph),
                    timeserie.ToRecord(avg(assetPrice, alpha=0.65), ctx.price_graph),
                    timeserie.ToRecord(avg(assetPrice, alpha=0.015), ctx.price_graph)
                    ]

        for b in books:
            b.volumes_graph = veusz.Graph("Volume levels " + b.label)
            thisBook = orderbook.Proxy()
            ts = orderbook_ts()
            ts.append(timeserie.ToRecord(
                           observable.VolumeLevels(1, 
                                                   thisBook, 
                                                   Side.Sell, 
                                                   30, 
                                                   10), 
                           b.volumes_graph))
            ts.append(timeserie.ToRecord(
                           observable.VolumeLevels(1, 
                                                   thisBook, 
                                                   Side.Buy, 
                                                   30, 
                                                   10), 
                           b.volumes_graph))
            b.timeseries = ts
            graphs.append(b.volumes_graph)
        
        r = registry.create()
        root = registry.Simulation(traders, list(ctx.books.itervalues()), graphs)
        r.insert(root)
        r.pushAllReferences()
        context.bind(root, {'world' : world })
        
        world.workTill(500)
        
        non_empty_graphs = [g for g in graphs if len(g._datas)]
        
        veusz.render(name, non_empty_graphs)
        
        world._reset()
        context.reset(root)

        if runTwoTimes:
            world.workTill(500)
            veusz.render(name, non_empty_graphs)
