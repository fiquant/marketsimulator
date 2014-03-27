from marketsim import types, getLabel

def aux(name):
    return name[0:2] == "__" or name == '_processing'

from marketsim.gen._out._intrinsic_base.trader.proxy import Single_Base

class Base(object):

    def __init__(self):

        self.__dict__['_impl'] = None

    def _bind(self, impl):
        assert self._impl is  None
        self.__dict__['_impl'] = impl

    def __getattr__(self, name):
        if not aux(name) and self._impl:
            return getattr(self._impl, name)
        else:
            raise AttributeError

    def __setattr__(self, name, value):
        if not aux(name) and self._impl:
            setattr(self._impl, name, value)
        else:
            self.__dict__[name] = value

    def __delattr__(self, name):
        if not aux(name) and self._impl:
            del self._impl.name
        else:
            del self.__dict__[name]

    def __repr__(self):
        return getLabel(self._impl) if self._impl else ""


    def _new_property_changed_listener_added(self, propname):
        pass

    _properties = {}

class SingleProxyBase(Base):

    def __init__(self):
        Base.__init__(self)
        self.__dict__['_alias'] = ["$(Trader)"]

class Single_Impl(SingleProxyBase, Single_Base):

    def bind(self, ctx):
        self._bind(ctx.trader)
