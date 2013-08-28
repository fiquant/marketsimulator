from marketsim import types, Side, ops, context, combine
from marketsim.types import *

from meta.factory import *

from _market import (Factory                as Market, 
                     FactorySigned          as MarketSigned,
                     SignedVolume_Factory   as SignedVolume_Market,
                     Side_Factory           as Side_Market) 

from _limit import  (Factory                as Limit, 
                     Side_Factory           as Side_Limit, 
                     SidePrice_Factory      as SidePrice_Limit, 
                     Side_Price_Factory     as Side_Price_Limit)

class side:
    Market = Side_Market
    Limit = Side_Limit
    FixedBudget = Side_FixedBudget
    FloatingPrice = Side_FloatingPrice
    Iceberg = Side_Iceberg
    ImmediateOrCancel = Side_ImmediateOrCancel
    Peg = Side_Peg
    StopLoss = Side_StopLoss
    WithExpiry = Side_WithExpiry
    
class sideprice:
    Limit = SidePrice_Limit
    
class side_price:
    Limit = Side_Price_Limit
    
class signedvolume:
    Market = SignedVolume_Market
