from marketsim.gen._out._ilink import ILink
from marketsim.gen._out._itwowaylink import ITwoWayLink
from marketsim import meta
#(.ILink,.ILink) => .ITwoWayLink
class IFunctionITwoWayLinkILinkILink(object):
    _types = [meta.function((ILink,ILink,),ITwoWayLink)]
    
    pass



