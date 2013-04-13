from flask import Flask, render_template, request, session, current_app
import sys, os, json, time, pickle, weakref
sys.path.append(r'..')
sys.setrecursionlimit(10000)

from marketsim import (strategy, orderbook, trader, order, js, signal, remote,
                       scheduler, observable, veusz, mathutils, registry)

from marketsim.types import Side

const = mathutils.constant

app = Flask(__name__)
app.secret_key = 'A0Zr98j/8769876IUOYOHOA0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

inmemory = {}

def createSimulation():
    myRegistry = registry.create()
    
    with scheduler.create() as world:
        
        book_A = orderbook.Local(tickSize=0.01, label="Asset A")
        myRegistry.insert(book_A)
        remote_A = orderbook.Remote(book_A, 
                                    remote.TwoWayLink(
                                        remote.Link(mathutils.rnd.expovariate(1)), 
                                        remote.Link(mathutils.rnd.expovariate(1))))
        
        def register(annotated_objects):
            for obj, alias in annotated_objects:
                obj._alias = alias
                myRegistry.insert(obj)
                
        register([
                  (signal.RandomWalk(), "Random walk"),
                  (strategy.Signal(signal.RandomWalk()), "Signal"),
                  (remote_A, "Remote asset A"),
        ])
        
        price_graph = js.Graph("Price")
         
        assetPrice = observable.Price(book_A)
        price_graph.addTimeSeries([assetPrice, observable.AskPrice(book_A), observable.BidPrice(book_A)])
        
        avg = observable.avg
        trend = observable.trend
        
        price_graph.addTimeSerie(avg(assetPrice))
        
        t_A = trader.SASM(book_A, 
                          strategy.LiquidityProvider(
                                volumeDistr=const(70.), 
                                orderFactoryT=order.WithExpiryFactory(
                                    expirationDistr=const(10))))
        
        c_200 = const(200.)
        
        fv_200_12 = strategy.FundamentalValue(fundamentalValue=c_200, volumeDistr=const(12))
        
        trader_200 = trader.SASM(book_A, fv_200_12, "t200")
        
        fv_200 = fv_200_12.With(volumeDistr=const(1.))
         
        trader_200_1 = trader.SASM(book_A, fv_200, "t200_1")    
        trader_200_2 = trader.SASM(book_A, fv_200.With(), "t200_2")
        
        trader_150 = trader.SASM(book_A,
                                 strategy.FundamentalValue(fundamentalValue=const(150.),
                                                                volumeDistr=const(1.)),
                                 "t150")
        
        meanreversion = trader.SASM(book_A,
                                    strategy.MeanReversion(volumeDistr=const(1.)),
                                    "mr_0_15")
        
        avg_plus = trader.SASM(book_A,
                               strategy.TwoAverages(average1=mathutils.ewma(0.15),
                                                    average2=mathutils.ewma(0.015),
                                                    volumeDistr=const(1.)),
                               label="avg+")
    
        avg_minus = trader.SASM(book_A,
                               strategy.TwoAverages(average1=mathutils.ewma(0.015),
                                                    average2=mathutils.ewma(0.15),
                                                    volumeDistr=const(1.)),
                               label="avg-")
        
        v_fv200 = trader.SASM(book_A,
                              strategy.TradeIfProfitable(fv_200),
                              "v_fv200")
        def s_fv(fv):
            return strategy.TradeIfProfitable(fv_200.With(fundamentalValue=const(fv)))
    
        def fv_virtual(fv):
            return trader.SASM(book_A, s_fv(fv), "v" + str(fv))
            
        
        virtual_160 = fv_virtual(160.)
        virtual_170 = fv_virtual(170.)
        virtual_180 = fv_virtual(180.)
        virtual_190 = fv_virtual(190.)
        
        best = trader.SASM(book_A,
                           strategy.chooseTheBest([s_fv(160.),
                                                   s_fv(170.),
                                                   s_fv(180.),
                                                   s_fv(190.), ]),
                           "best")
    
        eff_graph = js.Graph("efficiency")
        trend_graph = js.Graph("efficiency trend")
        pnl_graph = js.Graph("P&L")
        volume_graph = js.Graph("volume")
        
        def addToGraph(traders):
            for t in traders:
                e = observable.Efficiency(t)
                # eff_graph.addTimeSerie(e)
                # eff_graph.addTimeSerie(InstEfficiency(t))
                eff_graph.addTimeSerie(avg(e))
                trend_graph.addTimeSerie(trend(e))
                # trend_graph.addTimeSerie(trend(InstEfficiency(t)))
                pnl_graph.addTimeSerie(observable.PnL(t))
                volume_graph.addTimeSerie(observable.VolumeTraded(t))
        
        traders = [trader_150, trader_200, trader_200_1, trader_200_2,
                    best,
    #                tf, tf_0_15, tf_0_015, 
                    meanreversion, avg_plus, avg_minus, v_fv200,
                    virtual_160, virtual_170, virtual_180, virtual_190
                   ]
        
        addToGraph(traders)
        
        for t in traders + [t_A] + [price_graph, eff_graph, trend_graph, pnl_graph, volume_graph]:
            myRegistry.insert(t)
        
        fv_200 = trader_200.strategies[0]
        
        def new(name, fields):
            return myRegistry.createFromMeta(myRegistry.getUniqueId(), 
                                                    [name, fields])
    
        def setAttr(obj, name, value):
            myRegistry.setAttr(myRegistry.insert(obj), name, value)
        
        c = new('marketsim.mathutils.constant', {'value': '50.0'})
    
        interval = new('marketsim.mathutils.rnd.expovariate', {'Lambda': '+1.0'})
        
        setAttr(fv_200, 'orderFactory', order.MarketFactory)
        setAttr(fv_200, 'creationIntervalDistr', interval)
        setAttr(avg_plus.strategies[0], 'average1', new('marketsim.mathutils.ewma', {'alpha' : 0.15 }))
        setAttr(virtual_160.strategies[0], 'estimator', strategy.virtualWithUnitVolume)
    
        myRegistry.insert(Side.Sell)
        myRegistry.insert(Side.Buy)    
        myRegistry.insert(world)
        
        root = myRegistry.insert(registry.createSimulation(myRegistry))
        
        return root, myRegistry, world
    
def _timeseries(myRegistry):
    return [(k,v) for (k,v) in myRegistry._id2obj.iteritems()\
                     if type(v) == js.TimeSerie]

def save_state_before_changes(myRegistry):
    myRegistry.save_state_before_changes()
    for (_,ts) in _timeseries(myRegistry): 
        ts.save_state_before_changes()
        
def get_ts_changes(myRegistry):
    return dict([(k, v.get_changes()) for (k,v) in _timeseries(myRegistry)])

KEY = 'LLHJLKH'

def ensure_dir_ex(d):
    if not os.path.exists(d):
        os.makedirs(d)

def ensure_dir(f):
    ensure_dir_ex(os.path.dirname(f))

        
def make_filename_safe(s):
    return s.replace(":", '_').replace("/", '_').replace('\\', '_')

def current_user_dir():
    return os.path.join('_saved', str(session[KEY]))

def latest_workspace_for_user():
    d = current_user_dir()
    bestt = 0
    bestw = None
    for w in os.listdir(d):
        f = os.path.join(d, w)
        t = os.path.getmtime(f)
        if t > bestt:
            bestt = t
            bestw = w
    return bestw

class Workspace(object):
    
    def __init__(self, name, root, registry, world):
        self.root = root
        self.registry = registry
        self.world = world
        self.name = name

def current_user_workspace():
    if session[KEY] not in inmemory:
        _load(latest_workspace_for_user())
    return inmemory[session[KEY]]

def set_current_workspace(workspace):
    inmemory[session[KEY]] = workspace 
    
def request_parsed():
    raw = request.form.iterkeys().__iter__().next()
    return json.loads(raw)

def save_current_workspace():
    w = current_user_workspace()
    filename = os.path.join(current_user_dir(), w.name)
    ensure_dir(filename)
    with open(filename, 'wb') as output:
        pickle.dump(w, output)
    
@app.route('/save', methods=['POST'])
def save():
    parsed = request_parsed()
    workspace = current_user_workspace()
    workspace.name = parsed["saveTo"]
    save_current_workspace()
    return ""

def _load(workspace_name):
    filename = os.path.join(current_user_dir(), workspace_name)
    with open(filename, 'r') as input:
        set_current_workspace(pickle.load(input))

@app.route('/load', methods=['POST'])
def load():
    _load(request_parsed()['loadFrom'])
    return ""

@app.route('/all')
def get_all():
    w = current_user_workspace()
    files = os.listdir(current_user_dir())
    result = {
        "simulations" : files,
        "name"  :   w.name,
        "root"  :   w.root,
        "objects" : w.registry.tojsonall(),
        "currentTime" : w.world.currentTime,
        "ts_changes" : dict([(k,v.data) for (k,v) in _timeseries(w.registry)])
    }
    return json.dumps(result)

def changes(w):
    result = {
        "currentTime" : w.world.currentTime,
        "changes" : w.registry.get_changes(),
        "ts_changes" : get_ts_changes(w.registry)
    }
    return json.dumps(result)

@app.route('/reset', methods=['POST', 'GET'])
def reset():
    w = current_user_workspace()
    save_state_before_changes(w.registry)
    with w.world: 
        w.registry.reset()
    save_current_workspace()
    return changes(w)

def run(world, timeout, limitTime):
    t0 = time.clock()
    world._to_be_stopped = False
    while time.clock() - t0 < timeout and not world._to_be_stopped:
        if not world.step(limitTime):
            world.workTill(limitTime)
            return
    

@app.route('/update', methods=['POST'])
def update():
    w = current_user_workspace()
    
    parsed = request_parsed()

    metaToCreate = {int(Id) : (meta[0], meta[1]) for (Id, meta) in parsed['created']}

    with w.world: 
        w.registry.createNewObjects(metaToCreate)
        
        # changing fields for existing ones    
        for (Id, field, value) in parsed['updates']:
            w.registry.setAttr(Id, field, value)
            
    save_state_before_changes(w.registry) 

    save_current_workspace()
    
    if 'limitTime' in parsed:
        limitTime = parsed['limitTime']
        timeout = parsed["timeout"]
        run(w.world, timeout, limitTime)
        
    save_current_workspace()
    return changes(w)

@app.route('/stop', methods=['POST'])
def stop():
    w = current_user_workspace()
    w.world._to_be_stopped = True
    return ""

@app.route('/')
def index():
    if KEY not in session:
        session[KEY] = time.time()
        set_current_workspace(Workspace('default', *createSimulation()))
        ensure_dir_ex(current_user_dir())
    elif session[KEY] not in inmemory:
        _load(latest_workspace_for_user())
    return render_template('index.html')

app.run(debug=True, use_reloader=False, threaded=True, port=80)
