""" Virtual orderbook observes price at another orderbook and pretends that 
    trades are done at price from that orderbook without any market impact
"""

class Queue(object):
    
    def __init__(self, original):
        self.original = original
        
    

class Virtual(object):
    
    def __init__(self, original):
        self.original = original
        
    