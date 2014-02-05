var typeinfo = {
    "marketsim.gen._out.strategy._Arbitrage.Arbitrage_": {
        "castsTo": [
            "marketsim.types.IMultiAssetStrategy"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n<p>It believes that these assets represent a single asset traded on different venues\nOnce an ask at one venue becomes lower than a bid at another venue\nit sends market sell and buy orders in order to exploit this arbitrage possibility</p>\n</div>\n"
    },
    "marketsim.gen._out.math.Cumulative._StdDev.StdDev_Optional__IObservable__Float__": {
        "castsTo": [
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "source": {
                "type": "marketsim.types.IObservable_float"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._curried._sidevolume_WithExpiry.sidevolume_WithExpiry": {
        "castsTo": [
            "marketsim.types.IFunction_IOrderGenerator_IFunction_Tag_IFunction_float"
        ],
        "properties": {
            "expiry": {
                "type": "marketsim.types.IFunction_float"
            },
            "proto": {
                "type": "marketsim.types.IFunction_IOrderGenerator_IFunction_Tag_IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>WithExpiry orders can be viewed as ImmediateOrCancel orders\nwhere cancel order is sent not immediately but after some delay</p>\n</div>\n"
    },
    "marketsim.gen._out.math.macd._MACD.MACD_Optional__IObservable__Float____Optional__Float___Optional__Float_": {
        "castsTo": [
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "x": {
                "type": "marketsim.types.IObservable_float"
            },
            "slow": {
                "type": "_parseFloat"
            },
            "fast": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.weight._IdentityL.IdentityL_Optional_List__Float__": {
        "castsTo": [],
        "properties": {
            "array": {
                "type": {
                    "elementType": "_parseFloat"
                }
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.orderbook.ask._WeightedPrice.WeightedPrice_Optional__IOrderBook___Optional__Float_": {
        "castsTo": [
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "alpha": {
                "type": "_parseFloat"
            },
            "book": {
                "type": "marketsim.types.IOrderBook"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._FixedBudget.FixedBudget": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IObservable_object",
            "marketsim.types.IOrderGenerator"
        ],
        "properties": {
            "side": {
                "type": "marketsim.types.IFunction_Tag"
            },
            "budget": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>Fixed budget order acts like a market order\nbut the volume is implicitly given by a budget available for trades.\nInternally first it sends request.EvalVolumesForBudget\nto estimate volumes and prices of orders to sent and\nthen sends a sequence of order.ImmediateOrCancel to be sure that\ncumulative price of trades to be done won't exceed the given budget.</p>\n</div>\n"
    },
    "marketsim.gen._out.math._Sqrt.Sqrt_Optional__IFunction__Float__": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "x": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math.EW._Avg.Avg_Optional__IObservable__Float____Optional__Float_": {
        "castsTo": [
            "marketsim.types.IDifferentiable",
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "source": {
                "type": "marketsim.types.IObservable_float"
            },
            "alpha": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.weight.trader._trader_Efficiency.trader_Efficiency_": {
        "castsTo": [
            "marketsim.types.IFunction_IFunction_float_IAccount"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.ops._LessEqual.LessEqual_Optional__IFunction__Float____Optional__IFunction__Float__": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_bool",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "y": {
                "type": "marketsim.types.IFunction_float"
            },
            "x": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out._const.const_Optional__Float_": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "x": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.orderbook.bid._Price.Price_Optional__IOrderBook_": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "book": {
                "type": "marketsim.types.IOrderBook"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.orderbook.bid._WeightedPrice.WeightedPrice_Optional__IOrderBook___Optional__Float_": {
        "castsTo": [
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "alpha": {
                "type": "_parseFloat"
            },
            "book": {
                "type": "marketsim.types.IOrderBook"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.account.inner._inner_VirtualMarket.inner_VirtualMarket_": {
        "castsTo": [
            "marketsim.types.IFunction_IAccount_ISingleAssetStrategy"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n<p>how it would be traded by sending request.evalMarketOrder\n(note: orders sent by a strategy wrapped into an adaptive strategy may not come to the market\nbut we want evaluate in any case would it be profitable or not)</p>\n</div>\n"
    },
    "marketsim.gen._out.observable._BreaksAtChanges.BreaksAtChanges_Optional__IFunction__Float__": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "source": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>When <em>source</em> changes it inserts <em>undefined</em> value and then immidiately becomes equal to <em>source</em> value</p>\n</div>\n"
    },
    "marketsim.gen._out.math._Log.Log_Optional__IFunction__Float__": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "x": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.side._Sell.Sell_": {
        "castsTo": [
            "marketsim.types.IFunction_Tag"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._curried._side_price_Limit.side_price_Limit": {
        "castsTo": [
            "marketsim.types.IFunction_IFunction_IOrderGenerator_IFunction_float_IFunction_Tag"
        ],
        "properties": {
            "volume": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>Limit orders ask to buy or sell some asset at price better than some limit price.\nIf a limit order is not competely fulfilled\nit remains in an order book waiting to be matched with another order.</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy.weight.f._f_Clamp0.f_Clamp0_": {
        "castsTo": [
            "marketsim.types.IFunction_IFunction_float_IFunction_float"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math.EW._Var.Var_Optional__IObservable__Float____Optional__Float_": {
        "castsTo": [
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "source": {
                "type": "marketsim.types.IObservable_float"
            },
            "alpha": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.orderbook._WeightedPrice.WeightedPrice_Optional__IOrderQueue___Optional__Float_": {
        "castsTo": [
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "queue": {
                "type": "marketsim.types.IOrderQueue"
            },
            "alpha": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.js.Graph": {
        "castsTo": [
            "marketsim.types.IGraph"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n<p>Generic 2D graph to be rendered by means of javascript libraries</p>\n</div>\n"
    },
    "marketsim.gen._out.order._LimitSigned.LimitSigned": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IObservable_object",
            "marketsim.types.IOrderGenerator"
        ],
        "properties": {
            "signedVolume": {
                "type": "marketsim.types.IFunction_float"
            },
            "price": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>Limit orders ask to buy or sell some asset at price better than some limit price.\nIf a limit order is not competely fulfilled\nit remains in an order book waiting to be matched with another order.</p>\n</div>\n"
    },
    "marketsim.gen._out.order._curried._price_ImmediateOrCancel.price_ImmediateOrCancel": {
        "castsTo": [
            "marketsim.types.IFunction_IOrderGenerator_IFunction_float"
        ],
        "properties": {
            "proto": {
                "type": "marketsim.types.IFunction_IOrderGenerator_IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>Immediate-Or-Cancel order sends an underlying order to the market and\nimmediately sends a cancel request for it.\nIt allows to combine market and limit order behaviour:\nthe order is either executed immediately\nat price equal or better than given one\neither it is cancelled (and consequently never stored in the order queue).</p>\n</div>\n"
    },
    "marketsim.gen._out.order._StopLoss.StopLoss": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IObservable_object",
            "marketsim.types.IOrderGenerator"
        ],
        "properties": {
            "maxloss": {
                "type": "marketsim.types.IFunction_float"
            },
            "proto": {
                "type": "marketsim.types.IOrderGenerator"
            }
        },
        "description": "<div class=\"document\">\n<p>StopLoss order is initialised by an underlying order and a maximal acceptable loss factor.\nIt keeps track of position and balance change induced by trades of the underlying order and\nif losses from keeping the position exceed certain limit (given by maximum loss factor),\nthe meta order clears its position.</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy.weight.f._f_IdentityF.f_IdentityF_": {
        "castsTo": [
            "marketsim.types.IFunction_IFunction_float_IFunction_float"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._curried._side_FloatingPrice.side_FloatingPrice": {
        "castsTo": [
            "marketsim.types.IFunction_IOrderGenerator_IFunction_Tag"
        ],
        "properties": {
            "floatingPrice": {
                "type": "marketsim.types.IObservable_float"
            },
            "proto": {
                "type": "marketsim.types.IFunction_IFunction_IOrderGenerator_IFunction_float_IFunction_Tag"
            }
        },
        "description": "<div class=\"document\">\n<p>Floating price order is initialized by an order having a price and an observable that generates new prices.\nWhen the observable value changes the order is cancelled and\na new order with new price is created and sent to the order book.</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy.weight._Clamp0.Clamp0_Optional__IFunction__Float__": {
        "castsTo": [
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "f": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math.Cumulative._Avg.Avg_Optional__IObservable__Float__": {
        "castsTo": [
            "marketsim.types.IDifferentiable",
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "source": {
                "type": "marketsim.types.IObservable_float"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._FloatingPrice.FloatingPrice": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IObservable_object",
            "marketsim.types.IOrderGenerator"
        ],
        "properties": {
            "floatingPrice": {
                "type": "marketsim.types.IObservable_float"
            },
            "proto": {
                "type": "marketsim.types.IFunction_IOrderGenerator_IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>Floating price order is initialized by an order having a price and an observable that generates new prices.\nWhen the observable value changes the order is cancelled and\na new order with new price is created and sent to the order book.</p>\n</div>\n"
    },
    "marketsim.gen._out.math.Cumulative._RelStdDev.RelStdDev_Optional__IObservable__Float__": {
        "castsTo": [
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "source": {
                "type": "marketsim.types.IObservable_float"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.trader._EfficiencyTrend.EfficiencyTrend_Optional__IAccount___Optional__Float_": {
        "castsTo": [
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "alpha": {
                "type": "_parseFloat"
            },
            "trader": {
                "type": "marketsim.types.IAccount"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.orderbook._Link.Link_Optional__IObservable__Float__": {
        "castsTo": [
            "marketsim.ILink"
        ],
        "properties": {
            "latency": {
                "type": "marketsim.types.IObservable_float"
            }
        },
        "description": "<div class=\"document\">\n<p>(normally between a trader and a market).\nEnsures that sending packets via a link preserves their order.</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy.weight._Unit.Unit__IAccount": {
        "castsTo": [
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "trader": {
                "type": "marketsim.types.IAccount"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math.Cumulative._MinEpsilon.MinEpsilon_Optional__IFunction__Float____Optional__IFunction__Float__": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "source": {
                "type": "marketsim.types.IFunction_float"
            },
            "epsilon": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>It fires updates only if <em>source</em> value becomes less than the old value minus <em>epsilon</em></p>\n</div>\n"
    },
    "marketsim.gen._out.order._MarketSigned.MarketSigned": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IObservable_object",
            "marketsim.types.IOrderGenerator"
        ],
        "properties": {
            "signedVolume": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>Market order intructs buy or sell given volume immediately</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy.weight.trader._trader_Unit.trader_Unit_": {
        "castsTo": [
            "marketsim.types.IFunction_IFunction_float_IAccount"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._curried._side_price_Iceberg.side_price_Iceberg": {
        "castsTo": [
            "marketsim.types.IFunction_IFunction_IOrderGenerator_IFunction_float_IFunction_Tag"
        ],
        "properties": {
            "lotSize": {
                "type": "marketsim.types.IFunction_float"
            },
            "proto": {
                "type": "marketsim.types.IFunction_IFunction_IOrderGenerator_IFunction_float_IFunction_Tag"
            }
        },
        "description": "<div class=\"document\">\n<p>Iceberg order is initialized by an underlying order and a lot size.\nIt sends consequently pieces of the underlying order of size equal or less to the lot size\nthus maximum lot size volume is visible at the market at any moment.</p>\n</div>\n"
    },
    "marketsim.gen._out.order._curried._sidevolume_price_Iceberg.sidevolume_price_Iceberg": {
        "castsTo": [
            "marketsim.types.IFunction_IFunction_IOrderGenerator_IFunction_float_IFunction_Tag_IFunction_float"
        ],
        "properties": {
            "lotSize": {
                "type": "marketsim.types.IFunction_float"
            },
            "proto": {
                "type": "marketsim.types.IFunction_IFunction_IOrderGenerator_IFunction_float_IFunction_Tag_IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>Iceberg order is initialized by an underlying order and a lot size.\nIt sends consequently pieces of the underlying order of size equal or less to the lot size\nthus maximum lot size volume is visible at the market at any moment.</p>\n</div>\n"
    },
    "marketsim.gen._out.math.Moving._Avg.Avg_Optional__IObservable__Float____Optional__Float_": {
        "castsTo": [
            "marketsim.types.IDifferentiable",
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "source": {
                "type": "marketsim.types.IObservable_float"
            },
            "timeframe": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.orderbook._Local.Local_Optional__Float___Optional__Int___Optional__String___Optional_List__ITimeSerie__": {
        "castsTo": [
            "marketsim.types.IOrderBook"
        ],
        "properties": {
            "_digitsToShow": {
                "hidden": true,
                "type": "_parseInt"
            },
            "tickSize": {
                "type": "_parseFloat"
            },
            "name": {
                "type": "identity"
            },
            "timeseries": {
                "type": {
                    "elementType": "marketsim.types.ITimeSerie"
                }
            }
        },
        "description": "<div class=\"document\">\n<p>Maintains two order queues for orders of different sides</p>\n</div>\n"
    },
    "marketsim.gen._out.orderbook._TwoWayLink.TwoWayLink_Optional__ILink___Optional__ILink_": {
        "castsTo": [
            "marketsim.ITwoWayLink"
        ],
        "properties": {
            "down": {
                "type": "marketsim.ILink"
            },
            "up": {
                "type": "marketsim.ILink"
            }
        },
        "description": "<div class=\"document\">\n<p>(normally between a trader and a market).\nEnsures that sending packets via links preserves their order.\nHolds two one-way links in opposite directions.</p>\n</div>\n"
    },
    "marketsim.gen._out.order._curried._sideprice_Peg.sideprice_Peg": {
        "castsTo": [
            "marketsim.types.IFunction_IOrderGenerator_IFunction_Tag_IFunction_float"
        ],
        "properties": {
            "proto": {
                "type": "marketsim.types.IFunction_IFunction_IOrderGenerator_IFunction_float_IFunction_Tag"
            }
        },
        "description": "<div class=\"document\">\n<p>A peg order is a particular case of the floating price order\nwith the price better at one tick than the best price of the order queue.\nIt implies that if several peg orders are sent to the same order queue\nthey start to race until being matched against the counterparty orders.</p>\n</div>\n"
    },
    "marketsim.gen._out.orderbook._LastTradeVolume.LastTradeVolume_Optional__IOrderQueue_": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "queue": {
                "type": "marketsim.types.IOrderQueue"
            }
        },
        "description": "<div class=\"document\">\n<p>Returns None if there haven't been any trades</p>\n</div>\n"
    },
    "marketsim.gen._out.order._curried._signedVolume_MarketSigned.signedVolume_MarketSigned": {
        "castsTo": [
            "marketsim.types.IFunction_IOrderGenerator_IFunction_float"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n<p>Market order intructs buy or sell given volume immediately</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy.weight.array._array_ChooseTheBest.array_ChooseTheBest_": {
        "castsTo": [
            "marketsim.types.IFunction_listOf_listOf"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n<p>having 1 at the index of the maximal element and 0 are at the rest</p>\n</div>\n"
    },
    "marketsim.gen._out.orderbook._CumulativePrice.CumulativePrice_Optional__IOrderBook___Optional__IFunction__Float__": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "depth": {
                "type": "marketsim.types.IFunction_float"
            },
            "book": {
                "type": "marketsim.types.IOrderBook"
            }
        },
        "description": "<div class=\"document\">\n<p>In other words cumulative price corresponds to trader balance change\nif a market order of volume <em>depth</em> is completely matched</p>\n<p>Negative <em>depth</em> correponds to will buy assets\nPositive <em>depth</em> correponds to will sell assets</p>\n</div>\n"
    },
    "marketsim.gen._out.math.Moving._StdDev.StdDev_Optional__IObservable__Float____Optional__Float_": {
        "castsTo": [
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "source": {
                "type": "marketsim.types.IObservable_float"
            },
            "timeframe": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.weight._IdentityF.IdentityF_Optional__IFunction__Float__": {
        "castsTo": [
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "f": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.account._VirtualMarket.VirtualMarket_Optional__ISingleAssetStrategy_": {
        "castsTo": [
            "marketsim.types.IAccount"
        ],
        "properties": {
            "inner": {
                "type": "marketsim.types.ISingleAssetStrategy"
            }
        },
        "description": "<div class=\"document\">\n<p>how it would be traded by sending request.evalMarketOrder\n(note: orders sent by a strategy wrapped into an adaptive strategy may not come to the market\nbut we want evaluate in any case would it be profitable or not)</p>\n</div>\n"
    },
    "marketsim.gen._out.order._curried._price_WithExpiry.price_WithExpiry": {
        "castsTo": [
            "marketsim.types.IFunction_IOrderGenerator_IFunction_float"
        ],
        "properties": {
            "expiry": {
                "type": "marketsim.types.IFunction_float"
            },
            "proto": {
                "type": "marketsim.types.IFunction_IOrderGenerator_IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>WithExpiry orders can be viewed as ImmediateOrCancel orders\nwhere cancel order is sent not immediately but after some delay</p>\n</div>\n"
    },
    "marketsim.gen._out.side._Nothing.Nothing_": {
        "castsTo": [
            "marketsim.types.IFunction_Tag"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math.random._normalvariate.normalvariate": {
        "castsTo": [
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "Mu": {
                "type": "_parseFloat"
            },
            "Sigma": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.orderbook._OfTrader.OfTrader_Optional__IAccount_": {
        "castsTo": [
            "marketsim.types.IOrderBook"
        ],
        "properties": {
            "Trader": {
                "type": "marketsim.types.IAccount"
            }
        },
        "description": "<div class=\"document\">\n<p>May be used only in objects that are held by traders (so it is used in trader properties and strategies)</p>\n</div>\n"
    },
    "marketsim.gen._out.orderbook._LastPrice.LastPrice_Optional__IOrderQueue_": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "queue": {
                "type": "marketsim.types.IOrderQueue"
            }
        },
        "description": "<div class=\"document\">\n<p>Returns None is <em>queue</em> has been always empty</p>\n</div>\n"
    },
    "marketsim.gen._out.order._curried._sidevolume_Peg.sidevolume_Peg": {
        "castsTo": [
            "marketsim.types.IFunction_IOrderGenerator_IFunction_Tag_IFunction_float"
        ],
        "properties": {
            "proto": {
                "type": "marketsim.types.IFunction_IFunction_IOrderGenerator_IFunction_float_IFunction_Tag_IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>A peg order is a particular case of the floating price order\nwith the price better at one tick than the best price of the order queue.\nIt implies that if several peg orders are sent to the same order queue\nthey start to race until being matched against the counterparty orders.</p>\n</div>\n"
    },
    "marketsim.gen._out.order._curried._volume_StopLoss.volume_StopLoss": {
        "castsTo": [
            "marketsim.types.IFunction_IOrderGenerator_IFunction_float"
        ],
        "properties": {
            "maxloss": {
                "type": "marketsim.types.IFunction_float"
            },
            "proto": {
                "type": "marketsim.types.IFunction_IOrderGenerator_IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>StopLoss order is initialised by an underlying order and a maximal acceptable loss factor.\nIt keeps track of position and balance change induced by trades of the underlying order and\nif losses from keeping the position exceed certain limit (given by maximum loss factor),\nthe meta order clears its position.</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy._RSI_linear.RSI_linear_Optional_________Float______IOrderGenerator___Optional__Float___Optional__IObservable__Float____Optional__Float_": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy"
        ],
        "properties": {
            "alpha": {
                "type": "_parseFloat"
            },
            "k": {
                "type": "marketsim.types.IObservable_float"
            },
            "orderFactory": {
                "type": "marketsim.types.IFunction_IOrderGenerator_IFunction_float"
            },
            "timeframe": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out._CandleSticks.CandleSticks_Optional__IObservable__Float____Optional__Float_": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "source": {
                "type": "marketsim.types.IObservable_float"
            },
            "timeframe": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n<p>open/close/min/max price, its average and standard deviation</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy._TradeIfProfitable.TradeIfProfitable_Optional__ISingleAssetStrategy___Optional_Optional__ISingleAssetStrategy______IAccount___Optional__IAccount_____IFunction__Float__": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy"
        ],
        "properties": {
            "performance": {
                "type": "marketsim.types.IFunction_IFunction_float_IAccount"
            },
            "account": {
                "type": "marketsim.types.IFunction_IAccount_ISingleAssetStrategy"
            },
            "inner": {
                "type": "marketsim.types.ISingleAssetStrategy"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._curried._side_Limit.side_Limit": {
        "castsTo": [
            "marketsim.types.IFunction_IOrderGenerator_IFunction_Tag"
        ],
        "properties": {
            "volume": {
                "type": "marketsim.types.IFunction_float"
            },
            "price": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>Limit orders ask to buy or sell some asset at price better than some limit price.\nIf a limit order is not competely fulfilled\nit remains in an order book waiting to be matched with another order.</p>\n</div>\n"
    },
    "marketsim.gen._out.orderbook._Bids.Bids_Optional__IOrderBook_": {
        "castsTo": [
            "marketsim.types.IOrderQueue"
        ],
        "properties": {
            "book": {
                "type": "marketsim.types.IOrderBook"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy._FundamentalValue.FundamentalValue_Optional__IEvent___Optional_________Side______IOrderGenerator___Optional__IFunction__Float__": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy"
        ],
        "properties": {
            "fundamentalValue": {
                "type": "marketsim.types.IFunction_float"
            },
            "eventGen": {
                "type": "marketsim.types.IEvent"
            },
            "orderFactory": {
                "type": "marketsim.types.IFunction_IOrderGenerator_IFunction_Tag"
            }
        },
        "description": "<div class=\"document\">\n<p>(<em>fundamental value</em>) and if the current asset price is lower than the fundamental value\nit starts to buy the asset and if the price is higher it starts to sell the asset.</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy.side._FundamentalValue.FundamentalValue_Optional__IFunction__Float____Optional__IOrderBook_": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_Tag",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "book": {
                "type": "marketsim.types.IOrderBook"
            },
            "fv": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._curried._side_WithExpiry.side_WithExpiry": {
        "castsTo": [
            "marketsim.types.IFunction_IOrderGenerator_IFunction_Tag"
        ],
        "properties": {
            "expiry": {
                "type": "marketsim.types.IFunction_float"
            },
            "proto": {
                "type": "marketsim.types.IFunction_IOrderGenerator_IFunction_Tag"
            }
        },
        "description": "<div class=\"document\">\n<p>WithExpiry orders can be viewed as ImmediateOrCancel orders\nwhere cancel order is sent not immediately but after some delay</p>\n</div>\n"
    },
    "marketsim.gen._out.orderbook._Asks.Asks_Optional__IOrderBook_": {
        "castsTo": [
            "marketsim.types.IOrderQueue"
        ],
        "properties": {
            "book": {
                "type": "marketsim.types.IOrderBook"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._curried._volume_Peg.volume_Peg": {
        "castsTo": [
            "marketsim.types.IFunction_IOrderGenerator_IFunction_float"
        ],
        "properties": {
            "proto": {
                "type": "marketsim.types.IFunction_IFunction_IOrderGenerator_IFunction_float_IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>A peg order is a particular case of the floating price order\nwith the price better at one tick than the best price of the order queue.\nIt implies that if several peg orders are sent to the same order queue\nthey start to race until being matched against the counterparty orders.</p>\n</div>\n"
    },
    "marketsim.gen._out.math.EW._RelStdDev.RelStdDev_Optional__IObservable__Float____Optional__Float_": {
        "castsTo": [
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "source": {
                "type": "marketsim.types.IObservable_float"
            },
            "alpha": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._curried._side_Market.side_Market": {
        "castsTo": [
            "marketsim.types.IFunction_IOrderGenerator_IFunction_Tag"
        ],
        "properties": {
            "volume": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>Market order intructs buy or sell given volume immediately</p>\n</div>\n"
    },
    "marketsim.gen._out.observable._Volume.Volume_Optional__IFunction__Float__": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "x": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>Needed since generic functions aren't implemented yet</p>\n</div>\n"
    },
    "marketsim.gen._out.order._curried._volume_price_Iceberg.volume_price_Iceberg": {
        "castsTo": [
            "marketsim.types.IFunction_IFunction_IOrderGenerator_IFunction_float_IFunction_float"
        ],
        "properties": {
            "lotSize": {
                "type": "marketsim.types.IFunction_float"
            },
            "proto": {
                "type": "marketsim.types.IFunction_IFunction_IOrderGenerator_IFunction_float_IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>Iceberg order is initialized by an underlying order and a lot size.\nIt sends consequently pieces of the underlying order of size equal or less to the lot size\nthus maximum lot size volume is visible at the market at any moment.</p>\n</div>\n"
    },
    "marketsim.gen._out.order._curried._sidevolume_Market.sidevolume_Market": {
        "castsTo": [
            "marketsim.types.IFunction_IOrderGenerator_IFunction_Tag_IFunction_float"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n<p>Market order intructs buy or sell given volume immediately</p>\n</div>\n"
    },
    "marketsim.gen._out.trader._Position.Position_Optional__IAccount_": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "trader": {
                "type": "marketsim.types.IAccount"
            }
        },
        "description": "<div class=\"document\">\n<p>It is negative if trader has sold more assets than has bought and\npositive otherwise</p>\n</div>\n"
    },
    "marketsim.gen._out._constant.constant_Optional__Float_": {
        "castsTo": [
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "x": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.weight._Efficiency.Efficiency__IAccount": {
        "castsTo": [
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "trader": {
                "type": "marketsim.types.IAccount"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.ops._Less.Less_Optional__IFunction__Float____Optional__IFunction__Float__": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_bool",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "y": {
                "type": "marketsim.types.IFunction_float"
            },
            "x": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._WithExpiry.WithExpiry": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IObservable_object",
            "marketsim.types.IOrderGenerator"
        ],
        "properties": {
            "expiry": {
                "type": "marketsim.types.IFunction_float"
            },
            "proto": {
                "type": "marketsim.types.IOrderGenerator"
            }
        },
        "description": "<div class=\"document\">\n<p>WithExpiry orders can be viewed as ImmediateOrCancel orders\nwhere cancel order is sent not immediately but after some delay</p>\n</div>\n"
    },
    "marketsim.gen._out.math.random._uniform.uniform": {
        "castsTo": [
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "High": {
                "type": "_parseFloat"
            },
            "Low": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n<p>Return a random floating point number <em>N</em> such that\n<em>a</em> &lt;= <em>N</em> &lt;= <em>b</em> for <em>a</em> &lt;= <em>b</em> and <em>b</em> &lt;= <em>N</em> &lt;= <em>a</em> for <em>b</em> &lt; <em>a</em>.\nThe end-point value <em>b</em> may or may not be included in the range depending on\nfloating-point rounding in the equation <em>a</em> + (<em>b</em>-<em>a</em>) * <em>random()</em>.</p>\n</div>\n"
    },
    "marketsim.gen._out._IfDefined.IfDefined_Optional__IFunction__Float____Optional__IFunction__Float__": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "elsePart": {
                "type": "marketsim.types.IFunction_float"
            },
            "x": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math._LogReturns.LogReturns_Optional__IObservable__Float____Optional__Float_": {
        "castsTo": [
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "x": {
                "type": "marketsim.types.IObservable_float"
            },
            "timeframe": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.ops._Greater.Greater_Optional__IFunction__Float____Optional__IFunction__Float__": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_bool",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "y": {
                "type": "marketsim.types.IFunction_float"
            },
            "x": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._curried._side_price_WithExpiry.side_price_WithExpiry": {
        "castsTo": [
            "marketsim.types.IFunction_IFunction_IOrderGenerator_IFunction_float_IFunction_Tag"
        ],
        "properties": {
            "expiry": {
                "type": "marketsim.types.IFunction_float"
            },
            "proto": {
                "type": "marketsim.types.IFunction_IFunction_IOrderGenerator_IFunction_float_IFunction_Tag"
            }
        },
        "description": "<div class=\"document\">\n<p>WithExpiry orders can be viewed as ImmediateOrCancel orders\nwhere cancel order is sent not immediately but after some delay</p>\n</div>\n"
    },
    "marketsim.gen._out.order._Market.Market": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IObservable_object",
            "marketsim.types.IOrderGenerator"
        ],
        "properties": {
            "volume": {
                "type": "marketsim.types.IFunction_float"
            },
            "side": {
                "type": "marketsim.types.IFunction_Tag"
            }
        },
        "description": "<div class=\"document\">\n<p>Market order intructs buy or sell given volume immediately</p>\n</div>\n"
    },
    "marketsim.gen._out.orderbook._Remote.Remote_Optional__IOrderBook___Optional__ITwoWayLink___Optional_List__ITimeSerie__": {
        "castsTo": [
            "marketsim.types.IOrderBook"
        ],
        "properties": {
            "link": {
                "type": "marketsim.ITwoWayLink"
            },
            "orderbook": {
                "type": "marketsim.types.IOrderBook"
            },
            "timeseries": {
                "type": {
                    "elementType": "marketsim.types.ITimeSerie"
                }
            }
        },
        "description": "<div class=\"document\">\n<p>to the market by means of a <em>link</em> that introduces some latency in information propagation</p>\n</div>\n"
    },
    "marketsim.gen._out.ops._Mul.Mul_Optional__IFunction__Float____Optional__IFunction__Float__": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "y": {
                "type": "marketsim.types.IFunction_float"
            },
            "x": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._curried._volume_price_ImmediateOrCancel.volume_price_ImmediateOrCancel": {
        "castsTo": [
            "marketsim.types.IFunction_IFunction_IOrderGenerator_IFunction_float_IFunction_float"
        ],
        "properties": {
            "proto": {
                "type": "marketsim.types.IFunction_IFunction_IOrderGenerator_IFunction_float_IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>Immediate-Or-Cancel order sends an underlying order to the market and\nimmediately sends a cancel request for it.\nIt allows to combine market and limit order behaviour:\nthe order is either executed immediately\nat price equal or better than given one\neither it is cancelled (and consequently never stored in the order queue).</p>\n</div>\n"
    },
    "marketsim.gen._out.orderbook._Proxy.Proxy_": {
        "castsTo": [
            "marketsim.types.IOrderBook"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n<p>May be used only in objects held by orderbooks (so it is normally used in orderbook properties)</p>\n</div>\n"
    },
    "marketsim.gen._out.order._curried._volume_FloatingPrice.volume_FloatingPrice": {
        "castsTo": [
            "marketsim.types.IFunction_IOrderGenerator_IFunction_float"
        ],
        "properties": {
            "floatingPrice": {
                "type": "marketsim.types.IObservable_float"
            },
            "proto": {
                "type": "marketsim.types.IFunction_IFunction_IOrderGenerator_IFunction_float_IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>Floating price order is initialized by an order having a price and an observable that generates new prices.\nWhen the observable value changes the order is cancelled and\na new order with new price is created and sent to the order book.</p>\n</div>\n"
    },
    "marketsim.gen._out.order._curried._volume_Limit.volume_Limit": {
        "castsTo": [
            "marketsim.types.IFunction_IOrderGenerator_IFunction_float"
        ],
        "properties": {
            "price": {
                "type": "marketsim.types.IFunction_float"
            },
            "side": {
                "type": "marketsim.types.IFunction_Tag"
            }
        },
        "description": "<div class=\"document\">\n<p>Limit orders ask to buy or sell some asset at price better than some limit price.\nIf a limit order is not competely fulfilled\nit remains in an order book waiting to be matched with another order.</p>\n</div>\n"
    },
    "marketsim.gen._out.orderbook.bid._LastTradePrice.LastTradePrice_Optional__IOrderBook_": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "book": {
                "type": "marketsim.types.IOrderBook"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._curried._sidevolume_Limit.sidevolume_Limit": {
        "castsTo": [
            "marketsim.types.IFunction_IOrderGenerator_IFunction_Tag_IFunction_float"
        ],
        "properties": {
            "price": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>Limit orders ask to buy or sell some asset at price better than some limit price.\nIf a limit order is not competely fulfilled\nit remains in an order book waiting to be matched with another order.</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy._PairTrading.PairTrading_Optional__IEvent___Optional_________Side______IOrderGenerator___Optional__IOrderBook___Optional__Float_": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy"
        ],
        "properties": {
            "bookToDependOn": {
                "type": "marketsim.types.IOrderBook"
            },
            "eventGen": {
                "type": "marketsim.types.IEvent"
            },
            "orderFactory": {
                "type": "marketsim.types.IFunction_IOrderGenerator_IFunction_Tag"
            },
            "factor": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n<p>is completely correlated with price of another asset <em>B</em> and the following relation\nshould be held: <em>PriceA</em> = <em>kPriceB</em>, where <em>k</em> is some factor.\nIt may be considered as a variety of a fundamental value strategy\nwith the exception that it is invoked every the time price of another\nasset <em>B</em> changes.</p>\n</div>\n"
    },
    "marketsim.gen._out.trader._Balance.Balance_Optional__IAccount_": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "trader": {
                "type": "marketsim.types.IAccount"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._curried._side_price_ImmediateOrCancel.side_price_ImmediateOrCancel": {
        "castsTo": [
            "marketsim.types.IFunction_IFunction_IOrderGenerator_IFunction_float_IFunction_Tag"
        ],
        "properties": {
            "proto": {
                "type": "marketsim.types.IFunction_IFunction_IOrderGenerator_IFunction_float_IFunction_Tag"
            }
        },
        "description": "<div class=\"document\">\n<p>Immediate-Or-Cancel order sends an underlying order to the market and\nimmediately sends a cancel request for it.\nIt allows to combine market and limit order behaviour:\nthe order is either executed immediately\nat price equal or better than given one\neither it is cancelled (and consequently never stored in the order queue).</p>\n</div>\n"
    },
    "marketsim.gen._out.orderbook.ask._LastTradeVolume.LastTradeVolume_Optional__IOrderBook_": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "book": {
                "type": "marketsim.types.IOrderBook"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.event._Every.Every_Optional________Float_": {
        "castsTo": [
            "marketsim.types.IEvent"
        ],
        "properties": {
            "intervalFunc": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.orderbook._VolumeLevels.VolumeLevels_Optional__IOrderQueue___Optional__Float___Optional__Int_": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_IVolumeLevels",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "queue": {
                "type": "marketsim.types.IOrderQueue"
            },
            "volumeCount": {
                "type": "_parseInt"
            },
            "volumeDelta": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n<p>Level of volume V is a price at which cumulative volume of better orders is V</p>\n</div>\n"
    },
    "marketsim.gen._out.trader._Efficiency.Efficiency_Optional__IAccount_": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "trader": {
                "type": "marketsim.types.IAccount"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out._false.false_": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_bool",
            "marketsim.types.IObservable_object"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.orderbook.ask._LastPrice.LastPrice_Optional__IOrderBook_": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "book": {
                "type": "marketsim.types.IOrderBook"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out._null.null_": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math._Exp.Exp_Optional__IFunction__Float__": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "x": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math.EW._StdDev.StdDev_Optional__IObservable__Float____Optional__Float_": {
        "castsTo": [
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "source": {
                "type": "marketsim.types.IObservable_float"
            },
            "alpha": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._curried._volume_WithExpiry.volume_WithExpiry": {
        "castsTo": [
            "marketsim.types.IFunction_IOrderGenerator_IFunction_float"
        ],
        "properties": {
            "expiry": {
                "type": "marketsim.types.IFunction_float"
            },
            "proto": {
                "type": "marketsim.types.IFunction_IOrderGenerator_IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>WithExpiry orders can be viewed as ImmediateOrCancel orders\nwhere cancel order is sent not immediately but after some delay</p>\n</div>\n"
    },
    "marketsim.gen._out.order._curried._side_StopLoss.side_StopLoss": {
        "castsTo": [
            "marketsim.types.IFunction_IOrderGenerator_IFunction_Tag"
        ],
        "properties": {
            "maxloss": {
                "type": "marketsim.types.IFunction_float"
            },
            "proto": {
                "type": "marketsim.types.IFunction_IOrderGenerator_IFunction_Tag"
            }
        },
        "description": "<div class=\"document\">\n<p>StopLoss order is initialised by an underlying order and a maximal acceptable loss factor.\nIt keeps track of position and balance change induced by trades of the underlying order and\nif losses from keeping the position exceed certain limit (given by maximum loss factor),\nthe meta order clears its position.</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy.weight.trader._trader_Score.trader_Score_": {
        "castsTo": [
            "marketsim.types.IFunction_IFunction_float_IAccount"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n<p>Returns difference between them.</p>\n<p>TODO: should be UpScore(timeframe, Efficiency(trader)) - DownScore(timeframe, Efficiency(trader))</p>\n</div>\n"
    },
    "marketsim.gen._out.order._curried._side_price_StopLoss.side_price_StopLoss": {
        "castsTo": [
            "marketsim.types.IFunction_IFunction_IOrderGenerator_IFunction_float_IFunction_Tag"
        ],
        "properties": {
            "maxloss": {
                "type": "marketsim.types.IFunction_float"
            },
            "proto": {
                "type": "marketsim.types.IFunction_IFunction_IOrderGenerator_IFunction_float_IFunction_Tag"
            }
        },
        "description": "<div class=\"document\">\n<p>StopLoss order is initialised by an underlying order and a maximal acceptable loss factor.\nIt keeps track of position and balance change induced by trades of the underlying order and\nif losses from keeping the position exceed certain limit (given by maximum loss factor),\nthe meta order clears its position.</p>\n</div>\n"
    },
    "marketsim.gen._out.math.random._triangular.triangular": {
        "castsTo": [
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "High": {
                "type": "_parseFloat"
            },
            "Low": {
                "type": "_parseFloat"
            },
            "Mode": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n<dl class=\"docutils\">\n<dt>Return a random floating point number <em>N</em> such that <em>low</em> &lt;= <em>N</em> &lt;= <em>high</em> and</dt>\n<dd>with the specified <em>mode</em> between those bounds.\nThe <em>low</em> and <em>high</em> bounds default to zero and one.\nThe <em>mode</em> argument defaults to the midpoint between the bounds,\ngiving a symmetric distribution.</dd>\n</dl>\n</div>\n"
    },
    "marketsim.gen._out.veusz._Graph.Graph_Optional__String_": {
        "castsTo": [
            "marketsim.types.IGraph"
        ],
        "properties": {
            "name": {
                "type": "identity"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._curried._sidevolume_price_StopLoss.sidevolume_price_StopLoss": {
        "castsTo": [
            "marketsim.types.IFunction_IFunction_IOrderGenerator_IFunction_float_IFunction_Tag_IFunction_float"
        ],
        "properties": {
            "maxloss": {
                "type": "marketsim.types.IFunction_float"
            },
            "proto": {
                "type": "marketsim.types.IFunction_IFunction_IOrderGenerator_IFunction_float_IFunction_Tag_IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>StopLoss order is initialised by an underlying order and a maximal acceptable loss factor.\nIt keeps track of position and balance change induced by trades of the underlying order and\nif losses from keeping the position exceed certain limit (given by maximum loss factor),\nthe meta order clears its position.</p>\n</div>\n"
    },
    "marketsim.gen._out.math._RSI.RSI_Optional__IOrderBook___Optional__Float___Optional__Float_": {
        "castsTo": [
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "alpha": {
                "type": "_parseFloat"
            },
            "book": {
                "type": "marketsim.types.IOrderBook"
            },
            "timeframe": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._curried._price_Peg.price_Peg": {
        "castsTo": [
            "marketsim.types.IFunction_IOrderGenerator_IFunction_float"
        ],
        "properties": {
            "proto": {
                "type": "marketsim.types.IFunction_IOrderGenerator_IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>A peg order is a particular case of the floating price order\nwith the price better at one tick than the best price of the order queue.\nIt implies that if several peg orders are sent to the same order queue\nthey start to race until being matched against the counterparty orders.</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy._Canceller.Canceller_Optional________Float_": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy"
        ],
        "properties": {
            "cancellationIntervalDistr": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>and in some moments of time it randomly chooses an order and cancels it\nNote: a similar effect can be obtained using order.WithExpiry meta orders</p>\n</div>\n"
    },
    "marketsim.gen._out.observable._Float.Float_Optional__IFunction__Float__": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "x": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>Needed since generic functions aren't implemented yet</p>\n</div>\n"
    },
    "marketsim.gen._out.orderbook.ask._LastTradePrice.LastTradePrice_Optional__IOrderBook_": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "book": {
                "type": "marketsim.types.IOrderBook"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._curried._price_Iceberg.price_Iceberg": {
        "castsTo": [
            "marketsim.types.IFunction_IOrderGenerator_IFunction_float"
        ],
        "properties": {
            "lotSize": {
                "type": "marketsim.types.IFunction_float"
            },
            "proto": {
                "type": "marketsim.types.IFunction_IOrderGenerator_IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>Iceberg order is initialized by an underlying order and a lot size.\nIt sends consequently pieces of the underlying order of size equal or less to the lot size\nthus maximum lot size volume is visible at the market at any moment.</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy._LiquidityProviderSide.LiquidityProviderSide_Optional__IEvent___Optional__________Side__________Float_______IOrderGenerator___Optional________Side___Optional__Float___Optional________Float_": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy"
        ],
        "properties": {
            "priceDistr": {
                "type": "marketsim.types.IFunction_float"
            },
            "initialValue": {
                "type": "_parseFloat"
            },
            "eventGen": {
                "type": "marketsim.types.IEvent"
            },
            "orderFactory": {
                "type": "marketsim.types.IFunction_IOrderGenerator_IFunction_Tag_IFunction_float"
            },
            "side": {
                "type": "marketsim.types.IFunction_Tag"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._curried._side_price_FloatingPrice.side_price_FloatingPrice": {
        "castsTo": [
            "marketsim.types.IFunction_IFunction_IOrderGenerator_IFunction_float_IFunction_Tag"
        ],
        "properties": {
            "floatingPrice": {
                "type": "marketsim.types.IObservable_float"
            },
            "proto": {
                "type": "marketsim.types.IFunction_IFunction_IOrderGenerator_IFunction_float_IFunction_Tag"
            }
        },
        "description": "<div class=\"document\">\n<p>Floating price order is initialized by an order having a price and an observable that generates new prices.\nWhen the observable value changes the order is cancelled and\na new order with new price is created and sent to the order book.</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy.account._Real.Real_Optional__ISingleAssetStrategy_": {
        "castsTo": [
            "marketsim.types.IAccount"
        ],
        "properties": {
            "inner": {
                "type": "marketsim.types.ISingleAssetStrategy"
            }
        },
        "description": "<div class=\"document\">\n<p>how orders sent by the strategy have been actually traded</p>\n</div>\n"
    },
    "marketsim.gen._out.trader._SingleAsset.SingleAsset__IOrderBook__Optional__ISingleAssetStrategy___Optional__String___Optional__Float___Optional__Float___Optional_List__ITimeSerie__": {
        "castsTo": [
            "marketsim.types.IAccount",
            "marketsim.types.ISingleAssetTrader",
            "marketsim.types.ITrader"
        ],
        "properties": {
            "name": {
                "type": "identity"
            },
            "orderBook": {
                "type": "marketsim.types.IOrderBook"
            },
            "strategy": {
                "type": "marketsim.types.ISingleAssetStrategy"
            },
            "amount": {
                "type": "_parseFloat"
            },
            "PnL": {
                "type": "_parseFloat"
            },
            "timeseries": {
                "type": {
                    "elementType": "marketsim.types.ITimeSerie"
                }
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.trader._PendingVolume.PendingVolume_Optional__IAccount_": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "trader": {
                "type": "marketsim.types.IAccount"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.account.inner._inner_Real.inner_Real_": {
        "castsTo": [
            "marketsim.types.IFunction_IAccount_ISingleAssetStrategy"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n<p>how orders sent by the strategy have been actually traded</p>\n</div>\n"
    },
    "marketsim.gen._out.order._curried._volume_Iceberg.volume_Iceberg": {
        "castsTo": [
            "marketsim.types.IFunction_IOrderGenerator_IFunction_float"
        ],
        "properties": {
            "lotSize": {
                "type": "marketsim.types.IFunction_float"
            },
            "proto": {
                "type": "marketsim.types.IFunction_IOrderGenerator_IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>Iceberg order is initialized by an underlying order and a lot size.\nIt sends consequently pieces of the underlying order of size equal or less to the lot size\nthus maximum lot size volume is visible at the market at any moment.</p>\n</div>\n"
    },
    "marketsim.gen._out.math._Derivative.Derivative_Optional__IDifferentiable_": {
        "castsTo": [
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "x": {
                "type": "marketsim.types.IDifferentiable"
            }
        },
        "description": "<div class=\"document\">\n<p><em>x</em> should provide <em>derivative</em> member</p>\n</div>\n"
    },
    "marketsim.gen._out.order._curried._sidevolume_price_WithExpiry.sidevolume_price_WithExpiry": {
        "castsTo": [
            "marketsim.types.IFunction_IFunction_IOrderGenerator_IFunction_float_IFunction_Tag_IFunction_float"
        ],
        "properties": {
            "expiry": {
                "type": "marketsim.types.IFunction_float"
            },
            "proto": {
                "type": "marketsim.types.IFunction_IFunction_IOrderGenerator_IFunction_float_IFunction_Tag_IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>WithExpiry orders can be viewed as ImmediateOrCancel orders\nwhere cancel order is sent not immediately but after some delay</p>\n</div>\n"
    },
    "marketsim.gen._out.math.Moving._Min.Min_Optional__IFunction__Float____Optional__Float_": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "source": {
                "type": "marketsim.types.IFunction_float"
            },
            "timeframe": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.orderbook.bid._LastTradeVolume.LastTradeVolume_Optional__IOrderBook_": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "book": {
                "type": "marketsim.types.IOrderBook"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out._true.true_": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_bool",
            "marketsim.types.IObservable_object"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.orderbook._TickSize.TickSize_Optional__IOrderBook_": {
        "castsTo": [
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "book": {
                "type": "marketsim.types.IOrderBook"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._curried._sidevolume_price_ImmediateOrCancel.sidevolume_price_ImmediateOrCancel": {
        "castsTo": [
            "marketsim.types.IFunction_IFunction_IOrderGenerator_IFunction_float_IFunction_Tag_IFunction_float"
        ],
        "properties": {
            "proto": {
                "type": "marketsim.types.IFunction_IFunction_IOrderGenerator_IFunction_float_IFunction_Tag_IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>Immediate-Or-Cancel order sends an underlying order to the market and\nimmediately sends a cancel request for it.\nIt allows to combine market and limit order behaviour:\nthe order is either executed immediately\nat price equal or better than given one\neither it is cancelled (and consequently never stored in the order queue).</p>\n</div>\n"
    },
    "marketsim.gen._out.orderbook._SafeSidePrice.SafeSidePrice_Optional__IOrderQueue___Optional__IFunction__Float__": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "queue": {
                "type": "marketsim.types.IOrderQueue"
            },
            "defaultValue": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>and <em>defaultValue</em> if there haven't been any trades</p>\n</div>\n"
    },
    "marketsim.gen._out.math._UpMovements.UpMovements_Optional__IObservable__Float____Optional__Float_": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "source": {
                "type": "marketsim.types.IObservable_float"
            },
            "timeframe": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math.random._gammavariate.gammavariate": {
        "castsTo": [
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "Alpha": {
                "type": "_parseFloat"
            },
            "Beta": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n<p>Conditions on the parameters are \u03b1 &gt; 0 and \u03b2 &gt; 0.</p>\n<p>The probability distribution function is:</p>\n<pre class=\"literal-block\">\n          x ** (alpha - 1) * math.exp(-x / beta)\npdf(x) =  --------------------------------------\n             math.gamma(alpha) * beta ** alpha\n</pre>\n</div>\n"
    },
    "marketsim.gen._out.orderbook.ask._Price.Price_Optional__IOrderBook_": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "book": {
                "type": "marketsim.types.IOrderBook"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._curried._volume_price_WithExpiry.volume_price_WithExpiry": {
        "castsTo": [
            "marketsim.types.IFunction_IFunction_IOrderGenerator_IFunction_float_IFunction_float"
        ],
        "properties": {
            "expiry": {
                "type": "marketsim.types.IFunction_float"
            },
            "proto": {
                "type": "marketsim.types.IFunction_IFunction_IOrderGenerator_IFunction_float_IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>WithExpiry orders can be viewed as ImmediateOrCancel orders\nwhere cancel order is sent not immediately but after some delay</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy.position._DesiredPosition.DesiredPosition_Optional__IObservable__Float____Optional__ISingleAssetTrader_": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "desiredPosition": {
                "type": "marketsim.types.IObservable_float"
            },
            "trader": {
                "type": "marketsim.types.ISingleAssetTrader"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.price._LiquidityProvider.LiquidityProvider_Optional________Side___Optional__Float___Optional________Float___Optional__IOrderBook_": {
        "castsTo": [
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "priceDistr": {
                "type": "marketsim.types.IFunction_float"
            },
            "initialValue": {
                "type": "_parseFloat"
            },
            "side": {
                "type": "marketsim.types.IFunction_Tag"
            },
            "book": {
                "type": "marketsim.types.IOrderBook"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.scheduler.Scheduler": {
        "castsTo": [],
        "properties": {
            "currentTime": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n<p>Keeps a set of events to be launched in the future</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy._ChooseTheBest.ChooseTheBest_Optional_List__ISingleAssetStrategy____Optional_Optional__ISingleAssetStrategy______IAccount___Optional__IAccount_____IFunction__Float__": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy"
        ],
        "properties": {
            "strategies": {
                "type": {
                    "elementType": "marketsim.types.ISingleAssetStrategy"
                }
            },
            "account": {
                "type": "marketsim.types.IFunction_IAccount_ISingleAssetStrategy"
            },
            "performance": {
                "type": "marketsim.types.IFunction_IFunction_float_IAccount"
            }
        },
        "description": "<div class=\"document\">\n<p>In some moments of time the most effective strategy\nis chosen and made running; other strategies are suspended.\nIt can be considered as a particular case for MultiArmedBandit strategy with\n<em>corrector</em> parameter set to <em>chooseTheBest</em></p>\n</div>\n"
    },
    "marketsim.gen._out.ops._Add.Add_Optional__IFunction__Float____Optional__IFunction__Float__": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "y": {
                "type": "marketsim.types.IFunction_float"
            },
            "x": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math._Lagged.Lagged_Optional__IObservable__Float____Optional__Float_": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "source": {
                "type": "marketsim.types.IObservable_float"
            },
            "timeframe": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.position._RSI_linear.RSI_linear_Optional__Float___Optional__IObservable__Float____Optional__Float___Optional__ISingleAssetTrader_": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "alpha": {
                "type": "_parseFloat"
            },
            "k": {
                "type": "marketsim.types.IObservable_float"
            },
            "trader": {
                "type": "marketsim.types.ISingleAssetTrader"
            },
            "timeframe": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.weight.array._array_IdentityL.array_IdentityL_": {
        "castsTo": [
            "marketsim.types.IFunction_listOf_listOf"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math.macd._Histogram.Histogram_Optional__IObservable__Float____Optional__Float___Optional__Float___Optional__Float___Optional__Float_": {
        "castsTo": [
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "x": {
                "type": "marketsim.types.IObservable_float"
            },
            "step": {
                "type": "_parseFloat"
            },
            "slow": {
                "type": "_parseFloat"
            },
            "fast": {
                "type": "_parseFloat"
            },
            "timeframe": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math._Atan.Atan_Optional__IFunction__Float__": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "x": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.trader._RoughPnL.RoughPnL_Optional__IAccount_": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "trader": {
                "type": "marketsim.types.IAccount"
            }
        },
        "description": "<div class=\"document\">\n<p>It takes into account only the best price of the order queue</p>\n</div>\n"
    },
    "marketsim.gen._out.order._curried._volume_price_FloatingPrice.volume_price_FloatingPrice": {
        "castsTo": [
            "marketsim.types.IFunction_IFunction_IOrderGenerator_IFunction_float_IFunction_float"
        ],
        "properties": {
            "floatingPrice": {
                "type": "marketsim.types.IObservable_float"
            },
            "proto": {
                "type": "marketsim.types.IFunction_IFunction_IOrderGenerator_IFunction_float_IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>Floating price order is initialized by an order having a price and an observable that generates new prices.\nWhen the observable value changes the order is cancelled and\na new order with new price is created and sent to the order book.</p>\n</div>\n"
    },
    "marketsim.gen._out.math._RandomWalk.RandomWalk_Optional__Float___Optional________Float___Optional________Float___Optional__String_": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "deltaDistr": {
                "type": "marketsim.types.IFunction_float"
            },
            "initialValue": {
                "type": "_parseFloat"
            },
            "intervalDistr": {
                "type": "marketsim.types.IFunction_float"
            },
            "name": {
                "type": "identity"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.observable._Quote.Quote_Optional__String___Optional__String___Optional__String_": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "ticker": {
                "type": "identity"
            },
            "start": {
                "type": "identity"
            },
            "end": {
                "type": "identity"
            }
        },
        "description": "<div class=\"document\">\n<p>and follows the price in scale 1 model unit of time = 1 real day</p>\n</div>\n"
    },
    "marketsim.gen._out.observable._OnEveryDt.OnEveryDt_Optional__Float___Optional__IFunction__Float__": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "x": {
                "type": "marketsim.types.IFunction_float"
            },
            "dt": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._curried._side_price_Peg.side_price_Peg": {
        "castsTo": [
            "marketsim.types.IFunction_IFunction_IOrderGenerator_IFunction_float_IFunction_Tag"
        ],
        "properties": {
            "proto": {
                "type": "marketsim.types.IFunction_IFunction_IOrderGenerator_IFunction_float_IFunction_Tag"
            }
        },
        "description": "<div class=\"document\">\n<p>A peg order is a particular case of the floating price order\nwith the price better at one tick than the best price of the order queue.\nIt implies that if several peg orders are sent to the same order queue\nthey start to race until being matched against the counterparty orders.</p>\n</div>\n"
    },
    "marketsim.gen._out.orderbook._MidPrice.MidPrice_Optional__IOrderBook_": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "book": {
                "type": "marketsim.types.IOrderBook"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math.random._betavariate.betavariate": {
        "castsTo": [
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "Alpha": {
                "type": "_parseFloat"
            },
            "Beta": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n<p>Conditions on the parameters are \u03b1 &gt; 0 and \u03b2 &gt; 0.\nReturned values range between 0 and 1.</p>\n</div>\n"
    },
    "marketsim.gen._out.order._curried._sidevolume_ImmediateOrCancel.sidevolume_ImmediateOrCancel": {
        "castsTo": [
            "marketsim.types.IFunction_IOrderGenerator_IFunction_Tag_IFunction_float"
        ],
        "properties": {
            "proto": {
                "type": "marketsim.types.IFunction_IOrderGenerator_IFunction_Tag_IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>Immediate-Or-Cancel order sends an underlying order to the market and\nimmediately sends a cancel request for it.\nIt allows to combine market and limit order behaviour:\nthe order is either executed immediately\nat price equal or better than given one\neither it is cancelled (and consequently never stored in the order queue).</p>\n</div>\n"
    },
    "marketsim.gen._out.trader._SingleProxy.SingleProxy_": {
        "castsTo": [
            "marketsim.types.IAccount",
            "marketsim.types.ISingleAssetTrader",
            "marketsim.types.ITrader"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n<p>(normally it is used to define trader properties and strategies)</p>\n</div>\n"
    },
    "marketsim.gen._out.math.random._weibullvariate.weibullvariate": {
        "castsTo": [
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "Alpha": {
                "type": "_parseFloat"
            },
            "Beta": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.side._Buy.Buy_": {
        "castsTo": [
            "marketsim.types.IFunction_Tag"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.side._MeanReversion.MeanReversion_Optional__Float___Optional__IOrderBook_": {
        "castsTo": [
            "marketsim.types.IFunction_Tag"
        ],
        "properties": {
            "alpha": {
                "type": "_parseFloat"
            },
            "book": {
                "type": "marketsim.types.IOrderBook"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math.random._expovariate.expovariate": {
        "castsTo": [
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "Lambda": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n<p>Returned values range from 0 to positive infinity</p>\n</div>\n"
    },
    "marketsim.gen._out.orderbook._LastTradePrice.LastTradePrice_Optional__IOrderQueue_": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "queue": {
                "type": "marketsim.types.IOrderQueue"
            }
        },
        "description": "<div class=\"document\">\n<p>Returns None if there haven't been any trades</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy._Combine.Combine_Optional__ISingleAssetStrategy___Optional__ISingleAssetStrategy_": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy"
        ],
        "properties": {
            "A": {
                "type": "marketsim.types.ISingleAssetStrategy"
            },
            "B": {
                "type": "marketsim.types.ISingleAssetStrategy"
            }
        },
        "description": "<div class=\"document\">\n<p>Can be considered as a particular case of Array strategy</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy._Bollinger_linear.Bollinger_linear_Optional_________Float______IOrderGenerator___Optional__Float___Optional__IObservable__Float__": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy"
        ],
        "properties": {
            "alpha": {
                "type": "_parseFloat"
            },
            "k": {
                "type": "marketsim.types.IObservable_float"
            },
            "orderFactory": {
                "type": "marketsim.types.IFunction_IOrderGenerator_IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math.Moving._RelStdDev.RelStdDev_Optional__IObservable__Float____Optional__Float_": {
        "castsTo": [
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "source": {
                "type": "marketsim.types.IObservable_float"
            },
            "timeframe": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.ops._GreaterEqual.GreaterEqual_Optional__IFunction__Float____Optional__IFunction__Float__": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_bool",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "y": {
                "type": "marketsim.types.IFunction_float"
            },
            "x": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._curried._sidevolume_FloatingPrice.sidevolume_FloatingPrice": {
        "castsTo": [
            "marketsim.types.IFunction_IOrderGenerator_IFunction_Tag_IFunction_float"
        ],
        "properties": {
            "floatingPrice": {
                "type": "marketsim.types.IObservable_float"
            },
            "proto": {
                "type": "marketsim.types.IFunction_IFunction_IOrderGenerator_IFunction_float_IFunction_Tag_IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>Floating price order is initialized by an order having a price and an observable that generates new prices.\nWhen the observable value changes the order is cancelled and\na new order with new price is created and sent to the order book.</p>\n</div>\n"
    },
    "marketsim.gen._out.math.random._paretovariate.paretovariate": {
        "castsTo": [
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "Alpha": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math._Max.Max_Optional__IFunction__Float____Optional__IFunction__Float__": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "y": {
                "type": "marketsim.types.IFunction_float"
            },
            "x": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>If <em>x</em> or/and <em>y</em> are observables, <em>Min</em> is also observable</p>\n</div>\n"
    },
    "marketsim.gen._out.ops._Sub.Sub_Optional__IFunction__Float____Optional__IFunction__Float__": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "y": {
                "type": "marketsim.types.IFunction_float"
            },
            "x": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._curried._sidevolume_price_Peg.sidevolume_price_Peg": {
        "castsTo": [
            "marketsim.types.IFunction_IFunction_IOrderGenerator_IFunction_float_IFunction_Tag_IFunction_float"
        ],
        "properties": {
            "proto": {
                "type": "marketsim.types.IFunction_IFunction_IOrderGenerator_IFunction_float_IFunction_Tag_IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>A peg order is a particular case of the floating price order\nwith the price better at one tick than the best price of the order queue.\nIt implies that if several peg orders are sent to the same order queue\nthey start to race until being matched against the counterparty orders.</p>\n</div>\n"
    },
    "marketsim.gen._out.order._curried._sideprice_FloatingPrice.sideprice_FloatingPrice": {
        "castsTo": [
            "marketsim.types.IFunction_IOrderGenerator_IFunction_Tag_IFunction_float"
        ],
        "properties": {
            "floatingPrice": {
                "type": "marketsim.types.IObservable_float"
            },
            "proto": {
                "type": "marketsim.types.IFunction_IFunction_IOrderGenerator_IFunction_float_IFunction_Tag"
            }
        },
        "description": "<div class=\"document\">\n<p>Floating price order is initialized by an order having a price and an observable that generates new prices.\nWhen the observable value changes the order is cancelled and\na new order with new price is created and sent to the order book.</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy.side._Signal.Signal_Optional__IFunction__Float____Optional__Float_": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_Tag",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "threshold": {
                "type": "_parseFloat"
            },
            "signal": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math._Pow.Pow_Optional__IFunction__Float____Optional__IFunction__Float__": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "base": {
                "type": "marketsim.types.IFunction_float"
            },
            "power": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>Exceptional cases follow Annex F of the C99 standard as far as possible.\nIn particular, <tt class=\"docutils literal\">pow(1.0, x)</tt> and <tt class=\"docutils literal\">pow(x, 0.0)</tt> always return 1.0,\neven when <em>x</em> is a zero or a NaN.\nIf both <em>x</em> and <em>y</em> are finite, <em>x</em> is negative, and <em>y</em> is not an integer then\n<tt class=\"docutils literal\">pow(x, y)</tt> is undefined, and raises <tt class=\"docutils literal\">ValueError</tt>.</p>\n</div>\n"
    },
    "marketsim.gen._out.order._curried._sidevolume_Iceberg.sidevolume_Iceberg": {
        "castsTo": [
            "marketsim.types.IFunction_IOrderGenerator_IFunction_Tag_IFunction_float"
        ],
        "properties": {
            "lotSize": {
                "type": "marketsim.types.IFunction_float"
            },
            "proto": {
                "type": "marketsim.types.IFunction_IOrderGenerator_IFunction_Tag_IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>Iceberg order is initialized by an underlying order and a lot size.\nIt sends consequently pieces of the underlying order of size equal or less to the lot size\nthus maximum lot size volume is visible at the market at any moment.</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy._TrendFollower.TrendFollower_Optional__IEvent___Optional_________Side______IOrderGenerator___Optional__Float___Optional__Float_": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy"
        ],
        "properties": {
            "threshold": {
                "type": "_parseFloat"
            },
            "ewma_alpha": {
                "type": "_parseFloat"
            },
            "eventGen": {
                "type": "marketsim.types.IEvent"
            },
            "orderFactory": {
                "type": "marketsim.types.IFunction_IOrderGenerator_IFunction_Tag"
            }
        },
        "description": "<div class=\"document\">\n<p>where the <em>signal</em> is a trend of the asset.\nUnder trend we understand the first derivative of some moving average of asset prices.\nIf the derivative is positive, the trader buys; if negative - it sells.\nSince moving average is a continuously changing signal, we check its\nderivative at moments of time given by <em>eventGen</em>.</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy._Empty.Empty_": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy._Array.Array_Optional_List__ISingleAssetStrategy__": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy"
        ],
        "properties": {
            "strategies": {
                "type": {
                    "elementType": "marketsim.types.ISingleAssetStrategy"
                }
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._curried._volume_Market.volume_Market": {
        "castsTo": [
            "marketsim.types.IFunction_IOrderGenerator_IFunction_float"
        ],
        "properties": {
            "side": {
                "type": "marketsim.types.IFunction_Tag"
            }
        },
        "description": "<div class=\"document\">\n<p>Market order intructs buy or sell given volume immediately</p>\n</div>\n"
    },
    "marketsim.gen._out.math.Moving._Var.Var_Optional__IObservable__Float____Optional__Float_": {
        "castsTo": [
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "source": {
                "type": "marketsim.types.IObservable_float"
            },
            "timeframe": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._curried._volume_price_Limit.volume_price_Limit": {
        "castsTo": [
            "marketsim.types.IFunction_IFunction_IOrderGenerator_IFunction_float_IFunction_float"
        ],
        "properties": {
            "side": {
                "type": "marketsim.types.IFunction_Tag"
            }
        },
        "description": "<div class=\"document\">\n<p>Limit orders ask to buy or sell some asset at price better than some limit price.\nIf a limit order is not competely fulfilled\nit remains in an order book waiting to be matched with another order.</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy._MarketData.MarketData_Optional__String___Optional__String___Optional__String___Optional__Float___Optional__Float_": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy"
        ],
        "properties": {
            "volume": {
                "type": "_parseFloat"
            },
            "start": {
                "type": "identity"
            },
            "end": {
                "type": "identity"
            },
            "ticker": {
                "type": "identity"
            },
            "delta": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n<p>by creating large volume orders for the given price.</p>\n<p>Every time step of 1 in the simulation corresponds to a 1 day in the market data.</p>\n<p>At each time step the previous Limit Buy/Sell orders are cancelled and new ones\nare created based on the next price of the market data.</p>\n</div>\n"
    },
    "marketsim.gen._out.order._curried._side_FixedBudget.side_FixedBudget": {
        "castsTo": [
            "marketsim.types.IFunction_IOrderGenerator_IFunction_Tag"
        ],
        "properties": {
            "budget": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>Fixed budget order acts like a market order\nbut the volume is implicitly given by a budget available for trades.\nInternally first it sends request.EvalVolumesForBudget\nto estimate volumes and prices of orders to sent and\nthen sends a sequence of order.ImmediateOrCancel to be sure that\ncumulative price of trades to be done won't exceed the given budget.</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy.weight._EfficiencyTrend.EfficiencyTrend__IAccount__Optional__Float_": {
        "castsTo": [
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "alpha": {
                "type": "_parseFloat"
            },
            "trader": {
                "type": "marketsim.types.IAccount"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.ops._Equal.Equal_Optional__IFunction__Float____Optional__IFunction__Float__": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_bool",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "y": {
                "type": "marketsim.types.IFunction_float"
            },
            "x": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.observable._Price.Price_Optional__IFunction__Float__": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "x": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>Needed since generic functions aren't implemented yet</p>\n</div>\n"
    },
    "marketsim.gen._out.math._Sqr.Sqr_Optional__IFunction__Float__": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "x": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.side._PairTrading.PairTrading_Optional__IOrderBook___Optional__Float___Optional__IOrderBook_": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_Tag",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "book": {
                "type": "marketsim.types.IOrderBook"
            },
            "bookToDependOn": {
                "type": "marketsim.types.IOrderBook"
            },
            "factor": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._curried._price_FloatingPrice.price_FloatingPrice": {
        "castsTo": [
            "marketsim.types.IFunction_IOrderGenerator_IFunction_float"
        ],
        "properties": {
            "floatingPrice": {
                "type": "marketsim.types.IObservable_float"
            },
            "proto": {
                "type": "marketsim.types.IFunction_IOrderGenerator_IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>Floating price order is initialized by an order having a price and an observable that generates new prices.\nWhen the observable value changes the order is cancelled and\na new order with new price is created and sent to the order book.</p>\n</div>\n"
    },
    "marketsim.gen._out.order._curried._volume_price_Peg.volume_price_Peg": {
        "castsTo": [
            "marketsim.types.IFunction_IFunction_IOrderGenerator_IFunction_float_IFunction_float"
        ],
        "properties": {
            "proto": {
                "type": "marketsim.types.IFunction_IFunction_IOrderGenerator_IFunction_float_IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>A peg order is a particular case of the floating price order\nwith the price better at one tick than the best price of the order queue.\nIt implies that if several peg orders are sent to the same order queue\nthey start to race until being matched against the counterparty orders.</p>\n</div>\n"
    },
    "marketsim.gen._out.ops._Div.Div_Optional__IFunction__Float____Optional__IFunction__Float__": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "y": {
                "type": "marketsim.types.IFunction_float"
            },
            "x": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy._MarketMaker.MarketMaker_Optional__Float___Optional__Float_": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy"
        ],
        "properties": {
            "volume": {
                "type": "_parseFloat"
            },
            "delta": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out._volumeLevels.volumeLevels__IFunction__IVolumeLevels___Optional__IGraph___Optional__Int___Optional__Int___Optional_List__Float____Optional__Int_": {
        "castsTo": [
            "marketsim.types.ITimeSerie"
        ],
        "properties": {
            "_digitsToShow": {
                "hidden": true,
                "type": "_parseInt"
            },
            "graph": {
                "type": "marketsim.types.IGraph"
            },
            "_smooth": {
                "hidden": true,
                "type": "_parseInt"
            },
            "source": {
                "type": "marketsim.types.IFunction_IVolumeLevels"
            },
            "_isBuy": {
                "hidden": true,
                "type": "_parseInt"
            },
            "_volumes": {
                "hidden": true,
                "type": {
                    "elementType": "_parseFloat"
                }
            }
        },
        "description": "<div class=\"document\">\n<p>Level of volume V is a price at which cumulative volume of better orders is V</p>\n</div>\n"
    },
    "marketsim.gen._out.order._curried._price_StopLoss.price_StopLoss": {
        "castsTo": [
            "marketsim.types.IFunction_IOrderGenerator_IFunction_float"
        ],
        "properties": {
            "maxloss": {
                "type": "marketsim.types.IFunction_float"
            },
            "proto": {
                "type": "marketsim.types.IFunction_IOrderGenerator_IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>StopLoss order is initialised by an underlying order and a maximal acceptable loss factor.\nIt keeps track of position and balance change induced by trades of the underlying order and\nif losses from keeping the position exceed certain limit (given by maximum loss factor),\nthe meta order clears its position.</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy._Signal.Signal_Optional__IEvent___Optional_________Side______IOrderGenerator___Optional__IFunction__Float____Optional__Float_": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy"
        ],
        "properties": {
            "threshold": {
                "type": "_parseFloat"
            },
            "signal": {
                "type": "marketsim.types.IFunction_float"
            },
            "eventGen": {
                "type": "marketsim.types.IEvent"
            },
            "orderFactory": {
                "type": "marketsim.types.IFunction_IOrderGenerator_IFunction_Tag"
            }
        },
        "description": "<div class=\"document\">\n<p>and when the signal becomes more than some threshold the strategy starts to buy.\nWhen the signal gets lower than -threshold the strategy starts to sell.</p>\n</div>\n"
    },
    "marketsim.gen._out.math.Moving._Max.Max_Optional__IFunction__Float____Optional__Float_": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "source": {
                "type": "marketsim.types.IFunction_float"
            },
            "timeframe": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.trader._MultiAsset.MultiAsset_Optional_List__ISingleAssetTrader____Optional__IMultiAssetStrategy___Optional__String___Optional__Float___Optional_List__ITimeSerie__": {
        "castsTo": [
            "marketsim.types.ITrader"
        ],
        "properties": {
            "traders": {
                "type": {
                    "elementType": "marketsim.types.ISingleAssetTrader"
                }
            },
            "strategy": {
                "type": "marketsim.types.IMultiAssetStrategy"
            },
            "PnL": {
                "type": "_parseFloat"
            },
            "timeseries": {
                "type": {
                    "elementType": "marketsim.types.ITimeSerie"
                }
            },
            "name": {
                "type": "identity"
            }
        },
        "description": "<div class=\"document\">\n<p>It can be considered as a composition of single asset traders and multi asset strategies\nAt the moment there is no way to instruct a multi asset strategy to trade only on subset of the assets</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy._RSIbis.RSIbis_Optional__IEvent___Optional_________Side______IOrderGenerator___Optional__Float___Optional__Float___Optional__Float_": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy"
        ],
        "properties": {
            "threshold": {
                "type": "_parseFloat"
            },
            "alpha": {
                "type": "_parseFloat"
            },
            "eventGen": {
                "type": "marketsim.types.IEvent"
            },
            "orderFactory": {
                "type": "marketsim.types.IFunction_IOrderGenerator_IFunction_Tag"
            },
            "timeframe": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n<p>and starts to buy when RSI is greater than 50 + <em>threshold</em>\nand sells when RSI is less than 50 - <em>thresold</em></p>\n</div>\n"
    },
    "marketsim.gen._out.orderbook._Spread.Spread_Optional__IOrderBook_": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "book": {
                "type": "marketsim.types.IOrderBook"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.orderbook._Queue.Queue_Optional__IOrderBook___Optional________Side_": {
        "castsTo": [
            "marketsim.types.IOrderQueue"
        ],
        "properties": {
            "book": {
                "type": "marketsim.types.IOrderBook"
            },
            "side": {
                "type": "marketsim.types.IFunction_Tag"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.weight.f._f_AtanPow.f_AtanPow_Optional__Float_": {
        "castsTo": [
            "marketsim.types.IFunction_IFunction_float_IFunction_float"
        ],
        "properties": {
            "base": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._curried._sideprice_Iceberg.sideprice_Iceberg": {
        "castsTo": [
            "marketsim.types.IFunction_IOrderGenerator_IFunction_Tag_IFunction_float"
        ],
        "properties": {
            "lotSize": {
                "type": "marketsim.types.IFunction_float"
            },
            "proto": {
                "type": "marketsim.types.IFunction_IOrderGenerator_IFunction_Tag_IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>Iceberg order is initialized by an underlying order and a lot size.\nIt sends consequently pieces of the underlying order of size equal or less to the lot size\nthus maximum lot size volume is visible at the market at any moment.</p>\n</div>\n"
    },
    "marketsim.gen._out.order._curried._sideprice_WithExpiry.sideprice_WithExpiry": {
        "castsTo": [
            "marketsim.types.IFunction_IOrderGenerator_IFunction_Tag_IFunction_float"
        ],
        "properties": {
            "expiry": {
                "type": "marketsim.types.IFunction_float"
            },
            "proto": {
                "type": "marketsim.types.IFunction_IOrderGenerator_IFunction_Tag_IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>WithExpiry orders can be viewed as ImmediateOrCancel orders\nwhere cancel order is sent not immediately but after some delay</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy._CrossingAverages.CrossingAverages_Optional__IEvent___Optional_________Side______IOrderGenerator___Optional__Float___Optional__Float___Optional__Float_": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy"
        ],
        "properties": {
            "threshold": {
                "type": "_parseFloat"
            },
            "ewma_alpha_2": {
                "type": "_parseFloat"
            },
            "eventGen": {
                "type": "marketsim.types.IEvent"
            },
            "orderFactory": {
                "type": "marketsim.types.IFunction_IOrderGenerator_IFunction_Tag"
            },
            "ewma_alpha_1": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n<p>with different parameters ('slow' and 'fast' averages) and when\nthe first is greater than the second one it buys,\nwhen the first is lower than the second one it sells</p>\n</div>\n"
    },
    "marketsim.gen._out.order._curried._sidevolume_StopLoss.sidevolume_StopLoss": {
        "castsTo": [
            "marketsim.types.IFunction_IOrderGenerator_IFunction_Tag_IFunction_float"
        ],
        "properties": {
            "maxloss": {
                "type": "marketsim.types.IFunction_float"
            },
            "proto": {
                "type": "marketsim.types.IFunction_IOrderGenerator_IFunction_Tag_IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>StopLoss order is initialised by an underlying order and a maximal acceptable loss factor.\nIt keeps track of position and balance change induced by trades of the underlying order and\nif losses from keeping the position exceed certain limit (given by maximum loss factor),\nthe meta order clears its position.</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy.side._Noise.Noise_Optional________Float_": {
        "castsTo": [
            "marketsim.types.IFunction_Tag"
        ],
        "properties": {
            "side_distribution": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.registry.Simulation": {
        "castsTo": [],
        "properties": {
            "traders": {
                "type": {
                    "elementType": "marketsim.types.ITrader"
                }
            },
            "graphs": {
                "type": {
                    "elementType": "marketsim.types.IGraph"
                }
            },
            "orderbooks": {
                "type": {
                    "elementType": "marketsim.types.IOrderBook"
                }
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.observable._Side.Side_Optional__IFunction__Side__": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_Tag",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "x": {
                "type": "marketsim.types.IFunction_Tag"
            }
        },
        "description": "<div class=\"document\">\n<p>Needed since generic functions aren't implemented yet</p>\n</div>\n"
    },
    "marketsim.gen._out.order._curried._side_Peg.side_Peg": {
        "castsTo": [
            "marketsim.types.IFunction_IOrderGenerator_IFunction_Tag"
        ],
        "properties": {
            "proto": {
                "type": "marketsim.types.IFunction_IFunction_IOrderGenerator_IFunction_float_IFunction_Tag"
            }
        },
        "description": "<div class=\"document\">\n<p>A peg order is a particular case of the floating price order\nwith the price better at one tick than the best price of the order queue.\nIt implies that if several peg orders are sent to the same order queue\nthey start to race until being matched against the counterparty orders.</p>\n</div>\n"
    },
    "marketsim.gen._out.math._DownMovements.DownMovements_Optional__IObservable__Float____Optional__Float_": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "source": {
                "type": "marketsim.types.IObservable_float"
            },
            "timeframe": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._curried._sideprice_Limit.sideprice_Limit": {
        "castsTo": [
            "marketsim.types.IFunction_IOrderGenerator_IFunction_Tag_IFunction_float"
        ],
        "properties": {
            "volume": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>Limit orders ask to buy or sell some asset at price better than some limit price.\nIf a limit order is not competely fulfilled\nit remains in an order book waiting to be matched with another order.</p>\n</div>\n"
    },
    "marketsim.gen._out.order._curried._volume_ImmediateOrCancel.volume_ImmediateOrCancel": {
        "castsTo": [
            "marketsim.types.IFunction_IOrderGenerator_IFunction_float"
        ],
        "properties": {
            "proto": {
                "type": "marketsim.types.IFunction_IOrderGenerator_IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>Immediate-Or-Cancel order sends an underlying order to the market and\nimmediately sends a cancel request for it.\nIt allows to combine market and limit order behaviour:\nthe order is either executed immediately\nat price equal or better than given one\neither it is cancelled (and consequently never stored in the order queue).</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy._Suspendable.Suspendable_Optional__ISingleAssetStrategy___Optional__IFunction__Boolean__": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy"
        ],
        "properties": {
            "predicate": {
                "type": "marketsim.types.IFunction_bool"
            },
            "inner": {
                "type": "marketsim.types.ISingleAssetStrategy"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.side._TrendFollower.TrendFollower_Optional__Float___Optional__Float___Optional__IOrderBook_": {
        "castsTo": [
            "marketsim.types.IFunction_Tag"
        ],
        "properties": {
            "threshold": {
                "type": "_parseFloat"
            },
            "alpha": {
                "type": "_parseFloat"
            },
            "book": {
                "type": "marketsim.types.IOrderBook"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.orderbook.bid._LastPrice.LastPrice_Optional__IOrderBook_": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "book": {
                "type": "marketsim.types.IOrderBook"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.ops._Negate.Negate_Optional__IFunction__Float__": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "x": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math.rsi._Raw.Raw_Optional__IObservable__Float____Optional__Float___Optional__Float_": {
        "castsTo": [
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "source": {
                "type": "marketsim.types.IObservable_float"
            },
            "timeframe": {
                "type": "_parseFloat"
            },
            "alpha": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math._Min.Min_Optional__IFunction__Float____Optional__IFunction__Float__": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "y": {
                "type": "marketsim.types.IFunction_float"
            },
            "x": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>If <em>x</em> or/and <em>y</em> are observables, <em>Min</em> is also observable</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy._MeanReversion.MeanReversion_Optional__IEvent___Optional_________Side______IOrderGenerator___Optional__Float_": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy"
        ],
        "properties": {
            "ewma_alpha": {
                "type": "_parseFloat"
            },
            "eventGen": {
                "type": "marketsim.types.IEvent"
            },
            "orderFactory": {
                "type": "marketsim.types.IFunction_IOrderGenerator_IFunction_Tag"
            }
        },
        "description": "<div class=\"document\">\n<p>It estimates this average using some functional and\nif the current asset price is lower than the average\nit buys the asset and if the price is higher it sells the asset.</p>\n</div>\n"
    },
    "marketsim.gen._out.math.Cumulative._Var.Var_Optional__IObservable__Float__": {
        "castsTo": [
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "source": {
                "type": "marketsim.types.IObservable_float"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy._MultiArmedBandit.MultiArmedBandit_Optional_List__ISingleAssetStrategy____Optional_Optional__ISingleAssetStrategy______IAccount___Optional__IAccount_____IFunction__Float____Optional_Optional__IFunction__Float_______IFunction__Float____Optional_Optional_List__Float______List__Float__": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy"
        ],
        "properties": {
            "corrector": {
                "type": "marketsim.types.IFunction_listOf_listOf"
            },
            "strategies": {
                "type": {
                    "elementType": "marketsim.types.ISingleAssetStrategy"
                }
            },
            "account": {
                "type": "marketsim.types.IFunction_IAccount_ISingleAssetStrategy"
            },
            "normalizer": {
                "type": "marketsim.types.IFunction_IFunction_float_IFunction_float"
            },
            "weight": {
                "type": "marketsim.types.IFunction_IFunction_float_IAccount"
            }
        },
        "description": "<div class=\"document\">\n<p>In some moments of time the efficiency of the strategies is evaluated\nThese efficiencies are mapped into weights using <em>weight</em> and <em>normilizer</em>\nfunctions per every strategy and <em>corrector</em> for the whole collection of weights\nThese weights are used to choose randomly a strategy to run for the next quant of time.\nAll other strategies are suspended</p>\n</div>\n"
    },
    "marketsim.gen._out.order._Iceberg.Iceberg": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IObservable_object",
            "marketsim.types.IOrderGenerator"
        ],
        "properties": {
            "lotSize": {
                "type": "marketsim.types.IFunction_float"
            },
            "proto": {
                "type": "marketsim.types.IOrderGenerator"
            }
        },
        "description": "<div class=\"document\">\n<p>Iceberg order is initialized by an underlying order and a lot size.\nIt sends consequently pieces of the underlying order of size equal or less to the lot size\nthus maximum lot size volume is visible at the market at any moment.</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy.weight._AtanPow.AtanPow_Optional__IFunction__Float____Optional__Float_": {
        "castsTo": [
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "base": {
                "type": "_parseFloat"
            },
            "f": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._Peg.Peg": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IObservable_object",
            "marketsim.types.IOrderGenerator"
        ],
        "properties": {
            "proto": {
                "type": "marketsim.types.IFunction_IOrderGenerator_IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>A peg order is a particular case of the floating price order\nwith the price better at one tick than the best price of the order queue.\nIt implies that if several peg orders are sent to the same order queue\nthey start to race until being matched against the counterparty orders.</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy.weight._Score.Score__IAccount": {
        "castsTo": [
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "trader": {
                "type": "marketsim.types.IAccount"
            }
        },
        "description": "<div class=\"document\">\n<p>Returns difference between them.</p>\n<p>TODO: should be UpScore(timeframe, Efficiency(trader)) - DownScore(timeframe, Efficiency(trader))</p>\n</div>\n"
    },
    "marketsim.gen._out.order._curried._signedVolume_LimitSigned.signedVolume_LimitSigned": {
        "castsTo": [
            "marketsim.types.IFunction_IOrderGenerator_IFunction_float"
        ],
        "properties": {
            "price": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>Limit orders ask to buy or sell some asset at price better than some limit price.\nIf a limit order is not competely fulfilled\nit remains in an order book waiting to be matched with another order.</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy._Noise.Noise_Optional__IEvent___Optional_________Side______IOrderGenerator_": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy"
        ],
        "properties": {
            "eventGen": {
                "type": "marketsim.types.IEvent"
            },
            "orderFactory": {
                "type": "marketsim.types.IFunction_IOrderGenerator_IFunction_Tag"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math.macd._Signal.Signal_Optional__IObservable__Float____Optional__Float___Optional__Float___Optional__Float___Optional__Float_": {
        "castsTo": [
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "x": {
                "type": "marketsim.types.IObservable_float"
            },
            "step": {
                "type": "_parseFloat"
            },
            "slow": {
                "type": "_parseFloat"
            },
            "fast": {
                "type": "_parseFloat"
            },
            "timeframe": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.ops._NotEqual.NotEqual_Optional__IFunction__Float____Optional__IFunction__Float__": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_bool",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "y": {
                "type": "marketsim.types.IFunction_float"
            },
            "x": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._ImmediateOrCancel.ImmediateOrCancel": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IObservable_object",
            "marketsim.types.IOrderGenerator"
        ],
        "properties": {
            "proto": {
                "type": "marketsim.types.IOrderGenerator"
            }
        },
        "description": "<div class=\"document\">\n<p>Immediate-Or-Cancel order sends an underlying order to the market and\nimmediately sends a cancel request for it.\nIt allows to combine market and limit order behaviour:\nthe order is either executed immediately\nat price equal or better than given one\neither it is cancelled (and consequently never stored in the order queue).</p>\n</div>\n"
    },
    "marketsim.gen._out.event._After.After_Optional__IFunction__Float__": {
        "castsTo": [
            "marketsim.types.IEvent"
        ],
        "properties": {
            "delay": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._curried._sidevolume_price_Limit.sidevolume_price_Limit": {
        "castsTo": [
            "marketsim.types.IFunction_IFunction_IOrderGenerator_IFunction_float_IFunction_Tag_IFunction_float"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n<p>Limit orders ask to buy or sell some asset at price better than some limit price.\nIf a limit order is not competely fulfilled\nit remains in an order book waiting to be matched with another order.</p>\n</div>\n"
    },
    "marketsim.gen._out.order._curried._sidevolume_price_FloatingPrice.sidevolume_price_FloatingPrice": {
        "castsTo": [
            "marketsim.types.IFunction_IFunction_IOrderGenerator_IFunction_float_IFunction_Tag_IFunction_float"
        ],
        "properties": {
            "floatingPrice": {
                "type": "marketsim.types.IObservable_float"
            },
            "proto": {
                "type": "marketsim.types.IFunction_IFunction_IOrderGenerator_IFunction_float_IFunction_Tag_IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>Floating price order is initialized by an order having a price and an observable that generates new prices.\nWhen the observable value changes the order is cancelled and\na new order with new price is created and sent to the order book.</p>\n</div>\n"
    },
    "marketsim.gen._out.math.random._vonmisesvariate.vonmisesvariate": {
        "castsTo": [
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "Mu": {
                "type": "_parseFloat"
            },
            "Kappa": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._curried._sideprice_ImmediateOrCancel.sideprice_ImmediateOrCancel": {
        "castsTo": [
            "marketsim.types.IFunction_IOrderGenerator_IFunction_Tag_IFunction_float"
        ],
        "properties": {
            "proto": {
                "type": "marketsim.types.IFunction_IOrderGenerator_IFunction_Tag_IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>Immediate-Or-Cancel order sends an underlying order to the market and\nimmediately sends a cancel request for it.\nIt allows to combine market and limit order behaviour:\nthe order is either executed immediately\nat price equal or better than given one\neither it is cancelled (and consequently never stored in the order queue).</p>\n</div>\n"
    },
    "marketsim.gen._out.order._curried._side_ImmediateOrCancel.side_ImmediateOrCancel": {
        "castsTo": [
            "marketsim.types.IFunction_IOrderGenerator_IFunction_Tag"
        ],
        "properties": {
            "proto": {
                "type": "marketsim.types.IFunction_IOrderGenerator_IFunction_Tag"
            }
        },
        "description": "<div class=\"document\">\n<p>Immediate-Or-Cancel order sends an underlying order to the market and\nimmediately sends a cancel request for it.\nIt allows to combine market and limit order behaviour:\nthe order is either executed immediately\nat price equal or better than given one\neither it is cancelled (and consequently never stored in the order queue).</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy.weight.trader._trader_EfficiencyTrend.trader_EfficiencyTrend_Optional__Float_": {
        "castsTo": [
            "marketsim.types.IFunction_IFunction_float_IAccount"
        ],
        "properties": {
            "alpha": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.orderbook._NaiveCumulativePrice.NaiveCumulativePrice_Optional__IOrderBook___Optional__IFunction__Float__": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "depth": {
                "type": "marketsim.types.IFunction_float"
            },
            "book": {
                "type": "marketsim.types.IOrderBook"
            }
        },
        "description": "<div class=\"document\">\n<p>by taking into account prices only for the best order</p>\n<p>Negative <em>depth</em> correponds to will buy assets\nPositive <em>depth</em> correponds to will sell assets</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy._LiquidityProvider.LiquidityProvider_Optional__IEvent___Optional__________Side__________Float_______IOrderGenerator___Optional__Float___Optional________Float_": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy"
        ],
        "properties": {
            "priceDistr": {
                "type": "marketsim.types.IFunction_float"
            },
            "initialValue": {
                "type": "_parseFloat"
            },
            "eventGen": {
                "type": "marketsim.types.IEvent"
            },
            "orderFactory": {
                "type": "marketsim.types.IFunction_IOrderGenerator_IFunction_Tag_IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.weight._ChooseTheBest.ChooseTheBest_Optional_List__Float__": {
        "castsTo": [],
        "properties": {
            "array": {
                "type": {
                    "elementType": "_parseFloat"
                }
            }
        },
        "description": "<div class=\"document\">\n<p>having 1 at the index of the maximal element and 0 are at the rest</p>\n</div>\n"
    },
    "marketsim.gen._out.math.random._lognormvariate.lognormvariate": {
        "castsTo": [
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "Mu": {
                "type": "_parseFloat"
            },
            "Sigma": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n<dl class=\"docutils\">\n<dt>If you take the natural logarithm of this distribution,</dt>\n<dd>you'll get a normal distribution with mean \u03bc and standard deviation \u03c3.\n\u03bc can have any value, and \u03c3 must be greater than zero.</dd>\n</dl>\n</div>\n"
    },
    "marketsim.gen._out.order._curried._side_Iceberg.side_Iceberg": {
        "castsTo": [
            "marketsim.types.IFunction_IOrderGenerator_IFunction_Tag"
        ],
        "properties": {
            "lotSize": {
                "type": "marketsim.types.IFunction_float"
            },
            "proto": {
                "type": "marketsim.types.IFunction_IOrderGenerator_IFunction_Tag"
            }
        },
        "description": "<div class=\"document\">\n<p>Iceberg order is initialized by an underlying order and a lot size.\nIt sends consequently pieces of the underlying order of size equal or less to the lot size\nthus maximum lot size volume is visible at the market at any moment.</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy.position._Bollinger_linear.Bollinger_linear_Optional__Float___Optional__IObservable__Float____Optional__ISingleAssetTrader_": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "alpha": {
                "type": "_parseFloat"
            },
            "k": {
                "type": "marketsim.types.IObservable_float"
            },
            "trader": {
                "type": "marketsim.types.ISingleAssetTrader"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math.Cumulative._MaxEpsilon.MaxEpsilon_Optional__IFunction__Float____Optional__IFunction__Float__": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "source": {
                "type": "marketsim.types.IFunction_float"
            },
            "epsilon": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>It fires updates only if <em>source</em> value becomes greater than the old value plus <em>epsilon</em></p>\n</div>\n"
    },
    "marketsim.gen._out.order._curried._volume_price_StopLoss.volume_price_StopLoss": {
        "castsTo": [
            "marketsim.types.IFunction_IFunction_IOrderGenerator_IFunction_float_IFunction_float"
        ],
        "properties": {
            "maxloss": {
                "type": "marketsim.types.IFunction_float"
            },
            "proto": {
                "type": "marketsim.types.IFunction_IFunction_IOrderGenerator_IFunction_float_IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>StopLoss order is initialised by an underlying order and a maximal acceptable loss factor.\nIt keeps track of position and balance change induced by trades of the underlying order and\nif losses from keeping the position exceed certain limit (given by maximum loss factor),\nthe meta order clears its position.</p>\n</div>\n"
    },
    "marketsim.gen._out._TimeSerie.TimeSerie_Optional__IObservable_Any____Optional__IGraph___Optional__Int___Optional__Int_": {
        "castsTo": [
            "marketsim.types.ITimeSerie"
        ],
        "properties": {
            "_digitsToShow": {
                "hidden": true,
                "type": "_parseInt"
            },
            "source": {
                "type": "marketsim.types.IObservable_object"
            },
            "_smooth": {
                "hidden": true,
                "type": "_parseInt"
            },
            "graph": {
                "type": "marketsim.types.IGraph"
            }
        },
        "description": "<div class=\"document\">\n<p>Used to specify what data should be collected about order books and traders</p>\n</div>\n"
    },
    "marketsim.gen._out.ops._Condition_Float.Condition_Float_Optional__IFunction__Boolean____Optional__IFunction__Float____Optional__IFunction__Float__": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "ifpart": {
                "type": "marketsim.types.IFunction_float"
            },
            "elsepart": {
                "type": "marketsim.types.IFunction_float"
            },
            "cond": {
                "type": "marketsim.types.IFunction_bool"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._Limit.Limit": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IObservable_object",
            "marketsim.types.IOrderGenerator"
        ],
        "properties": {
            "volume": {
                "type": "marketsim.types.IFunction_float"
            },
            "price": {
                "type": "marketsim.types.IFunction_float"
            },
            "side": {
                "type": "marketsim.types.IFunction_Tag"
            }
        },
        "description": "<div class=\"document\">\n<p>Limit orders ask to buy or sell some asset at price better than some limit price.\nIf a limit order is not competely fulfilled\nit remains in an order book waiting to be matched with another order.</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy.side._CrossingAverages.CrossingAverages_Optional__Float___Optional__Float___Optional__Float___Optional__IOrderBook_": {
        "castsTo": [
            "marketsim.types.IFunction_Tag"
        ],
        "properties": {
            "threshold": {
                "type": "_parseFloat"
            },
            "book": {
                "type": "marketsim.types.IOrderBook"
            },
            "alpha_2": {
                "type": "_parseFloat"
            },
            "alpha_1": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.ops._Condition_Side.Condition_Side_Optional__IFunction__Boolean____Optional________Side___Optional________Side_": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_Tag",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "ifpart": {
                "type": "marketsim.types.IFunction_Tag"
            },
            "elsepart": {
                "type": "marketsim.types.IFunction_Tag"
            },
            "cond": {
                "type": "marketsim.types.IFunction_bool"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.orderbook._BestPrice.BestPrice_Optional__IOrderQueue_": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "queue": {
                "type": "marketsim.types.IOrderQueue"
            }
        },
        "description": "<div class=\"document\">\n<p>Returns None is <em>queue</em> is empty</p>\n</div>\n"
    },
    "marketsim.gen._out.order._curried._sideprice_StopLoss.sideprice_StopLoss": {
        "castsTo": [
            "marketsim.types.IFunction_IOrderGenerator_IFunction_Tag_IFunction_float"
        ],
        "properties": {
            "maxloss": {
                "type": "marketsim.types.IFunction_float"
            },
            "proto": {
                "type": "marketsim.types.IFunction_IOrderGenerator_IFunction_Tag_IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>StopLoss order is initialised by an underlying order and a maximal acceptable loss factor.\nIt keeps track of position and balance change induced by trades of the underlying order and\nif losses from keeping the position exceed certain limit (given by maximum loss factor),\nthe meta order clears its position.</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy._Generic.Generic_Optional__IOrderGenerator___Optional__IEvent_": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy"
        ],
        "properties": {
            "orderFactory": {
                "type": "marketsim.types.IOrderGenerator"
            },
            "eventGen": {
                "type": "marketsim.types.IEvent"
            }
        },
        "description": "<div class=\"document\">\n<p>creates an order via <em>orderFactory</em> and sends the order to the market using its trader</p>\n</div>\n"
    },
    "marketsim.gen._out.order._curried._price_Limit.price_Limit": {
        "castsTo": [
            "marketsim.types.IFunction_IOrderGenerator_IFunction_float"
        ],
        "properties": {
            "volume": {
                "type": "marketsim.types.IFunction_float"
            },
            "side": {
                "type": "marketsim.types.IFunction_Tag"
            }
        },
        "description": "<div class=\"document\">\n<p>Limit orders ask to buy or sell some asset at price better than some limit price.\nIf a limit order is not competely fulfilled\nit remains in an order book waiting to be matched with another order.</p>\n</div>\n"
    }
}
var interfaces = [
    [
        "_parseInt",
        []
    ],
    [
        "marketsim.types.IObservable_object",
        [
            "marketsim.gen._out.math.Moving._Min.Min_Optional__IFunction__Float____Optional__Float_",
            "marketsim.gen._out._CandleSticks.CandleSticks_Optional__IObservable__Float____Optional__Float_",
            "marketsim.gen._out._true.true_",
            "marketsim.gen._out.math.Moving._Max.Max_Optional__IFunction__Float____Optional__Float_",
            "marketsim.gen._out.ops._Add.Add_Optional__IFunction__Float____Optional__IFunction__Float__",
            "marketsim.gen._out.orderbook._SafeSidePrice.SafeSidePrice_Optional__IOrderQueue___Optional__IFunction__Float__",
            "marketsim.gen._out.orderbook._Spread.Spread_Optional__IOrderBook_",
            "marketsim.gen._out.math._UpMovements.UpMovements_Optional__IObservable__Float____Optional__Float_",
            "marketsim.gen._out.observable._Volume.Volume_Optional__IFunction__Float__",
            "marketsim.gen._out.strategy.side._FundamentalValue.FundamentalValue_Optional__IFunction__Float____Optional__IOrderBook_",
            "marketsim.gen._out.order._FixedBudget.FixedBudget",
            "marketsim.gen._out.strategy.position._DesiredPosition.DesiredPosition_Optional__IObservable__Float____Optional__ISingleAssetTrader_",
            "marketsim.gen._out.math._Sqrt.Sqrt_Optional__IFunction__Float__",
            "marketsim.gen._out.strategy.side._Signal.Signal_Optional__IFunction__Float____Optional__Float_",
            "marketsim.gen._out.observable._Side.Side_Optional__IFunction__Side__",
            "marketsim.gen._out.order._Limit.Limit",
            "marketsim.gen._out.ops._LessEqual.LessEqual_Optional__IFunction__Float____Optional__IFunction__Float__",
            "marketsim.gen._out._const.const_Optional__Float_",
            "marketsim.gen._out.math._Lagged.Lagged_Optional__IObservable__Float____Optional__Float_",
            "marketsim.gen._out.strategy.position._RSI_linear.RSI_linear_Optional__Float___Optional__IObservable__Float____Optional__Float___Optional__ISingleAssetTrader_",
            "marketsim.gen._out.math._DownMovements.DownMovements_Optional__IObservable__Float____Optional__Float_",
            "marketsim.gen._out.math._Atan.Atan_Optional__IFunction__Float__",
            "marketsim.gen._out.observable._BreaksAtChanges.BreaksAtChanges_Optional__IFunction__Float__",
            "marketsim.gen._out.math._Log.Log_Optional__IFunction__Float__",
            "marketsim.gen._out.order._Iceberg.Iceberg",
            "marketsim.gen._out.orderbook._LastPrice.LastPrice_Optional__IOrderQueue_",
            "marketsim.gen._out.math._RandomWalk.RandomWalk_Optional__Float___Optional________Float___Optional________Float___Optional__String_",
            "marketsim.gen._out.ops._Less.Less_Optional__IFunction__Float____Optional__IFunction__Float__",
            "marketsim.gen._out.orderbook.bid._LastPrice.LastPrice_Optional__IOrderBook_",
            "marketsim.gen._out.observable._OnEveryDt.OnEveryDt_Optional__Float___Optional__IFunction__Float__",
            "marketsim.gen._out.ops._Negate.Negate_Optional__IFunction__Float__",
            "marketsim.gen._out.orderbook.ask._Price.Price_Optional__IOrderBook_",
            "marketsim.gen._out.orderbook._MidPrice.MidPrice_Optional__IOrderBook_",
            "marketsim.gen._out.math._Min.Min_Optional__IFunction__Float____Optional__IFunction__Float__",
            "marketsim.gen._out.ops._Greater.Greater_Optional__IFunction__Float____Optional__IFunction__Float__",
            "marketsim.gen._out.trader._RoughPnL.RoughPnL_Optional__IAccount_",
            "marketsim.gen._out.order._StopLoss.StopLoss",
            "marketsim.gen._out.math.Cumulative._MinEpsilon.MinEpsilon_Optional__IFunction__Float____Optional__IFunction__Float__",
            "marketsim.gen._out.order._Market.Market",
            "marketsim.gen._out.orderbook.bid._Price.Price_Optional__IOrderBook_",
            "marketsim.gen._out.order._Peg.Peg",
            "marketsim.gen._out.ops._NotEqual.NotEqual_Optional__IFunction__Float____Optional__IFunction__Float__",
            "marketsim.gen._out.strategy.side._PairTrading.PairTrading_Optional__IOrderBook___Optional__Float___Optional__IOrderBook_",
            "marketsim.gen._out.orderbook.ask._LastTradePrice.LastTradePrice_Optional__IOrderBook_",
            "marketsim.gen._out.order._FloatingPrice.FloatingPrice",
            "marketsim.gen._out.orderbook.bid._LastTradePrice.LastTradePrice_Optional__IOrderBook_",
            "marketsim.gen._out.orderbook._LastTradePrice.LastTradePrice_Optional__IOrderQueue_",
            "marketsim.gen._out.observable._Price.Price_Optional__IFunction__Float__",
            "marketsim.gen._out.orderbook.ask._LastPrice.LastPrice_Optional__IOrderBook_",
            "marketsim.gen._out._IfDefined.IfDefined_Optional__IFunction__Float____Optional__IFunction__Float__",
            "marketsim.gen._out.ops._Mul.Mul_Optional__IFunction__Float____Optional__IFunction__Float__",
            "marketsim.gen._out.trader._Balance.Balance_Optional__IAccount_",
            "marketsim.gen._out.ops._GreaterEqual.GreaterEqual_Optional__IFunction__Float____Optional__IFunction__Float__",
            "marketsim.gen._out.order._ImmediateOrCancel.ImmediateOrCancel",
            "marketsim.gen._out.orderbook.ask._LastTradeVolume.LastTradeVolume_Optional__IOrderBook_",
            "marketsim.gen._out.math._Max.Max_Optional__IFunction__Float____Optional__IFunction__Float__",
            "marketsim.gen._out.ops._Sub.Sub_Optional__IFunction__Float____Optional__IFunction__Float__",
            "marketsim.gen._out.trader._Efficiency.Efficiency_Optional__IAccount_",
            "marketsim.gen._out._false.false_",
            "marketsim.gen._out.order._LimitSigned.LimitSigned",
            "marketsim.gen._out._null.null_",
            "marketsim.gen._out.math._Pow.Pow_Optional__IFunction__Float____Optional__IFunction__Float__",
            "marketsim.gen._out.math._Exp.Exp_Optional__IFunction__Float__",
            "marketsim.gen._out.orderbook._NaiveCumulativePrice.NaiveCumulativePrice_Optional__IOrderBook___Optional__IFunction__Float__",
            "marketsim.gen._out.observable._Quote.Quote_Optional__String___Optional__String___Optional__String_",
            "marketsim.gen._out.orderbook.bid._LastTradeVolume.LastTradeVolume_Optional__IOrderBook_",
            "marketsim.gen._out.orderbook._LastTradeVolume.LastTradeVolume_Optional__IOrderQueue_",
            "marketsim.gen._out.trader._PendingVolume.PendingVolume_Optional__IAccount_",
            "marketsim.gen._out.order._WithExpiry.WithExpiry",
            "marketsim.gen._out.orderbook._CumulativePrice.CumulativePrice_Optional__IOrderBook___Optional__IFunction__Float__",
            "marketsim.gen._out.orderbook._VolumeLevels.VolumeLevels_Optional__IOrderQueue___Optional__Float___Optional__Int_",
            "marketsim.gen._out.strategy.position._Bollinger_linear.Bollinger_linear_Optional__Float___Optional__IObservable__Float____Optional__ISingleAssetTrader_",
            "marketsim.gen._out.math.Cumulative._MaxEpsilon.MaxEpsilon_Optional__IFunction__Float____Optional__IFunction__Float__",
            "marketsim.gen._out.observable._Float.Float_Optional__IFunction__Float__",
            "marketsim.gen._out.ops._Condition_Float.Condition_Float_Optional__IFunction__Boolean____Optional__IFunction__Float____Optional__IFunction__Float__",
            "marketsim.gen._out.ops._Equal.Equal_Optional__IFunction__Float____Optional__IFunction__Float__",
            "marketsim.gen._out.trader._Position.Position_Optional__IAccount_",
            "marketsim.gen._out.order._MarketSigned.MarketSigned",
            "marketsim.gen._out.math._Sqr.Sqr_Optional__IFunction__Float__",
            "marketsim.gen._out.ops._Condition_Side.Condition_Side_Optional__IFunction__Boolean____Optional________Side___Optional________Side_",
            "marketsim.gen._out.orderbook._BestPrice.BestPrice_Optional__IOrderQueue_",
            "marketsim.gen._out.ops._Div.Div_Optional__IFunction__Float____Optional__IFunction__Float__"
        ]
    ],
    [
        {
            "elementType": "_parseFloat"
        },
        []
    ],
    [
        "marketsim.types.ISingleAssetTrader",
        [
            "marketsim.gen._out.trader._SingleProxy.SingleProxy_",
            "marketsim.gen._out.trader._SingleAsset.SingleAsset__IOrderBook__Optional__ISingleAssetStrategy___Optional__String___Optional__Float___Optional__Float___Optional_List__ITimeSerie__"
        ]
    ],
    [
        "marketsim.types.IFunction_IFunction_IOrderGenerator_IFunction_float_IFunction_Tag_IFunction_float",
        [
            "marketsim.gen._out.order._curried._sidevolume_price_ImmediateOrCancel.sidevolume_price_ImmediateOrCancel",
            "marketsim.gen._out.order._curried._sidevolume_price_Iceberg.sidevolume_price_Iceberg",
            "marketsim.gen._out.order._curried._sidevolume_price_StopLoss.sidevolume_price_StopLoss",
            "marketsim.gen._out.order._curried._sidevolume_price_Limit.sidevolume_price_Limit",
            "marketsim.gen._out.order._curried._sidevolume_price_Peg.sidevolume_price_Peg",
            "marketsim.gen._out.order._curried._sidevolume_price_FloatingPrice.sidevolume_price_FloatingPrice",
            "marketsim.gen._out.order._curried._sidevolume_price_WithExpiry.sidevolume_price_WithExpiry"
        ]
    ],
    [
        "marketsim.types.ISingleAssetStrategy",
        [
            "marketsim.gen._out.strategy._MarketMaker.MarketMaker_Optional__Float___Optional__Float_",
            "marketsim.gen._out.strategy._TradeIfProfitable.TradeIfProfitable_Optional__ISingleAssetStrategy___Optional_Optional__ISingleAssetStrategy______IAccount___Optional__IAccount_____IFunction__Float__",
            "marketsim.gen._out.strategy._RSIbis.RSIbis_Optional__IEvent___Optional_________Side______IOrderGenerator___Optional__Float___Optional__Float___Optional__Float_",
            "marketsim.gen._out.strategy._FundamentalValue.FundamentalValue_Optional__IEvent___Optional_________Side______IOrderGenerator___Optional__IFunction__Float__",
            "marketsim.gen._out.strategy._Signal.Signal_Optional__IEvent___Optional_________Side______IOrderGenerator___Optional__IFunction__Float____Optional__Float_",
            "marketsim.gen._out.strategy._Empty.Empty_",
            "marketsim.gen._out.strategy._ChooseTheBest.ChooseTheBest_Optional_List__ISingleAssetStrategy____Optional_Optional__ISingleAssetStrategy______IAccount___Optional__IAccount_____IFunction__Float__",
            "marketsim.gen._out.strategy._CrossingAverages.CrossingAverages_Optional__IEvent___Optional_________Side______IOrderGenerator___Optional__Float___Optional__Float___Optional__Float_",
            "marketsim.gen._out.strategy._Suspendable.Suspendable_Optional__ISingleAssetStrategy___Optional__IFunction__Boolean__",
            "marketsim.gen._out.strategy._Generic.Generic_Optional__IOrderGenerator___Optional__IEvent_",
            "marketsim.gen._out.strategy._MeanReversion.MeanReversion_Optional__IEvent___Optional_________Side______IOrderGenerator___Optional__Float_",
            "marketsim.gen._out.strategy._MultiArmedBandit.MultiArmedBandit_Optional_List__ISingleAssetStrategy____Optional_Optional__ISingleAssetStrategy______IAccount___Optional__IAccount_____IFunction__Float____Optional_Optional__IFunction__Float_______IFunction__Float____Optional_Optional_List__Float______List__Float__",
            "marketsim.gen._out.strategy._Noise.Noise_Optional__IEvent___Optional_________Side______IOrderGenerator_",
            "marketsim.gen._out.strategy._Combine.Combine_Optional__ISingleAssetStrategy___Optional__ISingleAssetStrategy_",
            "marketsim.gen._out.strategy._Bollinger_linear.Bollinger_linear_Optional_________Float______IOrderGenerator___Optional__Float___Optional__IObservable__Float__",
            "marketsim.gen._out.strategy._PairTrading.PairTrading_Optional__IEvent___Optional_________Side______IOrderGenerator___Optional__IOrderBook___Optional__Float_",
            "marketsim.gen._out.strategy._RSI_linear.RSI_linear_Optional_________Float______IOrderGenerator___Optional__Float___Optional__IObservable__Float____Optional__Float_",
            "marketsim.gen._out.strategy._LiquidityProvider.LiquidityProvider_Optional__IEvent___Optional__________Side__________Float_______IOrderGenerator___Optional__Float___Optional________Float_",
            "marketsim.gen._out.strategy._TrendFollower.TrendFollower_Optional__IEvent___Optional_________Side______IOrderGenerator___Optional__Float___Optional__Float_",
            "marketsim.gen._out.strategy._MarketData.MarketData_Optional__String___Optional__String___Optional__String___Optional__Float___Optional__Float_",
            "marketsim.gen._out.strategy._Canceller.Canceller_Optional________Float_",
            "marketsim.gen._out.strategy._Array.Array_Optional_List__ISingleAssetStrategy__",
            "marketsim.gen._out.strategy._LiquidityProviderSide.LiquidityProviderSide_Optional__IEvent___Optional__________Side__________Float_______IOrderGenerator___Optional________Side___Optional__Float___Optional________Float_"
        ]
    ],
    [
        "marketsim.types.IFunction_float",
        [
            "marketsim.gen._out.math.Cumulative._StdDev.StdDev_Optional__IObservable__Float__",
            "marketsim.gen._out.math.macd._MACD.MACD_Optional__IObservable__Float____Optional__Float___Optional__Float_",
            "marketsim.gen._out.orderbook.ask._WeightedPrice.WeightedPrice_Optional__IOrderBook___Optional__Float_",
            "marketsim.gen._out.math._Sqrt.Sqrt_Optional__IFunction__Float__",
            "marketsim.gen._out.math.EW._Avg.Avg_Optional__IObservable__Float____Optional__Float_",
            "marketsim.gen._out._const.const_Optional__Float_",
            "marketsim.gen._out.observable._BreaksAtChanges.BreaksAtChanges_Optional__IFunction__Float__",
            "marketsim.gen._out.math._Log.Log_Optional__IFunction__Float__",
            "marketsim.gen._out.orderbook._LastPrice.LastPrice_Optional__IOrderQueue_",
            "marketsim.gen._out.math.EW._Var.Var_Optional__IObservable__Float____Optional__Float_",
            "marketsim.gen._out.orderbook._WeightedPrice.WeightedPrice_Optional__IOrderQueue___Optional__Float_",
            "marketsim.gen._out.trader._RoughPnL.RoughPnL_Optional__IAccount_",
            "marketsim.gen._out.strategy.weight._Clamp0.Clamp0_Optional__IFunction__Float__",
            "marketsim.gen._out.math.Cumulative._Avg.Avg_Optional__IObservable__Float__",
            "marketsim.gen._out.math.Cumulative._RelStdDev.RelStdDev_Optional__IObservable__Float__",
            "marketsim.gen._out.observable._Price.Price_Optional__IFunction__Float__",
            "marketsim.gen._out.math.Cumulative._MinEpsilon.MinEpsilon_Optional__IFunction__Float____Optional__IFunction__Float__",
            "marketsim.gen._out.math.Moving._Avg.Avg_Optional__IObservable__Float____Optional__Float_",
            "marketsim.gen._out.strategy.price._LiquidityProvider.LiquidityProvider_Optional________Side___Optional__Float___Optional________Float___Optional__IOrderBook_",
            "marketsim.gen._out.orderbook._CumulativePrice.CumulativePrice_Optional__IOrderBook___Optional__IFunction__Float__",
            "marketsim.gen._out.math.Moving._StdDev.StdDev_Optional__IObservable__Float____Optional__Float_",
            "marketsim.gen._out.strategy.weight._IdentityF.IdentityF_Optional__IFunction__Float__",
            "marketsim.gen._out.trader._Position.Position_Optional__IAccount_",
            "marketsim.gen._out.math.random._normalvariate.normalvariate",
            "marketsim.gen._out.math.EW._RelStdDev.RelStdDev_Optional__IObservable__Float____Optional__Float_",
            "marketsim.gen._out.observable._Volume.Volume_Optional__IFunction__Float__",
            "marketsim.gen._out._constant.constant_Optional__Float_",
            "marketsim.gen._out.strategy.weight._Efficiency.Efficiency__IAccount",
            "marketsim.gen._out.math.random._uniform.uniform",
            "marketsim.gen._out.math._LogReturns.LogReturns_Optional__IObservable__Float____Optional__Float_",
            "marketsim.gen._out.orderbook.bid._LastTradePrice.LastTradePrice_Optional__IOrderBook_",
            "marketsim.gen._out.trader._Balance.Balance_Optional__IAccount_",
            "marketsim.gen._out.trader._EfficiencyTrend.EfficiencyTrend_Optional__IAccount___Optional__Float_",
            "marketsim.gen._out.orderbook.ask._LastTradeVolume.LastTradeVolume_Optional__IOrderBook_",
            "marketsim.gen._out.trader._Efficiency.Efficiency_Optional__IAccount_",
            "marketsim.gen._out.orderbook.ask._LastPrice.LastPrice_Optional__IOrderBook_",
            "marketsim.gen._out._null.null_",
            "marketsim.gen._out.math._Exp.Exp_Optional__IFunction__Float__",
            "marketsim.gen._out.orderbook._TickSize.TickSize_Optional__IOrderBook_",
            "marketsim.gen._out.math.random._triangular.triangular",
            "marketsim.gen._out.math._RSI.RSI_Optional__IOrderBook___Optional__Float___Optional__Float_",
            "marketsim.gen._out.trader._PendingVolume.PendingVolume_Optional__IAccount_",
            "marketsim.gen._out.math._Derivative.Derivative_Optional__IDifferentiable_",
            "marketsim.gen._out.math.Moving._Min.Min_Optional__IFunction__Float____Optional__Float_",
            "marketsim.gen._out.observable._Float.Float_Optional__IFunction__Float__",
            "marketsim.gen._out.orderbook.bid._Price.Price_Optional__IOrderBook_",
            "marketsim.gen._out.orderbook._SafeSidePrice.SafeSidePrice_Optional__IOrderQueue___Optional__IFunction__Float__",
            "marketsim.gen._out.math._UpMovements.UpMovements_Optional__IObservable__Float____Optional__Float_",
            "marketsim.gen._out.math.random._gammavariate.gammavariate",
            "marketsim.gen._out.strategy.position._DesiredPosition.DesiredPosition_Optional__IObservable__Float____Optional__ISingleAssetTrader_",
            "marketsim.gen._out.orderbook._LastTradeVolume.LastTradeVolume_Optional__IOrderQueue_",
            "marketsim.gen._out.ops._Add.Add_Optional__IFunction__Float____Optional__IFunction__Float__",
            "marketsim.gen._out.math._Lagged.Lagged_Optional__IObservable__Float____Optional__Float_",
            "marketsim.gen._out.strategy.position._RSI_linear.RSI_linear_Optional__Float___Optional__IObservable__Float____Optional__Float___Optional__ISingleAssetTrader_",
            "marketsim.gen._out.math.macd._Histogram.Histogram_Optional__IObservable__Float____Optional__Float___Optional__Float___Optional__Float___Optional__Float_",
            "marketsim.gen._out.math._Atan.Atan_Optional__IFunction__Float__",
            "marketsim.gen._out.math._RandomWalk.RandomWalk_Optional__Float___Optional________Float___Optional________Float___Optional__String_",
            "marketsim.gen._out.observable._Quote.Quote_Optional__String___Optional__String___Optional__String_",
            "marketsim.gen._out.observable._OnEveryDt.OnEveryDt_Optional__Float___Optional__IFunction__Float__",
            "marketsim.gen._out.orderbook._MidPrice.MidPrice_Optional__IOrderBook_",
            "marketsim.gen._out.math.random._betavariate.betavariate",
            "marketsim.gen._out.math.random._weibullvariate.weibullvariate",
            "marketsim.gen._out.math.random._expovariate.expovariate",
            "marketsim.gen._out.orderbook._LastTradePrice.LastTradePrice_Optional__IOrderQueue_",
            "marketsim.gen._out.strategy.weight._AtanPow.AtanPow_Optional__IFunction__Float____Optional__Float_",
            "marketsim.gen._out.math.Moving._RelStdDev.RelStdDev_Optional__IObservable__Float____Optional__Float_",
            "marketsim.gen._out._IfDefined.IfDefined_Optional__IFunction__Float____Optional__IFunction__Float__",
            "marketsim.gen._out.math.random._paretovariate.paretovariate",
            "marketsim.gen._out.math._Max.Max_Optional__IFunction__Float____Optional__IFunction__Float__",
            "marketsim.gen._out.ops._Sub.Sub_Optional__IFunction__Float____Optional__IFunction__Float__",
            "marketsim.gen._out.orderbook.bid._LastPrice.LastPrice_Optional__IOrderBook_",
            "marketsim.gen._out.math._Pow.Pow_Optional__IFunction__Float____Optional__IFunction__Float__",
            "marketsim.gen._out.strategy.weight._Unit.Unit__IAccount",
            "marketsim.gen._out.math.Moving._Var.Var_Optional__IObservable__Float____Optional__Float_",
            "marketsim.gen._out.strategy.weight._EfficiencyTrend.EfficiencyTrend__IAccount__Optional__Float_",
            "marketsim.gen._out.math._Sqr.Sqr_Optional__IFunction__Float__",
            "marketsim.gen._out.ops._Div.Div_Optional__IFunction__Float____Optional__IFunction__Float__",
            "marketsim.gen._out.orderbook.bid._LastTradeVolume.LastTradeVolume_Optional__IOrderBook_",
            "marketsim.gen._out.orderbook.ask._Price.Price_Optional__IOrderBook_",
            "marketsim.gen._out.math.Moving._Max.Max_Optional__IFunction__Float____Optional__Float_",
            "marketsim.gen._out.orderbook.bid._WeightedPrice.WeightedPrice_Optional__IOrderBook___Optional__Float_",
            "marketsim.gen._out.orderbook._Spread.Spread_Optional__IOrderBook_",
            "marketsim.gen._out.math._DownMovements.DownMovements_Optional__IObservable__Float____Optional__Float_",
            "marketsim.gen._out.strategy.weight._Score.Score__IAccount",
            "marketsim.gen._out.ops._Negate.Negate_Optional__IFunction__Float__",
            "marketsim.gen._out.math.rsi._Raw.Raw_Optional__IObservable__Float____Optional__Float___Optional__Float_",
            "marketsim.gen._out.math._Min.Min_Optional__IFunction__Float____Optional__IFunction__Float__",
            "marketsim.gen._out.math.Cumulative._Var.Var_Optional__IObservable__Float__",
            "marketsim.gen._out.math.macd._Signal.Signal_Optional__IObservable__Float____Optional__Float___Optional__Float___Optional__Float___Optional__Float_",
            "marketsim.gen._out.ops._Mul.Mul_Optional__IFunction__Float____Optional__IFunction__Float__",
            "marketsim.gen._out.math.EW._StdDev.StdDev_Optional__IObservable__Float____Optional__Float_",
            "marketsim.gen._out.orderbook.ask._LastTradePrice.LastTradePrice_Optional__IOrderBook_",
            "marketsim.gen._out.math.random._vonmisesvariate.vonmisesvariate",
            "marketsim.gen._out.orderbook._NaiveCumulativePrice.NaiveCumulativePrice_Optional__IOrderBook___Optional__IFunction__Float__",
            "marketsim.gen._out.math.random._lognormvariate.lognormvariate",
            "marketsim.gen._out.strategy.position._Bollinger_linear.Bollinger_linear_Optional__Float___Optional__IObservable__Float____Optional__ISingleAssetTrader_",
            "marketsim.gen._out.math.Cumulative._MaxEpsilon.MaxEpsilon_Optional__IFunction__Float____Optional__IFunction__Float__",
            "marketsim.gen._out.ops._Condition_Float.Condition_Float_Optional__IFunction__Boolean____Optional__IFunction__Float____Optional__IFunction__Float__",
            "marketsim.gen._out.orderbook._BestPrice.BestPrice_Optional__IOrderQueue_"
        ]
    ],
    [
        {
            "elementType": "marketsim.types.ISingleAssetTrader"
        },
        []
    ],
    [
        "marketsim.ITwoWayLink",
        [
            "marketsim.gen._out.orderbook._TwoWayLink.TwoWayLink_Optional__ILink___Optional__ILink_"
        ]
    ],
    [
        {
            "elementType": "marketsim.types.ITrader"
        },
        []
    ],
    [
        "marketsim.types.IGraph",
        [
            "marketsim.js.Graph",
            "marketsim.gen._out.veusz._Graph.Graph_Optional__String_"
        ]
    ],
    [
        "marketsim.types.IFunction_IOrderGenerator_IFunction_Tag_IFunction_float",
        [
            "marketsim.gen._out.order._curried._sidevolume_ImmediateOrCancel.sidevolume_ImmediateOrCancel",
            "marketsim.gen._out.order._curried._sideprice_Iceberg.sideprice_Iceberg",
            "marketsim.gen._out.order._curried._sidevolume_Limit.sidevolume_Limit",
            "marketsim.gen._out.order._curried._sidevolume_WithExpiry.sidevolume_WithExpiry",
            "marketsim.gen._out.order._curried._sidevolume_Market.sidevolume_Market",
            "marketsim.gen._out.order._curried._sidevolume_Peg.sidevolume_Peg",
            "marketsim.gen._out.order._curried._sidevolume_FloatingPrice.sidevolume_FloatingPrice",
            "marketsim.gen._out.order._curried._sideprice_WithExpiry.sideprice_WithExpiry",
            "marketsim.gen._out.order._curried._sidevolume_StopLoss.sidevolume_StopLoss",
            "marketsim.gen._out.order._curried._sidevolume_Iceberg.sidevolume_Iceberg",
            "marketsim.gen._out.order._curried._sideprice_FloatingPrice.sideprice_FloatingPrice",
            "marketsim.gen._out.order._curried._sideprice_ImmediateOrCancel.sideprice_ImmediateOrCancel",
            "marketsim.gen._out.order._curried._sideprice_StopLoss.sideprice_StopLoss",
            "marketsim.gen._out.order._curried._sideprice_Peg.sideprice_Peg",
            "marketsim.gen._out.order._curried._sideprice_Limit.sideprice_Limit"
        ]
    ],
    [
        "marketsim.types.IFunction_IOrderGenerator_IFunction_float",
        [
            "marketsim.gen._out.order._curried._signedVolume_LimitSigned.signedVolume_LimitSigned",
            "marketsim.gen._out.order._curried._volume_FloatingPrice.volume_FloatingPrice",
            "marketsim.gen._out.order._curried._price_StopLoss.price_StopLoss",
            "marketsim.gen._out.order._curried._signedVolume_MarketSigned.signedVolume_MarketSigned",
            "marketsim.gen._out.order._curried._volume_ImmediateOrCancel.volume_ImmediateOrCancel",
            "marketsim.gen._out.order._curried._price_Peg.price_Peg",
            "marketsim.gen._out.order._curried._price_WithExpiry.price_WithExpiry",
            "marketsim.gen._out.order._curried._price_Iceberg.price_Iceberg",
            "marketsim.gen._out.order._curried._volume_Market.volume_Market",
            "marketsim.gen._out.order._curried._volume_WithExpiry.volume_WithExpiry",
            "marketsim.gen._out.order._curried._volume_StopLoss.volume_StopLoss",
            "marketsim.gen._out.order._curried._volume_Peg.volume_Peg",
            "marketsim.gen._out.order._curried._price_Limit.price_Limit",
            "marketsim.gen._out.order._curried._price_FloatingPrice.price_FloatingPrice",
            "marketsim.gen._out.order._curried._volume_Iceberg.volume_Iceberg",
            "marketsim.gen._out.order._curried._price_ImmediateOrCancel.price_ImmediateOrCancel",
            "marketsim.gen._out.order._curried._volume_Limit.volume_Limit"
        ]
    ],
    [
        "marketsim.types.IObservable_float",
        [
            "marketsim.gen._out.math.Moving._Min.Min_Optional__IFunction__Float____Optional__Float_",
            "marketsim.gen._out.orderbook.bid._LastTradeVolume.LastTradeVolume_Optional__IOrderBook_",
            "marketsim.gen._out.orderbook.ask._Price.Price_Optional__IOrderBook_",
            "marketsim.gen._out.math.Moving._Max.Max_Optional__IFunction__Float____Optional__Float_",
            "marketsim.gen._out.orderbook._SafeSidePrice.SafeSidePrice_Optional__IOrderQueue___Optional__IFunction__Float__",
            "marketsim.gen._out.orderbook._Spread.Spread_Optional__IOrderBook_",
            "marketsim.gen._out.math._UpMovements.UpMovements_Optional__IObservable__Float____Optional__Float_",
            "marketsim.gen._out.observable._Volume.Volume_Optional__IFunction__Float__",
            "marketsim.gen._out.strategy.position._DesiredPosition.DesiredPosition_Optional__IObservable__Float____Optional__ISingleAssetTrader_",
            "marketsim.gen._out.math._Sqrt.Sqrt_Optional__IFunction__Float__",
            "marketsim.gen._out.orderbook.bid._LastPrice.LastPrice_Optional__IOrderBook_",
            "marketsim.gen._out.ops._Add.Add_Optional__IFunction__Float____Optional__IFunction__Float__",
            "marketsim.gen._out._const.const_Optional__Float_",
            "marketsim.gen._out.math._Lagged.Lagged_Optional__IObservable__Float____Optional__Float_",
            "marketsim.gen._out.strategy.position._RSI_linear.RSI_linear_Optional__Float___Optional__IObservable__Float____Optional__Float___Optional__ISingleAssetTrader_",
            "marketsim.gen._out.math._DownMovements.DownMovements_Optional__IObservable__Float____Optional__Float_",
            "marketsim.gen._out.math._Atan.Atan_Optional__IFunction__Float__",
            "marketsim.gen._out.observable._BreaksAtChanges.BreaksAtChanges_Optional__IFunction__Float__",
            "marketsim.gen._out.math._Log.Log_Optional__IFunction__Float__",
            "marketsim.gen._out.orderbook._LastPrice.LastPrice_Optional__IOrderQueue_",
            "marketsim.gen._out.math._RandomWalk.RandomWalk_Optional__Float___Optional________Float___Optional________Float___Optional__String_",
            "marketsim.gen._out.observable._Quote.Quote_Optional__String___Optional__String___Optional__String_",
            "marketsim.gen._out.observable._OnEveryDt.OnEveryDt_Optional__Float___Optional__IFunction__Float__",
            "marketsim.gen._out.ops._Negate.Negate_Optional__IFunction__Float__",
            "marketsim.gen._out.math._Min.Min_Optional__IFunction__Float____Optional__IFunction__Float__",
            "marketsim.gen._out.trader._RoughPnL.RoughPnL_Optional__IAccount_",
            "marketsim.gen._out.orderbook.bid._Price.Price_Optional__IOrderBook_",
            "marketsim.gen._out.orderbook.ask._LastTradePrice.LastTradePrice_Optional__IOrderBook_",
            "marketsim.gen._out.orderbook.bid._LastTradePrice.LastTradePrice_Optional__IOrderBook_",
            "marketsim.gen._out.orderbook._LastTradePrice.LastTradePrice_Optional__IOrderQueue_",
            "marketsim.gen._out.observable._Price.Price_Optional__IFunction__Float__",
            "marketsim.gen._out.math.Cumulative._MinEpsilon.MinEpsilon_Optional__IFunction__Float____Optional__IFunction__Float__",
            "marketsim.gen._out.ops._Mul.Mul_Optional__IFunction__Float____Optional__IFunction__Float__",
            "marketsim.gen._out.trader._Balance.Balance_Optional__IAccount_",
            "marketsim.gen._out._IfDefined.IfDefined_Optional__IFunction__Float____Optional__IFunction__Float__",
            "marketsim.gen._out.orderbook.ask._LastTradeVolume.LastTradeVolume_Optional__IOrderBook_",
            "marketsim.gen._out.math._Max.Max_Optional__IFunction__Float____Optional__IFunction__Float__",
            "marketsim.gen._out.ops._Sub.Sub_Optional__IFunction__Float____Optional__IFunction__Float__",
            "marketsim.gen._out.trader._Efficiency.Efficiency_Optional__IAccount_",
            "marketsim.gen._out.orderbook.ask._LastPrice.LastPrice_Optional__IOrderBook_",
            "marketsim.gen._out._null.null_",
            "marketsim.gen._out.math._Pow.Pow_Optional__IFunction__Float____Optional__IFunction__Float__",
            "marketsim.gen._out.math._Exp.Exp_Optional__IFunction__Float__",
            "marketsim.gen._out.orderbook._NaiveCumulativePrice.NaiveCumulativePrice_Optional__IOrderBook___Optional__IFunction__Float__",
            "marketsim.gen._out.orderbook._LastTradeVolume.LastTradeVolume_Optional__IOrderQueue_",
            "marketsim.gen._out.orderbook._MidPrice.MidPrice_Optional__IOrderBook_",
            "marketsim.gen._out.orderbook._CumulativePrice.CumulativePrice_Optional__IOrderBook___Optional__IFunction__Float__",
            "marketsim.gen._out.strategy.position._Bollinger_linear.Bollinger_linear_Optional__Float___Optional__IObservable__Float____Optional__ISingleAssetTrader_",
            "marketsim.gen._out.math.Cumulative._MaxEpsilon.MaxEpsilon_Optional__IFunction__Float____Optional__IFunction__Float__",
            "marketsim.gen._out.observable._Float.Float_Optional__IFunction__Float__",
            "marketsim.gen._out.ops._Condition_Float.Condition_Float_Optional__IFunction__Boolean____Optional__IFunction__Float____Optional__IFunction__Float__",
            "marketsim.gen._out.trader._Position.Position_Optional__IAccount_",
            "marketsim.gen._out.math._Sqr.Sqr_Optional__IFunction__Float__",
            "marketsim.gen._out.trader._PendingVolume.PendingVolume_Optional__IAccount_",
            "marketsim.gen._out.orderbook._BestPrice.BestPrice_Optional__IOrderQueue_",
            "marketsim.gen._out.ops._Div.Div_Optional__IFunction__Float____Optional__IFunction__Float__"
        ]
    ],
    [
        "marketsim.types.IFunction_IFunction_IOrderGenerator_IFunction_float_IFunction_Tag",
        [
            "marketsim.gen._out.order._curried._side_price_StopLoss.side_price_StopLoss",
            "marketsim.gen._out.order._curried._side_price_Limit.side_price_Limit",
            "marketsim.gen._out.order._curried._side_price_ImmediateOrCancel.side_price_ImmediateOrCancel",
            "marketsim.gen._out.order._curried._side_price_Iceberg.side_price_Iceberg",
            "marketsim.gen._out.order._curried._side_price_FloatingPrice.side_price_FloatingPrice",
            "marketsim.gen._out.order._curried._side_price_WithExpiry.side_price_WithExpiry",
            "marketsim.gen._out.order._curried._side_price_Peg.side_price_Peg"
        ]
    ],
    [
        "marketsim.types.IMultiAssetStrategy",
        [
            "marketsim.gen._out.strategy._Arbitrage.Arbitrage_"
        ]
    ],
    [
        "marketsim.types.IOrderBook",
        [
            "marketsim.gen._out.orderbook._Local.Local_Optional__Float___Optional__Int___Optional__String___Optional_List__ITimeSerie__",
            "marketsim.gen._out.orderbook._Remote.Remote_Optional__IOrderBook___Optional__ITwoWayLink___Optional_List__ITimeSerie__",
            "marketsim.gen._out.orderbook._OfTrader.OfTrader_Optional__IAccount_",
            "marketsim.gen._out.orderbook._Proxy.Proxy_"
        ]
    ],
    [
        "marketsim.types.IFunction_IAccount_ISingleAssetStrategy",
        [
            "marketsim.gen._out.strategy.account.inner._inner_VirtualMarket.inner_VirtualMarket_",
            "marketsim.gen._out.strategy.account.inner._inner_Real.inner_Real_"
        ]
    ],
    [
        "_parseFloat",
        []
    ],
    [
        "marketsim.types.ITimeSerie",
        [
            "marketsim.gen._out._volumeLevels.volumeLevels__IFunction__IVolumeLevels___Optional__IGraph___Optional__Int___Optional__Int___Optional_List__Float____Optional__Int_",
            "marketsim.gen._out._TimeSerie.TimeSerie_Optional__IObservable_Any____Optional__IGraph___Optional__Int___Optional__Int_"
        ]
    ],
    [
        {
            "elementType": "marketsim.types.ISingleAssetStrategy"
        },
        []
    ],
    [
        "marketsim.types.IEvent",
        [
            "marketsim.gen._out.math.Moving._Min.Min_Optional__IFunction__Float____Optional__Float_",
            "marketsim.gen._out._CandleSticks.CandleSticks_Optional__IObservable__Float____Optional__Float_",
            "marketsim.gen._out._true.true_",
            "marketsim.gen._out.math.Moving._Max.Max_Optional__IFunction__Float____Optional__Float_",
            "marketsim.gen._out.ops._Add.Add_Optional__IFunction__Float____Optional__IFunction__Float__",
            "marketsim.gen._out.orderbook._SafeSidePrice.SafeSidePrice_Optional__IOrderQueue___Optional__IFunction__Float__",
            "marketsim.gen._out.orderbook._Spread.Spread_Optional__IOrderBook_",
            "marketsim.gen._out.math._UpMovements.UpMovements_Optional__IObservable__Float____Optional__Float_",
            "marketsim.gen._out.observable._Volume.Volume_Optional__IFunction__Float__",
            "marketsim.gen._out.strategy.side._FundamentalValue.FundamentalValue_Optional__IFunction__Float____Optional__IOrderBook_",
            "marketsim.gen._out.order._FixedBudget.FixedBudget",
            "marketsim.gen._out.strategy.position._DesiredPosition.DesiredPosition_Optional__IObservable__Float____Optional__ISingleAssetTrader_",
            "marketsim.gen._out.math._Sqrt.Sqrt_Optional__IFunction__Float__",
            "marketsim.gen._out.strategy.side._Signal.Signal_Optional__IFunction__Float____Optional__Float_",
            "marketsim.gen._out.observable._Side.Side_Optional__IFunction__Side__",
            "marketsim.gen._out.order._Limit.Limit",
            "marketsim.gen._out.ops._LessEqual.LessEqual_Optional__IFunction__Float____Optional__IFunction__Float__",
            "marketsim.gen._out._const.const_Optional__Float_",
            "marketsim.gen._out.math._Lagged.Lagged_Optional__IObservable__Float____Optional__Float_",
            "marketsim.gen._out.strategy.position._RSI_linear.RSI_linear_Optional__Float___Optional__IObservable__Float____Optional__Float___Optional__ISingleAssetTrader_",
            "marketsim.gen._out.math._DownMovements.DownMovements_Optional__IObservable__Float____Optional__Float_",
            "marketsim.gen._out.math._Atan.Atan_Optional__IFunction__Float__",
            "marketsim.gen._out.observable._BreaksAtChanges.BreaksAtChanges_Optional__IFunction__Float__",
            "marketsim.gen._out.math._Log.Log_Optional__IFunction__Float__",
            "marketsim.gen._out.order._Iceberg.Iceberg",
            "marketsim.gen._out.orderbook._LastPrice.LastPrice_Optional__IOrderQueue_",
            "marketsim.gen._out.math._RandomWalk.RandomWalk_Optional__Float___Optional________Float___Optional________Float___Optional__String_",
            "marketsim.gen._out.ops._Less.Less_Optional__IFunction__Float____Optional__IFunction__Float__",
            "marketsim.gen._out.orderbook.bid._LastPrice.LastPrice_Optional__IOrderBook_",
            "marketsim.gen._out.observable._OnEveryDt.OnEveryDt_Optional__Float___Optional__IFunction__Float__",
            "marketsim.gen._out.ops._Negate.Negate_Optional__IFunction__Float__",
            "marketsim.gen._out.orderbook.ask._Price.Price_Optional__IOrderBook_",
            "marketsim.gen._out.orderbook._MidPrice.MidPrice_Optional__IOrderBook_",
            "marketsim.gen._out.math._Min.Min_Optional__IFunction__Float____Optional__IFunction__Float__",
            "marketsim.gen._out.ops._Greater.Greater_Optional__IFunction__Float____Optional__IFunction__Float__",
            "marketsim.gen._out.trader._RoughPnL.RoughPnL_Optional__IAccount_",
            "marketsim.gen._out.order._StopLoss.StopLoss",
            "marketsim.gen._out.math.Cumulative._MinEpsilon.MinEpsilon_Optional__IFunction__Float____Optional__IFunction__Float__",
            "marketsim.gen._out.order._Market.Market",
            "marketsim.gen._out.orderbook.bid._Price.Price_Optional__IOrderBook_",
            "marketsim.gen._out.order._Peg.Peg",
            "marketsim.gen._out.ops._NotEqual.NotEqual_Optional__IFunction__Float____Optional__IFunction__Float__",
            "marketsim.gen._out.strategy.side._PairTrading.PairTrading_Optional__IOrderBook___Optional__Float___Optional__IOrderBook_",
            "marketsim.gen._out.orderbook.ask._LastTradePrice.LastTradePrice_Optional__IOrderBook_",
            "marketsim.gen._out.order._FloatingPrice.FloatingPrice",
            "marketsim.gen._out.orderbook.bid._LastTradePrice.LastTradePrice_Optional__IOrderBook_",
            "marketsim.gen._out.orderbook._LastTradePrice.LastTradePrice_Optional__IOrderQueue_",
            "marketsim.gen._out.observable._Price.Price_Optional__IFunction__Float__",
            "marketsim.gen._out.orderbook.ask._LastPrice.LastPrice_Optional__IOrderBook_",
            "marketsim.gen._out._IfDefined.IfDefined_Optional__IFunction__Float____Optional__IFunction__Float__",
            "marketsim.gen._out.ops._Mul.Mul_Optional__IFunction__Float____Optional__IFunction__Float__",
            "marketsim.gen._out.trader._Balance.Balance_Optional__IAccount_",
            "marketsim.gen._out.ops._GreaterEqual.GreaterEqual_Optional__IFunction__Float____Optional__IFunction__Float__",
            "marketsim.gen._out.order._ImmediateOrCancel.ImmediateOrCancel",
            "marketsim.gen._out.orderbook.ask._LastTradeVolume.LastTradeVolume_Optional__IOrderBook_",
            "marketsim.gen._out.event._After.After_Optional__IFunction__Float__",
            "marketsim.gen._out.math._Max.Max_Optional__IFunction__Float____Optional__IFunction__Float__",
            "marketsim.gen._out.ops._Sub.Sub_Optional__IFunction__Float____Optional__IFunction__Float__",
            "marketsim.gen._out.trader._Efficiency.Efficiency_Optional__IAccount_",
            "marketsim.gen._out._false.false_",
            "marketsim.gen._out.order._LimitSigned.LimitSigned",
            "marketsim.gen._out._null.null_",
            "marketsim.gen._out.math._Pow.Pow_Optional__IFunction__Float____Optional__IFunction__Float__",
            "marketsim.gen._out.math._Exp.Exp_Optional__IFunction__Float__",
            "marketsim.gen._out.event._Every.Every_Optional________Float_",
            "marketsim.gen._out.orderbook._NaiveCumulativePrice.NaiveCumulativePrice_Optional__IOrderBook___Optional__IFunction__Float__",
            "marketsim.gen._out.observable._Quote.Quote_Optional__String___Optional__String___Optional__String_",
            "marketsim.gen._out.orderbook.bid._LastTradeVolume.LastTradeVolume_Optional__IOrderBook_",
            "marketsim.gen._out.orderbook._LastTradeVolume.LastTradeVolume_Optional__IOrderQueue_",
            "marketsim.gen._out.trader._PendingVolume.PendingVolume_Optional__IAccount_",
            "marketsim.gen._out.order._WithExpiry.WithExpiry",
            "marketsim.gen._out.orderbook._CumulativePrice.CumulativePrice_Optional__IOrderBook___Optional__IFunction__Float__",
            "marketsim.gen._out.orderbook._VolumeLevels.VolumeLevels_Optional__IOrderQueue___Optional__Float___Optional__Int_",
            "marketsim.gen._out.strategy.position._Bollinger_linear.Bollinger_linear_Optional__Float___Optional__IObservable__Float____Optional__ISingleAssetTrader_",
            "marketsim.gen._out.math.Cumulative._MaxEpsilon.MaxEpsilon_Optional__IFunction__Float____Optional__IFunction__Float__",
            "marketsim.gen._out.observable._Float.Float_Optional__IFunction__Float__",
            "marketsim.gen._out.ops._Condition_Float.Condition_Float_Optional__IFunction__Boolean____Optional__IFunction__Float____Optional__IFunction__Float__",
            "marketsim.gen._out.ops._Equal.Equal_Optional__IFunction__Float____Optional__IFunction__Float__",
            "marketsim.gen._out.trader._Position.Position_Optional__IAccount_",
            "marketsim.gen._out.order._MarketSigned.MarketSigned",
            "marketsim.gen._out.math._Sqr.Sqr_Optional__IFunction__Float__",
            "marketsim.gen._out.ops._Condition_Side.Condition_Side_Optional__IFunction__Boolean____Optional________Side___Optional________Side_",
            "marketsim.gen._out.orderbook._BestPrice.BestPrice_Optional__IOrderQueue_",
            "marketsim.gen._out.ops._Div.Div_Optional__IFunction__Float____Optional__IFunction__Float__"
        ]
    ],
    [
        {
            "elementType": "marketsim.types.ITimeSerie"
        },
        []
    ],
    [
        "marketsim.types.ITrader",
        [
            "marketsim.gen._out.trader._SingleProxy.SingleProxy_",
            "marketsim.gen._out.trader._SingleAsset.SingleAsset__IOrderBook__Optional__ISingleAssetStrategy___Optional__String___Optional__Float___Optional__Float___Optional_List__ITimeSerie__",
            "marketsim.gen._out.trader._MultiAsset.MultiAsset_Optional_List__ISingleAssetTrader____Optional__IMultiAssetStrategy___Optional__String___Optional__Float___Optional_List__ITimeSerie__"
        ]
    ],
    [
        "marketsim.types.IOrderQueue",
        [
            "marketsim.gen._out.orderbook._Queue.Queue_Optional__IOrderBook___Optional________Side_",
            "marketsim.gen._out.orderbook._Asks.Asks_Optional__IOrderBook_",
            "marketsim.gen._out.orderbook._Bids.Bids_Optional__IOrderBook_"
        ]
    ],
    [
        "marketsim.types.IFunction_IFunction_float_IAccount",
        [
            "marketsim.gen._out.strategy.weight.trader._trader_Score.trader_Score_",
            "marketsim.gen._out.strategy.weight.trader._trader_Unit.trader_Unit_",
            "marketsim.gen._out.strategy.weight.trader._trader_EfficiencyTrend.trader_EfficiencyTrend_Optional__Float_",
            "marketsim.gen._out.strategy.weight.trader._trader_Efficiency.trader_Efficiency_"
        ]
    ],
    [
        "marketsim.types.IFunction_IFunction_IOrderGenerator_IFunction_float_IFunction_float",
        [
            "marketsim.gen._out.order._curried._volume_price_FloatingPrice.volume_price_FloatingPrice",
            "marketsim.gen._out.order._curried._volume_price_Limit.volume_price_Limit",
            "marketsim.gen._out.order._curried._volume_price_Peg.volume_price_Peg",
            "marketsim.gen._out.order._curried._volume_price_WithExpiry.volume_price_WithExpiry",
            "marketsim.gen._out.order._curried._volume_price_Iceberg.volume_price_Iceberg",
            "marketsim.gen._out.order._curried._volume_price_StopLoss.volume_price_StopLoss",
            "marketsim.gen._out.order._curried._volume_price_ImmediateOrCancel.volume_price_ImmediateOrCancel"
        ]
    ],
    [
        "marketsim.types.IFunction_IFunction_float_IFunction_float",
        [
            "marketsim.gen._out.strategy.weight.f._f_Clamp0.f_Clamp0_",
            "marketsim.gen._out.strategy.weight.f._f_AtanPow.f_AtanPow_Optional__Float_",
            "marketsim.gen._out.strategy.weight.f._f_IdentityF.f_IdentityF_"
        ]
    ],
    [
        "marketsim.types.IFunction_bool",
        [
            "marketsim.gen._out._true.true_",
            "marketsim.gen._out.ops._NotEqual.NotEqual_Optional__IFunction__Float____Optional__IFunction__Float__",
            "marketsim.gen._out.ops._GreaterEqual.GreaterEqual_Optional__IFunction__Float____Optional__IFunction__Float__",
            "marketsim.gen._out.ops._Less.Less_Optional__IFunction__Float____Optional__IFunction__Float__",
            "marketsim.gen._out.ops._Equal.Equal_Optional__IFunction__Float____Optional__IFunction__Float__",
            "marketsim.gen._out.ops._Greater.Greater_Optional__IFunction__Float____Optional__IFunction__Float__",
            "marketsim.gen._out._false.false_",
            "marketsim.gen._out.ops._LessEqual.LessEqual_Optional__IFunction__Float____Optional__IFunction__Float__"
        ]
    ],
    [
        "marketsim.types.IDifferentiable",
        [
            "marketsim.gen._out.math.EW._Avg.Avg_Optional__IObservable__Float____Optional__Float_",
            "marketsim.gen._out.math.Moving._Avg.Avg_Optional__IObservable__Float____Optional__Float_",
            "marketsim.gen._out.math.Cumulative._Avg.Avg_Optional__IObservable__Float__"
        ]
    ],
    [
        "marketsim.ILink",
        [
            "marketsim.gen._out.orderbook._Link.Link_Optional__IObservable__Float__"
        ]
    ],
    [
        {
            "elementType": "marketsim.types.IOrderBook"
        },
        []
    ],
    [
        "marketsim.types.IOrderGenerator",
        [
            "marketsim.gen._out.order._ImmediateOrCancel.ImmediateOrCancel",
            "marketsim.gen._out.order._WithExpiry.WithExpiry",
            "marketsim.gen._out.order._MarketSigned.MarketSigned",
            "marketsim.gen._out.order._FloatingPrice.FloatingPrice",
            "marketsim.gen._out.order._Limit.Limit",
            "marketsim.gen._out.order._Iceberg.Iceberg",
            "marketsim.gen._out.order._FixedBudget.FixedBudget",
            "marketsim.gen._out.order._StopLoss.StopLoss",
            "marketsim.gen._out.order._LimitSigned.LimitSigned",
            "marketsim.gen._out.order._Market.Market",
            "marketsim.gen._out.order._Peg.Peg"
        ]
    ],
    [
        "marketsim.types.IAccount",
        [
            "marketsim.gen._out.trader._SingleProxy.SingleProxy_",
            "marketsim.gen._out.strategy.account._VirtualMarket.VirtualMarket_Optional__ISingleAssetStrategy_",
            "marketsim.gen._out.trader._SingleAsset.SingleAsset__IOrderBook__Optional__ISingleAssetStrategy___Optional__String___Optional__Float___Optional__Float___Optional_List__ITimeSerie__",
            "marketsim.gen._out.strategy.account._Real.Real_Optional__ISingleAssetStrategy_"
        ]
    ],
    [
        {
            "elementType": "marketsim.types.IGraph"
        },
        []
    ],
    [
        "marketsim.types.IFunction_Tag",
        [
            "marketsim.gen._out.side._Sell.Sell_",
            "marketsim.gen._out.strategy.side._TrendFollower.TrendFollower_Optional__Float___Optional__Float___Optional__IOrderBook_",
            "marketsim.gen._out.observable._Side.Side_Optional__IFunction__Side__",
            "marketsim.gen._out.strategy.side._FundamentalValue.FundamentalValue_Optional__IFunction__Float____Optional__IOrderBook_",
            "marketsim.gen._out.strategy.side._Noise.Noise_Optional________Float_",
            "marketsim.gen._out.side._Nothing.Nothing_",
            "marketsim.gen._out.side._Buy.Buy_",
            "marketsim.gen._out.ops._Condition_Side.Condition_Side_Optional__IFunction__Boolean____Optional________Side___Optional________Side_",
            "marketsim.gen._out.strategy.side._Signal.Signal_Optional__IFunction__Float____Optional__Float_",
            "marketsim.gen._out.strategy.side._MeanReversion.MeanReversion_Optional__Float___Optional__IOrderBook_",
            "marketsim.gen._out.strategy.side._CrossingAverages.CrossingAverages_Optional__Float___Optional__Float___Optional__Float___Optional__IOrderBook_",
            "marketsim.gen._out.strategy.side._PairTrading.PairTrading_Optional__IOrderBook___Optional__Float___Optional__IOrderBook_"
        ]
    ],
    [
        "marketsim.types.IFunction_IOrderGenerator_IFunction_Tag",
        [
            "marketsim.gen._out.order._curried._side_Limit.side_Limit",
            "marketsim.gen._out.order._curried._side_Iceberg.side_Iceberg",
            "marketsim.gen._out.order._curried._side_WithExpiry.side_WithExpiry",
            "marketsim.gen._out.order._curried._side_StopLoss.side_StopLoss",
            "marketsim.gen._out.order._curried._side_Market.side_Market",
            "marketsim.gen._out.order._curried._side_Peg.side_Peg",
            "marketsim.gen._out.order._curried._side_FloatingPrice.side_FloatingPrice",
            "marketsim.gen._out.order._curried._side_ImmediateOrCancel.side_ImmediateOrCancel",
            "marketsim.gen._out.order._curried._side_FixedBudget.side_FixedBudget"
        ]
    ],
    [
        "identity",
        []
    ],
    [
        "marketsim.types.IFunction_IVolumeLevels",
        [
            "marketsim.gen._out.orderbook._VolumeLevels.VolumeLevels_Optional__IOrderQueue___Optional__Float___Optional__Int_"
        ]
    ],
    [
        "marketsim.types.IFunction_listOf_listOf",
        [
            "marketsim.gen._out.strategy.weight.array._array_IdentityL.array_IdentityL_",
            "marketsim.gen._out.strategy.weight.array._array_ChooseTheBest.array_ChooseTheBest_"
        ]
    ]
]