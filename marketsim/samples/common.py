import sys, itertools
sys.path.append(r'..')

from marketsim import (orderbook, observable, timeserie, scheduler, veusz, registry, 
                       context, trader, orderbook, Side, remote, mathutils, strategy)

simulations = {}

def expose(label, module):
    def inner(f):
        if module == '__main__':
            run(label, f)
        else:
            simulations[label] = f
        return f
    return inner
    

class Context(object):
    
    def __init__(self, world, graph_renderer):
        
        self.world = world 
        self.book_A = orderbook.Local(tickSize=0.01, label="A")
        self.book_B = orderbook.Local(tickSize=0.01, label="B")
        
        delay = mathutils.constant(1.07)

        self.link_A = remote.TwoWayLink(remote.Link(delay), remote.Link(delay))
        self.link_B = remote.TwoWayLink(remote.Link(delay), remote.Link(delay))

        self.remote_A = orderbook.Remote(self.book_A, self.link_A)
        self.remote_B = orderbook.Remote(self.book_B, self.link_B)
    
        self.graph = graph_renderer
        self.price_graph = self.graph("Price")
        self.eff_graph = self.graph("efficiency")
        self.amount_graph = self.graph("amount")
        
        self.graphs = [
                       self.price_graph, 
                       self.eff_graph, 
                       self.amount_graph
                       ]
         
        self.books = { 'Asset A' : self.book_A ,
                       'Asset B' : self.book_B , 
                       'Remote A': self.remote_A,
                       'Remote B': self.remote_B }
        
    def addGraph(self, name):
        graph = self.graph(name)
        self.graphs.append(graph)
        return graph
            
    def makeTrader(self, book, strategy, label, additional_ts = []):
        def trader_ts():
            thisTrader = trader.SASM_Proxy()
            return { observable.VolumeTraded(thisTrader) : self.amount_graph, 
                     observable.Efficiency(thisTrader)   : self.eff_graph }
        
        t = trader.SASM(book, strategy, label = label, timeseries = trader_ts())
                    
        for (ts, graph) in additional_ts:
            t.addTimeSerie(ts, graph)
            
        return t
    
    def makeMultiAssetTrader(self, books, aStrategy, label, additional_ts = []):
#        def trader_ts():
#            thisTrader = trader.SAMM_Proxy()
#            return { observable.VolumeTraded(thisTrader) : self.amount_graph, 
#                     observable.Efficiency(thisTrader)   : self.eff_graph }
        traders = [self.makeTrader(b, strategy.Empty(), label + "_" + b.label) for b in books]
        t = trader.MultiAsset(traders, aStrategy, label = label)
                    
        for (ts, graph) in additional_ts:
            t.addTimeSerie(ts, graph)
            
        return t
    
    
        
    def makeTrader_A(self, strategy, label, additional_ts = []):
        return self.makeTrader(self.book_A, strategy, label, additional_ts)
    
    def makeTrader_B(self, strategy, label, additional_ts = []):
        return self.makeTrader(self.book_B, strategy, label, additional_ts)
    
def orderBooksToRender(ctx, traders):
        books = list(set(itertools.chain(*[t.orderBooks for t in traders]))) 
        
        books = filter(lambda b: type(b) is orderbook.Local, books)       
        
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
            b.volumes_graph = ctx.addGraph("Volume levels " + b.label)
            thisBook = orderbook.Proxy()
            ts = orderbook_ts()
            ts.append(timeserie.VolumeLevels(
                           observable.VolumeLevels(1, 
                                                   thisBook, 
                                                   Side.Sell, 
                                                   30, 
                                                   10), 
                           b.volumes_graph))
            ts.append(timeserie.VolumeLevels(
                           observable.VolumeLevels(1, 
                                                   thisBook, 
                                                   Side.Buy, 
                                                   30, 
                                                   10), 
                           b.volumes_graph))
            b.timeseries = ts
            
            b.rsi_graph = ctx.addGraph("RSI " + b.label)
            ts.append(timeserie.ToRecord(observable.Price(thisBook), b.rsi_graph))
            for timeframe in [0., 1., 5., 10.]:
                ts.append(
                    timeserie.ToRecord(
                        observable.OnEveryDt(1, 
                            observable.RSI(thisBook, 
                                           timeframe, 
                                           1./14)), 
                        b.rsi_graph))
            
        return books
    
runTwoTimes = True
    
def run(name, constructor):
    with scheduler.create() as world:
        
        ctx = Context(world, veusz.Graph)
        traders = constructor(ctx)
        
        books = orderBooksToRender(ctx, traders)
        
        for t in traders + books:
            for ts in t.timeseries:
                ts.graph.addTimeSerie(ts)
        
        r = registry.create()
        root = registry.Simulation(traders, list(ctx.books.itervalues()), ctx.graphs)
        r.insert(root)
        r.pushAllReferences()
        context.bind(root, {'world' : world })
        
        world.workTill(500)
        
        non_empty_graphs = [g for g in ctx.graphs if len(g._datas)]
        
        veusz.render(name, non_empty_graphs)
        
        world._reset()
        context.reset(root)

        if runTwoTimes:
            world.workTill(500)
            veusz.render(name, non_empty_graphs)
