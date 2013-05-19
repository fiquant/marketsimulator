from flask import Flask, render_template, request, session, current_app
import sys, os, json, time, cPickle as pickle, weakref
sys.path.append(r'..')
sys.setrecursionlimit(10000)

from marketsim import (strategy, orderbook, trader, order, js, signal, remote,
                       scheduler, observable, veusz, mathutils, registry, translations)

from marketsim.types import Side

import samples

const = mathutils.constant

app = Flask(__name__)
app.secret_key = 'A0Zr98j/8769876IUOYOHOA0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

inmemory = {}


predefined = {"Default"             : samples.Complete,
              "Fundamental Value"   : samples.FundamentalValue,
              "Dependency"          : samples.Dependency,
              "Noise"               : samples.Noise,
              "Signal 20-0.1t"      : samples.Signal,
              "Trend Follower"      : samples.TrendFollower,
              "Two Averages"        : samples.TwoAverages,
              "Mean Reversion"      : samples.MeanReversion,
              "Canceller"           : samples.Canceller  }

def createSimulation(name='All'):
    
    with scheduler.create() as world:
        
        myRegistry = registry.create()
    
        myRegistry.insert(Side.Sell)
        myRegistry.insert(Side.Buy)    
        book_A = orderbook.Local(tickSize=0.01, label="Asset A")
        book_B = orderbook.Local(tickSize=0.01, label="Asset B")
        
        myRegistry.insert(book_A)
        remote_A = orderbook.Remote(book_A,
                                    remote.TwoWayLink(
                                        remote.Link(mathutils.rnd.expovariate(1)),
                                        remote.Link(mathutils.rnd.expovariate(1))))
        twoaverages = strategy.TwoAveragesEx()
        trendfollower = strategy.TrendFollowerEx()
        fundamentalvalue = strategy.FundamentalValueEx()
        meanreversion = strategy.MeanReversionEx()
        dependency = strategy.Dependency(book_B)
        dependency_ex = strategy.DependencyEx(book_B)
        lp_sell = strategy.LiquidityProviderSideEx()
        lp = strategy.LiquidityProviderEx()
        
        def register(annotated_objects):
            for obj, alias in annotated_objects:
                if alias is not None:
                    obj._alias = alias
                myRegistry.insert(obj)
                
        register([
                  (signal.RandomWalk(), ["Random walk"]),
                  (strategy.Signal(signal.RandomWalk()), ["Basic", "Signal"]),
                  (remote_A, ["Remote asset A"]),
                  (twoaverages, None),
                  (trendfollower, None),
                  (fundamentalvalue, None),
                  (meanreversion, None),
                  (dependency, ["Basic", "Dependency"]),
                  (dependency_ex, None),
                  (lp_sell, None),
                  (lp, None),
        ])
        
        myRegistry.pushAllReferences()

        def process(name):
            constructor = predefined[name]
        
            traders, graphs = constructor(js.Graph, world, myRegistry.orderBooksByName)
        
            for t in traders + graphs:
                myRegistry.insert(t)
                
        if name != 'All':
            process(name)
        else: 
            for n in predefined.iterkeys():
                process(n)
            
        myRegistry.insert(world)
        
        root = myRegistry.insert(registry.createSimulation(myRegistry))

        if name != 'All':
            current_dir = current_user_dir()
            ensure_dir_ex(current_dir)
            
            if os.path.exists(os.path.join(current_dir, name)):
                i = 0
                while os.path.exists(os.path.join(current_dir, name + "." + str(i))): 
                    i += 1
                name += '.' + str(i) 
        
        return name, root, myRegistry, world
    
def _timeseries(myRegistry):
    return [(k, v) for (k, v) in myRegistry._id2obj.iteritems()\
                     if type(v) == js.TimeSerie]

def save_state_before_changes(myRegistry):
    myRegistry.save_state_before_changes()
    for (_, ts) in _timeseries(myRegistry): 
        ts.save_state_before_changes()
        
def get_ts_changes(myRegistry):
    return dict([(k, v.get_changes()) for (k, v) in _timeseries(myRegistry)])

KEY = 'LLHJLKH'

def ensure_dir_ex(d):
    if not os.path.exists(d):
        os.makedirs(d)

def ensure_dir(f):
    ensure_dir_ex(os.path.dirname(f))

        
def make_filename_safe(s):
    return s.replace(":", '_').replace("/", '_').replace('\\', '_')

def current_user_dir():
    p = os.path.join('_saved', str(session[KEY]))
    ensure_dir_ex(p)
    return p

forceGenerate = False

def collectTypeInfo():
    filename = os.path.join('static', '_generated', 'typeinfo.js')
    ensure_dir(filename)
    if not os.path.exists(filename) or forceGenerate:
        _, _, myRegistry, _ = createSimulation('All')
        typeinfo = myRegistry.getTypeInfo()
        with open(filename, 'w') as f:
            f.write('var typeinfo = ');
            json.dump(typeinfo, f)
        
def generateTranslations():
    filename = os.path.join('static', '_generated', 'translations', 'en.js')
    ensure_dir(filename)
    if not os.path.exists(filename) or forceGenerate:
        with open(filename, 'w') as f:
            f.write('var translations_en = ');
            r = {}
            r.update(translations.en.property_names)
            r.update(translations.en.greeks)
            json.dump(r, f)
        
collectTypeInfo()
generateTranslations()

def latest_workspace_for_user():
    d = current_user_dir()
    ensure_dir_ex(d)
    bestt = 0
    bestw = None
    for w in os.listdir(d):
        f = os.path.join(d, w)
        t = os.path.getatime(f)
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

@app.route('/remove', methods=['POST'])
def remove():
    w = current_user_workspace()
    filename = os.path.join(current_user_dir(), w.name)
    if os.path.exists(filename):
        os.remove(filename)
    del inmemory[session[KEY]]
    return ""

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
        
@app.route('/common')
def common():
    return json.dumps(list(predefined.iterkeys()))
    
@app.route('/fork', methods=['POST'])
def fork():
    parsed = request_parsed()
    save_current_workspace()
    workspace = current_user_workspace()
    workspace.name = parsed["forkAs"]
    save_current_workspace()
    return ""

def _createFrom(name):
    set_current_workspace(Workspace(*createSimulation(name)))    

def _load(workspace_name):
    if workspace_name is None:
        _createFrom('Default')
    else:    
        filename = os.path.join(current_user_dir(), workspace_name)
        with open(filename, 'r') as input:
            set_current_workspace(pickle.load(input))
            
@app.route('/createFrom', methods=['POST'])
def createFrom():
    save_current_workspace()
    _createFrom(request_parsed()['createFrom'])
    save_current_workspace()
    return ""

@app.route('/load', methods=['POST'])
def load():
    save_current_workspace()
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
        "ts_changes" : dict([(k, v.data) for (k, v) in _timeseries(w.registry)])
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

    metaToCreate = {int(Id) : (meta[0], meta[1], meta[2]) for (Id, meta) in parsed['created']}

    with w.world: 
        w.registry.createNewObjects(metaToCreate)
        
        # changing fields for existing ones    
        for (Id, field, value) in parsed['updates']:
            w.registry.setAttr(Id, field, value)
            
    save_state_before_changes(w.registry) 

    save_current_workspace()
    
    if 'limitTime' in parsed:
        w.registry.bindVariables(w.registry.get(w.root),  { "world" : w.world })
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
        _createFrom("Default")
    elif session[KEY] not in inmemory:
        _load(latest_workspace_for_user())
    return render_template('index.html')

app.run(debug=True, use_reloader=False, threaded=True, port=80)
