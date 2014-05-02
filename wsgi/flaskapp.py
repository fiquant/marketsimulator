from flask import Flask, render_template, request, session, current_app
import sys, os, json, time, cPickle as pickle, weakref, itertools
sys.path.append(r'..')
sys.setrecursionlimit(10000)

from marketsim import (event,
                       registry, translations, config)

from marketsim.gen._out.event._createscheduler import createScheduler

from marketsim._pub import math, strategy, trader, order

from marketsim.samples.common import Context, orderBooksToRender, simulations
from marketsim.gen._out._constant import constant

const = constant

app = Flask(__name__)
app.secret_key = config.secret_key

inmemory = {}


predefined = simulations

from marketsim.gen._out.js._graph import Graph

def createSimulation(name='All'):
    
    with createScheduler() as world:
        
        myRegistry = registry.create()
    
        ctx = Context(world, Graph)
        dependency_ex = strategy.side.PairTrading(ctx.book_B)\
                                     .Strategy(event.Every(math.random.expovariate(1.)),
                                               order.side.Market())
        
        def register(annotated_objects):
            for obj, alias in annotated_objects:
                if alias is not None:
                    obj._alias = alias
                myRegistry.insert(obj)
                
        register([
                  (dependency_ex, None),
        ])
        
        myRegistry.pushAllReferences()

        def process(name):
            constructor = predefined[name]
        
            traders = constructor(ctx)

            books = orderBooksToRender(ctx, traders)
        
            for t in traders + list(ctx.books.itervalues()) + ctx.graphs:
                myRegistry.insert(t)
                
        if name != 'All':
            process(name)
        else: 
            for n in predefined.iterkeys():
                process(n)
            
        myRegistry.insert(world)
        
        root = myRegistry.insert(registry.createSimulation(myRegistry))
        from marketsim.context import BindingContextEx
        myRegistry.get(root).bind_ex(BindingContextEx({ "world" : world }))
        myRegistry.get(root).registerIn(myRegistry)

        if name != 'All':
            current_dir = current_user_dir()
            ensure_dir_ex(current_dir)
            
            if os.path.exists(os.path.join(current_dir, name)):
                i = 0
                while os.path.exists(os.path.join(current_dir, name + "." + str(i))): 
                    i += 1
                name += '.' + str(i) 
        
        return name, root, myRegistry, world

from marketsim.gen._out._itimeserie import ITimeSerie
    
def _timeseries(myRegistry):
    return [(k, v) for (k, v) in myRegistry._id2obj.iteritems()\
                     if isinstance(v, ITimeSerie) ]

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
        typeinfo, interfaces = myRegistry.getTypeInfo()
        interfaces = [(myRegistry._dumpPropertyConstraint(key), list(value)) \
                        for key, value in interfaces.iteritems()]
                    
        myRegistry.typecheck()
        with open(filename, 'w') as f:
            f.write('var typeinfo = ');
            json.dump(typeinfo, f, indent=4, separators=(',', ': '))
            f.write('\nvar interfaces = ');
            json.dump(interfaces, f, indent=4, separators=(',', ': '))
        
def generateTranslations():
    filename = os.path.join('static', '_generated', 'translations', 'en.js')
    ensure_dir(filename)
    if not os.path.exists(filename) or forceGenerate:
        with open(filename, 'w') as f:
            f.write('var translations_en = ');
            r = {}
            r.update(translations.en.property_names)
            r.update(translations.en.greeks)
            json.dump(r, f, f, indent=4, separators=(',', ': '))
        
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
    w.registry.typecheck()
    result = {
        "simulations" : files,
        "name"  :   w.name,
        "root"  :   w.root,
        "objects" : w.registry.tojsonall(),
        "type2alias2id" : w.registry.getObjectsForAliases(),
        "currentTime" : w.world.currentTime,
        "ts_changes" : dict([(k, v.data) for (k, v) in _timeseries(w.registry)])
    }
    return json.dumps(result, sort_keys=True, indent=4, separators=(',', ': '))

def changes(w):
    result = {
        "currentTime" : w.world.currentTime,
        "changes" : w.registry.get_changes(),
        "ts_changes" : get_ts_changes(w.registry)
    }
    return json.dumps(result, sort_keys=True, indent=4, separators=(',', ': '))

@app.route('/reset', methods=['POST', 'GET'])
def reset():
    w = current_user_workspace()
    save_state_before_changes(w.registry)
    with w.world:
        reset_generation = getattr(w, 'reset_generation', 0)
        w.world.reset_ex(reset_generation)
        w.registry.get(w.root).reset_ex(reset_generation)
        w.reset_generation = reset_generation + 1
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
    print "update...",w.world.currentTime, 
    
    parsed = request_parsed()

    metaToCreate = dict([(int(Id), (meta[0], meta[1], meta[2])) for (Id, meta) in parsed['created']])

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

    result = changes(w)
    print "->", w.world.currentTime
    return result

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

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, threaded=True, port=80)
