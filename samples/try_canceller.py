import sys
sys.path.append(r'..')

from marketsim import (strategy, trader, orderbook, order, mathutils, Side,
                       scheduler, observable, veusz, registry)

from common import run 

def Canceller(graph, world, books):

    book_A = books['Asset A']
    proxy_A = books['Proxy A']

    price_graph = graph("Price")
     
    assetPrice = observable.AskPrice(book_A)
    
    avg = observable.avg
    
    lp = trader.SASM(book_A, 
                     strategy.LiquidityProviderSide(side = Side.Sell),
                     "LiquidityProvider-")
    
    lp_ex = trader.SASM(book_A, 
                     strategy.LiquidityProviderEx(
                        proxy_A, 
                        orderFactory=order.WithExpiryFactory(
                                expirationDistr=mathutils.constant(1))),
                     "LiquidityProviderEx-")
    
    lp_B = trader.SASM(book_A, 
                     strategy.LiquidityProviderSide(side = Side.Buy),
                     "LiquidityProviderBuy")

    lp_C = trader.SASM(book_A, 
                       strategies = [
                            strategy.LiquidityProviderSide(side = Side.Sell),
                            strategy.Canceller()
                        ],
                       label = "LiquidityProviderWithCanceller")
    
    lp_A = trader.SASM(book_A, 
                       strategy.LiquidityProviderSide(
                            side = Side.Sell,
                            orderFactoryT=order.WithExpiryFactory(
                                expirationDistr=mathutils.constant(10))),
                       "LiquidityProviderWithExpiry")
    
    fv_trader = trader.SASM(book_A, 
                            strategy.FundamentalValue(fundamentalValue = mathutils.constant(1000)), 
                            "fv_1000")
    
    price_graph += [assetPrice,
                    avg(assetPrice)]
    
    amount_graph = graph("amount")
    amount_graph += [observable.VolumeTraded(lp),
                     observable.VolumeTraded(lp_ex),
                     observable.VolumeTraded(lp_C),
                     observable.VolumeTraded(lp_A)]
    
    return [lp_A, lp, lp_C, lp_B, lp_ex, fv_trader], [price_graph, amount_graph]

if __name__ == '__main__':    
    run("canceller", Canceller)
