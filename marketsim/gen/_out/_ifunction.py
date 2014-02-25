from marketsim import meta
IFunction = {}
class IFunctionobject(object):
    _types = [meta.function((),object)]
    pass


IFunction[object] = IFunctionobject


from marketsim.types import Function_impl
class IFunctionint(Function_impl):
    _types = [meta.function((),int)]
    pass


IFunction[int] = IFunctionint


from marketsim.gen._out._side import Side
class IFunctionSide(object):
    _types = [meta.function((),Side)]
    pass


IFunction[Side] = IFunctionSide


from marketsim.types import Function_impl
class IFunctionfloat(Function_impl):
    _types = [meta.function((),float)]
    @property
    def Negate(self):
        from marketsim.gen._out.ops._negate import Negate
        return Negate(self)
    
    def OnEveryDt(self, dt = None):
        from marketsim.gen._out.observable._oneverydt import OnEveryDt
        return OnEveryDt(self,dt)
    
    def Min(self, y = None):
        from marketsim.gen._out.math._min import Min
        return Min(self,y)
    
    def Add(self, y = None):
        from marketsim.gen._out.ops._add import Add
        return Add(self,y)
    
    @property
    def Atan(self):
        from marketsim.gen._out.math._atan import Atan
        return Atan(self)
    
    def Less(self, y = None):
        from marketsim.gen._out.ops._less import Less
        return Less(self,y)
    
    def Mul(self, y = None):
        from marketsim.gen._out.ops._mul import Mul
        return Mul(self,y)
    
    def NotEqual(self, y = None):
        from marketsim.gen._out.ops._notequal import NotEqual
        return NotEqual(self,y)
    
    def Max(self, y = None):
        from marketsim.gen._out.math._max import Max
        return Max(self,y)
    
    @property
    def Sqr(self):
        from marketsim.gen._out.math._sqr import Sqr
        return Sqr(self)
    
    @property
    def Sqrt(self):
        from marketsim.gen._out.math._sqrt import Sqrt
        return Sqrt(self)
    
    def GreaterEqual(self, y = None):
        from marketsim.gen._out.ops._greaterequal import GreaterEqual
        return GreaterEqual(self,y)
    
    @property
    def Exp(self):
        from marketsim.gen._out.math._exp import Exp
        return Exp(self)
    
    @property
    def Log(self):
        from marketsim.gen._out.math._log import Log
        return Log(self)
    
    def Sub(self, y = None):
        from marketsim.gen._out.ops._sub import Sub
        return Sub(self,y)
    
    def Pow(self, power = None):
        from marketsim.gen._out.math._pow import Pow
        return Pow(self,power)
    
    def IfDefined(self, elsePart = None):
        from marketsim.gen._out._ifdefined import IfDefined
        return IfDefined(self,elsePart)
    
    def Div(self, y = None):
        from marketsim.gen._out.ops._div import Div
        return Div(self,y)
    
    def LessEqual(self, y = None):
        from marketsim.gen._out.ops._lessequal import LessEqual
        return LessEqual(self,y)
    
    def Equal(self, y = None):
        from marketsim.gen._out.ops._equal import Equal
        return Equal(self,y)
    
    def Greater(self, y = None):
        from marketsim.gen._out.ops._greater import Greater
        return Greater(self,y)
    
    pass


IFunction[float] = IFunctionfloat


class IFunctionstr(object):
    _types = [meta.function((),str)]
    pass


IFunction[str] = IFunctionstr


from marketsim.gen._out._iorder import IOrder
class IFunctionIOrder(object):
    _types = [meta.function((),IOrder)]
    pass


IFunction[IOrder] = IFunctionIOrder


class IFunctionbool(object):
    _types = [meta.function((),bool)]
    def Condition(self, ifpart = None,elsepart = None):
        from marketsim.gen._out.ops._condition import Condition
        return Condition(self,ifpart,elsepart)
    
    pass


IFunction[bool] = IFunctionbool


from marketsim.gen._out._iorderbook import IOrderBook
class IFunctionIOrderBook(object):
    _types = [meta.function((),IOrderBook)]
    pass


IFunction[IOrderBook] = IFunctionIOrderBook


from marketsim import listOf
class IFunctionlistOffloat(object):
    _types = [meta.function((),listOf(float))]
    pass


IFunction[listOf(float)] = IFunctionlistOffloat


class IFunctionIFunctionint(object):
    _types = [meta.function((),IFunctionint)]
    pass


IFunction[IFunctionint] = IFunctionIFunctionint


class IFunctionIFunctionSide(object):
    _types = [meta.function((),IFunctionSide)]
    pass


IFunction[IFunctionSide] = IFunctionIFunctionSide


from marketsim.gen._out._icandlestick import ICandleStick
class IFunctionICandleStick(object):
    _types = [meta.function((),ICandleStick)]
    pass


IFunction[ICandleStick] = IFunctionICandleStick


from marketsim.gen._out._ivolumelevels import IVolumeLevels
class IFunctionIVolumeLevels(object):
    _types = [meta.function((),IVolumeLevels)]
    pass


IFunction[IVolumeLevels] = IFunctionIVolumeLevels


class IFunctionIFunctionfloat(object):
    _types = [meta.function((),IFunctionfloat)]
    pass


IFunction[IFunctionfloat] = IFunctionIFunctionfloat


from marketsim.gen._out._test.types._t import T
class IFunctionT(object):
    _types = [meta.function((),T)]
    pass


IFunction[T] = IFunctionT


from marketsim.gen._out._test.types._u import U
class IFunctionU(object):
    _types = [meta.function((),U)]
    pass


IFunction[U] = IFunctionU


from marketsim.gen._out._test.types._r import R
class IFunctionR(object):
    _types = [meta.function((),R)]
    pass


IFunction[R] = IFunctionR


class IFunctionIFunctionbool(object):
    _types = [meta.function((),IFunctionbool)]
    pass


IFunction[IFunctionbool] = IFunctionIFunctionbool


class IFunctionstr(object):
    _types = [meta.function((),str)]
    pass


IFunction[str] = IFunctionstr


from marketsim.gen._out._iobservable import IObservableint
class IFunctionIObservableint(object):
    _types = [meta.function((),IObservableint)]
    pass


IFunction[IObservableint] = IFunctionIObservableint


from marketsim.gen._out._side import Side
from marketsim.gen._out._iobservable import IObservableSide
class IFunctionIObservableSide(object):
    _types = [meta.function((),IObservableSide)]
    pass


IFunction[IObservableSide] = IFunctionIObservableSide


from marketsim.gen._out._isingleassettrader import ISingleAssetTrader
class IFunctionISingleAssetTrader(object):
    _types = [meta.function((),ISingleAssetTrader)]
    pass


IFunction[ISingleAssetTrader] = IFunctionISingleAssetTrader


from marketsim.gen._out._imultiassetstrategy import IMultiAssetStrategy
class IFunctionIMultiAssetStrategy(object):
    _types = [meta.function((),IMultiAssetStrategy)]
    pass


IFunction[IMultiAssetStrategy] = IFunctionIMultiAssetStrategy


from marketsim.gen._out._iaccount import IAccount
class IFunctionIFunctionfloatIAccount(object):
    _types = [meta.function((IAccount,),IFunctionfloat)]
    pass


IFunction[IFunctionfloat,(IAccount,)] = IFunctionIFunctionfloatIAccount


from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
class IFunctionISingleAssetStrategy(object):
    _types = [meta.function((),ISingleAssetStrategy)]
    pass


IFunction[ISingleAssetStrategy] = IFunctionISingleAssetStrategy


class IFunctionstrstr(object):
    _types = [meta.function((str,),str)]
    pass


IFunction[str,(str,)] = IFunctionstrstr


class IFunctionIFunctionintIFunctionint(object):
    _types = [meta.function((IFunctionint,),IFunctionint)]
    pass


IFunction[IFunctionint,(IFunctionint,)] = IFunctionIFunctionintIFunctionint


from marketsim.gen._out._igraph import IGraph
class IFunctionIGraphstr(object):
    _types = [meta.function((str,),IGraph)]
    pass


IFunction[IGraph,(str,)] = IFunctionIGraphstr


from marketsim.gen._out._iobservable import IObservablebool
class IFunctionIObservablebool(object):
    _types = [meta.function((),IObservablebool)]
    pass


IFunction[IObservablebool] = IFunctionIObservablebool


class IFunctionIFunctionintint(object):
    _types = [meta.function((int,),IFunctionint)]
    pass


IFunction[IFunctionint,(int,)] = IFunctionIFunctionintint


class IFunctionIFunctionfloatIFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,),IFunctionfloat)]
    pass


IFunction[IFunctionfloat,(IFunctionfloat,)] = IFunctionIFunctionfloatIFunctionfloat


from marketsim.gen._out._ievent import IEvent
class IFunctionIEventIFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,),IEvent)]
    pass


IFunction[IEvent,(IFunctionfloat,)] = IFunctionIEventIFunctionfloat


from marketsim.gen._out._iaccount import IAccount
from marketsim.gen._out._iorderbook import IOrderBook
class IFunctionIOrderBookIAccount(object):
    _types = [meta.function((IAccount,),IOrderBook)]
    pass


IFunction[IOrderBook,(IAccount,)] = IFunctionIOrderBookIAccount


class IFunctionIFunctionfloatfloat(object):
    _types = [meta.function((float,),IFunctionfloat)]
    pass


IFunction[IFunctionfloat,(float,)] = IFunctionIFunctionfloatfloat


class IFunctionIFunctionIFunctionfloatIAccount(object):
    _types = [meta.function((),IFunctionIFunctionfloatIAccount)]
    pass


IFunction[IFunctionIFunctionfloatIAccount] = IFunctionIFunctionIFunctionfloatIAccount


from marketsim.gen._out._iobservable import IObservableint
class IFunctionIObservableintint(object):
    _types = [meta.function((int,),IObservableint)]
    pass


IFunction[IObservableint,(int,)] = IFunctionIObservableintint


from marketsim.gen._out._iorderbook import IOrderBook
from marketsim.gen._out._iorderqueue import IOrderQueue
class IFunctionIOrderQueueIOrderBook(object):
    _types = [meta.function((IOrderBook,),IOrderQueue)]
    pass


IFunction[IOrderQueue,(IOrderBook,)] = IFunctionIOrderQueueIOrderBook


from marketsim.gen._out._iorder import IOrder
from marketsim.gen._out._iobservable import IObservableIOrder
class IFunctionIObservableIOrderIFunctionSide(object):
    _types = [meta.function((IFunctionSide,),IObservableIOrder)]
    pass


IFunction[IObservableIOrder,(IFunctionSide,)] = IFunctionIObservableIOrderIFunctionSide


class IFunctionIFunctionSideIFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,),IFunctionSide)]
    pass


IFunction[IFunctionSide,(IFunctionfloat,)] = IFunctionIFunctionSideIFunctionfloat


from marketsim.gen._out._iorder import IOrder
from marketsim.gen._out._iobservable import IObservableIOrder
class IFunctionIObservableIOrderIFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,),IObservableIOrder)]
    pass


IFunction[IObservableIOrder,(IFunctionfloat,)] = IFunctionIObservableIOrderIFunctionfloat


from marketsim.gen._out._iorderbook import IOrderBook
class IFunctionIFunctionfloatIOrderBook(object):
    _types = [meta.function((IOrderBook,),IFunctionfloat)]
    pass


IFunction[IFunctionfloat,(IOrderBook,)] = IFunctionIFunctionfloatIOrderBook


from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIObservablefloatfloat(object):
    _types = [meta.function((float,),IObservablefloat)]
    pass


IFunction[IObservablefloat,(float,)] = IFunctionIObservablefloatfloat


from marketsim.gen._out._iobservable import IObservablefloat
from marketsim.gen._out._ilink import ILink
class IFunctionILinkIObservablefloat(object):
    _types = [meta.function((IObservablefloat,),ILink)]
    pass


IFunction[ILink,(IObservablefloat,)] = IFunctionILinkIObservablefloat


class IFunctionIFunctionfloatIFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,),IFunctionfloat)]
    pass


IFunction[IFunctionfloat,(IFunctionfloat,)] = IFunctionIFunctionfloatIFunctionfloat


from marketsim.gen._out._iaccount import IAccount
from marketsim.gen._out._iobservable import IObservableint
class IFunctionIObservableintIAccount(object):
    _types = [meta.function((IAccount,),IObservableint)]
    pass


IFunction[IObservableint,(IAccount,)] = IFunctionIObservableintIAccount


from marketsim.gen._out._iaccount import IAccount
from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIObservablefloatIAccount(object):
    _types = [meta.function((IAccount,),IObservablefloat)]
    pass


IFunction[IObservablefloat,(IAccount,)] = IFunctionIObservablefloatIAccount


from marketsim.gen._out._iorderbook import IOrderBook
from marketsim.gen._out._iobservable import IObservableint
class IFunctionIObservableintIOrderBook(object):
    _types = [meta.function((IOrderBook,),IObservableint)]
    pass


IFunction[IObservableint,(IOrderBook,)] = IFunctionIObservableintIOrderBook


from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim.gen._out._iaccount import IAccount
class IFunctionIAccountISingleAssetStrategy(object):
    _types = [meta.function((ISingleAssetStrategy,),IAccount)]
    pass


IFunction[IAccount,(ISingleAssetStrategy,)] = IFunctionIAccountISingleAssetStrategy


from marketsim.gen._out._iorderqueue import IOrderQueue
from marketsim.gen._out._iobservable import IObservableint
class IFunctionIObservableintIOrderQueue(object):
    _types = [meta.function((IOrderQueue,),IObservableint)]
    pass


IFunction[IObservableint,(IOrderQueue,)] = IFunctionIObservableintIOrderQueue


from marketsim.gen._out._idifferentiable import IDifferentiable
class IFunctionIFunctionfloatIDifferentiable(object):
    _types = [meta.function((IDifferentiable,),IFunctionfloat)]
    pass


IFunction[IFunctionfloat,(IDifferentiable,)] = IFunctionIFunctionfloatIDifferentiable


from marketsim.gen._out._iorderbook import IOrderBook
from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIObservablefloatIOrderBook(object):
    _types = [meta.function((IOrderBook,),IObservablefloat)]
    pass


IFunction[IObservablefloat,(IOrderBook,)] = IFunctionIObservablefloatIOrderBook


from marketsim.gen._out._iorder import IOrder
from marketsim.gen._out._iobservable import IObservableIOrder
class IFunctionIObservableIOrderIFunctionSide(object):
    _types = [meta.function((IFunctionSide,),IObservableIOrder)]
    pass


IFunction[IObservableIOrder,(IFunctionSide,)] = IFunctionIObservableIOrderIFunctionSide


from marketsim.gen._out._iaccount import IAccount
class IFunctionIFunctionfloatIAccountfloat(object):
    _types = [meta.function((IAccount,float,),IFunctionfloat)]
    pass


IFunction[IFunctionfloat,(IAccount,float,)] = IFunctionIFunctionfloatIAccountfloat


from marketsim.gen._out._iorderqueue import IOrderQueue
from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIObservablefloatIOrderQueue(object):
    _types = [meta.function((IOrderQueue,),IObservablefloat)]
    pass


IFunction[IObservablefloat,(IOrderQueue,)] = IFunctionIObservablefloatIOrderQueue


from marketsim import listOf
class IFunctionIFunctionlistOffloatlistOffloat(object):
    _types = [meta.function((listOf(float),),IFunctionlistOffloat)]
    pass


IFunction[IFunctionlistOffloat,(listOf(float),)] = IFunctionIFunctionlistOffloatlistOffloat


class IFunctionintIFunctionICandleStickint(object):
    _types = [meta.function((IFunctionICandleStick,int,),int)]
    pass


IFunction[int,(IFunctionICandleStick,int,)] = IFunctionintIFunctionICandleStickint


class IFunctionIFunctionIObservableIOrderIFunctionfloat(object):
    _types = [meta.function((),IFunctionIObservableIOrderIFunctionfloat)]
    pass


IFunction[IFunctionIObservableIOrderIFunctionfloat] = IFunctionIFunctionIObservableIOrderIFunctionfloat


from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
class IFunctionISingleAssetStrategyIFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,),ISingleAssetStrategy)]
    pass


IFunction[ISingleAssetStrategy,(IFunctionfloat,)] = IFunctionISingleAssetStrategyIFunctionfloat


from marketsim.gen._out._iorder import IOrder
from marketsim.gen._out._iobservable import IObservableIOrder
class IFunctionIObservableIOrderIFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,),IObservableIOrder)]
    pass


IFunction[IObservableIOrder,(IFunctionfloat,)] = IFunctionIObservableIOrderIFunctionfloat


class IFunctionIFunctionIFunctionfloatIFunctionfloat(object):
    _types = [meta.function((),IFunctionIFunctionfloatIFunctionfloat)]
    pass


IFunction[IFunctionIFunctionfloatIFunctionfloat] = IFunctionIFunctionIFunctionfloatIFunctionfloat


class IFunctionIFunctionUIFunctionT(object):
    _types = [meta.function((IFunctionT,),IFunctionU)]
    pass


IFunction[IFunctionU,(IFunctionT,)] = IFunctionIFunctionUIFunctionT


from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIFunctionfloatIObservablefloat(object):
    _types = [meta.function((IObservablefloat,),IFunctionfloat)]
    pass


IFunction[IFunctionfloat,(IObservablefloat,)] = IFunctionIFunctionfloatIObservablefloat


class IFunctionIFunctionIFunctionfloatIAccountfloat(object):
    _types = [meta.function((float,),IFunctionIFunctionfloatIAccount)]
    pass


IFunction[IFunctionIFunctionfloatIAccount,(float,)] = IFunctionIFunctionIFunctionfloatIAccountfloat


from marketsim.gen._out._iobservable import IObservablefloat
from marketsim.gen._out._idifferentiable import IDifferentiable
class IFunctionIDifferentiableIObservablefloat(object):
    _types = [meta.function((IObservablefloat,),IDifferentiable)]
    pass


IFunction[IDifferentiable,(IObservablefloat,)] = IFunctionIDifferentiableIObservablefloat


from marketsim.gen._out._ilink import ILink
from marketsim.gen._out._itwowaylink import ITwoWayLink
class IFunctionITwoWayLinkILinkILink(object):
    _types = [meta.function((ILink,ILink,),ITwoWayLink)]
    pass


IFunction[ITwoWayLink,(ILink,ILink,)] = IFunctionITwoWayLinkILinkILink


class IFunctionIFunctionIAccountISingleAssetStrategy(object):
    _types = [meta.function((),IFunctionIAccountISingleAssetStrategy)]
    pass


IFunction[IFunctionIAccountISingleAssetStrategy] = IFunctionIFunctionIAccountISingleAssetStrategy


class IFunctionIFunctionfloatfloatfloat(object):
    _types = [meta.function((float,float,),IFunctionfloat)]
    pass


IFunction[IFunctionfloat,(float,float,)] = IFunctionIFunctionfloatfloatfloat


from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIObservablefloatIObservablefloat(object):
    _types = [meta.function((IObservablefloat,),IObservablefloat)]
    pass


IFunction[IObservablefloat,(IObservablefloat,)] = IFunctionIObservablefloatIObservablefloat


class IFunctionIFunctionIFunctionlistOffloatlistOffloat(object):
    _types = [meta.function((),IFunctionIFunctionlistOffloatlistOffloat)]
    pass


IFunction[IFunctionIFunctionlistOffloatlistOffloat] = IFunctionIFunctionIFunctionlistOffloatlistOffloat


from marketsim.gen._out._iobservable import IObservableIOrder
from marketsim.gen._out._iorder import IOrder
class IFunctionIObservableIOrderIFunctionSideIFunctionfloat(object):
    _types = [meta.function((IFunctionSide,IFunctionfloat,),IObservableIOrder)]
    pass


IFunction[IObservableIOrder,(IFunctionSide,IFunctionfloat,)] = IFunctionIObservableIOrderIFunctionSideIFunctionfloat


from marketsim.gen._out._iaccount import IAccount
class IFunctionIFunctionfloatIAccountfloat(object):
    _types = [meta.function((IAccount,float,),IFunctionfloat)]
    pass


IFunction[IFunctionfloat,(IAccount,float,)] = IFunctionIFunctionfloatIAccountfloat


class IFunctionIFunctionRIFunctionT(object):
    _types = [meta.function((IFunctionT,),IFunctionR)]
    pass


IFunction[IFunctionR,(IFunctionT,)] = IFunctionIFunctionRIFunctionT


from marketsim.gen._out._iorder import IOrder
from marketsim.gen._out._iobservable import IObservableIOrder
class IFunctionIObservableIOrderIObservableIOrder(object):
    _types = [meta.function((IObservableIOrder,),IObservableIOrder)]
    pass


IFunction[IObservableIOrder,(IObservableIOrder,)] = IFunctionIObservableIOrderIObservableIOrder


class IFunctionIFunctionSideIFunctionfloatfloat(object):
    _types = [meta.function((IFunctionfloat,float,),IFunctionSide)]
    pass


IFunction[IFunctionSide,(IFunctionfloat,float,)] = IFunctionIFunctionSideIFunctionfloatfloat


from marketsim.gen._out._iorderbook import IOrderBook
class IFunctionIFunctionfloatIOrderBookfloat(object):
    _types = [meta.function((IOrderBook,float,),IFunctionfloat)]
    pass


IFunction[IFunctionfloat,(IOrderBook,float,)] = IFunctionIFunctionfloatIOrderBookfloat


class IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide(object):
    _types = [meta.function((IFunctionSide,),IFunctionIObservableIOrderIFunctionfloat)]
    pass


IFunction[IFunctionIObservableIOrderIFunctionfloat,(IFunctionSide,)] = IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide


from marketsim.gen._out._iorderqueue import IOrderQueue
class IFunctionIFunctionfloatIOrderQueuefloat(object):
    _types = [meta.function((IOrderQueue,float,),IFunctionfloat)]
    pass


IFunction[IFunctionfloat,(IOrderQueue,float,)] = IFunctionIFunctionfloatIOrderQueuefloat


class IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,),IFunctionIObservableIOrderIFunctionfloat)]
    pass


IFunction[IFunctionIObservableIOrderIFunctionfloat,(IFunctionfloat,)] = IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat


class IFunctionIFunctionfloatIFunctionfloatfloat(object):
    _types = [meta.function((IFunctionfloat,float,),IFunctionfloat)]
    pass


IFunction[IFunctionfloat,(IFunctionfloat,float,)] = IFunctionIFunctionfloatIFunctionfloatfloat


from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
class IFunctionISingleAssetStrategyfloatfloat(object):
    _types = [meta.function((float,float,),ISingleAssetStrategy)]
    pass


IFunction[ISingleAssetStrategy,(float,float,)] = IFunctionISingleAssetStrategyfloatfloat


from marketsim.gen._out._iorderbook import IOrderBook
from marketsim.gen._out._iorderqueue import IOrderQueue
class IFunctionIOrderQueueIOrderBookIFunctionSide(object):
    _types = [meta.function((IOrderBook,IFunctionSide,),IOrderQueue)]
    pass


IFunction[IOrderQueue,(IOrderBook,IFunctionSide,)] = IFunctionIOrderQueueIOrderBookIFunctionSide


from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim import listOf
class IFunctionISingleAssetStrategylistOfISingleAssetStrategy(object):
    _types = [meta.function((listOf(ISingleAssetStrategy),),ISingleAssetStrategy)]
    pass


IFunction[ISingleAssetStrategy,(listOf(ISingleAssetStrategy),)] = IFunctionISingleAssetStrategylistOfISingleAssetStrategy


class IFunctionIFunctionIFunctionfloatIFunctionfloatfloat(object):
    _types = [meta.function((float,),IFunctionIFunctionfloatIFunctionfloat)]
    pass


IFunction[IFunctionIFunctionfloatIFunctionfloat,(float,)] = IFunctionIFunctionIFunctionfloatIFunctionfloatfloat


class IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionfloat(object):
    _types = [meta.function((),IFunctionIObservableIOrderIFunctionSideIFunctionfloat)]
    pass


IFunction[IFunctionIObservableIOrderIFunctionSideIFunctionfloat] = IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionfloat


from marketsim.gen._out._iorderbook import IOrderBook
from marketsim.gen._out._side import Side
from marketsim.gen._out._iobservable import IObservableSide
class IFunctionIObservableSidefloatIOrderBook(object):
    _types = [meta.function((float,IOrderBook,),IObservableSide)]
    pass


IFunction[IObservableSide,(float,IOrderBook,)] = IFunctionIObservableSidefloatIOrderBook


from marketsim.gen._out._iorder import IOrder
from marketsim.gen._out._iobservable import IObservableIOrder
class IFunctionIObservableIOrderIFunctionfloatIFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,IFunctionfloat,),IObservableIOrder)]
    pass


IFunction[IObservableIOrder,(IFunctionfloat,IFunctionfloat,)] = IFunctionIObservableIOrderIFunctionfloatIFunctionfloat


from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIObservablefloatIFunctionfloatfloat(object):
    _types = [meta.function((IFunctionfloat,float,),IObservablefloat)]
    pass


IFunction[IObservablefloat,(IFunctionfloat,float,)] = IFunctionIObservablefloatIFunctionfloatfloat


class IFunctionIFunctionfloatIFunctionfloatIFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,IFunctionfloat,),IFunctionfloat)]
    pass


IFunction[IFunctionfloat,(IFunctionfloat,IFunctionfloat,)] = IFunctionIFunctionfloatIFunctionfloatIFunctionfloat


class IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,),IFunctionIObservableIOrderIFunctionSide)]
    pass


IFunction[IFunctionIObservableIOrderIFunctionSide,(IFunctionfloat,)] = IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionfloat


class IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide(object):
    _types = [meta.function((IFunctionSide,),IFunctionIObservableIOrderIFunctionfloat)]
    pass


IFunction[IFunctionIObservableIOrderIFunctionfloat,(IFunctionSide,)] = IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide


class IFunctionIFunctionboolIFunctionfloatIFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,IFunctionfloat,),IFunctionbool)]
    pass


IFunction[IFunctionbool,(IFunctionfloat,IFunctionfloat,)] = IFunctionIFunctionboolIFunctionfloatIFunctionfloat


class IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,),IFunctionIObservableIOrderIFunctionfloat)]
    pass


IFunction[IFunctionIObservableIOrderIFunctionfloat,(IFunctionfloat,)] = IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat


from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIFunctionfloatIObservablefloatfloat(object):
    _types = [meta.function((IObservablefloat,float,),IFunctionfloat)]
    pass


IFunction[IFunctionfloat,(IObservablefloat,float,)] = IFunctionIFunctionfloatIObservablefloatfloat


from marketsim.gen._out._iobservable import IObservablefloat
from marketsim.gen._out._idifferentiable import IDifferentiable
class IFunctionIDifferentiableIObservablefloatfloat(object):
    _types = [meta.function((IObservablefloat,float,),IDifferentiable)]
    pass


IFunction[IDifferentiable,(IObservablefloat,float,)] = IFunctionIDifferentiableIObservablefloatfloat


from marketsim.gen._out._iorderbook import IOrderBook
from marketsim.gen._out._iobservable import IObservableSide
from marketsim.gen._out._side import Side
class IFunctionIObservableSideIFunctionfloatIOrderBook(object):
    _types = [meta.function((IFunctionfloat,IOrderBook,),IObservableSide)]
    pass


IFunction[IObservableSide,(IFunctionfloat,IOrderBook,)] = IFunctionIObservableSideIFunctionfloatIOrderBook


class IFunctionIFunctionfloatfloatfloatfloat(object):
    _types = [meta.function((float,float,float,),IFunctionfloat)]
    pass


IFunction[IFunctionfloat,(float,float,float,)] = IFunctionIFunctionfloatfloatfloatfloat


from marketsim.gen._out._iorderbook import IOrderBook
from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIObservablefloatIOrderBookIFunctionfloat(object):
    _types = [meta.function((IOrderBook,IFunctionfloat,),IObservablefloat)]
    pass


IFunction[IObservablefloat,(IOrderBook,IFunctionfloat,)] = IFunctionIObservablefloatIOrderBookIFunctionfloat


from marketsim.gen._out._iobservable import IObservableIOrder
from marketsim.gen._out._iorder import IOrder
class IFunctionIObservableIOrderIFunctionSideIFunctionfloat(object):
    _types = [meta.function((IFunctionSide,IFunctionfloat,),IObservableIOrder)]
    pass


IFunction[IObservableIOrder,(IFunctionSide,IFunctionfloat,)] = IFunctionIObservableIOrderIFunctionSideIFunctionfloat


class IFunctionIFunctionTIFunctionintIFunctionfloat(object):
    _types = [meta.function((IFunctionint,IFunctionfloat,),IFunctionT)]
    pass


IFunction[IFunctionT,(IFunctionint,IFunctionfloat,)] = IFunctionIFunctionTIFunctionintIFunctionfloat


from marketsim.gen._out._iorderqueue import IOrderQueue
from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIObservablefloatIOrderQueueIFunctionfloat(object):
    _types = [meta.function((IOrderQueue,IFunctionfloat,),IObservablefloat)]
    pass


IFunction[IObservablefloat,(IOrderQueue,IFunctionfloat,)] = IFunctionIObservablefloatIOrderQueueIFunctionfloat


from marketsim.gen._out._iobservable import IObservablefloat
from marketsim.gen._out._side import Side
from marketsim.gen._out._iobservable import IObservableSide
class IFunctionIObservableSideIObservablefloatfloat(object):
    _types = [meta.function((IObservablefloat,float,),IObservableSide)]
    pass


IFunction[IObservableSide,(IObservablefloat,float,)] = IFunctionIObservableSideIObservablefloatfloat


from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIObservablefloatIObservablefloatfloat(object):
    _types = [meta.function((IObservablefloat,float,),IObservablefloat)]
    pass


IFunction[IObservablefloat,(IObservablefloat,float,)] = IFunctionIObservablefloatIObservablefloatfloat


from marketsim.gen._out._iorderbook import IOrderBook
class IFunctionIFunctionSidefloatfloatIOrderBook(object):
    _types = [meta.function((float,float,IOrderBook,),IFunctionSide)]
    pass


IFunction[IFunctionSide,(float,float,IOrderBook,)] = IFunctionIFunctionSidefloatfloatIOrderBook


class IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide(object):
    _types = [meta.function((IFunctionSide,),IFunctionIObservableIOrderIFunctionfloat)]
    pass


IFunction[IFunctionIObservableIOrderIFunctionfloat,(IFunctionSide,)] = IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide


from marketsim.gen._out._iorder import IOrder
from marketsim.gen._out._iobservable import IObservableIOrder
class IFunctionIObservableIOrderIFunctionIObservableIOrderIFunctionfloat(object):
    _types = [meta.function((IFunctionIObservableIOrderIFunctionfloat,),IObservableIOrder)]
    pass


IFunction[IObservableIOrder,(IFunctionIObservableIOrderIFunctionfloat,)] = IFunctionIObservableIOrderIFunctionIObservableIOrderIFunctionfloat


class IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat(object):
    _types = [meta.function((IFunctionSide,IFunctionfloat,),IFunctionIObservableIOrderIFunctionfloat)]
    pass


IFunction[IFunctionIObservableIOrderIFunctionfloat,(IFunctionSide,IFunctionfloat,)] = IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat


class IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,),IFunctionIObservableIOrderIFunctionfloat)]
    pass


IFunction[IFunctionIObservableIOrderIFunctionfloat,(IFunctionfloat,)] = IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat


from marketsim.gen._out._iorderbook import IOrderBook
class IFunctionIFunctionfloatIOrderBookfloatfloat(object):
    _types = [meta.function((IOrderBook,float,float,),IFunctionfloat)]
    pass


IFunction[IFunctionfloat,(IOrderBook,float,float,)] = IFunctionIFunctionfloatIOrderBookfloatfloat


from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim.gen._out._iobservable import IObservableIOrder
from marketsim.gen._out._iorder import IOrder
class IFunctionISingleAssetStrategyIObservableIOrderIEvent(object):
    _types = [meta.function((IObservableIOrder,IEvent,),ISingleAssetStrategy)]
    pass


IFunction[ISingleAssetStrategy,(IObservableIOrder,IEvent,)] = IFunctionISingleAssetStrategyIObservableIOrderIEvent


from marketsim.gen._out._iobservable import IObservablefloat
from marketsim.gen._out._iorderbook import IOrderBook
from marketsim.gen._out._iobservable import IObservableSide
from marketsim.gen._out._side import Side
class IFunctionIObservableSideIObservablefloatIOrderBook(object):
    _types = [meta.function((IObservablefloat,IOrderBook,),IObservableSide)]
    pass


IFunction[IObservableSide,(IObservablefloat,IOrderBook,)] = IFunctionIObservableSideIObservablefloatIOrderBook


from marketsim.gen._out._iorderbook import IOrderBook
from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIObservablefloatIOrderBookIObservablefloat(object):
    _types = [meta.function((IOrderBook,IObservablefloat,),IObservablefloat)]
    pass


IFunction[IObservablefloat,(IOrderBook,IObservablefloat,)] = IFunctionIObservablefloatIOrderBookIObservablefloat


from marketsim.gen._out._iorderqueue import IOrderQueue
from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIObservablefloatIOrderQueueIObservablefloat(object):
    _types = [meta.function((IOrderQueue,IObservablefloat,),IObservablefloat)]
    pass


IFunction[IObservablefloat,(IOrderQueue,IObservablefloat,)] = IFunctionIObservablefloatIOrderQueueIObservablefloat


from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIObservablefloatIFunctionfloatIObservablefloat(object):
    _types = [meta.function((IFunctionfloat,IObservablefloat,),IObservablefloat)]
    pass


IFunction[IObservablefloat,(IFunctionfloat,IObservablefloat,)] = IFunctionIObservablefloatIFunctionfloatIObservablefloat


from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIObservablefloatstrstrstr(object):
    _types = [meta.function((str,str,str,),IObservablefloat)]
    pass


IFunction[IObservablefloat,(str,str,str,)] = IFunctionIObservablefloatstrstrstr


from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIObservablefloatIObservablefloatIFunctionfloat(object):
    _types = [meta.function((IObservablefloat,IFunctionfloat,),IObservablefloat)]
    pass


IFunction[IObservablefloat,(IObservablefloat,IFunctionfloat,)] = IFunctionIObservablefloatIObservablefloatIFunctionfloat


from marketsim.gen._out._iobservable import IObservablefloat
from marketsim.gen._out._icandlestick import ICandleStick
from marketsim.gen._out._iobservable import IObservableICandleStick
class IFunctionIObservableICandleStickIObservablefloatfloat(object):
    _types = [meta.function((IObservablefloat,float,),IObservableICandleStick)]
    pass


IFunction[IObservableICandleStick,(IObservablefloat,float,)] = IFunctionIObservableICandleStickIObservablefloatfloat


from marketsim.gen._out._iobservable import IObservablefloat
from marketsim.gen._out._iobservable import IObservablebool
class IFunctionIObservableboolIFunctionfloatIObservablefloat(object):
    _types = [meta.function((IFunctionfloat,IObservablefloat,),IObservablebool)]
    pass


IFunction[IObservablebool,(IFunctionfloat,IObservablefloat,)] = IFunctionIObservableboolIFunctionfloatIObservablefloat


from marketsim.gen._out._iobservable import IObservablefloat
from marketsim.gen._out._iobservable import IObservablebool
class IFunctionIObservableboolIObservablefloatIFunctionfloat(object):
    _types = [meta.function((IObservablefloat,IFunctionfloat,),IObservablebool)]
    pass


IFunction[IObservablebool,(IObservablefloat,IFunctionfloat,)] = IFunctionIObservableboolIObservablefloatIFunctionfloat


from marketsim.gen._out._iorder import IOrder
from marketsim.gen._out._iobservable import IObservableIOrder
class IFunctionIObservableIOrderIObservableIOrderIFunctionfloat(object):
    _types = [meta.function((IObservableIOrder,IFunctionfloat,),IObservableIOrder)]
    pass


IFunction[IObservableIOrder,(IObservableIOrder,IFunctionfloat,)] = IFunctionIObservableIOrderIObservableIOrderIFunctionfloat


from marketsim.gen._out._iorder import IOrder
from marketsim.gen._out._iobservable import IObservableIOrder
class IFunctionIObservableIOrderIFunctionfloatIObservableIOrder(object):
    _types = [meta.function((IFunctionfloat,IObservableIOrder,),IObservableIOrder)]
    pass


IFunction[IObservableIOrder,(IFunctionfloat,IObservableIOrder,)] = IFunctionIObservableIOrderIFunctionfloatIObservableIOrder


from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
class IFunctionISingleAssetStrategyISingleAssetStrategyIFunctionbool(object):
    _types = [meta.function((ISingleAssetStrategy,IFunctionbool,),ISingleAssetStrategy)]
    pass


IFunction[ISingleAssetStrategy,(ISingleAssetStrategy,IFunctionbool,)] = IFunctionISingleAssetStrategyISingleAssetStrategyIFunctionbool


class IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat(object):
    _types = [meta.function((),IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat)]
    pass


IFunction[IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat] = IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat


class IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionfloatIFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,),IFunctionIObservableIOrderIFunctionSideIFunctionfloat)]
    pass


IFunction[IFunctionIObservableIOrderIFunctionSideIFunctionfloat,(IFunctionfloat,)] = IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionfloatIFunctionfloat


from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIFunctionfloatIObservablefloatfloatfloat(object):
    _types = [meta.function((IObservablefloat,float,float,),IFunctionfloat)]
    pass


IFunction[IFunctionfloat,(IObservablefloat,float,float,)] = IFunctionIFunctionfloatIObservablefloatfloatfloat


from marketsim.gen._out._iorderbook import IOrderBook
from marketsim.gen._out._side import Side
from marketsim.gen._out._iobservable import IObservableSide
class IFunctionIObservableSideIOrderBookfloatIOrderBook(object):
    _types = [meta.function((IOrderBook,float,IOrderBook,),IObservableSide)]
    pass


IFunction[IObservableSide,(IOrderBook,float,IOrderBook,)] = IFunctionIObservableSideIOrderBookfloatIOrderBook


class IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,),IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide)]
    pass


IFunction[IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide,(IFunctionfloat,)] = IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat


from marketsim.gen._out._iobservable import IObservablefloat
from marketsim.gen._out._isingleassettrader import ISingleAssetTrader
class IFunctionIObservablefloatIObservablefloatISingleAssetTrader(object):
    _types = [meta.function((IObservablefloat,ISingleAssetTrader,),IObservablefloat)]
    pass


IFunction[IObservablefloat,(IObservablefloat,ISingleAssetTrader,)] = IFunctionIObservablefloatIObservablefloatISingleAssetTrader


class IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloatIFunctionSide(object):
    _types = [meta.function((IFunctionSide,),IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat)]
    pass


IFunction[IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat,(IFunctionSide,)] = IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloatIFunctionSide


from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIObservablefloatIObservablefloatIObservablefloat(object):
    _types = [meta.function((IObservablefloat,IObservablefloat,),IObservablefloat)]
    pass


IFunction[IObservablefloat,(IObservablefloat,IObservablefloat,)] = IFunctionIObservablefloatIObservablefloatIObservablefloat


class IFunctionIFunctionSideIFunctionboolIFunctionSideIFunctionSide(object):
    _types = [meta.function((IFunctionbool,IFunctionSide,IFunctionSide,),IFunctionSide)]
    pass


IFunction[IFunctionSide,(IFunctionbool,IFunctionSide,IFunctionSide,)] = IFunctionIFunctionSideIFunctionboolIFunctionSideIFunctionSide


from marketsim.gen._out._iorderqueue import IOrderQueue
from marketsim.gen._out._ivolumelevels import IVolumeLevels
from marketsim.gen._out._iobservable import IObservableIVolumeLevels
class IFunctionIObservableIVolumeLevelsIOrderQueuefloatint(object):
    _types = [meta.function((IOrderQueue,float,int,),IObservableIVolumeLevels)]
    pass


IFunction[IObservableIVolumeLevels,(IOrderQueue,float,int,)] = IFunctionIObservableIVolumeLevelsIOrderQueuefloatint


from marketsim.gen._out._iobservable import IObservablefloat
from marketsim.gen._out._iobservable import IObservablebool
class IFunctionIObservableboolIObservablefloatIObservablefloat(object):
    _types = [meta.function((IObservablefloat,IObservablefloat,),IObservablebool)]
    pass


IFunction[IObservablebool,(IObservablefloat,IObservablefloat,)] = IFunctionIObservableboolIObservablefloatIObservablefloat


from marketsim import listOf
from marketsim.gen._out._iorderbook import IOrderBook
from marketsim.gen._out._itimeserie import ITimeSerie
from marketsim.gen._out._itwowaylink import ITwoWayLink
class IFunctionIOrderBookIOrderBookITwoWayLinklistOfITimeSerie(object):
    _types = [meta.function((IOrderBook,ITwoWayLink,listOf(ITimeSerie),),IOrderBook)]
    pass


IFunction[IOrderBook,(IOrderBook,ITwoWayLink,listOf(ITimeSerie),)] = IFunctionIOrderBookIOrderBookITwoWayLinklistOfITimeSerie


class IFunctionIFunctionfloatIFunctionboolIFunctionfloatIFunctionfloat(object):
    _types = [meta.function((IFunctionbool,IFunctionfloat,IFunctionfloat,),IFunctionfloat)]
    pass


IFunction[IFunctionfloat,(IFunctionbool,IFunctionfloat,IFunctionfloat,)] = IFunctionIFunctionfloatIFunctionboolIFunctionfloatIFunctionfloat


from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
class IFunctionISingleAssetStrategyISingleAssetStrategyISingleAssetStrategy(object):
    _types = [meta.function((ISingleAssetStrategy,ISingleAssetStrategy,),ISingleAssetStrategy)]
    pass


IFunction[ISingleAssetStrategy,(ISingleAssetStrategy,ISingleAssetStrategy,)] = IFunctionISingleAssetStrategyISingleAssetStrategyISingleAssetStrategy


class IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat(object):
    _types = [meta.function((IFunctionSide,IFunctionfloat,),IFunctionIObservableIOrderIFunctionfloat)]
    pass


IFunction[IFunctionIObservableIOrderIFunctionfloat,(IFunctionSide,IFunctionfloat,)] = IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat


from marketsim.gen._out._iorderbook import IOrderBook
class IFunctionIFunctionSidefloatfloatfloatIOrderBook(object):
    _types = [meta.function((float,float,float,IOrderBook,),IFunctionSide)]
    pass


IFunction[IFunctionSide,(float,float,float,IOrderBook,)] = IFunctionIFunctionSidefloatfloatfloatIOrderBook


class IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionfloatIFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,IFunctionfloat,),IFunctionIObservableIOrderIFunctionSide)]
    pass


IFunction[IFunctionIObservableIOrderIFunctionSide,(IFunctionfloat,IFunctionfloat,)] = IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionfloatIFunctionfloat


from marketsim.gen._out._iobservable import IObservableobject
from marketsim.gen._out._igraph import IGraph
from marketsim.gen._out._itimeserie import ITimeSerie
class IFunctionITimeSerieIObservableobjectIGraphintint(object):
    _types = [meta.function((IObservableobject,IGraph,int,int,),ITimeSerie)]
    pass


IFunction[ITimeSerie,(IObservableobject,IGraph,int,int,)] = IFunctionITimeSerieIObservableobjectIGraphintint


class IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionIObservableIOrderIFunctionSide(object):
    _types = [meta.function((IFunctionIObservableIOrderIFunctionSide,),IFunctionIObservableIOrderIFunctionSide)]
    pass


IFunction[IFunctionIObservableIOrderIFunctionSide,(IFunctionIObservableIOrderIFunctionSide,)] = IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionIObservableIOrderIFunctionSide


from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
class IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSide(object):
    _types = [meta.function((IEvent,IFunctionIObservableIOrderIFunctionSide,),ISingleAssetStrategy)]
    pass


IFunction[ISingleAssetStrategy,(IEvent,IFunctionIObservableIOrderIFunctionSide,)] = IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSide


class IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionIObservableIOrderIFunctionfloat(object):
    _types = [meta.function((IFunctionIObservableIOrderIFunctionfloat,),IFunctionIObservableIOrderIFunctionfloat)]
    pass


IFunction[IFunctionIObservableIOrderIFunctionfloat,(IFunctionIObservableIOrderIFunctionfloat,)] = IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionIObservableIOrderIFunctionfloat


from marketsim.gen._out._itimeserie import ITimeSerie
from marketsim import listOf
from marketsim.gen._out._iorderbook import IOrderBook
class IFunctionIOrderBookstrfloatintlistOfITimeSerie(object):
    _types = [meta.function((str,float,int,listOf(ITimeSerie),),IOrderBook)]
    pass


IFunction[IOrderBook,(str,float,int,listOf(ITimeSerie),)] = IFunctionIOrderBookstrfloatintlistOfITimeSerie


from marketsim.gen._out._iobservable import IObservableIOrder
from marketsim.gen._out._iorder import IOrder
class IFunctionIObservableIOrderIFunctionSideIFunctionfloatIFunctionfloat(object):
    _types = [meta.function((IFunctionSide,IFunctionfloat,IFunctionfloat,),IObservableIOrder)]
    pass


IFunction[IObservableIOrder,(IFunctionSide,IFunctionfloat,IFunctionfloat,)] = IFunctionIObservableIOrderIFunctionSideIFunctionfloatIFunctionfloat


class IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat(object):
    _types = [meta.function((IFunctionSide,IFunctionfloat,),IFunctionIObservableIOrderIFunctionfloat)]
    pass


IFunction[IFunctionIObservableIOrderIFunctionfloat,(IFunctionSide,IFunctionfloat,)] = IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat


from marketsim.gen._out._iobservable import IObservableSide
from marketsim.gen._out._side import Side
class IFunctionIObservableSideIFunctionboolIFunctionSideIObservableSide(object):
    _types = [meta.function((IFunctionbool,IFunctionSide,IObservableSide,),IObservableSide)]
    pass


IFunction[IObservableSide,(IFunctionbool,IFunctionSide,IObservableSide,)] = IFunctionIObservableSideIFunctionboolIFunctionSideIObservableSide


from marketsim.gen._out._iobservable import IObservableSide
from marketsim.gen._out._side import Side
from marketsim.gen._out._iobservable import IObservablebool
class IFunctionIObservableSideIObservableboolIFunctionSideIFunctionSide(object):
    _types = [meta.function((IObservablebool,IFunctionSide,IFunctionSide,),IObservableSide)]
    pass


IFunction[IObservableSide,(IObservablebool,IFunctionSide,IFunctionSide,)] = IFunctionIObservableSideIObservableboolIFunctionSideIFunctionSide


from marketsim.gen._out._iobservable import IObservableSide
from marketsim.gen._out._side import Side
class IFunctionIObservableSideIFunctionboolIObservableSideIFunctionSide(object):
    _types = [meta.function((IFunctionbool,IObservableSide,IFunctionSide,),IObservableSide)]
    pass


IFunction[IObservableSide,(IFunctionbool,IObservableSide,IFunctionSide,)] = IFunctionIObservableSideIFunctionboolIObservableSideIFunctionSide


from marketsim.gen._out._iobservable import IObservablefloat
from marketsim.gen._out._isingleassettrader import ISingleAssetTrader
class IFunctionIObservablefloatfloatIObservablefloatISingleAssetTrader(object):
    _types = [meta.function((float,IObservablefloat,ISingleAssetTrader,),IObservablefloat)]
    pass


IFunction[IObservablefloat,(float,IObservablefloat,ISingleAssetTrader,)] = IFunctionIObservablefloatfloatIObservablefloatISingleAssetTrader


from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIObservablefloatIFunctionboolIFunctionfloatIObservablefloat(object):
    _types = [meta.function((IFunctionbool,IFunctionfloat,IObservablefloat,),IObservablefloat)]
    pass


IFunction[IObservablefloat,(IFunctionbool,IFunctionfloat,IObservablefloat,)] = IFunctionIObservablefloatIFunctionboolIFunctionfloatIObservablefloat


from marketsim.gen._out._iobservable import IObservablebool
from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIObservablefloatIObservableboolIFunctionfloatIFunctionfloat(object):
    _types = [meta.function((IObservablebool,IFunctionfloat,IFunctionfloat,),IObservablefloat)]
    pass


IFunction[IObservablefloat,(IObservablebool,IFunctionfloat,IFunctionfloat,)] = IFunctionIObservablefloatIObservableboolIFunctionfloatIFunctionfloat


from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIObservablefloatIFunctionboolIObservablefloatIFunctionfloat(object):
    _types = [meta.function((IFunctionbool,IObservablefloat,IFunctionfloat,),IObservablefloat)]
    pass


IFunction[IObservablefloat,(IFunctionbool,IObservablefloat,IFunctionfloat,)] = IFunctionIObservablefloatIFunctionboolIObservablefloatIFunctionfloat


from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIObservablefloatfloatIFunctionfloatIFunctionfloatstr(object):
    _types = [meta.function((float,IFunctionfloat,IFunctionfloat,str,),IObservablefloat)]
    pass


IFunction[IObservablefloat,(float,IFunctionfloat,IFunctionfloat,str,)] = IFunctionIObservablefloatfloatIFunctionfloatIFunctionfloatstr


from marketsim.gen._out._iobservable import IObservablefloat
from marketsim.gen._out._iobservable import IObservableIOrder
from marketsim.gen._out._iorder import IOrder
class IFunctionIObservableIOrderIFunctionIObservableIOrderIFunctionfloatIObservablefloat(object):
    _types = [meta.function((IFunctionIObservableIOrderIFunctionfloat,IObservablefloat,),IObservableIOrder)]
    pass


IFunction[IObservableIOrder,(IFunctionIObservableIOrderIFunctionfloat,IObservablefloat,)] = IFunctionIObservableIOrderIFunctionIObservableIOrderIFunctionfloatIObservablefloat


from marketsim.gen._out._side import Side
from marketsim.gen._out._iobservable import IObservableSide
class IFunctionIObservableSideIFunctionboolIObservableSideIObservableSide(object):
    _types = [meta.function((IFunctionbool,IObservableSide,IObservableSide,),IObservableSide)]
    pass


IFunction[IObservableSide,(IFunctionbool,IObservableSide,IObservableSide,)] = IFunctionIObservableSideIFunctionboolIObservableSideIObservableSide


from marketsim.gen._out._iobservable import IObservablefloat
from marketsim.gen._out._iorderbook import IOrderBook
class IFunctionIObservablefloatIFunctionSidefloatIFunctionfloatIOrderBook(object):
    _types = [meta.function((IFunctionSide,float,IFunctionfloat,IOrderBook,),IObservablefloat)]
    pass


IFunction[IObservablefloat,(IFunctionSide,float,IFunctionfloat,IOrderBook,)] = IFunctionIObservablefloatIFunctionSidefloatIFunctionfloatIOrderBook


from marketsim.gen._out._iobservable import IObservableSide
from marketsim.gen._out._side import Side
from marketsim.gen._out._iobservable import IObservablebool
class IFunctionIObservableSideIObservableboolIObservableSideIFunctionSide(object):
    _types = [meta.function((IObservablebool,IObservableSide,IFunctionSide,),IObservableSide)]
    pass


IFunction[IObservableSide,(IObservablebool,IObservableSide,IFunctionSide,)] = IFunctionIObservableSideIObservableboolIObservableSideIFunctionSide


from marketsim.gen._out._iobservable import IObservableSide
from marketsim.gen._out._side import Side
from marketsim.gen._out._iobservable import IObservablebool
class IFunctionIObservableSideIObservableboolIFunctionSideIObservableSide(object):
    _types = [meta.function((IObservablebool,IFunctionSide,IObservableSide,),IObservableSide)]
    pass


IFunction[IObservableSide,(IObservablebool,IFunctionSide,IObservableSide,)] = IFunctionIObservableSideIObservableboolIFunctionSideIObservableSide


from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
class IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSidefloat(object):
    _types = [meta.function((IEvent,IFunctionIObservableIOrderIFunctionSide,float,),ISingleAssetStrategy)]
    pass


IFunction[ISingleAssetStrategy,(IEvent,IFunctionIObservableIOrderIFunctionSide,float,)] = IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSidefloat


from marketsim.gen._out._iobservable import IObservablebool
from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIObservablefloatIObservableboolIObservablefloatIFunctionfloat(object):
    _types = [meta.function((IObservablebool,IObservablefloat,IFunctionfloat,),IObservablefloat)]
    pass


IFunction[IObservablefloat,(IObservablebool,IObservablefloat,IFunctionfloat,)] = IFunctionIObservablefloatIObservableboolIObservablefloatIFunctionfloat


from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIObservablefloatIFunctionboolIObservablefloatIObservablefloat(object):
    _types = [meta.function((IFunctionbool,IObservablefloat,IObservablefloat,),IObservablefloat)]
    pass


IFunction[IObservablefloat,(IFunctionbool,IObservablefloat,IObservablefloat,)] = IFunctionIObservablefloatIFunctionboolIObservablefloatIObservablefloat


from marketsim.gen._out._iobservable import IObservablebool
from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIObservablefloatIObservableboolIFunctionfloatIObservablefloat(object):
    _types = [meta.function((IObservablebool,IFunctionfloat,IObservablefloat,),IObservablefloat)]
    pass


IFunction[IObservablefloat,(IObservablebool,IFunctionfloat,IObservablefloat,)] = IFunctionIObservablefloatIObservableboolIFunctionfloatIObservablefloat


class IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide(object):
    _types = [meta.function((IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide,),IFunctionIObservableIOrderIFunctionSide)]
    pass


IFunction[IFunctionIObservableIOrderIFunctionSide,(IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide,)] = IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide


class IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat(object):
    _types = [meta.function((IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat,),IFunctionIObservableIOrderIFunctionfloat)]
    pass


IFunction[IFunctionIObservableIOrderIFunctionfloat,(IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat,)] = IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat


from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
class IFunctionISingleAssetStrategystrstrstrfloatfloat(object):
    _types = [meta.function((str,str,str,float,float,),ISingleAssetStrategy)]
    pass


IFunction[ISingleAssetStrategy,(str,str,str,float,float,)] = IFunctionISingleAssetStrategystrstrstrfloatfloat


from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
class IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSideIFunctionfloat(object):
    _types = [meta.function((IEvent,IFunctionIObservableIOrderIFunctionSide,IFunctionfloat,),ISingleAssetStrategy)]
    pass


IFunction[ISingleAssetStrategy,(IEvent,IFunctionIObservableIOrderIFunctionSide,IFunctionfloat,)] = IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSideIFunctionfloat


class IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionfloatIFunctionIObservableIOrderIFunctionSide(object):
    _types = [meta.function((IFunctionfloat,IFunctionIObservableIOrderIFunctionSide,),IFunctionIObservableIOrderIFunctionSide)]
    pass


IFunction[IFunctionIObservableIOrderIFunctionSide,(IFunctionfloat,IFunctionIObservableIOrderIFunctionSide,)] = IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionfloatIFunctionIObservableIOrderIFunctionSide


from marketsim.gen._out._iobservable import IObservablebool
from marketsim.gen._out._side import Side
from marketsim.gen._out._iobservable import IObservableSide
class IFunctionIObservableSideIObservableboolIObservableSideIObservableSide(object):
    _types = [meta.function((IObservablebool,IObservableSide,IObservableSide,),IObservableSide)]
    pass


IFunction[IObservableSide,(IObservablebool,IObservableSide,IObservableSide,)] = IFunctionIObservableSideIObservableboolIObservableSideIObservableSide


class IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionIObservableIOrderIFunctionSideIFunctionfloat(object):
    _types = [meta.function((IFunctionIObservableIOrderIFunctionSide,IFunctionfloat,),IFunctionIObservableIOrderIFunctionSide)]
    pass


IFunction[IFunctionIObservableIOrderIFunctionSide,(IFunctionIObservableIOrderIFunctionSide,IFunctionfloat,)] = IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionIObservableIOrderIFunctionSideIFunctionfloat


from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIFunctionfloatIObservablefloatfloatfloatfloatfloat(object):
    _types = [meta.function((IObservablefloat,float,float,float,float,),IFunctionfloat)]
    pass


IFunction[IFunctionfloat,(IObservablefloat,float,float,float,float,)] = IFunctionIFunctionfloatIObservablefloatfloatfloatfloatfloat


class IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionIObservableIOrderIFunctionfloatIFunctionfloat(object):
    _types = [meta.function((IFunctionIObservableIOrderIFunctionfloat,IFunctionfloat,),IFunctionIObservableIOrderIFunctionfloat)]
    pass


IFunction[IFunctionIObservableIOrderIFunctionfloat,(IFunctionIObservableIOrderIFunctionfloat,IFunctionfloat,)] = IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionIObservableIOrderIFunctionfloatIFunctionfloat


class IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloatIFunctionIObservableIOrderIFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,IFunctionIObservableIOrderIFunctionfloat,),IFunctionIObservableIOrderIFunctionfloat)]
    pass


IFunction[IFunctionIObservableIOrderIFunctionfloat,(IFunctionfloat,IFunctionIObservableIOrderIFunctionfloat,)] = IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloatIFunctionIObservableIOrderIFunctionfloat


from marketsim.gen._out._iobservable import IObservablebool
from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIObservablefloatIObservableboolIObservablefloatIObservablefloat(object):
    _types = [meta.function((IObservablebool,IObservablefloat,IObservablefloat,),IObservablefloat)]
    pass


IFunction[IObservablefloat,(IObservablebool,IObservablefloat,IObservablefloat,)] = IFunctionIObservablefloatIObservableboolIObservablefloatIObservablefloat


from marketsim.gen._out._iobservable import IObservablefloat
from marketsim.gen._out._isingleassettrader import ISingleAssetTrader
class IFunctionIObservablefloatfloatIObservablefloatfloatISingleAssetTrader(object):
    _types = [meta.function((float,IObservablefloat,float,ISingleAssetTrader,),IObservablefloat)]
    pass


IFunction[IObservablefloat,(float,IObservablefloat,float,ISingleAssetTrader,)] = IFunctionIObservablefloatfloatIObservablefloatfloatISingleAssetTrader


from marketsim.gen._out._iobservable import IObservablefloat
from marketsim.gen._out._idifferentiable import IDifferentiable
class IFunctionIDifferentiableIObservablefloatfloatfloatfloatfloat(object):
    _types = [meta.function((IObservablefloat,float,float,float,float,),IDifferentiable)]
    pass


IFunction[IDifferentiable,(IObservablefloat,float,float,float,float,)] = IFunctionIDifferentiableIObservablefloatfloatfloatfloatfloat


from marketsim.gen._out._iobservable import IObservablefloat
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
class IFunctionISingleAssetStrategyIFunctionIObservableIOrderIFunctionfloatfloatIObservablefloat(object):
    _types = [meta.function((IFunctionIObservableIOrderIFunctionfloat,float,IObservablefloat,),ISingleAssetStrategy)]
    pass


IFunction[ISingleAssetStrategy,(IFunctionIObservableIOrderIFunctionfloat,float,IObservablefloat,)] = IFunctionISingleAssetStrategyIFunctionIObservableIOrderIFunctionfloatfloatIObservablefloat


from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSideIObservablefloat(object):
    _types = [meta.function((IEvent,IFunctionIObservableIOrderIFunctionSide,IObservablefloat,),ISingleAssetStrategy)]
    pass


IFunction[ISingleAssetStrategy,(IEvent,IFunctionIObservableIOrderIFunctionSide,IObservablefloat,)] = IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSideIObservablefloat


from marketsim import listOf
from marketsim.gen._out._itimeserie import ITimeSerie
from marketsim.gen._out._igraph import IGraph
class IFunctionITimeSerieIFunctionIVolumeLevelsIGraphintintlistOffloatint(object):
    _types = [meta.function((IFunctionIVolumeLevels,IGraph,int,int,listOf(float),int,),ITimeSerie)]
    pass


IFunction[ITimeSerie,(IFunctionIVolumeLevels,IGraph,int,int,listOf(float),int,)] = IFunctionITimeSerieIFunctionIVolumeLevelsIGraphintintlistOffloatint


class IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionfloatIFunctionIObservableIOrderIFunctionSideIFunctionfloat(object):
    _types = [meta.function((IFunctionIObservableIOrderIFunctionSideIFunctionfloat,),IFunctionIObservableIOrderIFunctionSideIFunctionfloat)]
    pass


IFunction[IFunctionIObservableIOrderIFunctionSideIFunctionfloat,(IFunctionIObservableIOrderIFunctionSideIFunctionfloat,)] = IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionfloatIFunctionIObservableIOrderIFunctionSideIFunctionfloat


from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionIObservableIOrderIFunctionfloatIObservablefloat(object):
    _types = [meta.function((IFunctionIObservableIOrderIFunctionfloat,IObservablefloat,),IFunctionIObservableIOrderIFunctionfloat)]
    pass


IFunction[IFunctionIObservableIOrderIFunctionfloat,(IFunctionIObservableIOrderIFunctionfloat,IObservablefloat,)] = IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionIObservableIOrderIFunctionfloatIObservablefloat


from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
class IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSidefloatfloat(object):
    _types = [meta.function((IEvent,IFunctionIObservableIOrderIFunctionSide,float,float,),ISingleAssetStrategy)]
    pass


IFunction[ISingleAssetStrategy,(IEvent,IFunctionIObservableIOrderIFunctionSide,float,float,)] = IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSidefloatfloat


class IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionfloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide(object):
    _types = [meta.function((IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide,),IFunctionIObservableIOrderIFunctionSideIFunctionfloat)]
    pass


IFunction[IFunctionIObservableIOrderIFunctionSideIFunctionfloat,(IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide,)] = IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionfloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide


from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim.gen._out._iorderbook import IOrderBook
class IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSideIOrderBookfloat(object):
    _types = [meta.function((IEvent,IFunctionIObservableIOrderIFunctionSide,IOrderBook,float,),ISingleAssetStrategy)]
    pass


IFunction[ISingleAssetStrategy,(IEvent,IFunctionIObservableIOrderIFunctionSide,IOrderBook,float,)] = IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSideIOrderBookfloat


class IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide(object):
    _types = [meta.function((IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide,),IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide)]
    pass


IFunction[IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide,(IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide,)] = IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide


from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
class IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSideIFunctionfloatfloat(object):
    _types = [meta.function((IEvent,IFunctionIObservableIOrderIFunctionSide,IFunctionfloat,float,),ISingleAssetStrategy)]
    pass


IFunction[ISingleAssetStrategy,(IEvent,IFunctionIObservableIOrderIFunctionSide,IFunctionfloat,float,)] = IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSideIFunctionfloatfloat


class IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat(object):
    _types = [meta.function((IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat,),IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat)]
    pass


IFunction[IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat,(IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat,)] = IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat


from marketsim.gen._out._iobservable import IObservablefloat
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
class IFunctionISingleAssetStrategyIFunctionIObservableIOrderIFunctionfloatfloatIObservablefloatfloat(object):
    _types = [meta.function((IFunctionIObservableIOrderIFunctionfloat,float,IObservablefloat,float,),ISingleAssetStrategy)]
    pass


IFunction[ISingleAssetStrategy,(IFunctionIObservableIOrderIFunctionfloat,float,IObservablefloat,float,)] = IFunctionISingleAssetStrategyIFunctionIObservableIOrderIFunctionfloatfloatIObservablefloatfloat


from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSideIObservablefloatfloat(object):
    _types = [meta.function((IEvent,IFunctionIObservableIOrderIFunctionSide,IObservablefloat,float,),ISingleAssetStrategy)]
    pass


IFunction[ISingleAssetStrategy,(IEvent,IFunctionIObservableIOrderIFunctionSide,IObservablefloat,float,)] = IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSideIObservablefloatfloat


from marketsim.gen._out._itimeserie import ITimeSerie
from marketsim.gen._out._imultiassetstrategy import IMultiAssetStrategy
from marketsim.gen._out._itrader import ITrader
from marketsim.gen._out._isingleassettrader import ISingleAssetTrader
from marketsim import listOf
class IFunctionITraderlistOfISingleAssetTraderIMultiAssetStrategystrfloatlistOfITimeSerie(object):
    _types = [meta.function((listOf(ISingleAssetTrader),IMultiAssetStrategy,str,float,listOf(ITimeSerie),),ITrader)]
    pass


IFunction[ITrader,(listOf(ISingleAssetTrader),IMultiAssetStrategy,str,float,listOf(ITimeSerie),)] = IFunctionITraderlistOfISingleAssetTraderIMultiAssetStrategystrfloatlistOfITimeSerie


from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
class IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSidefloatfloatfloat(object):
    _types = [meta.function((IEvent,IFunctionIObservableIOrderIFunctionSide,float,float,float,),ISingleAssetStrategy)]
    pass


IFunction[ISingleAssetStrategy,(IEvent,IFunctionIObservableIOrderIFunctionSide,float,float,float,)] = IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSidefloatfloatfloat


from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIObservablefloat(object):
    _types = [meta.function((IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide,IObservablefloat,),IFunctionIObservableIOrderIFunctionSide)]
    pass


IFunction[IFunctionIObservableIOrderIFunctionSide,(IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide,IObservablefloat,)] = IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIObservablefloat


class IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionfloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat(object):
    _types = [meta.function((IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat,),IFunctionIObservableIOrderIFunctionSideIFunctionfloat)]
    pass


IFunction[IFunctionIObservableIOrderIFunctionSideIFunctionfloat,(IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat,)] = IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionfloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat


from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloatIObservablefloat(object):
    _types = [meta.function((IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat,IObservablefloat,),IFunctionIObservableIOrderIFunctionfloat)]
    pass


IFunction[IFunctionIObservableIOrderIFunctionfloat,(IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat,IObservablefloat,)] = IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloatIObservablefloat


from marketsim.gen._out._itimeserie import ITimeSerie
from marketsim.gen._out._iorderbook import IOrderBook
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim.gen._out._isingleassettrader import ISingleAssetTrader
from marketsim import listOf
class IFunctionISingleAssetTraderIOrderBookISingleAssetStrategystrfloatfloatlistOfITimeSerie(object):
    _types = [meta.function((IOrderBook,ISingleAssetStrategy,str,float,float,listOf(ITimeSerie),),ISingleAssetTrader)]
    pass


IFunction[ISingleAssetTrader,(IOrderBook,ISingleAssetStrategy,str,float,float,listOf(ITimeSerie),)] = IFunctionISingleAssetTraderIOrderBookISingleAssetStrategystrfloatfloatlistOfITimeSerie


from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
class IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSideIFunctionfloatfloatIFunctionfloat(object):
    _types = [meta.function((IEvent,IFunctionIObservableIOrderIFunctionSideIFunctionfloat,float,IFunctionfloat,),ISingleAssetStrategy)]
    pass


IFunction[ISingleAssetStrategy,(IEvent,IFunctionIObservableIOrderIFunctionSideIFunctionfloat,float,IFunctionfloat,)] = IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSideIFunctionfloatfloatIFunctionfloat


from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
class IFunctionISingleAssetStrategyfloatIFunctionfloatIEventIFunctionIObservableIOrderIFunctionSideIFunctionfloat(object):
    _types = [meta.function((float,IFunctionfloat,IEvent,IFunctionIObservableIOrderIFunctionSideIFunctionfloat,),ISingleAssetStrategy)]
    pass


IFunction[ISingleAssetStrategy,(float,IFunctionfloat,IEvent,IFunctionIObservableIOrderIFunctionSideIFunctionfloat,)] = IFunctionISingleAssetStrategyfloatIFunctionfloatIEventIFunctionIObservableIOrderIFunctionSideIFunctionfloat


from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
class IFunctionISingleAssetStrategyISingleAssetStrategyIFunctionIAccountISingleAssetStrategyIFunctionIFunctionfloatIAccount(object):
    _types = [meta.function((ISingleAssetStrategy,IFunctionIAccountISingleAssetStrategy,IFunctionIFunctionfloatIAccount,),ISingleAssetStrategy)]
    pass


IFunction[ISingleAssetStrategy,(ISingleAssetStrategy,IFunctionIAccountISingleAssetStrategy,IFunctionIFunctionfloatIAccount,)] = IFunctionISingleAssetStrategyISingleAssetStrategyIFunctionIAccountISingleAssetStrategyIFunctionIFunctionfloatIAccount


class IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionfloatIFunctionfloatIFunctionIObservableIOrderIFunctionSideIFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,IFunctionIObservableIOrderIFunctionSideIFunctionfloat,),IFunctionIObservableIOrderIFunctionSideIFunctionfloat)]
    pass


IFunction[IFunctionIObservableIOrderIFunctionSideIFunctionfloat,(IFunctionfloat,IFunctionIObservableIOrderIFunctionSideIFunctionfloat,)] = IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionfloatIFunctionfloatIFunctionIObservableIOrderIFunctionSideIFunctionfloat


class IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionfloatIFunctionIObservableIOrderIFunctionSideIFunctionfloatIFunctionfloat(object):
    _types = [meta.function((IFunctionIObservableIOrderIFunctionSideIFunctionfloat,IFunctionfloat,),IFunctionIObservableIOrderIFunctionSideIFunctionfloat)]
    pass


IFunction[IFunctionIObservableIOrderIFunctionSideIFunctionfloat,(IFunctionIObservableIOrderIFunctionSideIFunctionfloat,IFunctionfloat,)] = IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionfloatIFunctionIObservableIOrderIFunctionSideIFunctionfloatIFunctionfloat


class IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat(object):
    _types = [meta.function((IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide,IFunctionfloat,),IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide)]
    pass


IFunction[IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide,(IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide,IFunctionfloat,)] = IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat


from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim import listOf
class IFunctionISingleAssetStrategylistOfISingleAssetStrategyIFunctionIAccountISingleAssetStrategyIFunctionIFunctionfloatIAccount(object):
    _types = [meta.function((listOf(ISingleAssetStrategy),IFunctionIAccountISingleAssetStrategy,IFunctionIFunctionfloatIAccount,),ISingleAssetStrategy)]
    pass


IFunction[ISingleAssetStrategy,(listOf(ISingleAssetStrategy),IFunctionIAccountISingleAssetStrategy,IFunctionIFunctionfloatIAccount,)] = IFunctionISingleAssetStrategylistOfISingleAssetStrategyIFunctionIAccountISingleAssetStrategyIFunctionIFunctionfloatIAccount


class IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide(object):
    _types = [meta.function((IFunctionfloat,IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide,),IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide)]
    pass


IFunction[IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide,(IFunctionfloat,IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide,)] = IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide


class IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloatIFunctionfloat(object):
    _types = [meta.function((IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat,IFunctionfloat,),IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat)]
    pass


IFunction[IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat,(IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat,IFunctionfloat,)] = IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloatIFunctionfloat


class IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloatIFunctionfloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat,),IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat)]
    pass


IFunction[IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat,(IFunctionfloat,IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat,)] = IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloatIFunctionfloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat


from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionfloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIObservablefloat(object):
    _types = [meta.function((IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide,IObservablefloat,),IFunctionIObservableIOrderIFunctionSideIFunctionfloat)]
    pass


IFunction[IFunctionIObservableIOrderIFunctionSideIFunctionfloat,(IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide,IObservablefloat,)] = IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionfloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIObservablefloat


from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIObservablefloat(object):
    _types = [meta.function((IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide,IObservablefloat,),IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide)]
    pass


IFunction[IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide,(IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide,IObservablefloat,)] = IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIObservablefloat


class IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat(object):
    _types = [meta.function((IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat,),IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat)]
    pass


IFunction[IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat,(IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat,)] = IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat


from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloatIObservablefloat(object):
    _types = [meta.function((IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat,IObservablefloat,),IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat)]
    pass


IFunction[IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat,(IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat,IObservablefloat,)] = IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloatIObservablefloat


from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
class IFunctionISingleAssetStrategyfloatIFunctionfloatIEventIFunctionIObservableIOrderIFunctionSideIFunctionfloatIFunctionSide(object):
    _types = [meta.function((float,IFunctionfloat,IEvent,IFunctionIObservableIOrderIFunctionSideIFunctionfloat,IFunctionSide,),ISingleAssetStrategy)]
    pass


IFunction[ISingleAssetStrategy,(float,IFunctionfloat,IEvent,IFunctionIObservableIOrderIFunctionSideIFunctionfloat,IFunctionSide,)] = IFunctionISingleAssetStrategyfloatIFunctionfloatIEventIFunctionIObservableIOrderIFunctionSideIFunctionfloatIFunctionSide


from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
class IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSideIFunctionfloatIFunctionSidefloatIFunctionfloat(object):
    _types = [meta.function((IEvent,IFunctionIObservableIOrderIFunctionSideIFunctionfloat,IFunctionSide,float,IFunctionfloat,),ISingleAssetStrategy)]
    pass


IFunction[ISingleAssetStrategy,(IEvent,IFunctionIObservableIOrderIFunctionSideIFunctionfloat,IFunctionSide,float,IFunctionfloat,)] = IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSideIFunctionfloatIFunctionSidefloatIFunctionfloat


from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionfloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloatIObservablefloat(object):
    _types = [meta.function((IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat,IObservablefloat,),IFunctionIObservableIOrderIFunctionSideIFunctionfloat)]
    pass


IFunction[IFunctionIObservableIOrderIFunctionSideIFunctionfloat,(IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat,IObservablefloat,)] = IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionfloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloatIObservablefloat


class IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloatIFunctionfloat(object):
    _types = [meta.function((IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat,IFunctionfloat,),IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat)]
    pass


IFunction[IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat,(IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat,IFunctionfloat,)] = IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloatIFunctionfloat


class IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloatIFunctionfloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat,),IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat)]
    pass


IFunction[IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat,(IFunctionfloat,IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat,)] = IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloatIFunctionfloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat


from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloatIObservablefloat(object):
    _types = [meta.function((IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat,IObservablefloat,),IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat)]
    pass


IFunction[IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat,(IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat,IObservablefloat,)] = IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloatIObservablefloat


from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim import listOf
class IFunctionISingleAssetStrategylistOfISingleAssetStrategyIFunctionIAccountISingleAssetStrategyIFunctionIFunctionfloatIAccountIFunctionIFunctionfloatIFunctionfloatIFunctionIFunctionlistOffloatlistOffloat(object):
    _types = [meta.function((listOf(ISingleAssetStrategy),IFunctionIAccountISingleAssetStrategy,IFunctionIFunctionfloatIAccount,IFunctionIFunctionfloatIFunctionfloat,IFunctionIFunctionlistOffloatlistOffloat,),ISingleAssetStrategy)]
    pass


IFunction[ISingleAssetStrategy,(listOf(ISingleAssetStrategy),IFunctionIAccountISingleAssetStrategy,IFunctionIFunctionfloatIAccount,IFunctionIFunctionfloatIFunctionfloat,IFunctionIFunctionlistOffloatlistOffloat,)] = IFunctionISingleAssetStrategylistOfISingleAssetStrategyIFunctionIAccountISingleAssetStrategyIFunctionIFunctionfloatIAccountIFunctionIFunctionfloatIFunctionfloatIFunctionIFunctionlistOffloatlistOffloat


IFunction[int]._types.append(IFunction[float])
IFunction[int]._types.append(IFunction[object])
IFunction[float]._types.append(IFunction[object])
