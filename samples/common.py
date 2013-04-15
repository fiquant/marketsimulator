import sys
sys.path.append(r'..')

from marketsim import orderbook, scheduler, veusz

def run(name, constructor):
    with scheduler.create() as world:
        
        books = { 'Asset A' : orderbook.Local(tickSize=0.01, label="A"),
                  'Asset B' : orderbook.Local(tickSize=0.01, label="B") }
        
        traders, graphs = constructor(veusz.Graph, world, books)
        
        for t in traders: t.run()
        
        world.workTill(500)
        
        veusz.render(name, graphs)

def simulation(f):
    a = f
    return f