import sys
sys.path.append(r'..')

from marketsim import orderbook, scheduler, veusz, registry, context

class Context(object):
    
    def __init__(self, world):
        
        self.world = world 
        self.book_A = orderbook.Local(tickSize=0.01, label="A")
        self.book_B = orderbook.Local(tickSize=0.01, label="B")
        
        self.books = { 'Asset A' : self.book_A ,
                       'Asset B' : self.book_B  }
        
        self.graph = veusz.Graph
        
def run(name, constructor):
    with scheduler.create() as world:
        
        ctx = Context(world)
        traders, graphs = constructor(ctx)
        
        r = registry.create()
        root = registry.Simulation(traders, list(ctx.books.itervalues()), graphs)
        r.insert(root)
        r.pushAllReferences()
        context.Binder({'world' : world }).bind(root)
        
        world.workTill(500)
        
        veusz.render(name, graphs)
