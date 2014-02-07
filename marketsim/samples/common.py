import sys, itertools, pickle
sys.path.append(r'..')
sys.setrecursionlimit(10000)

from marketsim import (_, scheduler, veusz, registry, config,
                       context, bind, IEvent)

from marketsim.ops import Function

from marketsim._pub import orderbook, TimeSerie, volumeLevels, trader, math, observable, const, strategy, side

simulations = {}

def expose(label, module, only_veusz=False):
    def inner(f):
        if module == '__main__':
            run(label, f, only_veusz)
        else:
            if not only_veusz:
                simulations[label] = f
        return f
    return inner
    
constant = const

def _print(*args):
    if len(args) == 1:
        print args[0],
    else:
        print args


def makeTimeSerie(source, graph):
    if not isinstance(source, IEvent):
        source = observable.OnEveryDt(1, source)
    return TimeSerie(source, graph)


class Context(object):
    
    def __init__(self, world, graph_renderer):
        
        self.world = world 
        self.book_A = orderbook.Local(tickSize=0.01, name="A")
        self.book_B = orderbook.Local(tickSize=0.01, name="B")
        self.book_C = orderbook.Local(tickSize=0.01, name="C")

        if config.showTiming:
            self.world.process(const(10), bind.Function(_print, '.'))
            self.world.process(const(100), bind.Function(_print, '\n'))
        
        delay = constant(1.07)

        self.link_A = orderbook.TwoWayLink(orderbook.Link(delay), orderbook.Link(delay))
        self.link_B = orderbook.TwoWayLink(orderbook.Link(delay), orderbook.Link(delay))
        self.link_C = orderbook.TwoWayLink(orderbook.Link(delay), orderbook.Link(delay))

        self.remote_A = orderbook.Remote(self.book_A, self.link_A)
        self.remote_B = orderbook.Remote(self.book_B, self.link_B)
        self.remote_C = orderbook.Remote(self.book_C, self.link_C)

        self.graph = graph_renderer
        self.price_graph = self.graph("Price")
        self.askbid_graph = self.graph("AskBid")
        self.candles_graph = self.graph("Candles")
        self.avgs_graph = self.graph("Averages")
        self.macd_graph = self.graph("MACD")
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
                       self.askbid_graph,
                       self.candles_graph,
                       self.avgs_graph,
                       self.macd_graph,
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
        graph = self.graph(name = name)
        self.graphs.append(graph)
        return graph

    def makeTrader(self, book, strategy, label, additional_ts = []):
        def trader_ts():
            thisTrader = trader.SingleProxy()
            return [
                TimeSerie(trader.Position(thisTrader),      self.amount_graph),
                TimeSerie(trader.Balance(thisTrader),       self.balance_graph)
            ] + ([TimeSerie(trader.Efficiency(thisTrader),    self.eff_graph)] if config.collectMoving else [])

        t = trader.SingleAsset(book, strategy, name = label, timeseries = trader_ts())
                    
        for (ts, graph) in additional_ts:
            t.addTimeSerie(ts, graph)
            
        return t
    
    def makeMultiAssetTrader(self, books, aStrategy, label, additional_ts = []):
        traders = [self.makeTrader(b, strategy.Empty(), label + "_" + b.label) for b in books]
        t = trader.MultiAsset(traders, aStrategy, name = label)
                    
        for (ts, graph) in additional_ts:
            t.addTimeSerie(ts, graph)
            
        return t
    
    def makeMinorTrader(self, strategy, label):
        def trader_ts():
            thisTrader = trader.SingleProxy()
            return [ TimeSerie(trader.Efficiency(thisTrader), self.minors_eff_graph),
                     TimeSerie(trader.Position(thisTrader), self.minors_amount_graph) ]
        
        return trader.SingleAsset(self.book_A, strategy, name = label, timeseries = trader_ts())
        
    def makeTrader_A(self, strategy, label, additional_ts = []):
        return self.makeTrader(self.book_A, strategy, label, additional_ts)
    
    def makeTrader_rA(self, strategy, label, additional_ts = []):
        return self.makeTrader(self.remote_A, strategy, label, additional_ts)
    
    def makeTrader_B(self, strategy, label, additional_ts = []):
        return self.makeTrader(self.book_B, strategy, label, additional_ts)

    def makeTrader_C(self, strategy, label, additional_ts = []):
        return self.makeTrader(self.book_C, strategy, label, additional_ts)

from marketsim.gen._out.orderbook._Local import Local_StringFloatIntListITimeSerie

def orderBooksToRender(ctx, traders):
        books = list(set(itertools.chain(*[t.orderBooks for t in traders]))) 
        
        books = filter(lambda b: type(b) is Local_StringFloatIntListITimeSerie, books)
        
        graphs = ctx.graphs
        
        def orderbook_ts():
            from marketsim.gen._out.math._Max import Max

            thisBook = orderbook.Proxy()
            assetPrice = orderbook.MidPrice(thisBook)
            scaled = (assetPrice - 100) / 10

            def bollinger(avg, stddev):
                return [
                    assetPrice, 
                    avg, 
                    observable.OnEveryDt(1, avg + stddev*2), 
                    observable.OnEveryDt(1, avg - stddev*2)
                ]

            ts = {
                ctx.price_graph : [
                    assetPrice,
                    orderbook.ask.Price(),
                    orderbook.bid.Price(),
                ],
                ctx.askbid_graph : [
                    orderbook.ask.LastTradePrice(),
                    orderbook.ask.WeightedPrice(),
                    orderbook.bid.LastTradePrice(),
                    orderbook.bid.WeightedPrice()
                ],
                ctx.avgs_graph : [
                    math.Cumulative.Avg(assetPrice),
                    (math.Moving.Avg(assetPrice, 20), config.collectMoving),
                    (math.Moving.Avg(assetPrice, 100), config.collectMoving),
                    math.EW.Avg(assetPrice, 0.15),
                    math.EW.Avg(assetPrice, 0.65),
                    math.EW.Avg(assetPrice, 0.015),
                ],
                ctx.macd_graph : [
                    scaled,
                    math.EW.Avg(scaled, 2./27),
                    math.EW.Avg(scaled, 2./13),
                    math.macd.MACD(assetPrice),
                    math.macd.Signal(assetPrice),
                    math.macd.Histogram(assetPrice),
                    (observable.OnEveryDt(1, math.LogReturns(assetPrice) * 100), config.collectMoving)
                ],
                ctx.minmax_graph : [
                    assetPrice,
                    math.Cumulative.MaxEpsilon(assetPrice),
                    math.Cumulative.MinEpsilon(assetPrice),
                    (math.Moving.Max(assetPrice, 100.), config.collectMoving),
                    (math.Moving.Min(assetPrice, 100.), config.collectMoving)
                ],
                ctx.bollinger_100_graph : bollinger(math.Moving.Avg(assetPrice, 100), math.Moving.StdDev(assetPrice, 100)) if config.collectMoving else [],
                ctx.bollinger_20_graph : bollinger(math.Moving.Avg(assetPrice, 20), math.Moving.StdDev(assetPrice, 20)) if config.collectMoving else [],
                ctx.bollinger_a015_graph : bollinger(math.EW.Avg(assetPrice, 0.015), math.EW.StdDev(assetPrice, 0.015)),

            }

            out = []
            for (graph, timeserie_list) in ts.iteritems():
                for timeserie in timeserie_list:
                    if type(timeserie) is tuple:
                        if timeserie[1]:
                            timeserie = timeserie[0]
                        else:
                            continue
                    out.append(makeTimeSerie(timeserie, graph))

            return out

        for b in books:
            thisBook = orderbook.Proxy()
            ts = orderbook_ts()
            b.volumes_graph = ctx.addGraph("Volume levels " + b.label)
            ts.append(volumeLevels(
                           orderbook.VolumeLevels(orderbook.Queue(thisBook, side.Sell()),
                                                   30,
                                                   10),
                           b.volumes_graph))
            ts.append(volumeLevels(
                           orderbook.VolumeLevels(orderbook.Queue(thisBook, side.Buy()),
                                                   30,
                                                   10),
                           b.volumes_graph))
            b.timeseries = ts

            if config.collectRSI:
                b.rsi_graph = ctx.addGraph("RSI " + b.label)
                ts.append(TimeSerie(orderbook.MidPrice(thisBook), b.rsi_graph))
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
                        TimeSerie(
                            observable.OnEveryDt(1,
                                math.RSI(thisBook,
                                               timeframe,
                                               1./14)),
                            b.rsi_graph))

        return books
    
runTwoTimes = True

def run(name, constructor, only_veusz):
    with scheduler.create() as world:
        
        ctx = Context(world, veusz.Graph)
        traders = constructor(ctx)

        if config.useMinorTraders:
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

        def checks():
            if not only_veusz and config.checkConsistency:
                r.typecheck()
                try:
                    dumped = pickle.dumps(r)
                    pickle.loads(dumped)
                except Exception, err:
                    print err

        checks()        
        stat = world.workTill(500)
        checks()        

        if config.showTiming:
            print "\n", stat
        
        non_empty_graphs = [g for g in ctx.graphs if len(g._datas)]
        
        veusz.render(name, non_empty_graphs)
        
        world._reset()
        context.reset(root)

        if False and config.runTwoTimes:
            world.workTill(500)
            veusz.render(name, non_empty_graphs)

def Constant(c, demo):
    return [(observable.OnEveryDt(10, constant(c)), demo)]

class Interlacing(Function[float]):

    def __init__(self, phase = 1, timeframe = 10):
        self.timeframe = timeframe
        self.phase = phase
    
    def bind(self, ctx):
        self._scheduler = ctx.world
        
    def __call__(self):
        return int(self._scheduler.currentTime / self.timeframe) % 2 * 2 - 1

from marketsim import Side as SIDE

class InterlacingSide(Function[SIDE]):
    
    def __init__(self, phase = 1, timeframe = 10):
        self._impl = Interlacing(phase, timeframe)
        
    _internals = ['_impl']
        
    def __call__(self):
        return side.Buy() if self._impl() > 0 else side.Sell()
