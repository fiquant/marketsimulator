class IStatDomain(object):
    @property
    def Source(self):
        from marketsim.gen._out.math.impl._source import Source
        return Source(self)
    
    pass
