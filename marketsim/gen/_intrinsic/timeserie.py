from marketsim import event, _

class _ToRecord_Impl(object):  # TODO: should the source be split into dataSource and eventSource?
    
    def __init__(self):
        self.attributes = getattr(self.source, 'attributes', {})
        self._smooth =  1 if 'smooth' in self.attributes and self.attributes['smooth'] else 0
        self._lastPoint = None
        self._event = event.subscribe(self.source, _(self)._wakeUp, self)
        self.reset()
        
    def bind(self, context):
        self._sched = context.world
        
    @property
    def _digits(self):
        return self.source.digits if 'digits' in dir(self.source) else 4
    
    @property    
    def _alias(self):
        return [self.source.label]  if '__alias' not in dir(self) else self.__alias
    
    @_alias.setter
    def _alias(self, value):
        self.__alias = value      
        
    @property
    def label(self):
        return self.source.label
    
    def _pushLastPoint(self):
        if self._lastPoint:
            self._data.append(self._lastPoint)
            self._changes.append(self._lastPoint)
            self._lastPoint = None
    
    def _wakeUp(self, _):
        """ Called when the source has changed
        """
        def appendex(target, (x,y)):
            if y is not None:
                target.append((x,y))
            else:
                if len(target) and target[-1][1] is not None:
                    if x - target[-1][0] > 1e-10:
                        target.append((x - 1e-10, target[-1][1]))
                        target.append((x, None))
                
        x = self.source()
        if hasattr(self, "_sched"):
            appendex(self._data, (self._sched.currentTime, x))
            # we should also filter out constant segmemnts
            appendex(self._changes, (self._sched.currentTime, x))
                
    def reset(self):
        self._data = []
        self._changes = []

    def save_state_before_changes(self):
        self._changes = []        
    
    def get_changes(self):
        self._wakeUp(None)
        self._pushLastPoint()
        return self._changes    

    @property    
    def data(self):
        self._pushLastPoint()
        return self._data
    
    def drop(self): # later a more sophisticated protocol would be introduced
        self._data = []

class _VolumeLevels_Impl(_ToRecord_Impl):

    @property
    def _volumes(self):
        return self.source.dataSource.volumes

    @_volumes.setter
    def _volumes(self, s): pass

    @property
    def _isBuy(self):
        from marketsim.gen._out._side import Side
        return 1 if self.source.dataSource.queue.side() == Side.Buy else 0

    @_isBuy.setter
    def _isBuy(self, o): pass

