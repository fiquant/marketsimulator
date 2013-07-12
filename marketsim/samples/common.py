import sys, itertools
sys.path.append(r'..')

from marketsim import (orderbook, observable, timeserie, scheduler, veusz, registry, event,
                       context, trader, orderbook, Side, remote, ops, signal, strategy)

simulations = {}

def expose(label, module):
    def inner(f):
        if module == '__main__':
            run(label, f)
        else:
            simulations[label] = f
        return f
    return inner
    
const = ops.constant 

def _print(ch):
    print ch,

class Context(object):
    
    def __init__(self, world, graph_renderer):
        
        self.world = world 
        self.book_A = orderbook.Local(tickSize=0.01, label="A")
        self.book_B = orderbook.Local(tickSize=0.01, label="B")
        
        self.world.process(lambda: 10, lambda: _print('.'))
        self.world.process(lambda: 100, lambda: _print('\n'))
        
        delay = ops.constant(1.07)

        self.link_A = remote.TwoWayLink(remote.Link(delay), remote.Link(delay))
        self.link_B = remote.TwoWayLink(remote.Link(delay), remote.Link(delay))

        self.remote_A = orderbook.Remote(self.book_A, self.link_A)
        self.remote_B = orderbook.Remote(self.book_B, self.link_B)
    
        self.graph = graph_renderer
        self.price_graph = self.graph("Price")
        self.eff_graph = self.graph("efficiency")
        self.amount_graph = self.graph("amount")
        self.balance_graph = self.graph('balance')
        self.bollinger_a015_graph = self.graph('bollinger alpha 0.15')
        self.bollinger_20_graph = self.graph('bollinger 20')
        self.bollinger_100_graph = self.graph('bollinger 100')
        self.minmax_graph = self.graph('minmax')
        self.minors_eff_graph = self.graph('minor traders efficiency')
        self.minors_amount_graph = self.graph('minor traders position')
        
        self.graphs = [
                       self.price_graph, 
                       self.eff_graph, 
                       self.amount_graph,
                       self.balance_graph, 
                       self.bollinger_20_graph,
                       self.bollinger_a015_graph,
                       self.bollinger_100_graph,
                       self.minmax_graph, 
                       self.minors_eff_graph, 
                       self.minors_amount_graph
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
            thisTrader = trader.SingleProxy()
            return { observable.VolumeTraded(thisTrader) : self.amount_graph, 
                     observable.Efficiency(thisTrader)   : self.eff_graph,
                     observable.PnL(thisTrader)          : self.balance_graph 
                   }
        
        t = trader.SingleAsset(book, strategy, label = label, timeseries = trader_ts())
                    
        for (ts, graph) in additional_ts:
            t.addTimeSerie(ts, graph)
            
        return t
    
    def makeMultiAssetTrader(self, books, aStrategy, label, additional_ts = []):
        def trader_ts():
            thisTrader = trader.MultiProxy()
            return { 
#                        observable.VolumeTraded(thisTrader) : self.amount_graph, 
#                        observable.Efficiency(thisTrader)   : self.eff_graph,
                         observable.PnL(thisTrader)          : self.balance_graph 
                   }
        traders = [self.makeTrader(b, strategy.Empty(), label + "_" + b.label) for b in books]
        t = trader.MultiAsset(traders, aStrategy, label = label, timeseries = trader_ts())
                    
        for (ts, graph) in additional_ts:
            t.addTimeSerie(ts, graph)
            
        return t
    
    def makeMinorTrader(self, strategy, label):
        def trader_ts():
            thisTrader = trader.SingleProxy()
            return { observable.Efficiency(thisTrader)   : self.minors_eff_graph, 
                     observable.VolumeTraded(thisTrader) : self.minors_amount_graph    }
        
        return trader.SingleAsset(self.book_A, strategy, label = label, timeseries = trader_ts())
        
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
            assetPrice = observable.MidPrice(thisBook)
            avg = observable.avg
            cma = observable.CMA(assetPrice)
            stddev = observable.StdDev(assetPrice)
            ma100 = observable.MA(assetPrice, 100)
            ma20 = observable.MA(assetPrice, 20)
            stddev100 = observable.StdDevRolling(assetPrice, 100)
            stddev20 = observable.StdDevRolling(assetPrice, 20)
            ewma015 = observable.EWMA(assetPrice, alpha=0.15)
            ewmsd = observable.StdDevEW(assetPrice, 0.15)
            min = observable.Min(assetPrice, 100)
            max = observable.Max(assetPrice, 100)
            candlesticks = observable.CandleSticks(assetPrice, 10)
            
            def bollinger(mean, stddev, graph):
                return [
                    timeserie.ToRecord(assetPrice, graph), 
                    timeserie.ToRecord(observable.OnEveryDt(1, mean), graph), 
                    timeserie.ToRecord(observable.OnEveryDt(1, mean + stddev*2), graph), 
                    timeserie.ToRecord(observable.OnEveryDt(1, mean - stddev*2), graph),
                ] 
            
            return ([
                timeserie.ToRecord(candlesticks, ctx.price_graph),
                timeserie.ToRecord(askPrice, ctx.price_graph),
                timeserie.ToRecord(bidPrice, ctx.price_graph),
                timeserie.ToRecord(assetPrice, ctx.price_graph), 
                timeserie.ToRecord(observable.LastTradePrice(thisBook), ctx.price_graph), 
                timeserie.ToRecord(observable.AskLastTradePrice(thisBook), ctx.price_graph), 
                timeserie.ToRecord(observable.BidLastTradePrice(thisBook), ctx.price_graph), 
                
                timeserie.ToRecord(observable.OnEveryDt(1, cma), ctx.price_graph), 
                
                timeserie.ToRecord(assetPrice, ctx.minmax_graph),
                timeserie.ToRecord(max, ctx.minmax_graph),
                timeserie.ToRecord(min, ctx.minmax_graph),

                timeserie.ToRecord(avg(assetPrice, alpha=0.15), ctx.price_graph),
                timeserie.ToRecord(avg(assetPrice, alpha=0.65), ctx.price_graph),
                timeserie.ToRecord(avg(assetPrice, alpha=0.015), ctx.price_graph)
            ] 
            + bollinger(ma100, stddev100, ctx.bollinger_100_graph) 
            + bollinger(ma20, stddev20, ctx.bollinger_20_graph)
            + bollinger(ewma015, ewmsd, ctx.bollinger_a015_graph))

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
            ts.append(timeserie.ToRecord(observable.MidPrice(thisBook), b.rsi_graph))
            for timeframe in [#0., 
                              #0.001,
                              #0.01,
                              0.1, 
                              #0.3, 
                              0.5, 
                              1., 
                              #1.5, 
                              2, 
                              #3, 
                              #4, 
                              5]:
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
        
        traders.extend([
            ctx.makeMinorTrader(strategy.RSI_linear(k = const(0.07)), "RSI 0.07"), 
            ctx.makeMinorTrader(strategy.RSI_linear(k = const(-0.07)), "RSI -0.07"),
            ctx.makeMinorTrader(strategy.Bollinger_linear(alpha=0.15, k = const(-0.5)), "Bollinger -0.5"),
            ctx.makeMinorTrader(strategy.Bollinger_linear(alpha=0.15, k = const(+0.5)), "Bollinger +0.5"),
        ])
        
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

        if False and runTwoTimes:
            world.workTill(500)
            veusz.render(name, non_empty_graphs)

def Constant(c, demo):
    return [(observable.OnEveryDt(10, ops.constant(c)), demo)]