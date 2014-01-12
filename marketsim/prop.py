""" Appends *callback* into collections of listeners for
    a change of property named *propname* of object *obj*
"""
def OnChanged(obj, propname, callback):
    from marketsim import event

    if '_on_property_changed' not in dir(obj):
        obj._on_property_changed = {}
        
    if propname not in obj._on_property_changed:
        obj._on_property_changed[propname] = event.Event()
        
        if '_new_property_changed_listener_added' in dir(obj):
            obj._new_property_changed_listener_added(propname)
        
    obj._on_property_changed[propname] += callback
    
def NotifyChanged(obj, propname, value):
    if '_on_property_changed' in dir(obj):
        if propname in obj._on_property_changed or '*' in obj._on_property_changed:
            obj._on_property_changed[propname](propname, value)

def Set(obj, propname, value):
    setattr(obj, propname, value)
    NotifyChanged(obj, propname, value)
