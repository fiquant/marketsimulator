class Int(float):
    @property
    def constant(self):
        from marketsim.gen._out._constant import constant
        return constant(self)
    
    @property
    def const(self):
        from marketsim.gen._out._const import const
        return const(self)
    
    pass
