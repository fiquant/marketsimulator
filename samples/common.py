import sys
sys.path.append(r'..')

from marketsim import orderbook, scheduler, veusz, registry, context

def run(name, constructor):
    with scheduler.create() as world:
        
        books = { 'Asset A' : orderbook.Local(tickSize=0.01, label="A"),
                  'Asset B' : orderbook.Local(tickSize=0.01, label="B") }
        
        traders, graphs = constructor(veusz.Graph, world, books)
        
        r = registry.create()
        root = registry.Simulation(traders, list(books.itervalues()), graphs)
        r.insert(root)
        r.pushAllReferences()
        context.Binder({'world' : world }).bind(root)
        
        world.workTill(500)
        
        veusz.render(name, graphs)
