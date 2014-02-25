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
    @property
    def volume_price_Limit(self):
        from marketsim.gen._out.order._curried._volume_price_limit import volume_price_Limit
        return volume_price_Limit(self)
    
    def LiquidityProvider(self, initialValue = None,priceDistr = None,book = None):
        from marketsim.gen._out.strategy.price._liquidityprovider import LiquidityProvider
        return LiquidityProvider(self,initialValue,priceDistr,book)
    
    def Limit(self, price = None,volume = None):
        from marketsim.gen._out.order._limit import Limit
        return Limit(self,price,volume)
    
    def Market(self, volume = None):
        from marketsim.gen._out.order._market import Market
        return Market(self,volume)
    
    @property
    def volume_Market(self):
        from marketsim.gen._out.order._curried._volume_market import volume_Market
        return volume_Market(self)
    
    def FixedBudget(self, budget = None):
        from marketsim.gen._out.order._fixedbudget import FixedBudget
        return FixedBudget(self,budget)
    
    def price_Limit(self, volume = None):
        from marketsim.gen._out.order._curried._price_limit import price_Limit
        return price_Limit(self,volume)
    
    def volume_Limit(self, price = None):
        from marketsim.gen._out.order._curried._volume_limit import volume_Limit
        return volume_Limit(self,price)
    
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
    
    @property
    def side_FixedBudget(self):
        from marketsim.gen._out.order._curried._side_fixedbudget import side_FixedBudget
        return side_FixedBudget(self)
    
    @property
    def sideprice_Limit(self):
        from marketsim.gen._out.order._curried._sideprice_limit import sideprice_Limit
        return sideprice_Limit(self)
    
    def Signal(self, threshold = None):
        from marketsim.gen._out.strategy.side._signal import Signal
        return Signal(self,threshold)
    
    @property
    def signedVolume_LimitSigned(self):
        from marketsim.gen._out.order._curried._signedvolume_limitsigned import signedVolume_LimitSigned
        return signedVolume_LimitSigned(self)
    
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
    
    def FundamentalValue(self, book = None):
        from marketsim.gen._out.strategy.side._fundamentalvalue import FundamentalValue
        return FundamentalValue(self,book)
    
    @property
    def MarketSigned(self):
        from marketsim.gen._out.order._marketsigned import MarketSigned
        return MarketSigned(self)
    
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
    
    def side_Limit(self, volume = None):
        from marketsim.gen._out.order._curried._side_limit import side_Limit
        return side_Limit(self,volume)
    
    @property
    def Exp(self):
        from marketsim.gen._out.math._exp import Exp
        return Exp(self)
    
    @property
    def Log(self):
        from marketsim.gen._out.math._log import Log
        return Log(self)
    
    @property
    def side_price_Limit(self):
        from marketsim.gen._out.order._curried._side_price_limit import side_price_Limit
        return side_price_Limit(self)
    
    @property
    def side_Market(self):
        from marketsim.gen._out.order._curried._side_market import side_Market
        return side_Market(self)
    
    @property
    def Clamp0(self):
        from marketsim.gen._out.strategy.weight._clamp0 import Clamp0
        return Clamp0(self)
    
    @property
    def Canceller(self):
        from marketsim.gen._out.strategy._canceller import Canceller
        return Canceller(self)
    
    def Sub(self, y = None):
        from marketsim.gen._out.ops._sub import Sub
        return Sub(self,y)
    
    def AtanPow(self, base = None):
        from marketsim.gen._out.strategy.weight._atanpow import AtanPow
        return AtanPow(self,base)
    
    def Pow(self, power = None):
        from marketsim.gen._out.math._pow import Pow
        return Pow(self,power)
    
    def LimitSigned(self, price = None):
        from marketsim.gen._out.order._limitsigned import LimitSigned
        return LimitSigned(self,price)
    
    @property
    def sidevolume_Limit(self):
        from marketsim.gen._out.order._curried._sidevolume_limit import sidevolume_Limit
        return sidevolume_Limit(self)
    
    def IfDefined(self, elsePart = None):
        from marketsim.gen._out._ifdefined import IfDefined
        return IfDefined(self,elsePart)
    
    @property
    def Noise(self):
        from marketsim.gen._out.strategy.side._noise import Noise
        return Noise(self)
    
    @property
    def IdentityF(self):
        from marketsim.gen._out.strategy.weight._identityf import IdentityF
        return IdentityF(self)
    
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


from marketsim.gen._out._test.types._u import U
class IFunctionU(object):
    _types = [meta.function((),U)]
    pass


IFunction[U] = IFunctionU


class IFunctionIFunctionfloat(object):
    _types = [meta.function((),IFunctionfloat)]
    pass


IFunction[IFunctionfloat] = IFunctionIFunctionfloat


from marketsim.gen._out._test.types._t import T
class IFunctionT(object):
    _types = [meta.function((),T)]
    pass


IFunction[T] = IFunctionT


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


from marketsim.gen._out._isingleassettrader import ISingleAssetTrader
class IFunctionISingleAssetTrader(object):
    _types = [meta.function((),ISingleAssetTrader)]
    pass


IFunction[ISingleAssetTrader] = IFunctionISingleAssetTrader


from marketsim.gen._out._side import Side
from marketsim.gen._out._iobservable import IObservableSide
class IFunctionIObservableSide(object):
    _types = [meta.function((),IObservableSide)]
    pass


IFunction[IObservableSide] = IFunctionIObservableSide


from marketsim.gen._out._imultiassetstrategy import IMultiAssetStrategy
class IFunctionIMultiAssetStrategy(object):
    _types = [meta.function((),IMultiAssetStrategy)]
    pass


IFunction[IMultiAssetStrategy] = IFunctionIMultiAssetStrategy


from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
class IFunctionISingleAssetStrategy(object):
    _types = [meta.function((),ISingleAssetStrategy)]
    pass


IFunction[ISingleAssetStrategy] = IFunctionISingleAssetStrategy


from marketsim.gen._out._iaccount import IAccount
class IFunctionIFunctionfloatIAccount(object):
    _types = [meta.function((IAccount,),IFunctionfloat)]
    pass


IFunction[IFunctionfloat,(IAccount,)] = IFunctionIFunctionfloatIAccount


from marketsim.gen._out._igraph import IGraph
class IFunctionIGraphstr(object):
    _types = [meta.function((str,),IGraph)]
    pass


IFunction[IGraph,(str,)] = IFunctionIGraphstr


class IFunctionstrstr(object):
    _types = [meta.function((str,),str)]
    pass


IFunction[str,(str,)] = IFunctionstrstr


from marketsim.gen._out._iobservable import IObservablebool
class IFunctionIObservablebool(object):
    _types = [meta.function((),IObservablebool)]
    pass


IFunction[IObservablebool] = IFunctionIObservablebool


class IFunctionIFunctionintIFunctionint(object):
    _types = [meta.function((IFunctionint,),IFunctionint)]
    pass


IFunction[IFunctionint,(IFunctionint,)] = IFunctionIFunctionintIFunctionint


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
    def side_StopLoss(self, maxloss = None):
        from marketsim.gen._out.order._curried._side_stoploss import side_StopLoss
        return side_StopLoss(self,maxloss)
    
    def side_WithExpiry(self, expiry = None):
        from marketsim.gen._out.order._curried._side_withexpiry import side_WithExpiry
        return side_WithExpiry(self,expiry)
    
    @property
    def side_ImmediateOrCancel(self):
        from marketsim.gen._out.order._curried._side_immediateorcancel import side_ImmediateOrCancel
        return side_ImmediateOrCancel(self)
    
    def side_Iceberg(self, lotSize = None):
        from marketsim.gen._out.order._curried._side_iceberg import side_Iceberg
        return side_Iceberg(self,lotSize)
    
    pass


IFunction[IObservableIOrder,(IFunctionSide,)] = IFunctionIObservableIOrderIFunctionSide


from marketsim.gen._out._iorderbook import IOrderBook
class IFunctionIFunctionfloatIOrderBook(object):
    _types = [meta.function((IOrderBook,),IFunctionfloat)]
    pass


IFunction[IFunctionfloat,(IOrderBook,)] = IFunctionIFunctionfloatIOrderBook


class IFunctionIFunctionSideIFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,),IFunctionSide)]
    pass


IFunction[IFunctionSide,(IFunctionfloat,)] = IFunctionIFunctionSideIFunctionfloat


from marketsim.gen._out._iorder import IOrder
from marketsim.gen._out._iobservable import IObservableIOrder
class IFunctionIObservableIOrderIFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,),IObservableIOrder)]
    def RSI_linear(self, alpha = None,k = None,timeframe = None):
        from marketsim.gen._out.strategy._rsi_linear import RSI_linear
        return RSI_linear(self,alpha,k,timeframe)
    
    def price_Iceberg(self, lotSize = None):
        from marketsim.gen._out.order._curried._price_iceberg import price_Iceberg
        return price_Iceberg(self,lotSize)
    
    def price_StopLoss(self, maxloss = None):
        from marketsim.gen._out.order._curried._price_stoploss import price_StopLoss
        return price_StopLoss(self,maxloss)
    
    @property
    def price_ImmediateOrCancel(self):
        from marketsim.gen._out.order._curried._price_immediateorcancel import price_ImmediateOrCancel
        return price_ImmediateOrCancel(self)
    
    @property
    def price_Peg(self):
        from marketsim.gen._out.order._curried._price_peg import price_Peg
        return price_Peg(self)
    
    def volume_StopLoss(self, maxloss = None):
        from marketsim.gen._out.order._curried._volume_stoploss import volume_StopLoss
        return volume_StopLoss(self,maxloss)
    
    def volume_WithExpiry(self, expiry = None):
        from marketsim.gen._out.order._curried._volume_withexpiry import volume_WithExpiry
        return volume_WithExpiry(self,expiry)
    
    @property
    def volume_ImmediateOrCancel(self):
        from marketsim.gen._out.order._curried._volume_immediateorcancel import volume_ImmediateOrCancel
        return volume_ImmediateOrCancel(self)
    
    def volume_Iceberg(self, lotSize = None):
        from marketsim.gen._out.order._curried._volume_iceberg import volume_Iceberg
        return volume_Iceberg(self,lotSize)
    
    def price_FloatingPrice(self, floatingPrice = None):
        from marketsim.gen._out.order._curried._price_floatingprice import price_FloatingPrice
        return price_FloatingPrice(self,floatingPrice)
    
    def price_WithExpiry(self, expiry = None):
        from marketsim.gen._out.order._curried._price_withexpiry import price_WithExpiry
        return price_WithExpiry(self,expiry)
    
    def FloatingPrice(self, floatingPrice = None):
        from marketsim.gen._out.order._floatingprice import FloatingPrice
        return FloatingPrice(self,floatingPrice)
    
    @property
    def Peg(self):
        from marketsim.gen._out.order._peg import Peg
        return Peg(self)
    
    def Bollinger_linear(self, alpha = None,k = None):
        from marketsim.gen._out.strategy._bollinger_linear import Bollinger_linear
        return Bollinger_linear(self,alpha,k)
    
    pass


IFunction[IObservableIOrder,(IFunctionfloat,)] = IFunctionIObservableIOrderIFunctionfloat


from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIObservablefloatfloat(object):
    _types = [meta.function((float,),IObservablefloat)]
    pass


IFunction[IObservablefloat,(float,)] = IFunctionIObservablefloatfloat


class IFunctionIFunctionfloatIFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,),IFunctionfloat)]
    pass


IFunction[IFunctionfloat,(IFunctionfloat,)] = IFunctionIFunctionfloatIFunctionfloat


from marketsim.gen._out._iobservable import IObservablefloat
from marketsim.gen._out._ilink import ILink
class IFunctionILinkIObservablefloat(object):
    _types = [meta.function((IObservablefloat,),ILink)]
    pass


IFunction[ILink,(IObservablefloat,)] = IFunctionILinkIObservablefloat


from marketsim.gen._out._iaccount import IAccount
from marketsim.gen._out._iobservable import IObservableint
class IFunctionIObservableintIAccount(object):
    _types = [meta.function((IAccount,),IObservableint)]
    pass


IFunction[IObservableint,(IAccount,)] = IFunctionIObservableintIAccount


from marketsim.gen._out._iorderbook import IOrderBook
from marketsim.gen._out._iobservable import IObservableint
class IFunctionIObservableintIOrderBook(object):
    _types = [meta.function((IOrderBook,),IObservableint)]
    pass


IFunction[IObservableint,(IOrderBook,)] = IFunctionIObservableintIOrderBook


from marketsim.gen._out._iaccount import IAccount
from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIObservablefloatIAccount(object):
    _types = [meta.function((IAccount,),IObservablefloat)]
    pass


IFunction[IObservablefloat,(IAccount,)] = IFunctionIObservablefloatIAccount


from marketsim.gen._out._idifferentiable import IDifferentiable
class IFunctionIFunctionfloatIDifferentiable(object):
    _types = [meta.function((IDifferentiable,),IFunctionfloat)]
    pass


IFunction[IFunctionfloat,(IDifferentiable,)] = IFunctionIFunctionfloatIDifferentiable


from marketsim.gen._out._iorderqueue import IOrderQueue
from marketsim.gen._out._iobservable import IObservableint
class IFunctionIObservableintIOrderQueue(object):
    _types = [meta.function((IOrderQueue,),IObservableint)]
    pass


IFunction[IObservableint,(IOrderQueue,)] = IFunctionIObservableintIOrderQueue


from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim.gen._out._iaccount import IAccount
class IFunctionIAccountISingleAssetStrategy(object):
    _types = [meta.function((ISingleAssetStrategy,),IAccount)]
    pass


IFunction[IAccount,(ISingleAssetStrategy,)] = IFunctionIAccountISingleAssetStrategy


from marketsim.gen._out._iorderbook import IOrderBook
from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIObservablefloatIOrderBook(object):
    _types = [meta.function((IOrderBook,),IObservablefloat)]
    pass


IFunction[IObservablefloat,(IOrderBook,)] = IFunctionIObservablefloatIOrderBook


from marketsim import listOf
class IFunctionIFunctionlistOffloatlistOffloat(object):
    _types = [meta.function((listOf(float),),IFunctionlistOffloat)]
    pass


IFunction[IFunctionlistOffloat,(listOf(float),)] = IFunctionIFunctionlistOffloatlistOffloat


from marketsim.gen._out._iaccount import IAccount
class IFunctionIFunctionfloatIAccountfloat(object):
    _types = [meta.function((IAccount,float,),IFunctionfloat)]
    pass


IFunction[IFunctionfloat,(IAccount,float,)] = IFunctionIFunctionfloatIAccountfloat


from marketsim.gen._out._iorder import IOrder
from marketsim.gen._out._iobservable import IObservableIOrder
class IFunctionIObservableIOrderIFunctionSide(object):
    _types = [meta.function((IFunctionSide,),IObservableIOrder)]
    pass


IFunction[IObservableIOrder,(IFunctionSide,)] = IFunctionIObservableIOrderIFunctionSide


class IFunctionintIFunctionICandleStickint(object):
    _types = [meta.function((IFunctionICandleStick,int,),int)]
    pass


IFunction[int,(IFunctionICandleStick,int,)] = IFunctionintIFunctionICandleStickint


from marketsim.gen._out._iorderqueue import IOrderQueue
from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIObservablefloatIOrderQueue(object):
    _types = [meta.function((IOrderQueue,),IObservablefloat)]
    pass


IFunction[IObservablefloat,(IOrderQueue,)] = IFunctionIObservablefloatIOrderQueue


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


class IFunctionIFunctionIObservableIOrderIFunctionfloat(object):
    _types = [meta.function((),IFunctionIObservableIOrderIFunctionfloat)]
    pass


IFunction[IFunctionIObservableIOrderIFunctionfloat] = IFunctionIFunctionIObservableIOrderIFunctionfloat


class IFunctionIFunctionUIFunctionT(object):
    _types = [meta.function((IFunctionT,),IFunctionU)]
    pass


IFunction[IFunctionU,(IFunctionT,)] = IFunctionIFunctionUIFunctionT


from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIFunctionfloatIObservablefloat(object):
    _types = [meta.function((IObservablefloat,),IFunctionfloat)]
    pass


IFunction[IFunctionfloat,(IObservablefloat,)] = IFunctionIFunctionfloatIObservablefloat


class IFunctionIFunctionIFunctionfloatIFunctionfloat(object):
    _types = [meta.function((),IFunctionIFunctionfloatIFunctionfloat)]
    pass


IFunction[IFunctionIFunctionfloatIFunctionfloat] = IFunctionIFunctionIFunctionfloatIFunctionfloat


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


class IFunctionIFunctionIFunctionlistOffloatlistOffloat(object):
    _types = [meta.function((),IFunctionIFunctionlistOffloatlistOffloat)]
    pass


IFunction[IFunctionIFunctionlistOffloatlistOffloat] = IFunctionIFunctionIFunctionlistOffloatlistOffloat


from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIObservablefloatIObservablefloat(object):
    _types = [meta.function((IObservablefloat,),IObservablefloat)]
    pass


IFunction[IObservablefloat,(IObservablefloat,)] = IFunctionIObservablefloatIObservablefloat


from marketsim.gen._out._iobservable import IObservableIOrder
from marketsim.gen._out._iorder import IOrder
class IFunctionIObservableIOrderIFunctionSideIFunctionfloat(object):
    _types = [meta.function((IFunctionSide,IFunctionfloat,),IObservableIOrder)]
    def sidevolume_Iceberg(self, lotSize = None):
        from marketsim.gen._out.order._curried._sidevolume_iceberg import sidevolume_Iceberg
        return sidevolume_Iceberg(self,lotSize)
    
    def sidevolume_WithExpiry(self, expiry = None):
        from marketsim.gen._out.order._curried._sidevolume_withexpiry import sidevolume_WithExpiry
        return sidevolume_WithExpiry(self,expiry)
    
    def sideprice_StopLoss(self, maxloss = None):
        from marketsim.gen._out.order._curried._sideprice_stoploss import sideprice_StopLoss
        return sideprice_StopLoss(self,maxloss)
    
    @property
    def sidevolume_ImmediateOrCancel(self):
        from marketsim.gen._out.order._curried._sidevolume_immediateorcancel import sidevolume_ImmediateOrCancel
        return sidevolume_ImmediateOrCancel(self)
    
    def sidevolume_StopLoss(self, maxloss = None):
        from marketsim.gen._out.order._curried._sidevolume_stoploss import sidevolume_StopLoss
        return sidevolume_StopLoss(self,maxloss)
    
    def sideprice_WithExpiry(self, expiry = None):
        from marketsim.gen._out.order._curried._sideprice_withexpiry import sideprice_WithExpiry
        return sideprice_WithExpiry(self,expiry)
    
    def sideprice_Iceberg(self, lotSize = None):
        from marketsim.gen._out.order._curried._sideprice_iceberg import sideprice_Iceberg
        return sideprice_Iceberg(self,lotSize)
    
    @property
    def sideprice_ImmediateOrCancel(self):
        from marketsim.gen._out.order._curried._sideprice_immediateorcancel import sideprice_ImmediateOrCancel
        return sideprice_ImmediateOrCancel(self)
    
    pass


IFunction[IObservableIOrder,(IFunctionSide,IFunctionfloat,)] = IFunctionIObservableIOrderIFunctionSideIFunctionfloat


class IFunctionIFunctionRIFunctionT(object):
    _types = [meta.function((IFunctionT,),IFunctionR)]
    pass


IFunction[IFunctionR,(IFunctionT,)] = IFunctionIFunctionRIFunctionT


from marketsim.gen._out._iaccount import IAccount
class IFunctionIFunctionfloatIAccountfloat(object):
    _types = [meta.function((IAccount,float,),IFunctionfloat)]
    pass


IFunction[IFunctionfloat,(IAccount,float,)] = IFunctionIFunctionfloatIAccountfloat


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


class IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide(object):
    _types = [meta.function((IFunctionSide,),IFunctionIObservableIOrderIFunctionfloat)]
    def side_price_StopLoss(self, maxloss = None):
        from marketsim.gen._out.order._curried._side_price_stoploss import side_price_StopLoss
        return side_price_StopLoss(self,maxloss)
    
    def sideprice_FloatingPrice(self, floatingPrice = None):
        from marketsim.gen._out.order._curried._sideprice_floatingprice import sideprice_FloatingPrice
        return sideprice_FloatingPrice(self,floatingPrice)
    
    @property
    def sideprice_Peg(self):
        from marketsim.gen._out.order._curried._sideprice_peg import sideprice_Peg
        return sideprice_Peg(self)
    
    @property
    def side_Peg(self):
        from marketsim.gen._out.order._curried._side_peg import side_Peg
        return side_Peg(self)
    
    def side_price_Iceberg(self, lotSize = None):
        from marketsim.gen._out.order._curried._side_price_iceberg import side_price_Iceberg
        return side_price_Iceberg(self,lotSize)
    
    @property
    def side_price_ImmediateOrCancel(self):
        from marketsim.gen._out.order._curried._side_price_immediateorcancel import side_price_ImmediateOrCancel
        return side_price_ImmediateOrCancel(self)
    
    def side_price_FloatingPrice(self, floatingPrice = None):
        from marketsim.gen._out.order._curried._side_price_floatingprice import side_price_FloatingPrice
        return side_price_FloatingPrice(self,floatingPrice)
    
    def side_FloatingPrice(self, floatingPrice = None):
        from marketsim.gen._out.order._curried._side_floatingprice import side_FloatingPrice
        return side_FloatingPrice(self,floatingPrice)
    
    def side_price_WithExpiry(self, expiry = None):
        from marketsim.gen._out.order._curried._side_price_withexpiry import side_price_WithExpiry
        return side_price_WithExpiry(self,expiry)
    
    @property
    def side_price_Peg(self):
        from marketsim.gen._out.order._curried._side_price_peg import side_price_Peg
        return side_price_Peg(self)
    
    pass


IFunction[IFunctionIObservableIOrderIFunctionfloat,(IFunctionSide,)] = IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide


from marketsim.gen._out._iorderbook import IOrderBook
class IFunctionIFunctionfloatIOrderBookfloat(object):
    _types = [meta.function((IOrderBook,float,),IFunctionfloat)]
    pass


IFunction[IFunctionfloat,(IOrderBook,float,)] = IFunctionIFunctionfloatIOrderBookfloat


class IFunctionIFunctionfloatIFunctionfloatfloat(object):
    _types = [meta.function((IFunctionfloat,float,),IFunctionfloat)]
    pass


IFunction[IFunctionfloat,(IFunctionfloat,float,)] = IFunctionIFunctionfloatIFunctionfloatfloat


from marketsim.gen._out._iorderqueue import IOrderQueue
class IFunctionIFunctionfloatIOrderQueuefloat(object):
    _types = [meta.function((IOrderQueue,float,),IFunctionfloat)]
    pass


IFunction[IFunctionfloat,(IOrderQueue,float,)] = IFunctionIFunctionfloatIOrderQueuefloat


class IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,),IFunctionIObservableIOrderIFunctionfloat)]
    def volume_price_WithExpiry(self, expiry = None):
        from marketsim.gen._out.order._curried._volume_price_withexpiry import volume_price_WithExpiry
        return volume_price_WithExpiry(self,expiry)
    
    @property
    def volume_price_Peg(self):
        from marketsim.gen._out.order._curried._volume_price_peg import volume_price_Peg
        return volume_price_Peg(self)
    
    @property
    def volume_Peg(self):
        from marketsim.gen._out.order._curried._volume_peg import volume_Peg
        return volume_Peg(self)
    
    def volume_FloatingPrice(self, floatingPrice = None):
        from marketsim.gen._out.order._curried._volume_floatingprice import volume_FloatingPrice
        return volume_FloatingPrice(self,floatingPrice)
    
    def volume_price_StopLoss(self, maxloss = None):
        from marketsim.gen._out.order._curried._volume_price_stoploss import volume_price_StopLoss
        return volume_price_StopLoss(self,maxloss)
    
    @property
    def volume_price_ImmediateOrCancel(self):
        from marketsim.gen._out.order._curried._volume_price_immediateorcancel import volume_price_ImmediateOrCancel
        return volume_price_ImmediateOrCancel(self)
    
    def volume_price_FloatingPrice(self, floatingPrice = None):
        from marketsim.gen._out.order._curried._volume_price_floatingprice import volume_price_FloatingPrice
        return volume_price_FloatingPrice(self,floatingPrice)
    
    def volume_price_Iceberg(self, lotSize = None):
        from marketsim.gen._out.order._curried._volume_price_iceberg import volume_price_Iceberg
        return volume_price_Iceberg(self,lotSize)
    
    pass


IFunction[IFunctionIObservableIOrderIFunctionfloat,(IFunctionfloat,)] = IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat


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


class IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide(object):
    _types = [meta.function((IFunctionSide,),IFunctionIObservableIOrderIFunctionfloat)]
    pass


IFunction[IFunctionIObservableIOrderIFunctionfloat,(IFunctionSide,)] = IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide


class IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,),IFunctionIObservableIOrderIFunctionSide)]
    pass


IFunction[IFunctionIObservableIOrderIFunctionSide,(IFunctionfloat,)] = IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionfloat


class IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,),IFunctionIObservableIOrderIFunctionfloat)]
    pass


IFunction[IFunctionIObservableIOrderIFunctionfloat,(IFunctionfloat,)] = IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat


class IFunctionIFunctionboolIFunctionfloatIFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,IFunctionfloat,),IFunctionbool)]
    pass


IFunction[IFunctionbool,(IFunctionfloat,IFunctionfloat,)] = IFunctionIFunctionboolIFunctionfloatIFunctionfloat


from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIFunctionfloatIObservablefloatfloat(object):
    _types = [meta.function((IObservablefloat,float,),IFunctionfloat)]
    pass


IFunction[IFunctionfloat,(IObservablefloat,float,)] = IFunctionIFunctionfloatIObservablefloatfloat


from marketsim.gen._out._iorderbook import IOrderBook
from marketsim.gen._out._iobservable import IObservableSide
from marketsim.gen._out._side import Side
class IFunctionIObservableSideIFunctionfloatIOrderBook(object):
    _types = [meta.function((IFunctionfloat,IOrderBook,),IObservableSide)]
    pass


IFunction[IObservableSide,(IFunctionfloat,IOrderBook,)] = IFunctionIObservableSideIFunctionfloatIOrderBook


from marketsim.gen._out._iobservable import IObservablefloat
from marketsim.gen._out._idifferentiable import IDifferentiable
class IFunctionIDifferentiableIObservablefloatfloat(object):
    _types = [meta.function((IObservablefloat,float,),IDifferentiable)]
    pass


IFunction[IDifferentiable,(IObservablefloat,float,)] = IFunctionIDifferentiableIObservablefloatfloat


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


from marketsim.gen._out._iorderqueue import IOrderQueue
from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIObservablefloatIOrderQueueIFunctionfloat(object):
    _types = [meta.function((IOrderQueue,IFunctionfloat,),IObservablefloat)]
    pass


IFunction[IObservablefloat,(IOrderQueue,IFunctionfloat,)] = IFunctionIObservablefloatIOrderQueueIFunctionfloat


class IFunctionIFunctionTIFunctionintIFunctionfloat(object):
    _types = [meta.function((IFunctionint,IFunctionfloat,),IFunctionT)]
    pass


IFunction[IFunctionT,(IFunctionint,IFunctionfloat,)] = IFunctionIFunctionTIFunctionintIFunctionfloat


from marketsim.gen._out._iobservable import IObservableIOrder
from marketsim.gen._out._iorder import IOrder
class IFunctionIObservableIOrderIFunctionSideIFunctionfloat(object):
    _types = [meta.function((IFunctionSide,IFunctionfloat,),IObservableIOrder)]
    pass


IFunction[IObservableIOrder,(IFunctionSide,IFunctionfloat,)] = IFunctionIObservableIOrderIFunctionSideIFunctionfloat


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


from marketsim.gen._out._iorder import IOrder
from marketsim.gen._out._iobservable import IObservableIOrder
class IFunctionIObservableIOrderIFunctionIObservableIOrderIFunctionfloat(object):
    _types = [meta.function((IFunctionIObservableIOrderIFunctionfloat,),IObservableIOrder)]
    pass


IFunction[IObservableIOrder,(IFunctionIObservableIOrderIFunctionfloat,)] = IFunctionIObservableIOrderIFunctionIObservableIOrderIFunctionfloat


class IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide(object):
    _types = [meta.function((IFunctionSide,),IFunctionIObservableIOrderIFunctionfloat)]
    pass


IFunction[IFunctionIObservableIOrderIFunctionfloat,(IFunctionSide,)] = IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide


from marketsim.gen._out._iorderbook import IOrderBook
class IFunctionIFunctionfloatIOrderBookfloatfloat(object):
    _types = [meta.function((IOrderBook,float,float,),IFunctionfloat)]
    pass


IFunction[IFunctionfloat,(IOrderBook,float,float,)] = IFunctionIFunctionfloatIOrderBookfloatfloat


class IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat(object):
    _types = [meta.function((IFunctionSide,IFunctionfloat,),IFunctionIObservableIOrderIFunctionfloat)]
    def sidevolume_price_WithExpiry(self, expiry = None):
        from marketsim.gen._out.order._curried._sidevolume_price_withexpiry import sidevolume_price_WithExpiry
        return sidevolume_price_WithExpiry(self,expiry)
    
    @property
    def sidevolume_Peg(self):
        from marketsim.gen._out.order._curried._sidevolume_peg import sidevolume_Peg
        return sidevolume_Peg(self)
    
    def sidevolume_price_StopLoss(self, maxloss = None):
        from marketsim.gen._out.order._curried._sidevolume_price_stoploss import sidevolume_price_StopLoss
        return sidevolume_price_StopLoss(self,maxloss)
    
    def sidevolume_FloatingPrice(self, floatingPrice = None):
        from marketsim.gen._out.order._curried._sidevolume_floatingprice import sidevolume_FloatingPrice
        return sidevolume_FloatingPrice(self,floatingPrice)
    
    def sidevolume_price_FloatingPrice(self, floatingPrice = None):
        from marketsim.gen._out.order._curried._sidevolume_price_floatingprice import sidevolume_price_FloatingPrice
        return sidevolume_price_FloatingPrice(self,floatingPrice)
    
    @property
    def sidevolume_price_ImmediateOrCancel(self):
        from marketsim.gen._out.order._curried._sidevolume_price_immediateorcancel import sidevolume_price_ImmediateOrCancel
        return sidevolume_price_ImmediateOrCancel(self)
    
    @property
    def sidevolume_price_Peg(self):
        from marketsim.gen._out.order._curried._sidevolume_price_peg import sidevolume_price_Peg
        return sidevolume_price_Peg(self)
    
    def sidevolume_price_Iceberg(self, lotSize = None):
        from marketsim.gen._out.order._curried._sidevolume_price_iceberg import sidevolume_price_Iceberg
        return sidevolume_price_Iceberg(self,lotSize)
    
    pass


IFunction[IFunctionIObservableIOrderIFunctionfloat,(IFunctionSide,IFunctionfloat,)] = IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat


class IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,),IFunctionIObservableIOrderIFunctionfloat)]
    pass


IFunction[IFunctionIObservableIOrderIFunctionfloat,(IFunctionfloat,)] = IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat


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
class IFunctionIObservablefloatIObservablefloatIFunctionfloat(object):
    _types = [meta.function((IObservablefloat,IFunctionfloat,),IObservablefloat)]
    pass


IFunction[IObservablefloat,(IObservablefloat,IFunctionfloat,)] = IFunctionIObservablefloatIObservablefloatIFunctionfloat


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
from marketsim.gen._out._icandlestick import ICandleStick
from marketsim.gen._out._iobservable import IObservableICandleStick
class IFunctionIObservableICandleStickIObservablefloatfloat(object):
    _types = [meta.function((IObservablefloat,float,),IObservableICandleStick)]
    pass


IFunction[IObservableICandleStick,(IObservablefloat,float,)] = IFunctionIObservableICandleStickIObservablefloatfloat


from marketsim.gen._out._iorder import IOrder
from marketsim.gen._out._iobservable import IObservableIOrder
class IFunctionIObservableIOrderIObservableIOrderIFunctionfloat(object):
    _types = [meta.function((IObservableIOrder,IFunctionfloat,),IObservableIOrder)]
    pass


IFunction[IObservableIOrder,(IObservableIOrder,IFunctionfloat,)] = IFunctionIObservableIOrderIObservableIOrderIFunctionfloat


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


class IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat(object):
    _types = [meta.function((),IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat)]
    pass


IFunction[IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat] = IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat


from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
class IFunctionISingleAssetStrategyISingleAssetStrategyIFunctionbool(object):
    _types = [meta.function((ISingleAssetStrategy,IFunctionbool,),ISingleAssetStrategy)]
    pass


IFunction[ISingleAssetStrategy,(ISingleAssetStrategy,IFunctionbool,)] = IFunctionISingleAssetStrategyISingleAssetStrategyIFunctionbool


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


class IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloatIFunctionSide(object):
    _types = [meta.function((IFunctionSide,),IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat)]
    pass


IFunction[IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat,(IFunctionSide,)] = IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloatIFunctionSide


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


class IFunctionIFunctionSideIFunctionboolIFunctionSideIFunctionSide(object):
    _types = [meta.function((IFunctionbool,IFunctionSide,IFunctionSide,),IFunctionSide)]
    pass


IFunction[IFunctionSide,(IFunctionbool,IFunctionSide,IFunctionSide,)] = IFunctionIFunctionSideIFunctionboolIFunctionSideIFunctionSide


from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIObservablefloatIObservablefloatIObservablefloat(object):
    _types = [meta.function((IObservablefloat,IObservablefloat,),IObservablefloat)]
    pass


IFunction[IObservablefloat,(IObservablefloat,IObservablefloat,)] = IFunctionIObservablefloatIObservablefloatIObservablefloat


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


from marketsim.gen._out._iorderbook import IOrderBook
class IFunctionIFunctionSidefloatfloatfloatIOrderBook(object):
    _types = [meta.function((float,float,float,IOrderBook,),IFunctionSide)]
    pass


IFunction[IFunctionSide,(float,float,float,IOrderBook,)] = IFunctionIFunctionSidefloatfloatfloatIOrderBook


class IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat(object):
    _types = [meta.function((IFunctionSide,IFunctionfloat,),IFunctionIObservableIOrderIFunctionfloat)]
    pass


IFunction[IFunctionIObservableIOrderIFunctionfloat,(IFunctionSide,IFunctionfloat,)] = IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat


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
class IFunctionIObservableSideIFunctionboolIObservableSideIFunctionSide(object):
    _types = [meta.function((IFunctionbool,IObservableSide,IFunctionSide,),IObservableSide)]
    pass


IFunction[IObservableSide,(IFunctionbool,IObservableSide,IFunctionSide,)] = IFunctionIObservableSideIFunctionboolIObservableSideIFunctionSide


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


from marketsim.gen._out._iobservable import IObservableSide
from marketsim.gen._out._side import Side
from marketsim.gen._out._iobservable import IObservablebool
class IFunctionIObservableSideIObservableboolIObservableSideIFunctionSide(object):
    _types = [meta.function((IObservablebool,IObservableSide,IFunctionSide,),IObservableSide)]
    pass


IFunction[IObservableSide,(IObservablebool,IObservableSide,IFunctionSide,)] = IFunctionIObservableSideIObservableboolIObservableSideIFunctionSide


from marketsim.gen._out._side import Side
from marketsim.gen._out._iobservable import IObservableSide
class IFunctionIObservableSideIFunctionboolIObservableSideIObservableSide(object):
    _types = [meta.function((IFunctionbool,IObservableSide,IObservableSide,),IObservableSide)]
    pass


IFunction[IObservableSide,(IFunctionbool,IObservableSide,IObservableSide,)] = IFunctionIObservableSideIFunctionboolIObservableSideIObservableSide


from marketsim.gen._out._iobservable import IObservableSide
from marketsim.gen._out._side import Side
from marketsim.gen._out._iobservable import IObservablebool
class IFunctionIObservableSideIObservableboolIFunctionSideIObservableSide(object):
    _types = [meta.function((IObservablebool,IFunctionSide,IObservableSide,),IObservableSide)]
    pass


IFunction[IObservableSide,(IObservablebool,IFunctionSide,IObservableSide,)] = IFunctionIObservableSideIObservableboolIFunctionSideIObservableSide


from marketsim.gen._out._iobservable import IObservablefloat
from marketsim.gen._out._iorderbook import IOrderBook
class IFunctionIObservablefloatIFunctionSidefloatIFunctionfloatIOrderBook(object):
    _types = [meta.function((IFunctionSide,float,IFunctionfloat,IOrderBook,),IObservablefloat)]
    pass


IFunction[IObservablefloat,(IFunctionSide,float,IFunctionfloat,IOrderBook,)] = IFunctionIObservablefloatIFunctionSidefloatIFunctionfloatIOrderBook


from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
class IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSidefloat(object):
    _types = [meta.function((IEvent,IFunctionIObservableIOrderIFunctionSide,float,),ISingleAssetStrategy)]
    pass


IFunction[ISingleAssetStrategy,(IEvent,IFunctionIObservableIOrderIFunctionSide,float,)] = IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSidefloat


class IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide(object):
    _types = [meta.function((IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide,),IFunctionIObservableIOrderIFunctionSide)]
    pass


IFunction[IFunctionIObservableIOrderIFunctionSide,(IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide,)] = IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide


from marketsim.gen._out._iobservable import IObservablebool
from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIObservablefloatIObservableboolIObservablefloatIFunctionfloat(object):
    _types = [meta.function((IObservablebool,IObservablefloat,IFunctionfloat,),IObservablefloat)]
    pass


IFunction[IObservablefloat,(IObservablebool,IObservablefloat,IFunctionfloat,)] = IFunctionIObservablefloatIObservableboolIObservablefloatIFunctionfloat


from marketsim.gen._out._iobservable import IObservablebool
from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIObservablefloatIObservableboolIFunctionfloatIObservablefloat(object):
    _types = [meta.function((IObservablebool,IFunctionfloat,IObservablefloat,),IObservablefloat)]
    pass


IFunction[IObservablefloat,(IObservablebool,IFunctionfloat,IObservablefloat,)] = IFunctionIObservablefloatIObservableboolIFunctionfloatIObservablefloat


from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIObservablefloatIFunctionboolIObservablefloatIObservablefloat(object):
    _types = [meta.function((IFunctionbool,IObservablefloat,IObservablefloat,),IObservablefloat)]
    pass


IFunction[IObservablefloat,(IFunctionbool,IObservablefloat,IObservablefloat,)] = IFunctionIObservablefloatIFunctionboolIObservablefloatIObservablefloat


from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
class IFunctionISingleAssetStrategystrstrstrfloatfloat(object):
    _types = [meta.function((str,str,str,float,float,),ISingleAssetStrategy)]
    pass


IFunction[ISingleAssetStrategy,(str,str,str,float,float,)] = IFunctionISingleAssetStrategystrstrstrfloatfloat


class IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat(object):
    _types = [meta.function((IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat,),IFunctionIObservableIOrderIFunctionfloat)]
    pass


IFunction[IFunctionIObservableIOrderIFunctionfloat,(IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat,)] = IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat


from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
class IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSideIFunctionfloat(object):
    _types = [meta.function((IEvent,IFunctionIObservableIOrderIFunctionSide,IFunctionfloat,),ISingleAssetStrategy)]
    pass


IFunction[ISingleAssetStrategy,(IEvent,IFunctionIObservableIOrderIFunctionSide,IFunctionfloat,)] = IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSideIFunctionfloat


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


from marketsim.gen._out._iobservable import IObservablefloat
from marketsim.gen._out._isingleassettrader import ISingleAssetTrader
class IFunctionIObservablefloatfloatIObservablefloatfloatISingleAssetTrader(object):
    _types = [meta.function((float,IObservablefloat,float,ISingleAssetTrader,),IObservablefloat)]
    pass


IFunction[IObservablefloat,(float,IObservablefloat,float,ISingleAssetTrader,)] = IFunctionIObservablefloatfloatIObservablefloatfloatISingleAssetTrader


from marketsim.gen._out._iobservable import IObservablebool
from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIObservablefloatIObservableboolIObservablefloatIObservablefloat(object):
    _types = [meta.function((IObservablebool,IObservablefloat,IObservablefloat,),IObservablefloat)]
    pass


IFunction[IObservablefloat,(IObservablebool,IObservablefloat,IObservablefloat,)] = IFunctionIObservablefloatIObservableboolIObservablefloatIObservablefloat


from marketsim.gen._out._iobservable import IObservablefloat
from marketsim.gen._out._idifferentiable import IDifferentiable
class IFunctionIDifferentiableIObservablefloatfloatfloatfloatfloat(object):
    _types = [meta.function((IObservablefloat,float,float,float,float,),IDifferentiable)]
    pass


IFunction[IDifferentiable,(IObservablefloat,float,float,float,float,)] = IFunctionIDifferentiableIObservablefloatfloatfloatfloatfloat


from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSideIObservablefloat(object):
    _types = [meta.function((IEvent,IFunctionIObservableIOrderIFunctionSide,IObservablefloat,),ISingleAssetStrategy)]
    pass


IFunction[ISingleAssetStrategy,(IEvent,IFunctionIObservableIOrderIFunctionSide,IObservablefloat,)] = IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSideIObservablefloat


from marketsim.gen._out._iobservable import IObservablefloat
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
class IFunctionISingleAssetStrategyIFunctionIObservableIOrderIFunctionfloatfloatIObservablefloat(object):
    _types = [meta.function((IFunctionIObservableIOrderIFunctionfloat,float,IObservablefloat,),ISingleAssetStrategy)]
    pass


IFunction[ISingleAssetStrategy,(IFunctionIObservableIOrderIFunctionfloat,float,IObservablefloat,)] = IFunctionISingleAssetStrategyIFunctionIObservableIOrderIFunctionfloatfloatIObservablefloat


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


from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
class IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSidefloatfloat(object):
    _types = [meta.function((IEvent,IFunctionIObservableIOrderIFunctionSide,float,float,),ISingleAssetStrategy)]
    pass


IFunction[ISingleAssetStrategy,(IEvent,IFunctionIObservableIOrderIFunctionSide,float,float,)] = IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSidefloatfloat


from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionIObservableIOrderIFunctionfloatIObservablefloat(object):
    _types = [meta.function((IFunctionIObservableIOrderIFunctionfloat,IObservablefloat,),IFunctionIObservableIOrderIFunctionfloat)]
    pass


IFunction[IFunctionIObservableIOrderIFunctionfloat,(IFunctionIObservableIOrderIFunctionfloat,IObservablefloat,)] = IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionIObservableIOrderIFunctionfloatIObservablefloat


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


from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSideIObservablefloatfloat(object):
    _types = [meta.function((IEvent,IFunctionIObservableIOrderIFunctionSide,IObservablefloat,float,),ISingleAssetStrategy)]
    pass


IFunction[ISingleAssetStrategy,(IEvent,IFunctionIObservableIOrderIFunctionSide,IObservablefloat,float,)] = IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSideIObservablefloatfloat


from marketsim.gen._out._iobservable import IObservablefloat
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
class IFunctionISingleAssetStrategyIFunctionIObservableIOrderIFunctionfloatfloatIObservablefloatfloat(object):
    _types = [meta.function((IFunctionIObservableIOrderIFunctionfloat,float,IObservablefloat,float,),ISingleAssetStrategy)]
    pass


IFunction[ISingleAssetStrategy,(IFunctionIObservableIOrderIFunctionfloat,float,IObservablefloat,float,)] = IFunctionISingleAssetStrategyIFunctionIObservableIOrderIFunctionfloatfloatIObservablefloatfloat


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


class IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionfloatIFunctionIObservableIOrderIFunctionSideIFunctionfloatIFunctionfloat(object):
    _types = [meta.function((IFunctionIObservableIOrderIFunctionSideIFunctionfloat,IFunctionfloat,),IFunctionIObservableIOrderIFunctionSideIFunctionfloat)]
    pass


IFunction[IFunctionIObservableIOrderIFunctionSideIFunctionfloat,(IFunctionIObservableIOrderIFunctionSideIFunctionfloat,IFunctionfloat,)] = IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionfloatIFunctionIObservableIOrderIFunctionSideIFunctionfloatIFunctionfloat


from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
class IFunctionISingleAssetStrategyISingleAssetStrategyIFunctionIAccountISingleAssetStrategyIFunctionIFunctionfloatIAccount(object):
    _types = [meta.function((ISingleAssetStrategy,IFunctionIAccountISingleAssetStrategy,IFunctionIFunctionfloatIAccount,),ISingleAssetStrategy)]
    pass


IFunction[ISingleAssetStrategy,(ISingleAssetStrategy,IFunctionIAccountISingleAssetStrategy,IFunctionIFunctionfloatIAccount,)] = IFunctionISingleAssetStrategyISingleAssetStrategyIFunctionIAccountISingleAssetStrategyIFunctionIFunctionfloatIAccount


from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim import listOf
class IFunctionISingleAssetStrategylistOfISingleAssetStrategyIFunctionIAccountISingleAssetStrategyIFunctionIFunctionfloatIAccount(object):
    _types = [meta.function((listOf(ISingleAssetStrategy),IFunctionIAccountISingleAssetStrategy,IFunctionIFunctionfloatIAccount,),ISingleAssetStrategy)]
    pass


IFunction[ISingleAssetStrategy,(listOf(ISingleAssetStrategy),IFunctionIAccountISingleAssetStrategy,IFunctionIFunctionfloatIAccount,)] = IFunctionISingleAssetStrategylistOfISingleAssetStrategyIFunctionIAccountISingleAssetStrategyIFunctionIFunctionfloatIAccount


class IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat(object):
    _types = [meta.function((IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide,IFunctionfloat,),IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide)]
    pass


IFunction[IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide,(IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide,IFunctionfloat,)] = IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat


class IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloatIFunctionfloat(object):
    _types = [meta.function((IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat,IFunctionfloat,),IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat)]
    pass


IFunction[IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat,(IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat,IFunctionfloat,)] = IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloatIFunctionfloat


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
