import sys
sys.path.append(r'..')

from marketsim import orderbook, scheduler, veusz, registry

def run(name, constructor):
    with scheduler.create() as world:
        
        books = { 'Asset A' : orderbook.Local(tickSize=0.01, label="A"),
                  'Asset B' : orderbook.Local(tickSize=0.01, label="B"),
                  'Proxy A' : orderbook.Proxy(),
                  'Proxy B' : orderbook.Proxy() }
        
        traders, graphs = constructor(veusz.Graph, world, books)
        
        r = registry.create()
        s = registry.Simulation(traders, list(books.itervalues()), graphs)
        r.insert(s)
        r.pushAllReferences()
        r.resolveVariables()
        r.activateObj(s, world)
        
        for t in traders: t.run()
        
        world.workTill(500)
        
        veusz.render(name, graphs)

def simulation(f):
    a = f
    return f