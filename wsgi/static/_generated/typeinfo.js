var typeinfo = {
    "marketsim.gen._out.ops._condition.Condition_IObservableBooleanIObservableSideIObservableSide": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionside.IFunctionSide",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject",
            "marketsim.gen._out._iobservable._iobservableside.IObservableSide"
        ],
        "properties": {
            "ifpart": {
                "type": "marketsim.gen._out._iobservable._iobservableside.IObservableSide"
            },
            "elsepart": {
                "type": "marketsim.gen._out._iobservable._iobservableside.IObservableSide"
            },
            "cond": {
                "type": "marketsim.gen._out._iobservable._iobservablebool.IObservablebool"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math._signal.Signal_mathmacdFloatFloat": {
        "castsTo": [
            "marketsim.gen._out._idifferentiable.IDifferentiable",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.math._macd.macd_IObservableFloatFloatFloat"
            },
            "step": {
                "type": "_parseFloat"
            },
            "timeframe": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.side._fundamental_value.Fundamental_Value_strategysideMeanReversion": {
        "castsTo": [
            "marketsim.gen._out._idifferentiable.IDifferentiable",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.side._meanreversion.MeanReversion_Float"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.side._noise.Noise_Float": {
        "castsTo": [
            "marketsim.gen._out.strategy.side._noise.Noise_Float"
        ],
        "properties": {
            "side_distribution": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out._test.in1.in2._intobs.IntObs_": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.trader._efficiency.Efficiency_IAccount": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "trader": {
                "type": "marketsim.gen._out._iaccount.IAccount"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.orderbook._naivecumulativeprice.NaiveCumulativePrice_IOrderBookFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "depth": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            },
            "book": {
                "type": "marketsim.gen._out._iorderbook.IOrderBook"
            }
        },
        "description": "<div class=\"document\">\n<p>by taking into account prices only for the best order</p>\n<p>Negative <em>depth</em> correponds to will buy assets\nPositive <em>depth</em> correponds to will sell assets</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy.position._strategy.Strategy_strategypositionRSI_linearFloatIObservableIOrder": {
        "castsTo": [
            "marketsim.gen._out._isingleassetstrategy.ISingleAssetStrategy"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.position._rsi_linear.RSI_linear_FloatIObservableFloatFloatISingleAssetTrader"
            },
            "orderFactory": {
                "type": "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionfloat.IFunctionIObservableIOrder_from_IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._curried._price_stoploss.price_StopLoss_FloatIObservableIOrderFloat": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionfloat.IFunctionIObservableIOrder_from_IFunctionfloat"
        ],
        "properties": {
            "maxloss": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            },
            "proto": {
                "type": "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionfloat.IFunctionIObservableIOrder_from_IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n<p>StopLoss order is initialised by an underlying order and a maximal acceptable loss factor.\nIt keeps track of position and balance change induced by trades of the underlying order and\nif losses from keeping the position exceed certain limit (given by maximum loss factor),\nthe meta order clears its position.</p>\n</div>\n"
    },
    "marketsim.gen._out.orderbook._cumulativeprice.CumulativePrice_IOrderBookFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "depth": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            },
            "book": {
                "type": "marketsim.gen._out._iorderbook.IOrderBook"
            }
        },
        "description": "<div class=\"document\">\n<p>In other words cumulative price corresponds to trader balance change\nif a market order of volume <em>depth</em> is completely matched</p>\n<p>Negative <em>depth</em> correponds to will buy assets\nPositive <em>depth</em> correponds to will sell assets</p>\n</div>\n"
    },
    "marketsim.gen._out.order._curried._side_limit.side_Limit_FloatFloat": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionside.IFunctionIObservableIOrder_from_IFunctionSide"
        ],
        "properties": {
            "volume": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            },
            "price": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n<p>Limit orders ask to buy or sell some asset at price better than some limit price.\nIf a limit order is not competely fulfilled\nit remains in an order book waiting to be matched with another order.</p>\n</div>\n"
    },
    "marketsim.gen._out.ops._greater.Greater_FloatIObservableFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool",
            "marketsim.gen._out._iobservable._iobservablebool.IObservablebool",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "y": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            },
            "x": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.trader._multiasset.MultiAsset_ListISingleAssetTraderIMultiAssetStrategyStringFloatListITimeSerie": {
        "castsTo": [
            "marketsim.gen._out._itrader.ITrader"
        ],
        "properties": {
            "traders": {
                "type": {
                    "elementType": "marketsim.gen._out._isingleassettrader.ISingleAssetTrader"
                }
            },
            "strategy": {
                "type": "marketsim.gen._out._imultiassetstrategy.IMultiAssetStrategy"
            },
            "PnL": {
                "type": "_parseFloat"
            },
            "timeseries": {
                "type": {
                    "elementType": "marketsim.gen._out._itimeserie.ITimeSerie"
                }
            },
            "name": {
                "type": "identity"
            }
        },
        "description": "<div class=\"document\">\n<p>It can be considered as a composition of single asset traders and multi asset strategies\nAt the moment there is no way to instruct a multi asset strategy to trade only on subset of the assets</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy.side._strategy.Strategy_strategysideTrendFollowerIEventSideIObservableIOrder": {
        "castsTo": [
            "marketsim.gen._out._isingleassetstrategy.ISingleAssetStrategy"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.side._trendfollower.TrendFollower_FloatFloatIOrderBook"
            },
            "eventGen": {
                "type": "marketsim.gen._out._ievent.IEvent"
            },
            "orderFactory": {
                "type": "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionside.IFunctionIObservableIOrder_from_IFunctionSide"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math._sqrt.Sqrt_Float": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out._observablefalse.observableFalse_": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool",
            "marketsim.gen._out._iobservable._iobservablebool.IObservablebool",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.side._observablesell.observableSell_": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionside.IFunctionSide",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject",
            "marketsim.gen._out._iobservable._iobservableside.IObservableSide"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.trader._balance.Balance_IAccount": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "trader": {
                "type": "marketsim.gen._out._iaccount.IAccount"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.weight._traderefficiencytrend.TraderEfficiencyTrend_IAccountFloat": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
        ],
        "properties": {
            "alpha": {
                "type": "_parseFloat"
            },
            "trader": {
                "type": "marketsim.gen._out._iaccount.IAccount"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math._min.Min_FloatFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "y": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            },
            "x": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n<p>If <em>x</em> or/and <em>y</em> are observables, <em>Min</em> is also observable</p>\n</div>\n"
    },
    "marketsim.gen._out.math._min.Min_IObservableFloatFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "y": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            },
            "x": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            }
        },
        "description": "<div class=\"document\">\n<p>If <em>x</em> or/and <em>y</em> are observables, <em>Min</em> is also observable</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy.side._fundamental_value.Fundamental_Value_strategysidePairTrading": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.side._pairtrading.PairTrading_IOrderBookFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.veusz._graph.Graph_String": {
        "castsTo": [
            "marketsim.gen._out._igraph.IGraph"
        ],
        "properties": {
            "name": {
                "type": "identity"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math._var.Var_mathMoving": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.math._moving.Moving_IObservableFloatFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.weight._identityl.IdentityL_ListFloat": {
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
    "marketsim.gen._out.strategy.price._strategy.Strategy_strategypriceLiquidityProviderIEventSideFloatIObservableIOrder": {
        "castsTo": [
            "marketsim.gen._out._isingleassetstrategy.ISingleAssetStrategy"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.price._liquidityprovider.LiquidityProvider_FloatFloatIOrderBook"
            },
            "eventGen": {
                "type": "marketsim.gen._out._ievent.IEvent"
            },
            "orderFactory": {
                "type": "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionsideifunctionfloat.IFunctionIObservableIOrder_from_IFunctionSideIFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.weight.array._array_choosethebest.array_ChooseTheBest_": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionifunctionlistoffloat_from_listoffloat.IFunctionIFunctionlistOffloat_from_listOffloat"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n<p>having 1 at the index of the maximal element and 0 are at the rest</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy.price._delta.Delta_strategypriceMarketMaker": {
        "castsTo": [],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.price._marketmaker.MarketMaker_FloatFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.position._k.K_strategypositionRSI_linear": {
        "castsTo": [],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.position._rsi_linear.RSI_linear_FloatIObservableFloatFloatISingleAssetTrader"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.ops._div.Div_IObservableFloatIObservableFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "y": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            },
            "x": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.weight._clamp0.Clamp0_Float": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
        ],
        "properties": {
            "f": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math.random._triangular.triangular_FloatFloatFloat": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
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
    "marketsim.gen._out.strategy.position._desiredposition.DesiredPosition_strategypositionBollinger_linear": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.position._bollinger_linear.Bollinger_linear_FloatIObservableFloatISingleAssetTrader"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.ops._greaterequal.GreaterEqual_FloatIObservableFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool",
            "marketsim.gen._out._iobservable._iobservablebool.IObservablebool",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "y": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            },
            "x": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math._value.Value_mathRSI": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.math._rsi.RSI_IObservableFloatFloatFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy._generic.Generic_IObservableIOrderIEvent": {
        "castsTo": [
            "marketsim.gen._out._isingleassetstrategy.ISingleAssetStrategy"
        ],
        "properties": {
            "orderFactory": {
                "type": "marketsim.gen._out._iobservable._iobservableiorder.IObservableIOrder"
            },
            "eventGen": {
                "type": "marketsim.gen._out._ievent.IEvent"
            }
        },
        "description": "<div class=\"document\">\n<p>creates an order via <em>orderFactory</em> and sends the order to the market using its trader</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy.side._alpha_2.Alpha_2_strategysideCrossingAverages": {
        "castsTo": [],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.side._crossingaverages.CrossingAverages_FloatFloatFloatIOrderBook"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.price._liquidityprovider.LiquidityProvider_FloatFloatIOrderBook": {
        "castsTo": [
            "marketsim.gen._out.strategy.price._liquidityprovider.LiquidityProvider_FloatFloatIOrderBook"
        ],
        "properties": {
            "priceDistr": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            },
            "initialValue": {
                "type": "_parseFloat"
            },
            "book": {
                "type": "marketsim.gen._out._iorderbook.IOrderBook"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.price._oneside.OneSide_strategypriceMarketMakerSideFloat": {
        "castsTo": [
            "marketsim.gen._out._isingleassetstrategy.ISingleAssetStrategy"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.price._marketmaker.MarketMaker_FloatFloat"
            },
            "side": {
                "type": "marketsim.gen._out._ifunction._ifunctionside.IFunctionSide"
            },
            "sign": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.orderbook._naivecumulativeprice.NaiveCumulativePrice_IOrderBookIObservableFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "depth": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            },
            "book": {
                "type": "marketsim.gen._out._iorderbook.IOrderBook"
            }
        },
        "description": "<div class=\"document\">\n<p>by taking into account prices only for the best order</p>\n<p>Negative <em>depth</em> correponds to will buy assets\nPositive <em>depth</em> correponds to will sell assets</p>\n</div>\n"
    },
    "marketsim.gen._out.order._curried._side_price_limit.side_price_Limit_Float": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionifunctioniobservableiorder_from_ifunctionfloat_from_ifunctionside.IFunctionIFunctionIObservableIOrder_from_IFunctionfloat_from_IFunctionSide"
        ],
        "properties": {
            "volume": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n<p>Limit orders ask to buy or sell some asset at price better than some limit price.\nIf a limit order is not competely fulfilled\nit remains in an order book waiting to be matched with another order.</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy._tradeifprofitable.TradeIfProfitable_ISingleAssetStrategyISingleAssetStrategyIAccountIAccountFloat": {
        "castsTo": [
            "marketsim.gen._out._isingleassetstrategy.ISingleAssetStrategy"
        ],
        "properties": {
            "performance": {
                "type": "marketsim.gen._out._ifunction._ifunctionifunctionfloat_from_iaccount.IFunctionIFunctionfloat_from_IAccount"
            },
            "account": {
                "type": "marketsim.gen._out._ifunction._ifunctioniaccount_from_isingleassetstrategy.IFunctionIAccount_from_ISingleAssetStrategy"
            },
            "inner": {
                "type": "marketsim.gen._out._isingleassetstrategy.ISingleAssetStrategy"
            }
        },
        "description": "<div class=\"document\">\n<p>and if it is considered as good, sends orders</p>\n</div>\n"
    },
    "marketsim.gen._out._test.in1.in2._intfunc.IntFunc_": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out._true.true_": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.ops._less.Less_FloatFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool",
            "marketsim.gen._out._iobservable._iobservablebool.IObservablebool",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "y": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            },
            "x": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math._source.Source_mathRSI": {
        "castsTo": [],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.math._rsi.RSI_IObservableFloatFloatFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.side._signal.Signal_FloatFloat": {
        "castsTo": [
            "marketsim.gen._out.strategy.side._signal.Signal_FloatFloat"
        ],
        "properties": {
            "threshold": {
                "type": "_parseFloat"
            },
            "source": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.ops._condition.Condition_BooleanIObservableFloatFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "ifpart": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            },
            "elsepart": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            },
            "cond": {
                "type": "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._curried._price_peg.price_Peg_FloatIObservableIOrder": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionfloat.IFunctionIObservableIOrder_from_IFunctionfloat"
        ],
        "properties": {
            "proto": {
                "type": "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionfloat.IFunctionIObservableIOrder_from_IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n<p>A peg order is a particular case of the floating price order\nwith the price better at one tick than the best price of the order queue.\nIt implies that if several peg orders are sent to the same order queue\nthey start to race until being matched against the counterparty orders.</p>\n</div>\n"
    },
    "marketsim.gen._out.math._max.Max_IObservableFloatFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "y": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            },
            "x": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            }
        },
        "description": "<div class=\"document\">\n<p>If <em>x</em> or/and <em>y</em> are observables, <em>Min</em> is also observable</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy.side._side.Side_strategysideCrossingAverages": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionside.IFunctionSide"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.side._crossingaverages.CrossingAverages_FloatFloatFloatIOrderBook"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.side._fundamental_value.Fundamental_Value_strategysideFundamentalValue": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.side._fundamentalvalue.FundamentalValue_Float"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.ops._equal.Equal_FloatFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool",
            "marketsim.gen._out._iobservable._iobservablebool.IObservablebool",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "y": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            },
            "x": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.price._end.End_strategypriceMarketData": {
        "castsTo": [],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.price._marketdata.MarketData_StringStringStringFloatFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.event._every.Every_Float": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent"
        ],
        "properties": {
            "intervalFunc": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy._arbitrage.Arbitrage_": {
        "castsTo": [
            "marketsim.gen._out._imultiassetstrategy.IMultiAssetStrategy"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n<p>It believes that these assets represent a single asset traded on different venues\nOnce an ask at one venue becomes lower than a bid at another venue\nit sends market sell and buy orders in order to exploit this arbitrage possibility</p>\n</div>\n"
    },
    "marketsim.gen._out.trader._efficiencytrend.EfficiencyTrend_IAccountFloat": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
        ],
        "properties": {
            "alpha": {
                "type": "_parseFloat"
            },
            "trader": {
                "type": "marketsim.gen._out._iaccount.IAccount"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math._rsi.RSI_IObservableFloatFloatFloat": {
        "castsTo": [
            "marketsim.gen._out.math._rsi.RSI_IObservableFloatFloatFloat"
        ],
        "properties": {
            "source": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
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
    "marketsim.gen._out.strategy.price._onesidestrategy.OneSideStrategy_strategypriceLiquidityProviderIEventSideFloatIObservableIOrderIObservableSide": {
        "castsTo": [
            "marketsim.gen._out._isingleassetstrategy.ISingleAssetStrategy"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.price._liquidityprovider.LiquidityProvider_FloatFloatIOrderBook"
            },
            "eventGen": {
                "type": "marketsim.gen._out._ievent.IEvent"
            },
            "orderFactory": {
                "type": "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionsideifunctionfloat.IFunctionIObservableIOrder_from_IFunctionSideIFunctionfloat"
            },
            "side": {
                "type": "marketsim.gen._out._iobservable._iobservableside.IObservableSide"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.side._side.Side_strategysideSignal": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionside.IFunctionSide"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.side._signal.Signal_FloatFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.side._pairtrading.PairTrading_IOrderBookFloat": {
        "castsTo": [
            "marketsim.gen._out.strategy.side._pairtrading.PairTrading_IOrderBookFloat"
        ],
        "properties": {
            "bookToDependOn": {
                "type": "marketsim.gen._out._iorderbook.IOrderBook"
            },
            "factor": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._curried._price_limit.price_Limit_SideFloat": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionfloat.IFunctionIObservableIOrder_from_IFunctionfloat"
        ],
        "properties": {
            "volume": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            },
            "side": {
                "type": "marketsim.gen._out._ifunction._ifunctionside.IFunctionSide"
            }
        },
        "description": "<div class=\"document\">\n<p>Limit orders ask to buy or sell some asset at price better than some limit price.\nIf a limit order is not competely fulfilled\nit remains in an order book waiting to be matched with another order.</p>\n</div>\n"
    },
    "marketsim.gen._out.order._peg.Peg_FloatIObservableIOrder": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._iobservable._iobservableiorder.IObservableIOrder",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "proto": {
                "type": "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionfloat.IFunctionIObservableIOrder_from_IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n<p>A peg order is a particular case of the floating price order\nwith the price better at one tick than the best price of the order queue.\nIt implies that if several peg orders are sent to the same order queue\nthey start to race until being matched against the counterparty orders.</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy.side._threshold.Threshold_strategysideSignal": {
        "castsTo": [],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.side._signal.Signal_FloatFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.side._book.book_strategysideMeanReversion": {
        "castsTo": [
            "marketsim.gen._out._iorderbook.IOrderBook"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.side._meanreversion.MeanReversion_Float"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.side._signal_value.Signal_Value_strategysideRSIbis": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.side._rsibis.RSIbis_FloatFloatFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math._randomwalk.RandomWalk_FloatFloatFloatString": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "deltaDistr": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            },
            "initialValue": {
                "type": "_parseFloat"
            },
            "intervalDistr": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            },
            "name": {
                "type": "identity"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._curried._side_price_immediateorcancel.side_price_ImmediateOrCancel_SideFloatIObservableIOrder": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionifunctioniobservableiorder_from_ifunctionfloat_from_ifunctionside.IFunctionIFunctionIObservableIOrder_from_IFunctionfloat_from_IFunctionSide"
        ],
        "properties": {
            "proto": {
                "type": "marketsim.gen._out._ifunction._ifunctionifunctioniobservableiorder_from_ifunctionfloat_from_ifunctionside.IFunctionIFunctionIObservableIOrder_from_IFunctionfloat_from_IFunctionSide"
            }
        },
        "description": "<div class=\"document\">\n<p>Immediate-Or-Cancel order sends an underlying order to the market and\nimmediately sends a cancel request for it.\nIt allows to combine market and limit order behaviour:\nthe order is either executed immediately\nat price equal or better than given one\neither it is cancelled (and consequently never stored in the order queue).</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy.side._threshold.Threshold_strategysideTrendFollower": {
        "castsTo": [],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.side._trendfollower.TrendFollower_FloatFloatIOrderBook"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.weight._atanpow.AtanPow_FloatFloat": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
        ],
        "properties": {
            "base": {
                "type": "_parseFloat"
            },
            "f": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.ops._lessequal.LessEqual_FloatFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool",
            "marketsim.gen._out._iobservable._iobservablebool.IObservablebool",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "y": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            },
            "x": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.account.inner._inner_real.inner_Real_": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctioniaccount_from_isingleassetstrategy.IFunctionIAccount_from_ISingleAssetStrategy"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n<p>how orders sent by the strategy have been actually traded</p>\n</div>\n"
    },
    "marketsim.gen._out.math._stddev.StdDev_mathEW": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.math._ew.EW_IObservableFloatFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.side._source.Source_strategysideSignal": {
        "castsTo": [],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.side._signal.Signal_FloatFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.ops._add.Add_FloatFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "y": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            },
            "x": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math.random._vonmisesvariate.vonmisesvariate_FloatFloat": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
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
    "marketsim.gen._out.math._sqr.Sqr_Float": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.ops._condition.Condition_BooleanIObservableFloatIObservableFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "ifpart": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            },
            "elsepart": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            },
            "cond": {
                "type": "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._curried._sideprice_immediateorcancel.sideprice_ImmediateOrCancel_SideFloatIObservableIOrder": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionsideifunctionfloat.IFunctionIObservableIOrder_from_IFunctionSideIFunctionfloat"
        ],
        "properties": {
            "proto": {
                "type": "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionsideifunctionfloat.IFunctionIObservableIOrder_from_IFunctionSideIFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n<p>Immediate-Or-Cancel order sends an underlying order to the market and\nimmediately sends a cancel request for it.\nIt allows to combine market and limit order behaviour:\nthe order is either executed immediately\nat price equal or better than given one\neither it is cancelled (and consequently never stored in the order queue).</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy.price._pricedistr.PriceDistr_strategypriceLiquidityProvider": {
        "castsTo": [],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.price._liquidityprovider.LiquidityProvider_FloatFloatIOrderBook"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.side._fv.Fv_strategysideFundamentalValue": {
        "castsTo": [],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.side._fundamentalvalue.FundamentalValue_Float"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.ops._condition.Condition_BooleanSideSide": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionside.IFunctionSide",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject",
            "marketsim.gen._out._iobservable._iobservableside.IObservableSide"
        ],
        "properties": {
            "ifpart": {
                "type": "marketsim.gen._out._ifunction._ifunctionside.IFunctionSide"
            },
            "elsepart": {
                "type": "marketsim.gen._out._ifunction._ifunctionside.IFunctionSide"
            },
            "cond": {
                "type": "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.side._observablenothing.observableNothing_": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionside.IFunctionSide",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject",
            "marketsim.gen._out._iobservable._iobservableside.IObservableSide"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.ops._add.Add_IObservableFloatIObservableFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "y": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            },
            "x": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math._value.Value_mathmacd": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.math._macd.macd_IObservableFloatFloatFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math._lagged.Lagged_IObservableFloatFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "source": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            },
            "timeframe": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n<p>so Lagged(x, dt)(t0+dt) == x(t0)</p>\n</div>\n"
    },
    "marketsim.gen._out.order._immediateorcancel.ImmediateOrCancel_IObservableIOrder": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._iobservable._iobservableiorder.IObservableIOrder",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "proto": {
                "type": "marketsim.gen._out._iobservable._iobservableiorder.IObservableIOrder"
            }
        },
        "description": "<div class=\"document\">\n<p>Immediate-Or-Cancel order sends an underlying order to the market and\nimmediately sends a cancel request for it.\nIt allows to combine market and limit order behaviour:\nthe order is either executed immediately\nat price equal or better than given one\neither it is cancelled (and consequently never stored in the order queue).</p>\n</div>\n"
    },
    "marketsim.gen._out.orderbook._bids.Bids_IOrderBook": {
        "castsTo": [
            "marketsim.gen._out._iorderqueue.IOrderQueue"
        ],
        "properties": {
            "book": {
                "type": "marketsim.gen._out._iorderbook.IOrderBook"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math._avg.Avg_mathCumulative": {
        "castsTo": [
            "marketsim.gen._out._idifferentiable.IDifferentiable",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.math._cumulative.Cumulative_IObservableFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.weight.f._f_atanpow.f_AtanPow_Float": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionifunctionfloat_from_ifunctionfloat.IFunctionIFunctionfloat_from_IFunctionfloat"
        ],
        "properties": {
            "base": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.side._book.Book_strategysideCrossingAverages": {
        "castsTo": [],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.side._crossingaverages.CrossingAverages_FloatFloatFloatIOrderBook"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math._minepsilon.MinEpsilon_mathCumulativeFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.math._cumulative.Cumulative_IObservableFloat"
            },
            "epsilon": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n<p>It fires updates only if <em>source</em> value becomes less than the old value minus <em>epsilon</em></p>\n</div>\n"
    },
    "marketsim.gen._out.math._source.Source_mathMoving": {
        "castsTo": [],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.math._moving.Moving_IObservableFloatFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._curried._sideprice_iceberg.sideprice_Iceberg_SideFloatIObservableIOrderFloat": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionsideifunctionfloat.IFunctionIObservableIOrder_from_IFunctionSideIFunctionfloat"
        ],
        "properties": {
            "lotSize": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            },
            "proto": {
                "type": "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionsideifunctionfloat.IFunctionIObservableIOrder_from_IFunctionSideIFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n<p>Iceberg order is initialized by an underlying order and a lot size.\nIt sends consequently pieces of the underlying order of size equal or less to the lot size\nthus maximum lot size volume is visible at the market at any moment.</p>\n</div>\n"
    },
    "marketsim.gen._out.ops._lessequal.LessEqual_FloatIObservableFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool",
            "marketsim.gen._out._iobservable._iobservablebool.IObservablebool",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "y": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            },
            "x": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._curried._sideprice_peg.sideprice_Peg_SideFloatIObservableIOrder": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionsideifunctionfloat.IFunctionIObservableIOrder_from_IFunctionSideIFunctionfloat"
        ],
        "properties": {
            "proto": {
                "type": "marketsim.gen._out._ifunction._ifunctionifunctioniobservableiorder_from_ifunctionfloat_from_ifunctionside.IFunctionIFunctionIObservableIOrder_from_IFunctionfloat_from_IFunctionSide"
            }
        },
        "description": "<div class=\"document\">\n<p>A peg order is a particular case of the floating price order\nwith the price better at one tick than the best price of the order queue.\nIt implies that if several peg orders are sent to the same order queue\nthey start to race until being matched against the counterparty orders.</p>\n</div>\n"
    },
    "marketsim.gen._out.trader._pendingvolume.PendingVolume_IAccount": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "trader": {
                "type": "marketsim.gen._out._iaccount.IAccount"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out._test.in1.in2._f.F_Float": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.side._buy.Buy_": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionside.IFunctionSide"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.side._threshold.Threshold_strategysideRSIbis": {
        "castsTo": [],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.side._rsibis.RSIbis_FloatFloatFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.orderbook._twowaylink.TwoWayLink_ILinkILink": {
        "castsTo": [
            "marketsim.gen._out._itwowaylink.ITwoWayLink"
        ],
        "properties": {
            "down": {
                "type": "marketsim.gen._out._ilink.ILink"
            },
            "up": {
                "type": "marketsim.gen._out._ilink.ILink"
            }
        },
        "description": "<div class=\"document\">\n<p>(normally between a trader and a market).\nEnsures that sending packets via links preserves their order.\nHolds two one-way links in opposite directions.</p>\n</div>\n"
    },
    "marketsim.gen._out.order._curried._sideprice_stoploss.sideprice_StopLoss_SideFloatIObservableIOrderFloat": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionsideifunctionfloat.IFunctionIObservableIOrder_from_IFunctionSideIFunctionfloat"
        ],
        "properties": {
            "maxloss": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            },
            "proto": {
                "type": "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionsideifunctionfloat.IFunctionIObservableIOrder_from_IFunctionSideIFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n<p>StopLoss order is initialised by an underlying order and a maximal acceptable loss factor.\nIt keeps track of position and balance change induced by trades of the underlying order and\nif losses from keeping the position exceed certain limit (given by maximum loss factor),\nthe meta order clears its position.</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy.price._volume.Volume_strategypriceMarketMaker": {
        "castsTo": [],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.price._marketmaker.MarketMaker_FloatFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.side._side.Side_strategysideTrendFollower": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionside.IFunctionSide"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.side._trendfollower.TrendFollower_FloatFloatIOrderBook"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.ops._mul.Mul_FloatIObservableFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "y": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            },
            "x": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.trader._roughpnl.RoughPnL_IAccount": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "trader": {
                "type": "marketsim.gen._out._iaccount.IAccount"
            }
        },
        "description": "<div class=\"document\">\n<p>It takes into account only the best price of the order queue</p>\n</div>\n"
    },
    "marketsim.gen._out.math.random._uniform.uniform_FloatFloat": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
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
    "marketsim.gen._out._test.in1.in2._s2.S2_": {
        "castsTo": [
            "identity"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.ops._lessequal.LessEqual_IObservableFloatIObservableFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool",
            "marketsim.gen._out._iobservable._iobservablebool.IObservablebool",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "y": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            },
            "x": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy._canceller.Canceller_Float": {
        "castsTo": [
            "marketsim.gen._out._isingleassetstrategy.ISingleAssetStrategy"
        ],
        "properties": {
            "cancellationIntervalDistr": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n<p>and in some moments of time it randomly chooses an order and cancels it\nNote: a similar effect can be obtained using order.WithExpiry meta orders</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy.side._booktodependon.BookToDependOn_strategysidePairTrading": {
        "castsTo": [],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.side._pairtrading.PairTrading_IOrderBookFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out._ifdefined.IfDefined_FloatIObservableFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "elsePart": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            },
            "x": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.orderbook._local.Local_StringFloatIntListITimeSerie": {
        "castsTo": [
            "marketsim.gen._out._iorderbook.IOrderBook"
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
                    "elementType": "marketsim.gen._out._itimeserie.ITimeSerie"
                }
            }
        },
        "description": "<div class=\"document\">\n<p>Maintains two order queues for orders of different sides</p>\n</div>\n"
    },
    "marketsim.gen._out.ops._condition.Condition_BooleanFloatIObservableFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "ifpart": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            },
            "elsepart": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            },
            "cond": {
                "type": "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.side._strategy.Strategy_strategysideCrossingAveragesIEventSideIObservableIOrder": {
        "castsTo": [
            "marketsim.gen._out._isingleassetstrategy.ISingleAssetStrategy"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.side._crossingaverages.CrossingAverages_FloatFloatFloatIOrderBook"
            },
            "eventGen": {
                "type": "marketsim.gen._out._ievent.IEvent"
            },
            "orderFactory": {
                "type": "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionside.IFunctionIObservableIOrder_from_IFunctionSide"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.side._side.Side_strategysideRSIbis": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionside.IFunctionSide"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.side._rsibis.RSIbis_FloatFloatFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy._choosethebest.ChooseTheBest_ListISingleAssetStrategyISingleAssetStrategyIAccountIAccountFloat": {
        "castsTo": [
            "marketsim.gen._out._isingleassetstrategy.ISingleAssetStrategy"
        ],
        "properties": {
            "strategies": {
                "type": {
                    "elementType": "marketsim.gen._out._isingleassetstrategy.ISingleAssetStrategy"
                }
            },
            "account": {
                "type": "marketsim.gen._out._ifunction._ifunctioniaccount_from_isingleassetstrategy.IFunctionIAccount_from_ISingleAssetStrategy"
            },
            "performance": {
                "type": "marketsim.gen._out._ifunction._ifunctionifunctionfloat_from_iaccount.IFunctionIFunctionfloat_from_IAccount"
            }
        },
        "description": "<div class=\"document\">\n<p>In some moments of time the most effective strategy\nis chosen and made running; other strategies are suspended.\nIt can be considered as a particular case for MultiArmedBandit strategy with\n<em>corrector</em> parameter set to <em>chooseTheBest</em></p>\n</div>\n"
    },
    "marketsim.gen._out.side._sell.Sell_": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionside.IFunctionSide"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.ops._div.Div_IObservableFloatFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "y": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            },
            "x": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.side._alpha.Alpha_strategysideRSIbis": {
        "castsTo": [],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.side._rsibis.RSIbis_FloatFloatFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._curried._side_fixedbudget.side_FixedBudget_Float": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionside.IFunctionIObservableIOrder_from_IFunctionSide"
        ],
        "properties": {
            "budget": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n<p>Fixed budget order acts like a market order\nbut the volume is implicitly given by a budget available for trades.\nInternally first it sends request.EvalVolumesForBudget\nto estimate volumes and prices of orders to sent and\nthen sends a sequence of order.ImmediateOrCancel to be sure that\ncumulative price of trades to be done won't exceed the given budget.</p>\n</div>\n"
    },
    "marketsim.gen._out._false.false_": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.side._side.Side_strategysideMeanReversion": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionside.IFunctionSide",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject",
            "marketsim.gen._out._iobservable._iobservableside.IObservableSide"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.side._meanreversion.MeanReversion_Float"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.side._crossingaverages.CrossingAverages_FloatFloatFloatIOrderBook": {
        "castsTo": [
            "marketsim.gen._out.strategy.side._crossingaverages.CrossingAverages_FloatFloatFloatIOrderBook"
        ],
        "properties": {
            "threshold": {
                "type": "_parseFloat"
            },
            "book": {
                "type": "marketsim.gen._out._iorderbook.IOrderBook"
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
    "marketsim.gen._out._null.null_": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._curried._side_floatingprice.side_FloatingPrice_SideFloatIObservableIOrderIObservableFloat": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionside.IFunctionIObservableIOrder_from_IFunctionSide"
        ],
        "properties": {
            "floatingPrice": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            },
            "proto": {
                "type": "marketsim.gen._out._ifunction._ifunctionifunctioniobservableiorder_from_ifunctionfloat_from_ifunctionside.IFunctionIFunctionIObservableIOrder_from_IFunctionfloat_from_IFunctionSide"
            }
        },
        "description": "<div class=\"document\">\n<p>Floating price order is initialized by an order having a price and an observable that generates new prices.\nWhen the observable value changes the order is cancelled and\na new order with new price is created and sent to the order book.</p>\n</div>\n"
    },
    "marketsim.gen._out.ops._sub.Sub_FloatIObservableFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "y": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            },
            "x": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.ops._greaterequal.GreaterEqual_FloatFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool",
            "marketsim.gen._out._iobservable._iobservablebool.IObservablebool",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "y": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            },
            "x": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.weight.f._f_identityf.f_IdentityF_": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionifunctionfloat_from_ifunctionfloat.IFunctionIFunctionfloat_from_IFunctionfloat"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.orderbook._safesideprice.SafeSidePrice_IOrderQueueFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "queue": {
                "type": "marketsim.gen._out._iorderqueue.IOrderQueue"
            },
            "defaultValue": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n<p>and <em>defaultValue</em> if there haven't been any trades</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy.price._oneside.OneSide_strategypriceMarketDataSideFloat": {
        "castsTo": [
            "marketsim.gen._out._isingleassetstrategy.ISingleAssetStrategy"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.price._marketdata.MarketData_StringStringStringFloatFloat"
            },
            "side": {
                "type": "marketsim.gen._out._ifunction._ifunctionside.IFunctionSide"
            },
            "sign": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._market.Market_SideFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._iobservable._iobservableiorder.IObservableIOrder",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "volume": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            },
            "side": {
                "type": "marketsim.gen._out._ifunction._ifunctionside.IFunctionSide"
            }
        },
        "description": "<div class=\"document\">\n<p>Market order intructs buy or sell given volume immediately</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy.side._side_distribution.Side_distribution_strategysideNoise": {
        "castsTo": [],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.side._noise.Noise_Float"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.ops._greater.Greater_IObservableFloatIObservableFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool",
            "marketsim.gen._out._iobservable._iobservablebool.IObservablebool",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "y": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            },
            "x": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.ops._negate.Negate_IObservableFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.weight.trader._trader_traderefficiencytrend.trader_TraderEfficiencyTrend_Float": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionifunctionfloat_from_iaccount.IFunctionIFunctionfloat_from_IAccount"
        ],
        "properties": {
            "alpha": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.ops._greaterequal.GreaterEqual_IObservableFloatIObservableFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool",
            "marketsim.gen._out._iobservable._iobservablebool.IObservablebool",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "y": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            },
            "x": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math._ew.EW_IObservableFloatFloat": {
        "castsTo": [
            "marketsim.gen._out.math._ew.EW_IObservableFloatFloat"
        ],
        "properties": {
            "source": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            },
            "alpha": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._withexpiry.WithExpiry_IObservableIOrderFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._iobservable._iobservableiorder.IObservableIOrder",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "proto": {
                "type": "marketsim.gen._out._iobservable._iobservableiorder.IObservableIOrder"
            },
            "expiry": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n<p>WithExpiry orders can be viewed as ImmediateOrCancel orders\nwhere cancel order is sent not immediately but after some delay</p>\n</div>\n"
    },
    "marketsim.gen._out.math._maximum.Maximum_mathMoving": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.math._moving.Moving_IObservableFloatFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.price._book.Book_strategypriceLiquidityProvider": {
        "castsTo": [],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.price._liquidityprovider.LiquidityProvider_FloatFloatIOrderBook"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._curried._side_price_withexpiry.side_price_WithExpiry_SideFloatIObservableIOrderFloat": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionifunctioniobservableiorder_from_ifunctionfloat_from_ifunctionside.IFunctionIFunctionIObservableIOrder_from_IFunctionfloat_from_IFunctionSide"
        ],
        "properties": {
            "proto": {
                "type": "marketsim.gen._out._ifunction._ifunctionifunctioniobservableiorder_from_ifunctionfloat_from_ifunctionside.IFunctionIFunctionIObservableIOrder_from_IFunctionfloat_from_IFunctionSide"
            },
            "expiry": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n<p>WithExpiry orders can be viewed as ImmediateOrCancel orders\nwhere cancel order is sent not immediately but after some delay</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy.position._timeframe.Timeframe_strategypositionRSI_linear": {
        "castsTo": [],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.position._rsi_linear.RSI_linear_FloatIObservableFloatFloatISingleAssetTrader"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._curried._side_price_stoploss.side_price_StopLoss_SideFloatIObservableIOrderFloat": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionifunctioniobservableiorder_from_ifunctionfloat_from_ifunctionside.IFunctionIFunctionIObservableIOrder_from_IFunctionfloat_from_IFunctionSide"
        ],
        "properties": {
            "maxloss": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            },
            "proto": {
                "type": "marketsim.gen._out._ifunction._ifunctionifunctioniobservableiorder_from_ifunctionfloat_from_ifunctionside.IFunctionIFunctionIObservableIOrder_from_IFunctionfloat_from_IFunctionSide"
            }
        },
        "description": "<div class=\"document\">\n<p>StopLoss order is initialised by an underlying order and a maximal acceptable loss factor.\nIt keeps track of position and balance change induced by trades of the underlying order and\nif losses from keeping the position exceed certain limit (given by maximum loss factor),\nthe meta order clears its position.</p>\n</div>\n"
    },
    "marketsim.gen._out.ops._sub.Sub_IObservableFloatFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "y": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            },
            "x": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.trader._position.Position_IAccount": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "trader": {
                "type": "marketsim.gen._out._iaccount.IAccount"
            }
        },
        "description": "<div class=\"document\">\n<p>It is negative if trader has sold more assets than has bought and\npositive otherwise</p>\n</div>\n"
    },
    "marketsim.gen._out.observable._quote.Quote_StringStringString": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
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
    "marketsim.gen._out.strategy.side._alpha_1.Alpha_1_strategysideCrossingAverages": {
        "castsTo": [],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.side._crossingaverages.CrossingAverages_FloatFloatFloatIOrderBook"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math._stddev.StdDev_mathMoving": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.math._moving.Moving_IObservableFloatFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math._atan.Atan_Float": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.side._book.Book_strategysideTrendFollower": {
        "castsTo": [],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.side._trendfollower.TrendFollower_FloatFloatIOrderBook"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.side._book.book_strategysidePairTrading": {
        "castsTo": [
            "marketsim.gen._out._iorderbook.IOrderBook"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.side._pairtrading.PairTrading_IOrderBookFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.ops._greater.Greater_FloatFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool",
            "marketsim.gen._out._iobservable._iobservablebool.IObservablebool",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "y": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            },
            "x": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.orderbook._ticksize.TickSize_IOrderBook": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
        ],
        "properties": {
            "book": {
                "type": "marketsim.gen._out._iorderbook.IOrderBook"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math._timeframe.Timeframe_mathRSI": {
        "castsTo": [],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.math._rsi.RSI_IObservableFloatFloatFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.registry.Simulation": {
        "castsTo": [],
        "properties": {
            "traders": {
                "type": {
                    "elementType": "marketsim.gen._out._itrader.ITrader"
                }
            },
            "graphs": {
                "type": {
                    "elementType": "marketsim.gen._out._igraph.IGraph"
                }
            },
            "orderbooks": {
                "type": {
                    "elementType": "marketsim.gen._out._iorderbook.IOrderBook"
                }
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math._max.Max_FloatFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "y": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            },
            "x": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n<p>If <em>x</em> or/and <em>y</em> are observables, <em>Min</em> is also observable</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy.side._book.book_strategysideFundamentalValue": {
        "castsTo": [
            "marketsim.gen._out._iorderbook.IOrderBook"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.side._fundamentalvalue.FundamentalValue_Float"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math.random._lognormvariate.lognormvariate_FloatFloat": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
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
    "marketsim.gen._out.math._var.Var_mathEW": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.math._ew.EW_IObservableFloatFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.ops._condition.Condition_IObservableBooleanSideSide": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionside.IFunctionSide",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject",
            "marketsim.gen._out._iobservable._iobservableside.IObservableSide"
        ],
        "properties": {
            "ifpart": {
                "type": "marketsim.gen._out._ifunction._ifunctionside.IFunctionSide"
            },
            "elsepart": {
                "type": "marketsim.gen._out._ifunction._ifunctionside.IFunctionSide"
            },
            "cond": {
                "type": "marketsim.gen._out._iobservable._iobservablebool.IObservablebool"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out._test.overloading._h.h_": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._curried._side_peg.side_Peg_SideFloatIObservableIOrder": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionside.IFunctionIObservableIOrder_from_IFunctionSide"
        ],
        "properties": {
            "proto": {
                "type": "marketsim.gen._out._ifunction._ifunctionifunctioniobservableiorder_from_ifunctionfloat_from_ifunctionside.IFunctionIFunctionIObservableIOrder_from_IFunctionfloat_from_IFunctionSide"
            }
        },
        "description": "<div class=\"document\">\n<p>A peg order is a particular case of the floating price order\nwith the price better at one tick than the best price of the order queue.\nIt implies that if several peg orders are sent to the same order queue\nthey start to race until being matched against the counterparty orders.</p>\n</div>\n"
    },
    "marketsim.gen._out.math._stddev.StdDev_mathCumulative": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.math._cumulative.Cumulative_IObservableFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.side._rsibis.RSIbis_FloatFloatFloat": {
        "castsTo": [
            "marketsim.gen._out.strategy.side._rsibis.RSIbis_FloatFloatFloat"
        ],
        "properties": {
            "threshold": {
                "type": "_parseFloat"
            },
            "alpha": {
                "type": "_parseFloat"
            },
            "timeframe": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math._timeframe.Timeframe_mathMoving": {
        "castsTo": [],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.math._moving.Moving_IObservableFloatFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out._ifdefined.IfDefined_IObservableFloatFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "elsePart": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            },
            "x": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.ops._mul.Mul_FloatFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "y": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            },
            "x": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math._moving.Moving_IObservableFloatFloat": {
        "castsTo": [
            "marketsim.gen._out.math._moving.Moving_IObservableFloatFloat"
        ],
        "properties": {
            "source": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            },
            "timeframe": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.weight._choosethebest.ChooseTheBest_ListFloat": {
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
    "marketsim.gen._out.math._source.Source_mathmacd": {
        "castsTo": [],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.math._macd.macd_IObservableFloatFloatFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._curried._side_price_peg.side_price_Peg_SideFloatIObservableIOrder": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionifunctioniobservableiorder_from_ifunctionfloat_from_ifunctionside.IFunctionIFunctionIObservableIOrder_from_IFunctionfloat_from_IFunctionSide"
        ],
        "properties": {
            "proto": {
                "type": "marketsim.gen._out._ifunction._ifunctionifunctioniobservableiorder_from_ifunctionfloat_from_ifunctionside.IFunctionIFunctionIObservableIOrder_from_IFunctionfloat_from_IFunctionSide"
            }
        },
        "description": "<div class=\"document\">\n<p>A peg order is a particular case of the floating price order\nwith the price better at one tick than the best price of the order queue.\nIt implies that if several peg orders are sent to the same order queue\nthey start to race until being matched against the counterparty orders.</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy.position._position.Position_strategypositionBollinger_linear": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.position._bollinger_linear.Bollinger_linear_FloatIObservableFloatISingleAssetTrader"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy._array.Array_ListISingleAssetStrategy": {
        "castsTo": [
            "marketsim.gen._out._isingleassetstrategy.ISingleAssetStrategy"
        ],
        "properties": {
            "strategies": {
                "type": {
                    "elementType": "marketsim.gen._out._isingleassetstrategy.ISingleAssetStrategy"
                }
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math._histogram.Histogram_mathmacdFloatFloat": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.math._macd.macd_IObservableFloatFloatFloat"
            },
            "step": {
                "type": "_parseFloat"
            },
            "timeframe": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math._relstddev.RelStdDev_mathEW": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.math._ew.EW_IObservableFloatFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out._constant.constant_Int": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
        ],
        "properties": {
            "x": {
                "type": "_parseInt"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.ops._equal.Equal_IObservableFloatFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool",
            "marketsim.gen._out._iobservable._iobservablebool.IObservablebool",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "y": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            },
            "x": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.price._oneside.OneSide_strategypriceMarketDataIObservableSideFloat": {
        "castsTo": [
            "marketsim.gen._out._isingleassetstrategy.ISingleAssetStrategy"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.price._marketdata.MarketData_StringStringStringFloatFloat"
            },
            "side": {
                "type": "marketsim.gen._out._iobservable._iobservableside.IObservableSide"
            },
            "sign": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.side._nothing.Nothing_": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionside.IFunctionSide"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math._macd.macd_IObservableFloatFloatFloat": {
        "castsTo": [
            "marketsim.gen._out.math._macd.macd_IObservableFloatFloatFloat"
        ],
        "properties": {
            "source": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
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
    "marketsim.gen._out.strategy.price._start.Start_strategypriceMarketData": {
        "castsTo": [],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.price._marketdata.MarketData_StringStringStringFloatFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.price._twosides.TwoSides_strategypriceMarketData": {
        "castsTo": [
            "marketsim.gen._out._isingleassetstrategy.ISingleAssetStrategy"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.price._marketdata.MarketData_StringStringStringFloatFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math._min.Min_FloatIObservableFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "y": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            },
            "x": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n<p>If <em>x</em> or/and <em>y</em> are observables, <em>Min</em> is also observable</p>\n</div>\n"
    },
    "marketsim.gen._out.order._limit.Limit_SideFloatFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._iobservable._iobservableiorder.IObservableIOrder",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "volume": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            },
            "price": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            },
            "side": {
                "type": "marketsim.gen._out._ifunction._ifunctionside.IFunctionSide"
            }
        },
        "description": "<div class=\"document\">\n<p>Limit orders ask to buy or sell some asset at price better than some limit price.\nIf a limit order is not competely fulfilled\nit remains in an order book waiting to be matched with another order.</p>\n</div>\n"
    },
    "marketsim.gen._out._constant.constant_Float": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
        ],
        "properties": {
            "x": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out._test.in1.in2._s1.S1_String": {
        "castsTo": [
            "identity"
        ],
        "properties": {
            "y": {
                "type": "identity"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out._const.const_Int": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "x": {
                "type": "_parseInt"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out._const.const_Float": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "x": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.price._marketmaker.MarketMaker_FloatFloat": {
        "castsTo": [
            "marketsim.gen._out.strategy.price._marketmaker.MarketMaker_FloatFloat"
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
    "marketsim.gen._out.strategy.side._meanreversion.MeanReversion_Float": {
        "castsTo": [
            "marketsim.gen._out.strategy.side._meanreversion.MeanReversion_Float"
        ],
        "properties": {
            "alpha": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.ops._greaterequal.GreaterEqual_IObservableFloatFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool",
            "marketsim.gen._out._iobservable._iobservablebool.IObservablebool",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "y": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            },
            "x": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.account._real.Real_ISingleAssetStrategy": {
        "castsTo": [
            "marketsim.gen._out._iaccount.IAccount"
        ],
        "properties": {
            "inner": {
                "type": "marketsim.gen._out._isingleassetstrategy.ISingleAssetStrategy"
            }
        },
        "description": "<div class=\"document\">\n<p>how orders sent by the strategy have been actually traded</p>\n</div>\n"
    },
    "marketsim.gen._out.ops._div.Div_FloatIObservableFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "y": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            },
            "x": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.side._fundamentalvalue.FundamentalValue_Float": {
        "castsTo": [
            "marketsim.gen._out.strategy.side._fundamentalvalue.FundamentalValue_Float"
        ],
        "properties": {
            "fv": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.weight._unit.Unit_IAccount": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
        ],
        "properties": {
            "trader": {
                "type": "marketsim.gen._out._iaccount.IAccount"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._curried._price_immediateorcancel.price_ImmediateOrCancel_FloatIObservableIOrder": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionfloat.IFunctionIObservableIOrder_from_IFunctionfloat"
        ],
        "properties": {
            "proto": {
                "type": "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionfloat.IFunctionIObservableIOrder_from_IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n<p>Immediate-Or-Cancel order sends an underlying order to the market and\nimmediately sends a cancel request for it.\nIt allows to combine market and limit order behaviour:\nthe order is either executed immediately\nat price equal or better than given one\neither it is cancelled (and consequently never stored in the order queue).</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy.price._oneside.OneSide_strategypriceMarketMakerIObservableSideFloat": {
        "castsTo": [
            "marketsim.gen._out._isingleassetstrategy.ISingleAssetStrategy"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.price._marketmaker.MarketMaker_FloatFloat"
            },
            "side": {
                "type": "marketsim.gen._out._iobservable._iobservableside.IObservableSide"
            },
            "sign": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.ops._condition.Condition_IObservableBooleanIObservableSideSide": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionside.IFunctionSide",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject",
            "marketsim.gen._out._iobservable._iobservableside.IObservableSide"
        ],
        "properties": {
            "ifpart": {
                "type": "marketsim.gen._out._iobservable._iobservableside.IObservableSide"
            },
            "elsepart": {
                "type": "marketsim.gen._out._ifunction._ifunctionside.IFunctionSide"
            },
            "cond": {
                "type": "marketsim.gen._out._iobservable._iobservablebool.IObservablebool"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out._ifdefined.IfDefined_FloatFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "elsePart": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            },
            "x": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.price._marketdata.MarketData_StringStringStringFloatFloat": {
        "castsTo": [
            "marketsim.gen._out.strategy.price._marketdata.MarketData_StringStringStringFloatFloat"
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
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.orderbook._proxy.Proxy_": {
        "castsTo": [
            "marketsim.gen._out._iorderbook.IOrderBook"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n<p>May be used only in objects held by orderbooks (so it is normally used in orderbook properties)</p>\n</div>\n"
    },
    "marketsim.gen._out.ops._condition.Condition_IObservableBooleanFloatFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "ifpart": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            },
            "elsepart": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            },
            "cond": {
                "type": "marketsim.gen._out._iobservable._iobservablebool.IObservablebool"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.side._factor.Factor_strategysidePairTrading": {
        "castsTo": [],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.side._pairtrading.PairTrading_IOrderBookFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.orderbook._bestprice.BestPrice_IOrderQueue": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "queue": {
                "type": "marketsim.gen._out._iorderqueue.IOrderQueue"
            }
        },
        "description": "<div class=\"document\">\n<p>Returns None is <em>queue</em> is empty</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy.position._position.Position_strategypositionRSI_linear": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.position._rsi_linear.RSI_linear_FloatIObservableFloatFloatISingleAssetTrader"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.orderbook._lasttradeprice.LastTradePrice_IOrderQueue": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "queue": {
                "type": "marketsim.gen._out._iorderqueue.IOrderQueue"
            }
        },
        "description": "<div class=\"document\">\n<p>Returns None if there haven't been any trades</p>\n</div>\n"
    },
    "marketsim.gen._out.order._curried._price_floatingprice.price_FloatingPrice_FloatIObservableIOrderIObservableFloat": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionfloat.IFunctionIObservableIOrder_from_IFunctionfloat"
        ],
        "properties": {
            "floatingPrice": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            },
            "proto": {
                "type": "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionfloat.IFunctionIObservableIOrder_from_IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n<p>Floating price order is initialized by an order having a price and an observable that generates new prices.\nWhen the observable value changes the order is cancelled and\na new order with new price is created and sent to the order book.</p>\n</div>\n"
    },
    "marketsim.gen._out.math._avg.Avg_mathMoving": {
        "castsTo": [
            "marketsim.gen._out._idifferentiable.IDifferentiable",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.math._moving.Moving_IObservableFloatFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.account._virtualmarket.VirtualMarket_ISingleAssetStrategy": {
        "castsTo": [
            "marketsim.gen._out._iaccount.IAccount"
        ],
        "properties": {
            "inner": {
                "type": "marketsim.gen._out._isingleassetstrategy.ISingleAssetStrategy"
            }
        },
        "description": "<div class=\"document\">\n<p>how it would be traded by sending request.evalMarketOrder\n(note: orders sent by a strategy wrapped into an adaptive strategy may not come to the market\nbut we want evaluate in any case would it be profitable or not)</p>\n</div>\n"
    },
    "marketsim.gen._out.orderbook._weightedprice.WeightedPrice_IOrderQueueFloat": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
        ],
        "properties": {
            "queue": {
                "type": "marketsim.gen._out._iorderqueue.IOrderQueue"
            },
            "alpha": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.side._side.Side_strategysidePairTrading": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionside.IFunctionSide",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject",
            "marketsim.gen._out._iobservable._iobservableside.IObservableSide"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.side._pairtrading.PairTrading_IOrderBookFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.ops._greater.Greater_IObservableFloatFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool",
            "marketsim.gen._out._iobservable._iobservablebool.IObservablebool",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "y": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            },
            "x": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.ops._condition.Condition_BooleanFloatFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "ifpart": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            },
            "elsepart": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            },
            "cond": {
                "type": "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math._fast.Fast_mathmacd": {
        "castsTo": [],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.math._macd.macd_IObservableFloatFloatFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.position._rsi_linear.RSI_linear_FloatIObservableFloatFloatISingleAssetTrader": {
        "castsTo": [
            "marketsim.gen._out.strategy.position._rsi_linear.RSI_linear_FloatIObservableFloatFloatISingleAssetTrader"
        ],
        "properties": {
            "alpha": {
                "type": "_parseFloat"
            },
            "k": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            },
            "trader": {
                "type": "marketsim.gen._out._isingleassettrader.ISingleAssetTrader"
            },
            "timeframe": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.ops._condition.Condition_BooleanSideIObservableSide": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionside.IFunctionSide",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject",
            "marketsim.gen._out._iobservable._iobservableside.IObservableSide"
        ],
        "properties": {
            "ifpart": {
                "type": "marketsim.gen._out._ifunction._ifunctionside.IFunctionSide"
            },
            "elsepart": {
                "type": "marketsim.gen._out._iobservable._iobservableside.IObservableSide"
            },
            "cond": {
                "type": "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.price._onesidestrategy.OneSideStrategy_strategypriceLiquidityProviderIEventSideFloatIObservableIOrderSide": {
        "castsTo": [
            "marketsim.gen._out._isingleassetstrategy.ISingleAssetStrategy"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.price._liquidityprovider.LiquidityProvider_FloatFloatIOrderBook"
            },
            "eventGen": {
                "type": "marketsim.gen._out._ievent.IEvent"
            },
            "orderFactory": {
                "type": "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionsideifunctionfloat.IFunctionIObservableIOrder_from_IFunctionSideIFunctionfloat"
            },
            "side": {
                "type": "marketsim.gen._out._ifunction._ifunctionside.IFunctionSide"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.orderbook._oftrader.OfTrader_IAccount": {
        "castsTo": [
            "marketsim.gen._out._iorderbook.IOrderBook"
        ],
        "properties": {
            "Trader": {
                "type": "marketsim.gen._out._iaccount.IAccount"
            }
        },
        "description": "<div class=\"document\">\n<p>May be used only in objects that are held by traders (so it is used in trader properties and strategies)</p>\n</div>\n"
    },
    "marketsim.gen._out.ops._sub.Sub_IObservableFloatIObservableFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "y": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            },
            "x": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.ops._add.Add_IObservableFloatFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "y": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            },
            "x": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._stoploss.StopLoss_IObservableIOrderFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._iobservable._iobservableiorder.IObservableIOrder",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "maxloss": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            },
            "proto": {
                "type": "marketsim.gen._out._iobservable._iobservableiorder.IObservableIOrder"
            }
        },
        "description": "<div class=\"document\">\n<p>StopLoss order is initialised by an underlying order and a maximal acceptable loss factor.\nIt keeps track of position and balance change induced by trades of the underlying order and\nif losses from keeping the position exceed certain limit (given by maximum loss factor),\nthe meta order clears its position.</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy.side._trendfollower.TrendFollower_FloatFloatIOrderBook": {
        "castsTo": [
            "marketsim.gen._out.strategy.side._trendfollower.TrendFollower_FloatFloatIOrderBook"
        ],
        "properties": {
            "threshold": {
                "type": "_parseFloat"
            },
            "alpha": {
                "type": "_parseFloat"
            },
            "book": {
                "type": "marketsim.gen._out._iorderbook.IOrderBook"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out._timeserie.TimeSerie_IObservableAnyIGraphIntInt": {
        "castsTo": [
            "marketsim.gen._out._itimeserie.ITimeSerie"
        ],
        "properties": {
            "_digitsToShow": {
                "hidden": true,
                "type": "_parseInt"
            },
            "source": {
                "type": "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
            },
            "_smooth": {
                "hidden": true,
                "type": "_parseInt"
            },
            "graph": {
                "type": "marketsim.gen._out._igraph.IGraph"
            }
        },
        "description": "<div class=\"document\">\n<p>Used to specify what data should be collected about order books and traders</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy.weight.trader._trader_score.trader_Score_": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionifunctionfloat_from_iaccount.IFunctionIFunctionfloat_from_IAccount"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n<p>Returns difference between them.</p>\n<p>TODO: should be UpScore(timeframe, Efficiency(trader)) - DownScore(timeframe, Efficiency(trader))</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy.weight._score.Score_IAccount": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
        ],
        "properties": {
            "trader": {
                "type": "marketsim.gen._out._iaccount.IAccount"
            }
        },
        "description": "<div class=\"document\">\n<p>Returns difference between them.</p>\n<p>TODO: should be UpScore(timeframe, Efficiency(trader)) - DownScore(timeframe, Efficiency(trader))</p>\n</div>\n"
    },
    "marketsim.gen._out.math._cumulative.Cumulative_IObservableFloat": {
        "castsTo": [
            "marketsim.gen._out.math._cumulative.Cumulative_IObservableFloat"
        ],
        "properties": {
            "source": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.weight.f._f_clamp0.f_Clamp0_": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionifunctionfloat_from_ifunctionfloat.IFunctionIFunctionfloat_from_IFunctionfloat"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.side._threshold.Threshold_strategysideCrossingAverages": {
        "castsTo": [],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.side._crossingaverages.CrossingAverages_FloatFloatFloatIOrderBook"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._curried._side_immediateorcancel.side_ImmediateOrCancel_SideIObservableIOrder": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionside.IFunctionIObservableIOrder_from_IFunctionSide"
        ],
        "properties": {
            "proto": {
                "type": "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionside.IFunctionIObservableIOrder_from_IFunctionSide"
            }
        },
        "description": "<div class=\"document\">\n<p>Immediate-Or-Cancel order sends an underlying order to the market and\nimmediately sends a cancel request for it.\nIt allows to combine market and limit order behaviour:\nthe order is either executed immediately\nat price equal or better than given one\neither it is cancelled (and consequently never stored in the order queue).</p>\n</div>\n"
    },
    "marketsim.gen._out.ops._equal.Equal_FloatIObservableFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool",
            "marketsim.gen._out._iobservable._iobservablebool.IObservablebool",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "y": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            },
            "x": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.weight.array._array_identityl.array_IdentityL_": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionifunctionlistoffloat_from_listoffloat.IFunctionIFunctionlistOffloat_from_listOffloat"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.ops._equal.Equal_IObservableFloatIObservableFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool",
            "marketsim.gen._out._iobservable._iobservablebool.IObservablebool",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "y": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            },
            "x": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy._empty.Empty_": {
        "castsTo": [
            "marketsim.gen._out._isingleassetstrategy.ISingleAssetStrategy"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._curried._sideprice_limit.sideprice_Limit_Float": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionsideifunctionfloat.IFunctionIObservableIOrder_from_IFunctionSideIFunctionfloat"
        ],
        "properties": {
            "volume": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n<p>Limit orders ask to buy or sell some asset at price better than some limit price.\nIf a limit order is not competely fulfilled\nit remains in an order book waiting to be matched with another order.</p>\n</div>\n"
    },
    "marketsim.gen._out.math._upmovements.UpMovements_IObservableFloatFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "source": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            },
            "timeframe": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math._sqr.Sqr_IObservableFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._curried._side_market.side_Market_Float": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionside.IFunctionIObservableIOrder_from_IFunctionSide"
        ],
        "properties": {
            "volume": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n<p>Market order intructs buy or sell given volume immediately</p>\n</div>\n"
    },
    "marketsim.gen._out.ops._notequal.NotEqual_FloatFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool",
            "marketsim.gen._out._iobservable._iobservablebool.IObservablebool",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "y": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            },
            "x": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.js.Graph": {
        "castsTo": [
            "marketsim.gen._out._igraph.IGraph"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n<p>Generic 2D graph to be rendered by means of javascript libraries</p>\n</div>\n"
    },
    "marketsim.gen._out.ops._notequal.NotEqual_FloatIObservableFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool",
            "marketsim.gen._out._iobservable._iobservablebool.IObservablebool",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "y": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            },
            "x": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math._exp.Exp_Float": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.ops._add.Add_FloatIObservableFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "y": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            },
            "x": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.price._delta.Delta_strategypriceMarketData": {
        "castsTo": [],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.price._marketdata.MarketData_StringStringStringFloatFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.weight.trader._trader_traderefficiency.trader_TraderEfficiency_": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionifunctionfloat_from_iaccount.IFunctionIFunctionfloat_from_IAccount"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.side._side.Side_strategysideFundamentalValue": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionside.IFunctionSide",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject",
            "marketsim.gen._out._iobservable._iobservableside.IObservableSide"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.side._fundamentalvalue.FundamentalValue_Float"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.ops._less.Less_IObservableFloatIObservableFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool",
            "marketsim.gen._out._iobservable._iobservablebool.IObservablebool",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "y": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            },
            "x": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy._suspendable.Suspendable_ISingleAssetStrategyBoolean": {
        "castsTo": [
            "marketsim.gen._out._isingleassetstrategy.ISingleAssetStrategy"
        ],
        "properties": {
            "predicate": {
                "type": "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool"
            },
            "inner": {
                "type": "marketsim.gen._out._isingleassetstrategy.ISingleAssetStrategy"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.ops._condition.Condition_IObservableBooleanFloatIObservableFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "ifpart": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            },
            "elsepart": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            },
            "cond": {
                "type": "marketsim.gen._out._iobservable._iobservablebool.IObservablebool"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math._max.Max_IObservableFloatIObservableFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "y": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            },
            "x": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            }
        },
        "description": "<div class=\"document\">\n<p>If <em>x</em> or/and <em>y</em> are observables, <em>Min</em> is also observable</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy.position._trader.Trader_strategypositionRSI_linear": {
        "castsTo": [],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.position._rsi_linear.RSI_linear_FloatIObservableFloatFloatISingleAssetTrader"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math._source.Source_mathCumulative": {
        "castsTo": [],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.math._cumulative.Cumulative_IObservableFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.ops._condition.Condition_BooleanIObservableSideIObservableSide": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionside.IFunctionSide",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject",
            "marketsim.gen._out._iobservable._iobservableside.IObservableSide"
        ],
        "properties": {
            "ifpart": {
                "type": "marketsim.gen._out._iobservable._iobservableside.IObservableSide"
            },
            "elsepart": {
                "type": "marketsim.gen._out._iobservable._iobservableside.IObservableSide"
            },
            "cond": {
                "type": "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.position._desiredposition.DesiredPosition_strategypositionRSI_linear": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.position._rsi_linear.RSI_linear_FloatIObservableFloatFloatISingleAssetTrader"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.price._ticker.Ticker_strategypriceMarketData": {
        "castsTo": [],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.price._marketdata.MarketData_StringStringStringFloatFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.side._strategy.Strategy_strategysideRSIbisIEventSideIObservableIOrder": {
        "castsTo": [
            "marketsim.gen._out._isingleassetstrategy.ISingleAssetStrategy"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.side._rsibis.RSIbis_FloatFloatFloat"
            },
            "eventGen": {
                "type": "marketsim.gen._out._ievent.IEvent"
            },
            "orderFactory": {
                "type": "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionside.IFunctionIObservableIOrder_from_IFunctionSide"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math._min.Min_IObservableFloatIObservableFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "y": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            },
            "x": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            }
        },
        "description": "<div class=\"document\">\n<p>If <em>x</em> or/and <em>y</em> are observables, <em>Min</em> is also observable</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy.position._strategy.Strategy_strategypositionBollinger_linearFloatIObservableIOrder": {
        "castsTo": [
            "marketsim.gen._out._isingleassetstrategy.ISingleAssetStrategy"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.position._bollinger_linear.Bollinger_linear_FloatIObservableFloatISingleAssetTrader"
            },
            "orderFactory": {
                "type": "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionfloat.IFunctionIObservableIOrder_from_IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy._multiarmedbandit.MultiArmedBandit_ListISingleAssetStrategyISingleAssetStrategyIAccountIAccountFloatFloatFloatListFloatListFloat": {
        "castsTo": [
            "marketsim.gen._out._isingleassetstrategy.ISingleAssetStrategy"
        ],
        "properties": {
            "corrector": {
                "type": "marketsim.gen._out._ifunction._ifunctionifunctionlistoffloat_from_listoffloat.IFunctionIFunctionlistOffloat_from_listOffloat"
            },
            "strategies": {
                "type": {
                    "elementType": "marketsim.gen._out._isingleassetstrategy.ISingleAssetStrategy"
                }
            },
            "account": {
                "type": "marketsim.gen._out._ifunction._ifunctioniaccount_from_isingleassetstrategy.IFunctionIAccount_from_ISingleAssetStrategy"
            },
            "normalizer": {
                "type": "marketsim.gen._out._ifunction._ifunctionifunctionfloat_from_ifunctionfloat.IFunctionIFunctionfloat_from_IFunctionfloat"
            },
            "weight": {
                "type": "marketsim.gen._out._ifunction._ifunctionifunctionfloat_from_iaccount.IFunctionIFunctionfloat_from_IAccount"
            }
        },
        "description": "<div class=\"document\">\n<p>In some moments of time the efficiency of the strategies is evaluated\nThese efficiencies are mapped into weights using <em>weight</em> and <em>normilizer</em>\nfunctions per every strategy and <em>corrector</em> for the whole collection of weights\nThese weights are used to choose randomly a strategy to run for the next quant of time.\nAll other strategies are suspended</p>\n</div>\n"
    },
    "marketsim.gen._out.math._relstddev.RelStdDev_mathMoving": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.math._moving.Moving_IObservableFloatFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.side._signal_value.Signal_Value_strategysideCrossingAverages": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.side._crossingaverages.CrossingAverages_FloatFloatFloatIOrderBook"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.ops._condition.Condition_IObservableBooleanIObservableFloatFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "ifpart": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            },
            "elsepart": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            },
            "cond": {
                "type": "marketsim.gen._out._iobservable._iobservablebool.IObservablebool"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out._observabletrue.observableTrue_": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool",
            "marketsim.gen._out._iobservable._iobservablebool.IObservablebool",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math._source.Source_mathEW": {
        "castsTo": [],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.math._ew.EW_IObservableFloatFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math.random._gammavariate.gammavariate_FloatFloat": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
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
    "marketsim.gen._out.orderbook._lastprice.LastPrice_IOrderQueue": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "queue": {
                "type": "marketsim.gen._out._iorderqueue.IOrderQueue"
            }
        },
        "description": "<div class=\"document\">\n<p>Returns None is <em>queue</em> has been always empty</p>\n</div>\n"
    },
    "marketsim.gen._out.ops._negate.Negate_Float": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._iceberg.Iceberg_IObservableIOrderFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._iobservable._iobservableiorder.IObservableIOrder",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "lotSize": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            },
            "proto": {
                "type": "marketsim.gen._out._iobservable._iobservableiorder.IObservableIOrder"
            }
        },
        "description": "<div class=\"document\">\n<p>Iceberg order is initialized by an underlying order and a lot size.\nIt sends consequently pieces of the underlying order of size equal or less to the lot size\nthus maximum lot size volume is visible at the market at any moment.</p>\n</div>\n"
    },
    "marketsim.gen._out.math._slow.Slow_mathmacd": {
        "castsTo": [],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.math._macd.macd_IObservableFloatFloatFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.ops._less.Less_FloatIObservableFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool",
            "marketsim.gen._out._iobservable._iobservablebool.IObservablebool",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "y": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            },
            "x": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.side._alpha.Alpha_strategysideTrendFollower": {
        "castsTo": [],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.side._trendfollower.TrendFollower_FloatFloatIOrderBook"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.price._twosides.TwoSides_strategypriceMarketMaker": {
        "castsTo": [
            "marketsim.gen._out._isingleassetstrategy.ISingleAssetStrategy"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.price._marketmaker.MarketMaker_FloatFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.side._strategy.Strategy_strategysideFundamentalValueIEventSideIObservableIOrder": {
        "castsTo": [
            "marketsim.gen._out._isingleassetstrategy.ISingleAssetStrategy"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.side._fundamentalvalue.FundamentalValue_Float"
            },
            "eventGen": {
                "type": "marketsim.gen._out._ievent.IEvent"
            },
            "orderFactory": {
                "type": "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionside.IFunctionIObservableIOrder_from_IFunctionSide"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math._relstddev.RelStdDev_mathCumulative": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.math._cumulative.Cumulative_IObservableFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math._minimum.Minimum_mathMoving": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.math._moving.Moving_IObservableFloatFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math.random._normalvariate.normalvariate_FloatFloat": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
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
    "marketsim.gen._out.order._limitsigned.LimitSigned_FloatFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._iobservable._iobservableiorder.IObservableIOrder",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "signedVolume": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            },
            "price": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n<p>Limit orders ask to buy or sell some asset at price better than some limit price.\nIf a limit order is not competely fulfilled\nit remains in an order book waiting to be matched with another order.</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy.side._side.Side_strategysideNoise": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionside.IFunctionSide"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.side._noise.Noise_Float"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.side._alpha.Alpha_strategysideMeanReversion": {
        "castsTo": [],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.side._meanreversion.MeanReversion_Float"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.observable._breaksatchanges.BreaksAtChanges_IObservableFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "source": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            }
        },
        "description": "<div class=\"document\">\n<p>When <em>source</em> changes it inserts <em>undefined</em> value and then immidiately becomes equal to <em>source</em> value</p>\n</div>\n"
    },
    "marketsim.gen._out.orderbook._volumelevels.VolumeLevels_IOrderQueueFloatInt": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionivolumelevels.IFunctionIVolumeLevels",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "queue": {
                "type": "marketsim.gen._out._iorderqueue.IOrderQueue"
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
    "marketsim.gen._out.math._downmovements.DownMovements_IObservableFloatFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "source": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            },
            "timeframe": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math._var.Var_mathCumulative": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.math._cumulative.Cumulative_IObservableFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.account.inner._inner_virtualmarket.inner_VirtualMarket_": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctioniaccount_from_isingleassetstrategy.IFunctionIAccount_from_ISingleAssetStrategy"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n<p>how it would be traded by sending request.evalMarketOrder\n(note: orders sent by a strategy wrapped into an adaptive strategy may not come to the market\nbut we want evaluate in any case would it be profitable or not)</p>\n</div>\n"
    },
    "marketsim.gen._out.orderbook._midprice.MidPrice_IOrderBook": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "book": {
                "type": "marketsim.gen._out._iorderbook.IOrderBook"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.observable._oneverydt.OnEveryDt_FloatFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            },
            "dt": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._floatingprice.FloatingPrice_FloatIObservableIOrderIObservableFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._iobservable._iobservableiorder.IObservableIOrder",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "floatingPrice": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            },
            "proto": {
                "type": "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionfloat.IFunctionIObservableIOrder_from_IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n<p>Floating price order is initialized by an order having a price and an observable that generates new prices.\nWhen the observable value changes the order is cancelled and\na new order with new price is created and sent to the order book.</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy.price._volume.Volume_strategypriceMarketData": {
        "castsTo": [],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.price._marketdata.MarketData_StringStringStringFloatFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy._combine.Combine_ISingleAssetStrategyISingleAssetStrategy": {
        "castsTo": [
            "marketsim.gen._out._isingleassetstrategy.ISingleAssetStrategy"
        ],
        "properties": {
            "A": {
                "type": "marketsim.gen._out._isingleassetstrategy.ISingleAssetStrategy"
            },
            "B": {
                "type": "marketsim.gen._out._isingleassetstrategy.ISingleAssetStrategy"
            }
        },
        "description": "<div class=\"document\">\n<p>Can be considered as a particular case of Array strategy</p>\n</div>\n"
    },
    "marketsim.gen._out._candlesticks.CandleSticks_IObservableFloatFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "source": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            },
            "timeframe": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n<p>open/close/min/max price, its average and standard deviation</p>\n</div>\n"
    },
    "marketsim.gen._out.ops._condition.Condition_BooleanIObservableSideSide": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionside.IFunctionSide",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject",
            "marketsim.gen._out._iobservable._iobservableside.IObservableSide"
        ],
        "properties": {
            "ifpart": {
                "type": "marketsim.gen._out._iobservable._iobservableside.IObservableSide"
            },
            "elsepart": {
                "type": "marketsim.gen._out._ifunction._ifunctionside.IFunctionSide"
            },
            "cond": {
                "type": "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.weight._identityf.IdentityF_Float": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
        ],
        "properties": {
            "f": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.weight._traderefficiency.TraderEfficiency_IAccount": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
        ],
        "properties": {
            "trader": {
                "type": "marketsim.gen._out._iaccount.IAccount"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.side._strategy.Strategy_strategysidePairTradingIEventSideIObservableIOrder": {
        "castsTo": [
            "marketsim.gen._out._isingleassetstrategy.ISingleAssetStrategy"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.side._pairtrading.PairTrading_IOrderBookFloat"
            },
            "eventGen": {
                "type": "marketsim.gen._out._ievent.IEvent"
            },
            "orderFactory": {
                "type": "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionside.IFunctionIObservableIOrder_from_IFunctionSide"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.ops._lessequal.LessEqual_IObservableFloatFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool",
            "marketsim.gen._out._iobservable._iobservablebool.IObservablebool",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "y": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            },
            "x": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.ops._less.Less_IObservableFloatFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool",
            "marketsim.gen._out._iobservable._iobservablebool.IObservablebool",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "y": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            },
            "x": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out._test.in1.in2._o.O_IObservableFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math.random._expovariate.expovariate_Float": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
        ],
        "properties": {
            "Lambda": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n<p>Returned values range from 0 to positive infinity</p>\n</div>\n"
    },
    "marketsim.gen._out.trader._singleproxy.SingleProxy_": {
        "castsTo": [
            "marketsim.gen._out._iaccount.IAccount",
            "marketsim.gen._out._isingleassettrader.ISingleAssetTrader",
            "marketsim.gen._out._itrader.ITrader"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n<p>(normally it is used to define trader properties and strategies)</p>\n</div>\n"
    },
    "marketsim.gen._out._volumelevels.volumeLevels_IVolumeLevelsIGraphIntIntListFloatInt": {
        "castsTo": [
            "marketsim.gen._out._itimeserie.ITimeSerie"
        ],
        "properties": {
            "_digitsToShow": {
                "hidden": true,
                "type": "_parseInt"
            },
            "graph": {
                "type": "marketsim.gen._out._igraph.IGraph"
            },
            "_smooth": {
                "hidden": true,
                "type": "_parseInt"
            },
            "source": {
                "type": "marketsim.gen._out._ifunction._ifunctionivolumelevels.IFunctionIVolumeLevels"
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
    "marketsim.gen._out.strategy.weight.trader._trader_unit.trader_Unit_": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionifunctionfloat_from_iaccount.IFunctionIFunctionfloat_from_IAccount"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out._ifdefined.IfDefined_IObservableFloatIObservableFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "elsePart": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            },
            "x": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._curried._side_stoploss.side_StopLoss_SideIObservableIOrderFloat": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionside.IFunctionIObservableIOrder_from_IFunctionSide"
        ],
        "properties": {
            "maxloss": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            },
            "proto": {
                "type": "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionside.IFunctionIObservableIOrder_from_IFunctionSide"
            }
        },
        "description": "<div class=\"document\">\n<p>StopLoss order is initialised by an underlying order and a maximal acceptable loss factor.\nIt keeps track of position and balance change induced by trades of the underlying order and\nif losses from keeping the position exceed certain limit (given by maximum loss factor),\nthe meta order clears its position.</p>\n</div>\n"
    },
    "marketsim.gen._out.math._alpha.Alpha_mathRSI": {
        "castsTo": [],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.math._rsi.RSI_IObservableFloatFloatFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._curried._sideprice_withexpiry.sideprice_WithExpiry_SideFloatIObservableIOrderFloat": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionsideifunctionfloat.IFunctionIObservableIOrder_from_IFunctionSideIFunctionfloat"
        ],
        "properties": {
            "proto": {
                "type": "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionsideifunctionfloat.IFunctionIObservableIOrder_from_IFunctionSideIFunctionfloat"
            },
            "expiry": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n<p>WithExpiry orders can be viewed as ImmediateOrCancel orders\nwhere cancel order is sent not immediately but after some delay</p>\n</div>\n"
    },
    "marketsim.gen._out.math._logreturns.LogReturns_IObservableFloatFloat": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            },
            "timeframe": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._curried._signedvolume_limitsigned.signedVolume_LimitSigned_Float": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionfloat.IFunctionIObservableIOrder_from_IFunctionfloat"
        ],
        "properties": {
            "price": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n<p>Limit orders ask to buy or sell some asset at price better than some limit price.\nIf a limit order is not competely fulfilled\nit remains in an order book waiting to be matched with another order.</p>\n</div>\n"
    },
    "marketsim.gen._out.ops._notequal.NotEqual_IObservableFloatFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool",
            "marketsim.gen._out._iobservable._iobservablebool.IObservablebool",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "y": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            },
            "x": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._curried._price_withexpiry.price_WithExpiry_FloatIObservableIOrderFloat": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionfloat.IFunctionIObservableIOrder_from_IFunctionfloat"
        ],
        "properties": {
            "proto": {
                "type": "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionfloat.IFunctionIObservableIOrder_from_IFunctionfloat"
            },
            "expiry": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n<p>WithExpiry orders can be viewed as ImmediateOrCancel orders\nwhere cancel order is sent not immediately but after some delay</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy.side._strategy.Strategy_strategysideNoiseIEventSideIObservableIOrder": {
        "castsTo": [
            "marketsim.gen._out._isingleassetstrategy.ISingleAssetStrategy"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.side._noise.Noise_Float"
            },
            "eventGen": {
                "type": "marketsim.gen._out._ievent.IEvent"
            },
            "orderFactory": {
                "type": "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionside.IFunctionIObservableIOrder_from_IFunctionSide"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._fixedbudget.FixedBudget_SideFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._iobservable._iobservableiorder.IObservableIOrder",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "side": {
                "type": "marketsim.gen._out._ifunction._ifunctionside.IFunctionSide"
            },
            "budget": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n<p>Fixed budget order acts like a market order\nbut the volume is implicitly given by a budget available for trades.\nInternally first it sends request.EvalVolumesForBudget\nto estimate volumes and prices of orders to sent and\nthen sends a sequence of order.ImmediateOrCancel to be sure that\ncumulative price of trades to be done won't exceed the given budget.</p>\n</div>\n"
    },
    "marketsim.gen._out.order._marketsigned.MarketSigned_Float": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._iobservable._iobservableiorder.IObservableIOrder",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "signedVolume": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n<p>Market order intructs buy or sell given volume immediately</p>\n</div>\n"
    },
    "marketsim.gen._out.math._alpha.Alpha_mathEW": {
        "castsTo": [],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.math._ew.EW_IObservableFloatFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math.random._paretovariate.paretovariate_Float": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
        ],
        "properties": {
            "Alpha": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.position._alpha.Alpha_strategypositionRSI_linear": {
        "castsTo": [],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.position._rsi_linear.RSI_linear_FloatIObservableFloatFloatISingleAssetTrader"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.orderbook._spread.Spread_IOrderBook": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "book": {
                "type": "marketsim.gen._out._iorderbook.IOrderBook"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.ops._sub.Sub_FloatFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "y": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            },
            "x": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math._maxepsilon.MaxEpsilon_mathCumulativeFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.math._cumulative.Cumulative_IObservableFloat"
            },
            "epsilon": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n<p>It fires updates only if <em>source</em> value becomes greater than the old value plus <em>epsilon</em></p>\n</div>\n"
    },
    "marketsim.gen._out.strategy.position._trader.Trader_strategypositionBollinger_linear": {
        "castsTo": [],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.position._bollinger_linear.Bollinger_linear_FloatIObservableFloatISingleAssetTrader"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.orderbook._lasttradevolume.LastTradeVolume_IOrderQueue": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "queue": {
                "type": "marketsim.gen._out._iorderqueue.IOrderQueue"
            }
        },
        "description": "<div class=\"document\">\n<p>Returns None if there haven't been any trades</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy.price._initialvalue.InitialValue_strategypriceLiquidityProvider": {
        "castsTo": [],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.price._liquidityprovider.LiquidityProvider_FloatFloatIOrderBook"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.ops._mul.Mul_IObservableFloatFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "y": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            },
            "x": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.ops._div.Div_FloatFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "y": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            },
            "x": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.ops._condition.Condition_IObservableBooleanIObservableFloatIObservableFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "ifpart": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            },
            "elsepart": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            },
            "cond": {
                "type": "marketsim.gen._out._iobservable._iobservablebool.IObservablebool"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math._raw.Raw_mathRSI": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.math._rsi.RSI_IObservableFloatFloatFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math._avg.Avg_mathEW": {
        "castsTo": [
            "marketsim.gen._out._idifferentiable.IDifferentiable",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.math._ew.EW_IObservableFloatFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.side._strategy.Strategy_strategysideMeanReversionIEventSideIObservableIOrder": {
        "castsTo": [
            "marketsim.gen._out._isingleassetstrategy.ISingleAssetStrategy"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.side._meanreversion.MeanReversion_Float"
            },
            "eventGen": {
                "type": "marketsim.gen._out._ievent.IEvent"
            },
            "orderFactory": {
                "type": "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionside.IFunctionIObservableIOrder_from_IFunctionSide"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.side._timeframe.Timeframe_strategysideRSIbis": {
        "castsTo": [],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.side._rsibis.RSIbis_FloatFloatFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math.random._betavariate.betavariate_FloatFloat": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
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
    "marketsim.gen._out.strategy.position._alpha.Alpha_strategypositionBollinger_linear": {
        "castsTo": [],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.position._bollinger_linear.Bollinger_linear_FloatIObservableFloatISingleAssetTrader"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.ops._condition.Condition_IObservableBooleanSideIObservableSide": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionside.IFunctionSide",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject",
            "marketsim.gen._out._iobservable._iobservableside.IObservableSide"
        ],
        "properties": {
            "ifpart": {
                "type": "marketsim.gen._out._ifunction._ifunctionside.IFunctionSide"
            },
            "elsepart": {
                "type": "marketsim.gen._out._iobservable._iobservableside.IObservableSide"
            },
            "cond": {
                "type": "marketsim.gen._out._iobservable._iobservablebool.IObservablebool"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.side._strategy.Strategy_strategysideSignalIEventSideIObservableIOrder": {
        "castsTo": [
            "marketsim.gen._out._isingleassetstrategy.ISingleAssetStrategy"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.side._signal.Signal_FloatFloat"
            },
            "eventGen": {
                "type": "marketsim.gen._out._ievent.IEvent"
            },
            "orderFactory": {
                "type": "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionside.IFunctionIObservableIOrder_from_IFunctionSide"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math._max.Max_FloatIObservableFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "y": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            },
            "x": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n<p>If <em>x</em> or/and <em>y</em> are observables, <em>Min</em> is also observable</p>\n</div>\n"
    },
    "marketsim.gen._out.order._curried._signedvolume_marketsigned.signedVolume_MarketSigned_": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionfloat.IFunctionIObservableIOrder_from_IFunctionfloat"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n<p>Market order intructs buy or sell given volume immediately</p>\n</div>\n"
    },
    "marketsim.gen._out.trader._singleasset.SingleAsset_IOrderBookISingleAssetStrategyStringFloatFloatListITimeSerie": {
        "castsTo": [
            "marketsim.gen._out._iaccount.IAccount",
            "marketsim.gen._out._isingleassettrader.ISingleAssetTrader",
            "marketsim.gen._out._itrader.ITrader"
        ],
        "properties": {
            "name": {
                "type": "identity"
            },
            "orderBook": {
                "type": "marketsim.gen._out._iorderbook.IOrderBook"
            },
            "strategy": {
                "type": "marketsim.gen._out._isingleassetstrategy.ISingleAssetStrategy"
            },
            "amount": {
                "type": "_parseFloat"
            },
            "PnL": {
                "type": "_parseFloat"
            },
            "timeseries": {
                "type": {
                    "elementType": "marketsim.gen._out._itimeserie.ITimeSerie"
                }
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._curried._side_price_iceberg.side_price_Iceberg_SideFloatIObservableIOrderFloat": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionifunctioniobservableiorder_from_ifunctionfloat_from_ifunctionside.IFunctionIFunctionIObservableIOrder_from_IFunctionfloat_from_IFunctionSide"
        ],
        "properties": {
            "lotSize": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            },
            "proto": {
                "type": "marketsim.gen._out._ifunction._ifunctionifunctioniobservableiorder_from_ifunctionfloat_from_ifunctionside.IFunctionIFunctionIObservableIOrder_from_IFunctionfloat_from_IFunctionSide"
            }
        },
        "description": "<div class=\"document\">\n<p>Iceberg order is initialized by an underlying order and a lot size.\nIt sends consequently pieces of the underlying order of size equal or less to the lot size\nthus maximum lot size volume is visible at the market at any moment.</p>\n</div>\n"
    },
    "marketsim.gen._out._test.overloading._hh.hh_": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._curried._side_price_floatingprice.side_price_FloatingPrice_SideFloatIObservableIOrderIObservableFloat": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionifunctioniobservableiorder_from_ifunctionfloat_from_ifunctionside.IFunctionIFunctionIObservableIOrder_from_IFunctionfloat_from_IFunctionSide"
        ],
        "properties": {
            "floatingPrice": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            },
            "proto": {
                "type": "marketsim.gen._out._ifunction._ifunctionifunctioniobservableiorder_from_ifunctionfloat_from_ifunctionside.IFunctionIFunctionIObservableIOrder_from_IFunctionfloat_from_IFunctionSide"
            }
        },
        "description": "<div class=\"document\">\n<p>Floating price order is initialized by an order having a price and an observable that generates new prices.\nWhen the observable value changes the order is cancelled and\na new order with new price is created and sent to the order book.</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy.side._signal_value.Signal_Value_strategysideTrendFollower": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.side._trendfollower.TrendFollower_FloatFloatIOrderBook"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math._derivative.Derivative_IDifferentiable": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out._idifferentiable.IDifferentiable"
            }
        },
        "description": "<div class=\"document\">\n<p><em>x</em> should provide <em>derivative</em> member</p>\n</div>\n"
    },
    "marketsim.gen._out.math.random._weibullvariate.weibullvariate_FloatFloat": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
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
    "marketsim.scheduler.Scheduler": {
        "castsTo": [],
        "properties": {
            "currentTime": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n<p>Keeps a set of events to be launched in the future</p>\n</div>\n"
    },
    "marketsim.gen._out.orderbook._safesideprice.SafeSidePrice_IOrderQueueIObservableFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "queue": {
                "type": "marketsim.gen._out._iorderqueue.IOrderQueue"
            },
            "defaultValue": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            }
        },
        "description": "<div class=\"document\">\n<p>and <em>defaultValue</em> if there haven't been any trades</p>\n</div>\n"
    },
    "marketsim.gen._out.event._after.After_Float": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent"
        ],
        "properties": {
            "delay": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.price._price.Price_strategypriceLiquidityProviderSide": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.price._liquidityprovider.LiquidityProvider_FloatFloatIOrderBook"
            },
            "side": {
                "type": "marketsim.gen._out._ifunction._ifunctionside.IFunctionSide"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._curried._price_iceberg.price_Iceberg_FloatIObservableIOrderFloat": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionfloat.IFunctionIObservableIOrder_from_IFunctionfloat"
        ],
        "properties": {
            "lotSize": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            },
            "proto": {
                "type": "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionfloat.IFunctionIObservableIOrder_from_IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n<p>Iceberg order is initialized by an underlying order and a lot size.\nIt sends consequently pieces of the underlying order of size equal or less to the lot size\nthus maximum lot size volume is visible at the market at any moment.</p>\n</div>\n"
    },
    "marketsim.gen._out.ops._notequal.NotEqual_IObservableFloatIObservableFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool",
            "marketsim.gen._out._iobservable._iobservablebool.IObservablebool",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "y": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            },
            "x": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.position._k.K_strategypositionBollinger_linear": {
        "castsTo": [],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.position._bollinger_linear.Bollinger_linear_FloatIObservableFloatISingleAssetTrader"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.orderbook._remote.Remote_IOrderBookITwoWayLinkListITimeSerie": {
        "castsTo": [
            "marketsim.gen._out._iorderbook.IOrderBook"
        ],
        "properties": {
            "link": {
                "type": "marketsim.gen._out._itwowaylink.ITwoWayLink"
            },
            "orderbook": {
                "type": "marketsim.gen._out._iorderbook.IOrderBook"
            },
            "timeseries": {
                "type": {
                    "elementType": "marketsim.gen._out._itimeserie.ITimeSerie"
                }
            }
        },
        "description": "<div class=\"document\">\n<p>to the market by means of a <em>link</em> that introduces some latency in information propagation</p>\n</div>\n"
    },
    "marketsim.gen._out.ops._mul.Mul_IObservableFloatIObservableFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "y": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            },
            "x": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.orderbook._queue.Queue_IOrderBookSide": {
        "castsTo": [
            "marketsim.gen._out._iorderqueue.IOrderQueue"
        ],
        "properties": {
            "book": {
                "type": "marketsim.gen._out._iorderbook.IOrderBook"
            },
            "side": {
                "type": "marketsim.gen._out._ifunction._ifunctionside.IFunctionSide"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._curried._sideprice_floatingprice.sideprice_FloatingPrice_SideFloatIObservableIOrderIObservableFloat": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionsideifunctionfloat.IFunctionIObservableIOrder_from_IFunctionSideIFunctionfloat"
        ],
        "properties": {
            "floatingPrice": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            },
            "proto": {
                "type": "marketsim.gen._out._ifunction._ifunctionifunctioniobservableiorder_from_ifunctionfloat_from_ifunctionside.IFunctionIFunctionIObservableIOrder_from_IFunctionfloat_from_IFunctionSide"
            }
        },
        "description": "<div class=\"document\">\n<p>Floating price order is initialized by an order having a price and an observable that generates new prices.\nWhen the observable value changes the order is cancelled and\na new order with new price is created and sent to the order book.</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy.position._bollinger_linear.Bollinger_linear_FloatIObservableFloatISingleAssetTrader": {
        "castsTo": [
            "marketsim.gen._out.strategy.position._bollinger_linear.Bollinger_linear_FloatIObservableFloatISingleAssetTrader"
        ],
        "properties": {
            "alpha": {
                "type": "_parseFloat"
            },
            "k": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            },
            "trader": {
                "type": "marketsim.gen._out._isingleassettrader.ISingleAssetTrader"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._curried._side_iceberg.side_Iceberg_SideIObservableIOrderFloat": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionside.IFunctionIObservableIOrder_from_IFunctionSide"
        ],
        "properties": {
            "lotSize": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            },
            "proto": {
                "type": "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionside.IFunctionIObservableIOrder_from_IFunctionSide"
            }
        },
        "description": "<div class=\"document\">\n<p>Iceberg order is initialized by an underlying order and a lot size.\nIt sends consequently pieces of the underlying order of size equal or less to the lot size\nthus maximum lot size volume is visible at the market at any moment.</p>\n</div>\n"
    },
    "marketsim.gen._out.side._observablebuy.observableBuy_": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionside.IFunctionSide",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject",
            "marketsim.gen._out._iobservable._iobservableside.IObservableSide"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.math._pow.Pow_FloatFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "base": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            },
            "power": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n<p>Exceptional cases follow Annex F of the C99 standard as far as possible.\nIn particular, <tt class=\"docutils literal\">pow(1.0, x)</tt> and <tt class=\"docutils literal\">pow(x, 0.0)</tt> always return 1.0,\neven when <em>x</em> is a zero or a NaN.\nIf both <em>x</em> and <em>y</em> are finite, <em>x</em> is negative, and <em>y</em> is not an integer then\n<tt class=\"docutils literal\">pow(x, y)</tt> is undefined, and raises <tt class=\"docutils literal\">ValueError</tt>.</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy.side._signal_value.Signal_Value_strategysideSignal": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.strategy.side._signal.Signal_FloatFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.orderbook._link.Link_IObservableFloat": {
        "castsTo": [
            "marketsim.gen._out._ilink.ILink"
        ],
        "properties": {
            "latency": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            }
        },
        "description": "<div class=\"document\">\n<p>(normally between a trader and a market).\nEnsures that sending packets via a link preserves their order.</p>\n</div>\n"
    },
    "marketsim.gen._out.order._curried._side_withexpiry.side_WithExpiry_SideIObservableIOrderFloat": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionside.IFunctionIObservableIOrder_from_IFunctionSide"
        ],
        "properties": {
            "proto": {
                "type": "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionside.IFunctionIObservableIOrder_from_IFunctionSide"
            },
            "expiry": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n<p>WithExpiry orders can be viewed as ImmediateOrCancel orders\nwhere cancel order is sent not immediately but after some delay</p>\n</div>\n"
    },
    "marketsim.gen._out.math._log.Log_Float": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "x": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.orderbook._asks.Asks_IOrderBook": {
        "castsTo": [
            "marketsim.gen._out._iorderqueue.IOrderQueue"
        ],
        "properties": {
            "book": {
                "type": "marketsim.gen._out._iorderbook.IOrderBook"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    }
}
var interfaces = [
    [
        "_parseInt",
        []
    ],
    [
        "marketsim.gen._out._ifunction._ifunctionifunctionfloat_from_ifunctionfloat.IFunctionIFunctionfloat_from_IFunctionfloat",
        [
            "marketsim.gen._out.strategy.weight.f._f_clamp0.f_Clamp0_",
            "marketsim.gen._out.strategy.weight.f._f_atanpow.f_AtanPow_Float",
            "marketsim.gen._out.strategy.weight.f._f_identityf.f_IdentityF_"
        ]
    ],
    [
        "marketsim.gen._out.math._macd.macd_IObservableFloatFloatFloat",
        [
            "marketsim.gen._out.math._macd.macd_IObservableFloatFloatFloat"
        ]
    ],
    [
        "marketsim.gen._out._iaccount.IAccount",
        [
            "marketsim.gen._out.trader._singleasset.SingleAsset_IOrderBookISingleAssetStrategyStringFloatFloatListITimeSerie",
            "marketsim.gen._out.trader._singleproxy.SingleProxy_",
            "marketsim.gen._out.strategy.account._virtualmarket.VirtualMarket_ISingleAssetStrategy",
            "marketsim.gen._out.strategy.account._real.Real_ISingleAssetStrategy"
        ]
    ],
    [
        "marketsim.gen._out.strategy.side._crossingaverages.CrossingAverages_FloatFloatFloatIOrderBook",
        [
            "marketsim.gen._out.strategy.side._crossingaverages.CrossingAverages_FloatFloatFloatIOrderBook"
        ]
    ],
    [
        {
            "elementType": "_parseFloat"
        },
        []
    ],
    [
        "marketsim.gen._out._igraph.IGraph",
        [
            "marketsim.js.Graph",
            "marketsim.gen._out.veusz._graph.Graph_String"
        ]
    ],
    [
        "marketsim.gen._out.math._moving.Moving_IObservableFloatFloat",
        [
            "marketsim.gen._out.math._moving.Moving_IObservableFloatFloat"
        ]
    ],
    [
        "marketsim.gen._out.strategy.side._signal.Signal_FloatFloat",
        [
            "marketsim.gen._out.strategy.side._signal.Signal_FloatFloat"
        ]
    ],
    [
        "marketsim.gen._out._iobservable._iobservableobject.IObservableobject",
        [
            "marketsim.gen._out.order._immediateorcancel.ImmediateOrCancel_IObservableIOrder",
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanIObservableFloatFloat",
            "marketsim.gen._out.orderbook._spread.Spread_IOrderBook",
            "marketsim.gen._out._observabletrue.observableTrue_",
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanIObservableSideIObservableSide",
            "marketsim.gen._out.math._relstddev.RelStdDev_mathEW",
            "marketsim.gen._out.ops._equal.Equal_IObservableFloatFloat",
            "marketsim.gen._out.orderbook._lastprice.LastPrice_IOrderQueue",
            "marketsim.gen._out.side._observablesell.observableSell_",
            "marketsim.gen._out._test.in1.in2._intobs.IntObs_",
            "marketsim.gen._out.ops._negate.Negate_Float",
            "marketsim.gen._out.strategy.position._position.Position_strategypositionRSI_linear",
            "marketsim.gen._out.math._min.Min_FloatIObservableFloat",
            "marketsim.gen._out.order._limit.Limit_SideFloatFloat",
            "marketsim.gen._out.orderbook._naivecumulativeprice.NaiveCumulativePrice_IOrderBookFloat",
            "marketsim.gen._out.ops._less.Less_FloatIObservableFloat",
            "marketsim.gen._out._const.const_Int",
            "marketsim.gen._out.math._minepsilon.MinEpsilon_mathCumulativeFloat",
            "marketsim.gen._out._const.const_Float",
            "marketsim.gen._out.orderbook._cumulativeprice.CumulativePrice_IOrderBookFloat",
            "marketsim.gen._out.math._relstddev.RelStdDev_mathCumulative",
            "marketsim.gen._out.ops._greater.Greater_FloatIObservableFloat",
            "marketsim.gen._out.math._max.Max_IObservableFloatIObservableFloat",
            "marketsim.gen._out.ops._lessequal.LessEqual_FloatIObservableFloat",
            "marketsim.gen._out.order._limitsigned.LimitSigned_FloatFloat",
            "marketsim.gen._out.observable._breaksatchanges.BreaksAtChanges_IObservableFloat",
            "marketsim.gen._out.ops._greaterequal.GreaterEqual_IObservableFloatFloat",
            "marketsim.gen._out.trader._pendingvolume.PendingVolume_IAccount",
            "marketsim.gen._out.ops._div.Div_FloatIObservableFloat",
            "marketsim.gen._out.orderbook._volumelevels.VolumeLevels_IOrderQueueFloatInt",
            "marketsim.gen._out.math._downmovements.DownMovements_IObservableFloatFloat",
            "marketsim.gen._out.orderbook._bestprice.BestPrice_IOrderQueue",
            "marketsim.gen._out.order._iceberg.Iceberg_IObservableIOrderFloat",
            "marketsim.gen._out.math._sqrt.Sqrt_Float",
            "marketsim.gen._out._observablefalse.observableFalse_",
            "marketsim.gen._out.orderbook._midprice.MidPrice_IOrderBook",
            "marketsim.gen._out.observable._oneverydt.OnEveryDt_FloatFloat",
            "marketsim.gen._out.order._floatingprice.FloatingPrice_FloatIObservableIOrderIObservableFloat",
            "marketsim.gen._out.trader._balance.Balance_IAccount",
            "marketsim.gen._out.math._min.Min_FloatFloat",
            "marketsim.gen._out.math._min.Min_IObservableFloatFloat",
            "marketsim.gen._out.ops._mul.Mul_FloatIObservableFloat",
            "marketsim.gen._out.trader._roughpnl.RoughPnL_IAccount",
            "marketsim.gen._out.strategy.side._fundamental_value.Fundamental_Value_strategysidePairTrading",
            "marketsim.gen._out._candlesticks.CandleSticks_IObservableFloatFloat",
            "marketsim.gen._out._ifdefined.IfDefined_FloatFloat",
            "marketsim.gen._out.ops._lessequal.LessEqual_IObservableFloatIObservableFloat",
            "marketsim.gen._out.ops._lessequal.LessEqual_IObservableFloatFloat",
            "marketsim.gen._out._ifdefined.IfDefined_FloatIObservableFloat",
            "marketsim.gen._out.ops._less.Less_IObservableFloatFloat",
            "marketsim.gen._out.ops._div.Div_IObservableFloatIObservableFloat",
            "marketsim.gen._out._test.in1.in2._o.O_IObservableFloat",
            "marketsim.gen._out.trader._efficiency.Efficiency_IAccount",
            "marketsim.gen._out.ops._condition.Condition_BooleanFloatIObservableFloat",
            "marketsim.gen._out._ifdefined.IfDefined_IObservableFloatIObservableFloat",
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanIObservableSideSide",
            "marketsim.gen._out.strategy.position._desiredposition.DesiredPosition_strategypositionBollinger_linear",
            "marketsim.gen._out.ops._greaterequal.GreaterEqual_FloatIObservableFloat",
            "marketsim.gen._out.ops._div.Div_IObservableFloatFloat",
            "marketsim.gen._out.orderbook._lasttradeprice.LastTradePrice_IOrderQueue",
            "marketsim.gen._out.ops._notequal.NotEqual_IObservableFloatFloat",
            "marketsim.gen._out.order._fixedbudget.FixedBudget_SideFloat",
            "marketsim.gen._out.order._marketsigned.MarketSigned_Float",
            "marketsim.gen._out.strategy.side._side.Side_strategysideMeanReversion",
            "marketsim.gen._out.strategy.side._side.Side_strategysidePairTrading",
            "marketsim.gen._out.ops._greater.Greater_IObservableFloatFloat",
            "marketsim.gen._out.ops._greaterequal.GreaterEqual_FloatFloat",
            "marketsim.gen._out.ops._sub.Sub_FloatFloat",
            "marketsim.gen._out.ops._condition.Condition_BooleanFloatFloat",
            "marketsim.gen._out.math._maxepsilon.MaxEpsilon_mathCumulativeFloat",
            "marketsim.gen._out.orderbook._safesideprice.SafeSidePrice_IOrderQueueFloat",
            "marketsim.gen._out.orderbook._naivecumulativeprice.NaiveCumulativePrice_IOrderBookIObservableFloat",
            "marketsim.gen._out.order._market.Market_SideFloat",
            "marketsim.gen._out.ops._div.Div_FloatFloat",
            "marketsim.gen._out.ops._less.Less_FloatFloat",
            "marketsim.gen._out.ops._condition.Condition_BooleanIObservableSideSide",
            "marketsim.gen._out.orderbook._lasttradevolume.LastTradeVolume_IOrderQueue",
            "marketsim.gen._out.ops._condition.Condition_BooleanIObservableFloatFloat",
            "marketsim.gen._out.math._minimum.Minimum_mathMoving",
            "marketsim.gen._out.ops._negate.Negate_IObservableFloat",
            "marketsim.gen._out.math._max.Max_IObservableFloatFloat",
            "marketsim.gen._out.ops._sub.Sub_IObservableFloatIObservableFloat",
            "marketsim.gen._out.ops._mul.Mul_IObservableFloatFloat",
            "marketsim.gen._out.ops._greaterequal.GreaterEqual_IObservableFloatIObservableFloat",
            "marketsim.gen._out.ops._add.Add_IObservableFloatFloat",
            "marketsim.gen._out.order._stoploss.StopLoss_IObservableIOrderFloat",
            "marketsim.gen._out.ops._equal.Equal_FloatFloat",
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanIObservableFloatIObservableFloat",
            "marketsim.gen._out.order._withexpiry.WithExpiry_IObservableIOrderFloat",
            "marketsim.gen._out.math._maximum.Maximum_mathMoving",
            "marketsim.gen._out.ops._mul.Mul_IObservableFloatIObservableFloat",
            "marketsim.gen._out.ops._equal.Equal_FloatIObservableFloat",
            "marketsim.gen._out.ops._sub.Sub_IObservableFloatFloat",
            "marketsim.gen._out.trader._position.Position_IAccount",
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanSideIObservableSide",
            "marketsim.gen._out.ops._greater.Greater_IObservableFloatIObservableFloat",
            "marketsim.gen._out.observable._quote.Quote_StringStringString",
            "marketsim.gen._out.order._peg.Peg_FloatIObservableIOrder",
            "marketsim.gen._out.ops._equal.Equal_IObservableFloatIObservableFloat",
            "marketsim.gen._out.math._max.Max_FloatIObservableFloat",
            "marketsim.gen._out.math._atan.Atan_Float",
            "marketsim.gen._out.math._pow.Pow_FloatFloat",
            "marketsim.gen._out.math._upmovements.UpMovements_IObservableFloatFloat",
            "marketsim.gen._out.ops._condition.Condition_BooleanSideIObservableSide",
            "marketsim.gen._out.math._sqr.Sqr_IObservableFloat",
            "marketsim.gen._out.ops._notequal.NotEqual_FloatFloat",
            "marketsim.gen._out.math._randomwalk.RandomWalk_FloatFloatFloatString",
            "marketsim.gen._out.ops._sub.Sub_FloatIObservableFloat",
            "marketsim.gen._out.ops._greater.Greater_FloatFloat",
            "marketsim.gen._out.ops._lessequal.LessEqual_FloatFloat",
            "marketsim.gen._out.ops._notequal.NotEqual_FloatIObservableFloat",
            "marketsim.gen._out.math._max.Max_FloatFloat",
            "marketsim.gen._out.math._exp.Exp_Float",
            "marketsim.gen._out.ops._add.Add_FloatIObservableFloat",
            "marketsim.gen._out.orderbook._safesideprice.SafeSidePrice_IOrderQueueIObservableFloat",
            "marketsim.gen._out.ops._add.Add_FloatFloat",
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanSideSide",
            "marketsim.gen._out.strategy.price._price.Price_strategypriceLiquidityProviderSide",
            "marketsim.gen._out.ops._less.Less_IObservableFloatIObservableFloat",
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanFloatIObservableFloat",
            "marketsim.gen._out.ops._notequal.NotEqual_IObservableFloatIObservableFloat",
            "marketsim.gen._out.math._sqr.Sqr_Float",
            "marketsim.gen._out.ops._condition.Condition_BooleanIObservableFloatIObservableFloat",
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanFloatFloat",
            "marketsim.gen._out._ifdefined.IfDefined_IObservableFloatFloat",
            "marketsim.gen._out.ops._mul.Mul_FloatFloat",
            "marketsim.gen._out.ops._condition.Condition_BooleanIObservableSideIObservableSide",
            "marketsim.gen._out.strategy.position._desiredposition.DesiredPosition_strategypositionRSI_linear",
            "marketsim.gen._out.ops._condition.Condition_BooleanSideSide",
            "marketsim.gen._out.side._observablebuy.observableBuy_",
            "marketsim.gen._out.strategy.side._side.Side_strategysideFundamentalValue",
            "marketsim.gen._out.side._observablenothing.observableNothing_",
            "marketsim.gen._out.math._min.Min_IObservableFloatIObservableFloat",
            "marketsim.gen._out.ops._add.Add_IObservableFloatIObservableFloat",
            "marketsim.gen._out.math._relstddev.RelStdDev_mathMoving",
            "marketsim.gen._out.math._lagged.Lagged_IObservableFloatFloat",
            "marketsim.gen._out.strategy.position._position.Position_strategypositionBollinger_linear",
            "marketsim.gen._out.math._log.Log_Float"
        ]
    ],
    [
        "marketsim.gen._out._ifunction._ifunctionivolumelevels.IFunctionIVolumeLevels",
        [
            "marketsim.gen._out.orderbook._volumelevels.VolumeLevels_IOrderQueueFloatInt"
        ]
    ],
    [
        "marketsim.gen._out._ifunction._ifunctioniaccount_from_isingleassetstrategy.IFunctionIAccount_from_ISingleAssetStrategy",
        [
            "marketsim.gen._out.strategy.account.inner._inner_virtualmarket.inner_VirtualMarket_",
            "marketsim.gen._out.strategy.account.inner._inner_real.inner_Real_"
        ]
    ],
    [
        "marketsim.gen._out.strategy.side._noise.Noise_Float",
        [
            "marketsim.gen._out.strategy.side._noise.Noise_Float"
        ]
    ],
    [
        "marketsim.gen._out.strategy.price._marketmaker.MarketMaker_FloatFloat",
        [
            "marketsim.gen._out.strategy.price._marketmaker.MarketMaker_FloatFloat"
        ]
    ],
    [
        {
            "elementType": "marketsim.gen._out._isingleassetstrategy.ISingleAssetStrategy"
        },
        []
    ],
    [
        "marketsim.gen._out.strategy.side._fundamentalvalue.FundamentalValue_Float",
        [
            "marketsim.gen._out.strategy.side._fundamentalvalue.FundamentalValue_Float"
        ]
    ],
    [
        "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionside.IFunctionIObservableIOrder_from_IFunctionSide",
        [
            "marketsim.gen._out.order._curried._side_floatingprice.side_FloatingPrice_SideFloatIObservableIOrderIObservableFloat",
            "marketsim.gen._out.order._curried._side_market.side_Market_Float",
            "marketsim.gen._out.order._curried._side_peg.side_Peg_SideFloatIObservableIOrder",
            "marketsim.gen._out.order._curried._side_iceberg.side_Iceberg_SideIObservableIOrderFloat",
            "marketsim.gen._out.order._curried._side_stoploss.side_StopLoss_SideIObservableIOrderFloat",
            "marketsim.gen._out.order._curried._side_fixedbudget.side_FixedBudget_Float",
            "marketsim.gen._out.order._curried._side_immediateorcancel.side_ImmediateOrCancel_SideIObservableIOrder",
            "marketsim.gen._out.order._curried._side_limit.side_Limit_FloatFloat",
            "marketsim.gen._out.order._curried._side_withexpiry.side_WithExpiry_SideIObservableIOrderFloat"
        ]
    ],
    [
        "marketsim.gen._out._idifferentiable.IDifferentiable",
        [
            "marketsim.gen._out.math._signal.Signal_mathmacdFloatFloat",
            "marketsim.gen._out.math._avg.Avg_mathCumulative",
            "marketsim.gen._out.math._avg.Avg_mathMoving",
            "marketsim.gen._out.math._avg.Avg_mathEW",
            "marketsim.gen._out.strategy.side._fundamental_value.Fundamental_Value_strategysideMeanReversion"
        ]
    ],
    [
        "marketsim.gen._out._itimeserie.ITimeSerie",
        [
            "marketsim.gen._out._timeserie.TimeSerie_IObservableAnyIGraphIntInt",
            "marketsim.gen._out._volumelevels.volumeLevels_IVolumeLevelsIGraphIntIntListFloatInt"
        ]
    ],
    [
        "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionfloat.IFunctionIObservableIOrder_from_IFunctionfloat",
        [
            "marketsim.gen._out.order._curried._price_iceberg.price_Iceberg_FloatIObservableIOrderFloat",
            "marketsim.gen._out.order._curried._signedvolume_limitsigned.signedVolume_LimitSigned_Float",
            "marketsim.gen._out.order._curried._price_limit.price_Limit_SideFloat",
            "marketsim.gen._out.order._curried._price_withexpiry.price_WithExpiry_FloatIObservableIOrderFloat",
            "marketsim.gen._out.order._curried._price_floatingprice.price_FloatingPrice_FloatIObservableIOrderIObservableFloat",
            "marketsim.gen._out.order._curried._price_stoploss.price_StopLoss_FloatIObservableIOrderFloat",
            "marketsim.gen._out.order._curried._signedvolume_marketsigned.signedVolume_MarketSigned_",
            "marketsim.gen._out.order._curried._price_immediateorcancel.price_ImmediateOrCancel_FloatIObservableIOrder",
            "marketsim.gen._out.order._curried._price_peg.price_Peg_FloatIObservableIOrder"
        ]
    ],
    [
        "marketsim.gen._out._iobservable._iobservablebool.IObservablebool",
        [
            "marketsim.gen._out.ops._greater.Greater_IObservableFloatIObservableFloat",
            "marketsim.gen._out._observabletrue.observableTrue_",
            "marketsim.gen._out.ops._lessequal.LessEqual_IObservableFloatIObservableFloat",
            "marketsim.gen._out.ops._equal.Equal_IObservableFloatFloat",
            "marketsim.gen._out.ops._less.Less_FloatFloat",
            "marketsim.gen._out.ops._greater.Greater_FloatFloat",
            "marketsim.gen._out.ops._lessequal.LessEqual_IObservableFloatFloat",
            "marketsim.gen._out.ops._lessequal.LessEqual_FloatFloat",
            "marketsim.gen._out.ops._notequal.NotEqual_FloatIObservableFloat",
            "marketsim.gen._out.ops._notequal.NotEqual_FloatFloat",
            "marketsim.gen._out.ops._less.Less_IObservableFloatFloat",
            "marketsim.gen._out.ops._greaterequal.GreaterEqual_IObservableFloatIObservableFloat",
            "marketsim.gen._out.ops._less.Less_IObservableFloatIObservableFloat",
            "marketsim.gen._out.ops._equal.Equal_FloatFloat",
            "marketsim.gen._out.ops._less.Less_FloatIObservableFloat",
            "marketsim.gen._out.ops._notequal.NotEqual_IObservableFloatIObservableFloat",
            "marketsim.gen._out.ops._greaterequal.GreaterEqual_FloatIObservableFloat",
            "marketsim.gen._out.ops._greater.Greater_FloatIObservableFloat",
            "marketsim.gen._out.ops._lessequal.LessEqual_FloatIObservableFloat",
            "marketsim.gen._out.ops._notequal.NotEqual_IObservableFloatFloat",
            "marketsim.gen._out.ops._greaterequal.GreaterEqual_IObservableFloatFloat",
            "marketsim.gen._out.ops._equal.Equal_FloatIObservableFloat",
            "marketsim.gen._out._observablefalse.observableFalse_",
            "marketsim.gen._out.ops._greater.Greater_IObservableFloatFloat",
            "marketsim.gen._out.ops._greaterequal.GreaterEqual_FloatFloat",
            "marketsim.gen._out.ops._equal.Equal_IObservableFloatIObservableFloat"
        ]
    ],
    [
        "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionsideifunctionfloat.IFunctionIObservableIOrder_from_IFunctionSideIFunctionfloat",
        [
            "marketsim.gen._out.order._curried._sideprice_floatingprice.sideprice_FloatingPrice_SideFloatIObservableIOrderIObservableFloat",
            "marketsim.gen._out.order._curried._sideprice_peg.sideprice_Peg_SideFloatIObservableIOrder",
            "marketsim.gen._out.order._curried._sideprice_stoploss.sideprice_StopLoss_SideFloatIObservableIOrderFloat",
            "marketsim.gen._out.order._curried._sideprice_withexpiry.sideprice_WithExpiry_SideFloatIObservableIOrderFloat",
            "marketsim.gen._out.order._curried._sideprice_iceberg.sideprice_Iceberg_SideFloatIObservableIOrderFloat",
            "marketsim.gen._out.order._curried._sideprice_limit.sideprice_Limit_Float",
            "marketsim.gen._out.order._curried._sideprice_immediateorcancel.sideprice_ImmediateOrCancel_SideFloatIObservableIOrder"
        ]
    ],
    [
        "marketsim.gen._out._iorderqueue.IOrderQueue",
        [
            "marketsim.gen._out.orderbook._queue.Queue_IOrderBookSide",
            "marketsim.gen._out.orderbook._bids.Bids_IOrderBook",
            "marketsim.gen._out.orderbook._asks.Asks_IOrderBook"
        ]
    ],
    [
        "_parseFloat",
        []
    ],
    [
        "marketsim.gen._out._isingleassetstrategy.ISingleAssetStrategy",
        [
            "marketsim.gen._out.strategy.price._oneside.OneSide_strategypriceMarketDataSideFloat",
            "marketsim.gen._out.strategy.price._onesidestrategy.OneSideStrategy_strategypriceLiquidityProviderIEventSideFloatIObservableIOrderSide",
            "marketsim.gen._out.strategy.price._strategy.Strategy_strategypriceLiquidityProviderIEventSideFloatIObservableIOrder",
            "marketsim.gen._out.strategy._canceller.Canceller_Float",
            "marketsim.gen._out.strategy.price._oneside.OneSide_strategypriceMarketDataIObservableSideFloat",
            "marketsim.gen._out.strategy.side._strategy.Strategy_strategysidePairTradingIEventSideIObservableIOrder",
            "marketsim.gen._out.strategy._combine.Combine_ISingleAssetStrategyISingleAssetStrategy",
            "marketsim.gen._out.strategy.price._twosides.TwoSides_strategypriceMarketData",
            "marketsim.gen._out.strategy.side._strategy.Strategy_strategysideCrossingAveragesIEventSideIObservableIOrder",
            "marketsim.gen._out.strategy.position._strategy.Strategy_strategypositionRSI_linearFloatIObservableIOrder",
            "marketsim.gen._out.strategy._suspendable.Suspendable_ISingleAssetStrategyBoolean",
            "marketsim.gen._out.strategy.price._twosides.TwoSides_strategypriceMarketMaker",
            "marketsim.gen._out.strategy._choosethebest.ChooseTheBest_ListISingleAssetStrategyISingleAssetStrategyIAccountIAccountFloat",
            "marketsim.gen._out.strategy.side._strategy.Strategy_strategysideFundamentalValueIEventSideIObservableIOrder",
            "marketsim.gen._out.strategy._generic.Generic_IObservableIOrderIEvent",
            "marketsim.gen._out.strategy.side._strategy.Strategy_strategysideMeanReversionIEventSideIObservableIOrder",
            "marketsim.gen._out.strategy.price._onesidestrategy.OneSideStrategy_strategypriceLiquidityProviderIEventSideFloatIObservableIOrderIObservableSide",
            "marketsim.gen._out.strategy.side._strategy.Strategy_strategysideNoiseIEventSideIObservableIOrder",
            "marketsim.gen._out.strategy.price._oneside.OneSide_strategypriceMarketMakerSideFloat",
            "marketsim.gen._out.strategy.side._strategy.Strategy_strategysideTrendFollowerIEventSideIObservableIOrder",
            "marketsim.gen._out.strategy.position._strategy.Strategy_strategypositionBollinger_linearFloatIObservableIOrder",
            "marketsim.gen._out.strategy.side._strategy.Strategy_strategysideRSIbisIEventSideIObservableIOrder",
            "marketsim.gen._out.strategy._tradeifprofitable.TradeIfProfitable_ISingleAssetStrategyISingleAssetStrategyIAccountIAccountFloat",
            "marketsim.gen._out.strategy._multiarmedbandit.MultiArmedBandit_ListISingleAssetStrategyISingleAssetStrategyIAccountIAccountFloatFloatFloatListFloatListFloat",
            "marketsim.gen._out.strategy.side._strategy.Strategy_strategysideSignalIEventSideIObservableIOrder",
            "marketsim.gen._out.strategy._empty.Empty_",
            "marketsim.gen._out.strategy.price._oneside.OneSide_strategypriceMarketMakerIObservableSideFloat",
            "marketsim.gen._out.strategy._array.Array_ListISingleAssetStrategy"
        ]
    ],
    [
        "marketsim.gen._out._iobservable._iobservableiorder.IObservableIOrder",
        [
            "marketsim.gen._out.order._immediateorcancel.ImmediateOrCancel_IObservableIOrder",
            "marketsim.gen._out.order._limitsigned.LimitSigned_FloatFloat",
            "marketsim.gen._out.order._floatingprice.FloatingPrice_FloatIObservableIOrderIObservableFloat",
            "marketsim.gen._out.order._market.Market_SideFloat",
            "marketsim.gen._out.order._limit.Limit_SideFloatFloat",
            "marketsim.gen._out.order._stoploss.StopLoss_IObservableIOrderFloat",
            "marketsim.gen._out.order._fixedbudget.FixedBudget_SideFloat",
            "marketsim.gen._out.order._marketsigned.MarketSigned_Float",
            "marketsim.gen._out.order._peg.Peg_FloatIObservableIOrder",
            "marketsim.gen._out.order._withexpiry.WithExpiry_IObservableIOrderFloat",
            "marketsim.gen._out.order._iceberg.Iceberg_IObservableIOrderFloat"
        ]
    ],
    [
        "marketsim.gen._out._ilink.ILink",
        [
            "marketsim.gen._out.orderbook._link.Link_IObservableFloat"
        ]
    ],
    [
        "marketsim.gen._out.strategy.side._trendfollower.TrendFollower_FloatFloatIOrderBook",
        [
            "marketsim.gen._out.strategy.side._trendfollower.TrendFollower_FloatFloatIOrderBook"
        ]
    ],
    [
        "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
        [
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanIObservableFloatFloat",
            "marketsim.gen._out._ifdefined.IfDefined_FloatFloat",
            "marketsim.gen._out.math._relstddev.RelStdDev_mathEW",
            "marketsim.gen._out.strategy.position._position.Position_strategypositionRSI_linear",
            "marketsim.gen._out.orderbook._safesideprice.SafeSidePrice_IOrderQueueIObservableFloat",
            "marketsim.gen._out.ops._div.Div_IObservableFloatFloat",
            "marketsim.gen._out.math._max.Max_FloatIObservableFloat",
            "marketsim.gen._out.math._max.Max_FloatFloat",
            "marketsim.gen._out.trader._balance.Balance_IAccount",
            "marketsim.gen._out.orderbook._lasttradevolume.LastTradeVolume_IOrderQueue",
            "marketsim.gen._out.orderbook._spread.Spread_IOrderBook",
            "marketsim.gen._out.orderbook._safesideprice.SafeSidePrice_IOrderQueueFloat",
            "marketsim.gen._out.strategy.side._fundamental_value.Fundamental_Value_strategysidePairTrading",
            "marketsim.gen._out.ops._condition.Condition_BooleanIObservableFloatFloat",
            "marketsim.gen._out._ifdefined.IfDefined_FloatIObservableFloat",
            "marketsim.gen._out.math._exp.Exp_Float",
            "marketsim.gen._out.ops._add.Add_FloatIObservableFloat",
            "marketsim.gen._out.ops._negate.Negate_Float",
            "marketsim.gen._out.ops._negate.Negate_IObservableFloat",
            "marketsim.gen._out.ops._div.Div_IObservableFloatIObservableFloat",
            "marketsim.gen._out.math._min.Min_FloatIObservableFloat",
            "marketsim.gen._out._test.in1.in2._o.O_IObservableFloat",
            "marketsim.gen._out._const.const_Int",
            "marketsim.gen._out.ops._sub.Sub_IObservableFloatIObservableFloat",
            "marketsim.gen._out.trader._efficiency.Efficiency_IAccount",
            "marketsim.gen._out.ops._add.Add_FloatFloat",
            "marketsim.gen._out.ops._mul.Mul_IObservableFloatFloat",
            "marketsim.gen._out.math._minepsilon.MinEpsilon_mathCumulativeFloat",
            "marketsim.gen._out.orderbook._naivecumulativeprice.NaiveCumulativePrice_IOrderBookFloat",
            "marketsim.gen._out.ops._add.Add_IObservableFloatFloat",
            "marketsim.gen._out.ops._div.Div_FloatFloat",
            "marketsim.gen._out.math._lagged.Lagged_IObservableFloatFloat",
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanIObservableFloatIObservableFloat",
            "marketsim.gen._out._ifdefined.IfDefined_IObservableFloatIObservableFloat",
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanFloatIObservableFloat",
            "marketsim.gen._out._const.const_Float",
            "marketsim.gen._out.math._sqr.Sqr_Float",
            "marketsim.gen._out.ops._condition.Condition_BooleanIObservableFloatIObservableFloat",
            "marketsim.gen._out.strategy.position._desiredposition.DesiredPosition_strategypositionBollinger_linear",
            "marketsim.gen._out.math._randomwalk.RandomWalk_FloatFloatFloatString",
            "marketsim.gen._out.orderbook._cumulativeprice.CumulativePrice_IOrderBookFloat",
            "marketsim.gen._out.math._maximum.Maximum_mathMoving",
            "marketsim.gen._out.math._relstddev.RelStdDev_mathCumulative",
            "marketsim.gen._out.orderbook._midprice.MidPrice_IOrderBook",
            "marketsim.gen._out.math._max.Max_IObservableFloatIObservableFloat",
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanFloatFloat",
            "marketsim.gen._out.orderbook._lasttradeprice.LastTradePrice_IOrderQueue",
            "marketsim.gen._out.math._min.Min_FloatFloat",
            "marketsim.gen._out.observable._breaksatchanges.BreaksAtChanges_IObservableFloat",
            "marketsim.gen._out._ifdefined.IfDefined_IObservableFloatFloat",
            "marketsim.gen._out.ops._mul.Mul_FloatFloat",
            "marketsim.gen._out.ops._mul.Mul_IObservableFloatIObservableFloat",
            "marketsim.gen._out.trader._roughpnl.RoughPnL_IAccount",
            "marketsim.gen._out.math._max.Max_IObservableFloatFloat",
            "marketsim.gen._out.math._sqr.Sqr_IObservableFloat",
            "marketsim.gen._out.ops._div.Div_FloatIObservableFloat",
            "marketsim.gen._out.math._downmovements.DownMovements_IObservableFloatFloat",
            "marketsim.gen._out.orderbook._lastprice.LastPrice_IOrderQueue",
            "marketsim.gen._out.orderbook._bestprice.BestPrice_IOrderQueue",
            "marketsim.gen._out.trader._pendingvolume.PendingVolume_IAccount",
            "marketsim.gen._out.ops._condition.Condition_BooleanFloatIObservableFloat",
            "marketsim.gen._out.math._minimum.Minimum_mathMoving",
            "marketsim.gen._out.ops._sub.Sub_IObservableFloatFloat",
            "marketsim.gen._out.math._sqrt.Sqrt_Float",
            "marketsim.gen._out.trader._position.Position_IAccount",
            "marketsim.gen._out.math._min.Min_IObservableFloatIObservableFloat",
            "marketsim.gen._out.strategy.position._desiredposition.DesiredPosition_strategypositionRSI_linear",
            "marketsim.gen._out.observable._oneverydt.OnEveryDt_FloatFloat",
            "marketsim.gen._out.ops._add.Add_IObservableFloatIObservableFloat",
            "marketsim.gen._out.observable._quote.Quote_StringStringString",
            "marketsim.gen._out.math._log.Log_Float",
            "marketsim.gen._out.ops._sub.Sub_FloatIObservableFloat",
            "marketsim.gen._out.math._relstddev.RelStdDev_mathMoving",
            "marketsim.gen._out.ops._sub.Sub_FloatFloat",
            "marketsim.gen._out.math._atan.Atan_Float",
            "marketsim.gen._out.ops._condition.Condition_BooleanFloatFloat",
            "marketsim.gen._out.math._min.Min_IObservableFloatFloat",
            "marketsim.gen._out.ops._mul.Mul_FloatIObservableFloat",
            "marketsim.gen._out.strategy.position._position.Position_strategypositionBollinger_linear",
            "marketsim.gen._out.strategy.price._price.Price_strategypriceLiquidityProviderSide",
            "marketsim.gen._out._test.in1.in2._intobs.IntObs_",
            "marketsim.gen._out.math._pow.Pow_FloatFloat",
            "marketsim.gen._out.math._upmovements.UpMovements_IObservableFloatFloat",
            "marketsim.gen._out.math._maxepsilon.MaxEpsilon_mathCumulativeFloat",
            "marketsim.gen._out.orderbook._naivecumulativeprice.NaiveCumulativePrice_IOrderBookIObservableFloat"
        ]
    ],
    [
        "marketsim.gen._out.math._rsi.RSI_IObservableFloatFloatFloat",
        [
            "marketsim.gen._out.math._rsi.RSI_IObservableFloatFloatFloat"
        ]
    ],
    [
        "marketsim.gen._out._ifunction._ifunctionifunctionlistoffloat_from_listoffloat.IFunctionIFunctionlistOffloat_from_listOffloat",
        [
            "marketsim.gen._out.strategy.weight.array._array_identityl.array_IdentityL_",
            "marketsim.gen._out.strategy.weight.array._array_choosethebest.array_ChooseTheBest_"
        ]
    ],
    [
        "marketsim.gen._out._ievent.IEvent",
        [
            "marketsim.gen._out.order._immediateorcancel.ImmediateOrCancel_IObservableIOrder",
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanIObservableFloatFloat",
            "marketsim.gen._out.orderbook._spread.Spread_IOrderBook",
            "marketsim.gen._out._observabletrue.observableTrue_",
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanIObservableSideIObservableSide",
            "marketsim.gen._out.math._relstddev.RelStdDev_mathEW",
            "marketsim.gen._out.ops._equal.Equal_IObservableFloatFloat",
            "marketsim.gen._out.orderbook._lastprice.LastPrice_IOrderQueue",
            "marketsim.gen._out.side._observablesell.observableSell_",
            "marketsim.gen._out._test.in1.in2._intobs.IntObs_",
            "marketsim.gen._out.ops._negate.Negate_Float",
            "marketsim.gen._out.strategy.position._position.Position_strategypositionRSI_linear",
            "marketsim.gen._out.math._min.Min_FloatIObservableFloat",
            "marketsim.gen._out.order._limit.Limit_SideFloatFloat",
            "marketsim.gen._out.orderbook._naivecumulativeprice.NaiveCumulativePrice_IOrderBookFloat",
            "marketsim.gen._out.ops._less.Less_FloatIObservableFloat",
            "marketsim.gen._out._const.const_Int",
            "marketsim.gen._out.math._minepsilon.MinEpsilon_mathCumulativeFloat",
            "marketsim.gen._out._const.const_Float",
            "marketsim.gen._out.orderbook._cumulativeprice.CumulativePrice_IOrderBookFloat",
            "marketsim.gen._out.math._relstddev.RelStdDev_mathCumulative",
            "marketsim.gen._out.ops._greater.Greater_FloatIObservableFloat",
            "marketsim.gen._out.math._max.Max_IObservableFloatIObservableFloat",
            "marketsim.gen._out.ops._lessequal.LessEqual_FloatIObservableFloat",
            "marketsim.gen._out.order._limitsigned.LimitSigned_FloatFloat",
            "marketsim.gen._out.observable._breaksatchanges.BreaksAtChanges_IObservableFloat",
            "marketsim.gen._out.ops._greaterequal.GreaterEqual_IObservableFloatFloat",
            "marketsim.gen._out.trader._pendingvolume.PendingVolume_IAccount",
            "marketsim.gen._out.ops._div.Div_FloatIObservableFloat",
            "marketsim.gen._out.orderbook._volumelevels.VolumeLevels_IOrderQueueFloatInt",
            "marketsim.gen._out.math._downmovements.DownMovements_IObservableFloatFloat",
            "marketsim.gen._out.orderbook._bestprice.BestPrice_IOrderQueue",
            "marketsim.gen._out.order._iceberg.Iceberg_IObservableIOrderFloat",
            "marketsim.gen._out.math._sqrt.Sqrt_Float",
            "marketsim.gen._out._observablefalse.observableFalse_",
            "marketsim.gen._out.orderbook._midprice.MidPrice_IOrderBook",
            "marketsim.gen._out.observable._oneverydt.OnEveryDt_FloatFloat",
            "marketsim.gen._out.order._floatingprice.FloatingPrice_FloatIObservableIOrderIObservableFloat",
            "marketsim.gen._out.trader._balance.Balance_IAccount",
            "marketsim.gen._out.math._min.Min_FloatFloat",
            "marketsim.gen._out.math._min.Min_IObservableFloatFloat",
            "marketsim.gen._out.ops._mul.Mul_FloatIObservableFloat",
            "marketsim.gen._out.trader._roughpnl.RoughPnL_IAccount",
            "marketsim.gen._out.strategy.side._fundamental_value.Fundamental_Value_strategysidePairTrading",
            "marketsim.gen._out._candlesticks.CandleSticks_IObservableFloatFloat",
            "marketsim.gen._out._ifdefined.IfDefined_FloatFloat",
            "marketsim.gen._out.ops._lessequal.LessEqual_IObservableFloatIObservableFloat",
            "marketsim.gen._out.ops._lessequal.LessEqual_IObservableFloatFloat",
            "marketsim.gen._out._ifdefined.IfDefined_FloatIObservableFloat",
            "marketsim.gen._out.ops._less.Less_IObservableFloatFloat",
            "marketsim.gen._out.ops._div.Div_IObservableFloatIObservableFloat",
            "marketsim.gen._out._test.in1.in2._o.O_IObservableFloat",
            "marketsim.gen._out.trader._efficiency.Efficiency_IAccount",
            "marketsim.gen._out.ops._condition.Condition_BooleanFloatIObservableFloat",
            "marketsim.gen._out._ifdefined.IfDefined_IObservableFloatIObservableFloat",
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanIObservableSideSide",
            "marketsim.gen._out.strategy.position._desiredposition.DesiredPosition_strategypositionBollinger_linear",
            "marketsim.gen._out.ops._greaterequal.GreaterEqual_FloatIObservableFloat",
            "marketsim.gen._out.ops._div.Div_IObservableFloatFloat",
            "marketsim.gen._out.orderbook._lasttradeprice.LastTradePrice_IOrderQueue",
            "marketsim.gen._out.ops._notequal.NotEqual_IObservableFloatFloat",
            "marketsim.gen._out.order._fixedbudget.FixedBudget_SideFloat",
            "marketsim.gen._out.order._marketsigned.MarketSigned_Float",
            "marketsim.gen._out.strategy.side._side.Side_strategysideMeanReversion",
            "marketsim.gen._out.strategy.side._side.Side_strategysidePairTrading",
            "marketsim.gen._out.ops._greater.Greater_IObservableFloatFloat",
            "marketsim.gen._out.ops._greaterequal.GreaterEqual_FloatFloat",
            "marketsim.gen._out.ops._sub.Sub_FloatFloat",
            "marketsim.gen._out.ops._condition.Condition_BooleanFloatFloat",
            "marketsim.gen._out.math._maxepsilon.MaxEpsilon_mathCumulativeFloat",
            "marketsim.gen._out.orderbook._safesideprice.SafeSidePrice_IOrderQueueFloat",
            "marketsim.gen._out.orderbook._naivecumulativeprice.NaiveCumulativePrice_IOrderBookIObservableFloat",
            "marketsim.gen._out.order._market.Market_SideFloat",
            "marketsim.gen._out.ops._div.Div_FloatFloat",
            "marketsim.gen._out.ops._less.Less_FloatFloat",
            "marketsim.gen._out.ops._condition.Condition_BooleanIObservableSideSide",
            "marketsim.gen._out.orderbook._lasttradevolume.LastTradeVolume_IOrderQueue",
            "marketsim.gen._out.ops._condition.Condition_BooleanIObservableFloatFloat",
            "marketsim.gen._out.math._minimum.Minimum_mathMoving",
            "marketsim.gen._out.ops._negate.Negate_IObservableFloat",
            "marketsim.gen._out.math._max.Max_IObservableFloatFloat",
            "marketsim.gen._out.ops._sub.Sub_IObservableFloatIObservableFloat",
            "marketsim.gen._out.ops._mul.Mul_IObservableFloatFloat",
            "marketsim.gen._out.ops._greaterequal.GreaterEqual_IObservableFloatIObservableFloat",
            "marketsim.gen._out.ops._add.Add_IObservableFloatFloat",
            "marketsim.gen._out.order._stoploss.StopLoss_IObservableIOrderFloat",
            "marketsim.gen._out.ops._equal.Equal_FloatFloat",
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanIObservableFloatIObservableFloat",
            "marketsim.gen._out.order._withexpiry.WithExpiry_IObservableIOrderFloat",
            "marketsim.gen._out.event._every.Every_Float",
            "marketsim.gen._out.math._maximum.Maximum_mathMoving",
            "marketsim.gen._out.ops._mul.Mul_IObservableFloatIObservableFloat",
            "marketsim.gen._out.ops._equal.Equal_FloatIObservableFloat",
            "marketsim.gen._out.ops._sub.Sub_IObservableFloatFloat",
            "marketsim.gen._out.trader._position.Position_IAccount",
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanSideIObservableSide",
            "marketsim.gen._out.ops._greater.Greater_IObservableFloatIObservableFloat",
            "marketsim.gen._out.observable._quote.Quote_StringStringString",
            "marketsim.gen._out.order._peg.Peg_FloatIObservableIOrder",
            "marketsim.gen._out.ops._equal.Equal_IObservableFloatIObservableFloat",
            "marketsim.gen._out.math._max.Max_FloatIObservableFloat",
            "marketsim.gen._out.math._atan.Atan_Float",
            "marketsim.gen._out.math._pow.Pow_FloatFloat",
            "marketsim.gen._out.math._upmovements.UpMovements_IObservableFloatFloat",
            "marketsim.gen._out.ops._condition.Condition_BooleanSideIObservableSide",
            "marketsim.gen._out.math._sqr.Sqr_IObservableFloat",
            "marketsim.gen._out.ops._notequal.NotEqual_FloatFloat",
            "marketsim.gen._out.math._randomwalk.RandomWalk_FloatFloatFloatString",
            "marketsim.gen._out.ops._sub.Sub_FloatIObservableFloat",
            "marketsim.gen._out.ops._greater.Greater_FloatFloat",
            "marketsim.gen._out.ops._lessequal.LessEqual_FloatFloat",
            "marketsim.gen._out.ops._notequal.NotEqual_FloatIObservableFloat",
            "marketsim.gen._out.math._max.Max_FloatFloat",
            "marketsim.gen._out.math._exp.Exp_Float",
            "marketsim.gen._out.ops._add.Add_FloatIObservableFloat",
            "marketsim.gen._out.orderbook._safesideprice.SafeSidePrice_IOrderQueueIObservableFloat",
            "marketsim.gen._out.event._after.After_Float",
            "marketsim.gen._out.ops._add.Add_FloatFloat",
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanSideSide",
            "marketsim.gen._out.strategy.price._price.Price_strategypriceLiquidityProviderSide",
            "marketsim.gen._out.ops._less.Less_IObservableFloatIObservableFloat",
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanFloatIObservableFloat",
            "marketsim.gen._out.ops._notequal.NotEqual_IObservableFloatIObservableFloat",
            "marketsim.gen._out.math._sqr.Sqr_Float",
            "marketsim.gen._out.ops._condition.Condition_BooleanIObservableFloatIObservableFloat",
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanFloatFloat",
            "marketsim.gen._out._ifdefined.IfDefined_IObservableFloatFloat",
            "marketsim.gen._out.ops._mul.Mul_FloatFloat",
            "marketsim.gen._out.ops._condition.Condition_BooleanIObservableSideIObservableSide",
            "marketsim.gen._out.strategy.position._desiredposition.DesiredPosition_strategypositionRSI_linear",
            "marketsim.gen._out.ops._condition.Condition_BooleanSideSide",
            "marketsim.gen._out.side._observablebuy.observableBuy_",
            "marketsim.gen._out.strategy.side._side.Side_strategysideFundamentalValue",
            "marketsim.gen._out.side._observablenothing.observableNothing_",
            "marketsim.gen._out.math._min.Min_IObservableFloatIObservableFloat",
            "marketsim.gen._out.ops._add.Add_IObservableFloatIObservableFloat",
            "marketsim.gen._out.math._relstddev.RelStdDev_mathMoving",
            "marketsim.gen._out.math._lagged.Lagged_IObservableFloatFloat",
            "marketsim.gen._out.strategy.position._position.Position_strategypositionBollinger_linear",
            "marketsim.gen._out.math._log.Log_Float"
        ]
    ],
    [
        "marketsim.gen._out._itrader.ITrader",
        [
            "marketsim.gen._out.trader._singleasset.SingleAsset_IOrderBookISingleAssetStrategyStringFloatFloatListITimeSerie",
            "marketsim.gen._out.trader._singleproxy.SingleProxy_",
            "marketsim.gen._out.trader._multiasset.MultiAsset_ListISingleAssetTraderIMultiAssetStrategyStringFloatListITimeSerie"
        ]
    ],
    [
        {
            "elementType": "marketsim.gen._out._isingleassettrader.ISingleAssetTrader"
        },
        []
    ],
    [
        "marketsim.gen._out.strategy.side._meanreversion.MeanReversion_Float",
        [
            "marketsim.gen._out.strategy.side._meanreversion.MeanReversion_Float"
        ]
    ],
    [
        "marketsim.gen._out._ifunction._ifunctionside.IFunctionSide",
        [
            "marketsim.gen._out.ops._condition.Condition_BooleanSideIObservableSide",
            "marketsim.gen._out.ops._condition.Condition_BooleanIObservableSideSide",
            "marketsim.gen._out.side._buy.Buy_",
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanIObservableSideIObservableSide",
            "marketsim.gen._out.side._observablesell.observableSell_",
            "marketsim.gen._out.strategy.side._side.Side_strategysideFundamentalValue",
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanSideSide",
            "marketsim.gen._out.strategy.side._side.Side_strategysideRSIbis",
            "marketsim.gen._out.side._sell.Sell_",
            "marketsim.gen._out.strategy.side._side.Side_strategysideNoise",
            "marketsim.gen._out.ops._condition.Condition_BooleanIObservableSideIObservableSide",
            "marketsim.gen._out.strategy.side._side.Side_strategysideSignal",
            "marketsim.gen._out.strategy.side._side.Side_strategysideMeanReversion",
            "marketsim.gen._out.side._observablebuy.observableBuy_",
            "marketsim.gen._out.strategy.side._side.Side_strategysideCrossingAverages",
            "marketsim.gen._out.side._observablenothing.observableNothing_",
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanSideIObservableSide",
            "marketsim.gen._out.strategy.side._side.Side_strategysidePairTrading",
            "marketsim.gen._out.side._nothing.Nothing_",
            "marketsim.gen._out.strategy.side._side.Side_strategysideTrendFollower",
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanIObservableSideSide",
            "marketsim.gen._out.ops._condition.Condition_BooleanSideSide"
        ]
    ],
    [
        {
            "elementType": "marketsim.gen._out._igraph.IGraph"
        },
        []
    ],
    [
        "marketsim.gen._out.strategy.position._rsi_linear.RSI_linear_FloatIObservableFloatFloatISingleAssetTrader",
        [
            "marketsim.gen._out.strategy.position._rsi_linear.RSI_linear_FloatIObservableFloatFloatISingleAssetTrader"
        ]
    ],
    [
        "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool",
        [
            "marketsim.gen._out._true.true_",
            "marketsim.gen._out._observabletrue.observableTrue_",
            "marketsim.gen._out.ops._lessequal.LessEqual_IObservableFloatIObservableFloat",
            "marketsim.gen._out.ops._equal.Equal_IObservableFloatFloat",
            "marketsim.gen._out.ops._less.Less_FloatFloat",
            "marketsim.gen._out.ops._greater.Greater_IObservableFloatIObservableFloat",
            "marketsim.gen._out.ops._greater.Greater_FloatFloat",
            "marketsim.gen._out.ops._lessequal.LessEqual_IObservableFloatFloat",
            "marketsim.gen._out.ops._lessequal.LessEqual_FloatFloat",
            "marketsim.gen._out.ops._notequal.NotEqual_FloatIObservableFloat",
            "marketsim.gen._out.ops._notequal.NotEqual_FloatFloat",
            "marketsim.gen._out.ops._less.Less_IObservableFloatFloat",
            "marketsim.gen._out.ops._greaterequal.GreaterEqual_IObservableFloatIObservableFloat",
            "marketsim.gen._out.ops._less.Less_IObservableFloatIObservableFloat",
            "marketsim.gen._out.ops._equal.Equal_FloatFloat",
            "marketsim.gen._out.ops._less.Less_FloatIObservableFloat",
            "marketsim.gen._out.ops._notequal.NotEqual_IObservableFloatIObservableFloat",
            "marketsim.gen._out.ops._greaterequal.GreaterEqual_FloatIObservableFloat",
            "marketsim.gen._out.ops._greater.Greater_FloatIObservableFloat",
            "marketsim.gen._out.ops._lessequal.LessEqual_FloatIObservableFloat",
            "marketsim.gen._out.ops._notequal.NotEqual_IObservableFloatFloat",
            "marketsim.gen._out.ops._greaterequal.GreaterEqual_IObservableFloatFloat",
            "marketsim.gen._out._false.false_",
            "marketsim.gen._out.ops._equal.Equal_FloatIObservableFloat",
            "marketsim.gen._out._observablefalse.observableFalse_",
            "marketsim.gen._out.ops._greater.Greater_IObservableFloatFloat",
            "marketsim.gen._out.ops._greaterequal.GreaterEqual_FloatFloat",
            "marketsim.gen._out.ops._equal.Equal_IObservableFloatIObservableFloat"
        ]
    ],
    [
        "marketsim.gen._out.strategy.position._bollinger_linear.Bollinger_linear_FloatIObservableFloatISingleAssetTrader",
        [
            "marketsim.gen._out.strategy.position._bollinger_linear.Bollinger_linear_FloatIObservableFloatISingleAssetTrader"
        ]
    ],
    [
        "marketsim.gen._out.math._cumulative.Cumulative_IObservableFloat",
        [
            "marketsim.gen._out.math._cumulative.Cumulative_IObservableFloat"
        ]
    ],
    [
        "marketsim.gen._out._isingleassettrader.ISingleAssetTrader",
        [
            "marketsim.gen._out.trader._singleasset.SingleAsset_IOrderBookISingleAssetStrategyStringFloatFloatListITimeSerie",
            "marketsim.gen._out.trader._singleproxy.SingleProxy_"
        ]
    ],
    [
        {
            "elementType": "marketsim.gen._out._itrader.ITrader"
        },
        []
    ],
    [
        "marketsim.gen._out._ifunction._ifunctionifunctionfloat_from_iaccount.IFunctionIFunctionfloat_from_IAccount",
        [
            "marketsim.gen._out.strategy.weight.trader._trader_traderefficiency.trader_TraderEfficiency_",
            "marketsim.gen._out.strategy.weight.trader._trader_score.trader_Score_",
            "marketsim.gen._out.strategy.weight.trader._trader_traderefficiencytrend.trader_TraderEfficiencyTrend_Float",
            "marketsim.gen._out.strategy.weight.trader._trader_unit.trader_Unit_"
        ]
    ],
    [
        "marketsim.gen._out._ifunction._ifunctionifunctioniobservableiorder_from_ifunctionfloat_from_ifunctionside.IFunctionIFunctionIObservableIOrder_from_IFunctionfloat_from_IFunctionSide",
        [
            "marketsim.gen._out.order._curried._side_price_floatingprice.side_price_FloatingPrice_SideFloatIObservableIOrderIObservableFloat",
            "marketsim.gen._out.order._curried._side_price_withexpiry.side_price_WithExpiry_SideFloatIObservableIOrderFloat",
            "marketsim.gen._out.order._curried._side_price_immediateorcancel.side_price_ImmediateOrCancel_SideFloatIObservableIOrder",
            "marketsim.gen._out.order._curried._side_price_peg.side_price_Peg_SideFloatIObservableIOrder",
            "marketsim.gen._out.order._curried._side_price_stoploss.side_price_StopLoss_SideFloatIObservableIOrderFloat",
            "marketsim.gen._out.order._curried._side_price_iceberg.side_price_Iceberg_SideFloatIObservableIOrderFloat",
            "marketsim.gen._out.order._curried._side_price_limit.side_price_Limit_Float"
        ]
    ],
    [
        "marketsim.gen._out.strategy.side._pairtrading.PairTrading_IOrderBookFloat",
        [
            "marketsim.gen._out.strategy.side._pairtrading.PairTrading_IOrderBookFloat"
        ]
    ],
    [
        "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
        [
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanIObservableFloatFloat",
            "marketsim.gen._out.orderbook._spread.Spread_IOrderBook",
            "marketsim.gen._out._constant.constant_Int",
            "marketsim.gen._out.math._relstddev.RelStdDev_mathEW",
            "marketsim.gen._out.math._signal.Signal_mathmacdFloatFloat",
            "marketsim.gen._out.strategy.side._fundamental_value.Fundamental_Value_strategysideMeanReversion",
            "marketsim.gen._out.math.random._gammavariate.gammavariate_FloatFloat",
            "marketsim.gen._out.orderbook._lastprice.LastPrice_IOrderQueue",
            "marketsim.gen._out._test.in1.in2._intobs.IntObs_",
            "marketsim.gen._out.ops._negate.Negate_Float",
            "marketsim.gen._out.strategy.position._position.Position_strategypositionRSI_linear",
            "marketsim.gen._out.math._min.Min_FloatIObservableFloat",
            "marketsim.gen._out.orderbook._naivecumulativeprice.NaiveCumulativePrice_IOrderBookFloat",
            "marketsim.gen._out._constant.constant_Float",
            "marketsim.gen._out._const.const_Int",
            "marketsim.gen._out.math._minepsilon.MinEpsilon_mathCumulativeFloat",
            "marketsim.gen._out._const.const_Float",
            "marketsim.gen._out.orderbook._cumulativeprice.CumulativePrice_IOrderBookFloat",
            "marketsim.gen._out.math._relstddev.RelStdDev_mathCumulative",
            "marketsim.gen._out.math._max.Max_IObservableFloatIObservableFloat",
            "marketsim.gen._out.math.random._normalvariate.normalvariate_FloatFloat",
            "marketsim.gen._out.observable._breaksatchanges.BreaksAtChanges_IObservableFloat",
            "marketsim.gen._out.trader._pendingvolume.PendingVolume_IAccount",
            "marketsim.gen._out.math._logreturns.LogReturns_IObservableFloatFloat",
            "marketsim.gen._out._test.in1.in2._f.F_Float",
            "marketsim.gen._out.math._downmovements.DownMovements_IObservableFloatFloat",
            "marketsim.gen._out.orderbook._bestprice.BestPrice_IOrderQueue",
            "marketsim.gen._out.math._var.Var_mathCumulative",
            "marketsim.gen._out.strategy.weight._unit.Unit_IAccount",
            "marketsim.gen._out.math._sqrt.Sqrt_Float",
            "marketsim.gen._out.orderbook._midprice.MidPrice_IOrderBook",
            "marketsim.gen._out.observable._oneverydt.OnEveryDt_FloatFloat",
            "marketsim.gen._out.trader._balance.Balance_IAccount",
            "marketsim.gen._out.strategy.weight._traderefficiencytrend.TraderEfficiencyTrend_IAccountFloat",
            "marketsim.gen._out.math._min.Min_FloatFloat",
            "marketsim.gen._out.math._min.Min_IObservableFloatFloat",
            "marketsim.gen._out.ops._mul.Mul_FloatIObservableFloat",
            "marketsim.gen._out.trader._roughpnl.RoughPnL_IAccount",
            "marketsim.gen._out.strategy.side._fundamental_value.Fundamental_Value_strategysidePairTrading",
            "marketsim.gen._out.math.random._uniform.uniform_FloatFloat",
            "marketsim.gen._out._ifdefined.IfDefined_FloatFloat",
            "marketsim.gen._out.math._var.Var_mathMoving",
            "marketsim.gen._out.strategy.weight._identityf.IdentityF_Float",
            "marketsim.gen._out.strategy.weight._traderefficiency.TraderEfficiency_IAccount",
            "marketsim.gen._out._ifdefined.IfDefined_FloatIObservableFloat",
            "marketsim.gen._out.ops._div.Div_IObservableFloatIObservableFloat",
            "marketsim.gen._out._test.in1.in2._o.O_IObservableFloat",
            "marketsim.gen._out.trader._efficiency.Efficiency_IAccount",
            "marketsim.gen._out.ops._condition.Condition_BooleanFloatIObservableFloat",
            "marketsim.gen._out.math.random._expovariate.expovariate_Float",
            "marketsim.gen._out._ifdefined.IfDefined_IObservableFloatIObservableFloat",
            "marketsim.gen._out.math.random._triangular.triangular_FloatFloatFloat",
            "marketsim.gen._out.strategy.position._desiredposition.DesiredPosition_strategypositionBollinger_linear",
            "marketsim.gen._out.math._value.Value_mathRSI",
            "marketsim.gen._out.ops._div.Div_IObservableFloatFloat",
            "marketsim.gen._out.orderbook._lasttradeprice.LastTradePrice_IOrderQueue",
            "marketsim.gen._out.math._avg.Avg_mathCumulative",
            "marketsim.gen._out.math._avg.Avg_mathMoving",
            "marketsim.gen._out.orderbook._naivecumulativeprice.NaiveCumulativePrice_IOrderBookIObservableFloat",
            "marketsim.gen._out._null.null_",
            "marketsim.gen._out.math.random._paretovariate.paretovariate_Float",
            "marketsim.gen._out.orderbook._weightedprice.WeightedPrice_IOrderQueueFloat",
            "marketsim.gen._out.strategy.side._signal_value.Signal_Value_strategysideRSIbis",
            "marketsim.gen._out.ops._sub.Sub_FloatIObservableFloat",
            "marketsim.gen._out.ops._sub.Sub_FloatFloat",
            "marketsim.gen._out.ops._condition.Condition_BooleanFloatFloat",
            "marketsim.gen._out._test.in1.in2._intfunc.IntFunc_",
            "marketsim.gen._out.math._maxepsilon.MaxEpsilon_mathCumulativeFloat",
            "marketsim.gen._out.orderbook._safesideprice.SafeSidePrice_IOrderQueueFloat",
            "marketsim.gen._out.orderbook._lasttradevolume.LastTradeVolume_IOrderQueue",
            "marketsim.gen._out.ops._condition.Condition_BooleanIObservableFloatFloat",
            "marketsim.gen._out.ops._negate.Negate_IObservableFloat",
            "marketsim.gen._out.math._max.Max_IObservableFloatFloat",
            "marketsim.gen._out.ops._sub.Sub_IObservableFloatIObservableFloat",
            "marketsim.gen._out.ops._mul.Mul_IObservableFloatFloat",
            "marketsim.gen._out.strategy.side._fundamental_value.Fundamental_Value_strategysideFundamentalValue",
            "marketsim.gen._out.ops._add.Add_IObservableFloatFloat",
            "marketsim.gen._out.ops._div.Div_FloatFloat",
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanIObservableFloatIObservableFloat",
            "marketsim.gen._out.math._raw.Raw_mathRSI",
            "marketsim.gen._out.math._avg.Avg_mathEW",
            "marketsim.gen._out.math._derivative.Derivative_IDifferentiable",
            "marketsim.gen._out.math._maximum.Maximum_mathMoving",
            "marketsim.gen._out.trader._efficiencytrend.EfficiencyTrend_IAccountFloat",
            "marketsim.gen._out.strategy.weight._score.Score_IAccount",
            "marketsim.gen._out.ops._mul.Mul_IObservableFloatIObservableFloat",
            "marketsim.gen._out.strategy.weight._clamp0.Clamp0_Float",
            "marketsim.gen._out.math.random._betavariate.betavariate_FloatFloat",
            "marketsim.gen._out.ops._sub.Sub_IObservableFloatFloat",
            "marketsim.gen._out.trader._position.Position_IAccount",
            "marketsim.gen._out.observable._quote.Quote_StringStringString",
            "marketsim.gen._out.math._stddev.StdDev_mathMoving",
            "marketsim.gen._out.math._max.Max_FloatIObservableFloat",
            "marketsim.gen._out.math._atan.Atan_Float",
            "marketsim.gen._out.orderbook._ticksize.TickSize_IOrderBook",
            "marketsim.gen._out.math._minimum.Minimum_mathMoving",
            "marketsim.gen._out.math._upmovements.UpMovements_IObservableFloatFloat",
            "marketsim.gen._out._test.overloading._hh.hh_",
            "marketsim.gen._out.math._sqr.Sqr_IObservableFloat",
            "marketsim.gen._out.strategy.side._signal_value.Signal_Value_strategysideTrendFollower",
            "marketsim.gen._out.math._randomwalk.RandomWalk_FloatFloatFloatString",
            "marketsim.gen._out.math.random._weibullvariate.weibullvariate_FloatFloat",
            "marketsim.gen._out.strategy.weight._atanpow.AtanPow_FloatFloat",
            "marketsim.gen._out.math._max.Max_FloatFloat",
            "marketsim.gen._out.math._exp.Exp_Float",
            "marketsim.gen._out.ops._add.Add_FloatIObservableFloat",
            "marketsim.gen._out.orderbook._safesideprice.SafeSidePrice_IOrderQueueIObservableFloat",
            "marketsim.gen._out.math._stddev.StdDev_mathEW",
            "marketsim.gen._out.ops._add.Add_FloatFloat",
            "marketsim.gen._out.math._var.Var_mathEW",
            "marketsim.gen._out._test.overloading._h.h_",
            "marketsim.gen._out.strategy.price._price.Price_strategypriceLiquidityProviderSide",
            "marketsim.gen._out.math.random._vonmisesvariate.vonmisesvariate_FloatFloat",
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanFloatIObservableFloat",
            "marketsim.gen._out.math._stddev.StdDev_mathCumulative",
            "marketsim.gen._out.math._sqr.Sqr_Float",
            "marketsim.gen._out.ops._condition.Condition_BooleanIObservableFloatIObservableFloat",
            "marketsim.gen._out.math.random._lognormvariate.lognormvariate_FloatFloat",
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanFloatFloat",
            "marketsim.gen._out._ifdefined.IfDefined_IObservableFloatFloat",
            "marketsim.gen._out.ops._mul.Mul_FloatFloat",
            "marketsim.gen._out.strategy.position._desiredposition.DesiredPosition_strategypositionRSI_linear",
            "marketsim.gen._out.math._pow.Pow_FloatFloat",
            "marketsim.gen._out.strategy.side._signal_value.Signal_Value_strategysideSignal",
            "marketsim.gen._out.math._min.Min_IObservableFloatIObservableFloat",
            "marketsim.gen._out.ops._add.Add_IObservableFloatIObservableFloat",
            "marketsim.gen._out.ops._div.Div_FloatIObservableFloat",
            "marketsim.gen._out.math._relstddev.RelStdDev_mathMoving",
            "marketsim.gen._out.math._value.Value_mathmacd",
            "marketsim.gen._out.math._lagged.Lagged_IObservableFloatFloat",
            "marketsim.gen._out.strategy.position._position.Position_strategypositionBollinger_linear",
            "marketsim.gen._out.strategy.side._signal_value.Signal_Value_strategysideCrossingAverages",
            "marketsim.gen._out.math._log.Log_Float",
            "marketsim.gen._out.math._histogram.Histogram_mathmacdFloatFloat"
        ]
    ],
    [
        "marketsim.gen._out.strategy.price._liquidityprovider.LiquidityProvider_FloatFloatIOrderBook",
        [
            "marketsim.gen._out.strategy.price._liquidityprovider.LiquidityProvider_FloatFloatIOrderBook"
        ]
    ],
    [
        {
            "elementType": "marketsim.gen._out._itimeserie.ITimeSerie"
        },
        []
    ],
    [
        "marketsim.gen._out._iorderbook.IOrderBook",
        [
            "marketsim.gen._out.strategy.side._book.book_strategysidePairTrading",
            "marketsim.gen._out.orderbook._local.Local_StringFloatIntListITimeSerie",
            "marketsim.gen._out.strategy.side._book.book_strategysideMeanReversion",
            "marketsim.gen._out.orderbook._oftrader.OfTrader_IAccount",
            "marketsim.gen._out.strategy.side._book.book_strategysideFundamentalValue",
            "marketsim.gen._out.orderbook._remote.Remote_IOrderBookITwoWayLinkListITimeSerie",
            "marketsim.gen._out.orderbook._proxy.Proxy_"
        ]
    ],
    [
        "marketsim.gen._out.strategy.side._rsibis.RSIbis_FloatFloatFloat",
        [
            "marketsim.gen._out.strategy.side._rsibis.RSIbis_FloatFloatFloat"
        ]
    ],
    [
        "marketsim.gen._out._itwowaylink.ITwoWayLink",
        [
            "marketsim.gen._out.orderbook._twowaylink.TwoWayLink_ILinkILink"
        ]
    ],
    [
        "marketsim.gen._out._imultiassetstrategy.IMultiAssetStrategy",
        [
            "marketsim.gen._out.strategy._arbitrage.Arbitrage_"
        ]
    ],
    [
        "marketsim.gen._out._iobservable._iobservableside.IObservableSide",
        [
            "marketsim.gen._out.ops._condition.Condition_BooleanSideIObservableSide",
            "marketsim.gen._out.ops._condition.Condition_BooleanIObservableSideSide",
            "marketsim.gen._out.strategy.side._side.Side_strategysideFundamentalValue",
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanSideIObservableSide",
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanIObservableSideIObservableSide",
            "marketsim.gen._out.ops._condition.Condition_BooleanIObservableSideIObservableSide",
            "marketsim.gen._out.strategy.side._side.Side_strategysidePairTrading",
            "marketsim.gen._out.side._observablesell.observableSell_",
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanIObservableSideSide",
            "marketsim.gen._out.ops._condition.Condition_BooleanSideSide",
            "marketsim.gen._out.side._observablebuy.observableBuy_",
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanSideSide",
            "marketsim.gen._out.side._observablenothing.observableNothing_",
            "marketsim.gen._out.strategy.side._side.Side_strategysideMeanReversion"
        ]
    ],
    [
        "identity",
        [
            "marketsim.gen._out._test.in1.in2._s2.S2_",
            "marketsim.gen._out._test.in1.in2._s1.S1_String"
        ]
    ],
    [
        {
            "elementType": "marketsim.gen._out._iorderbook.IOrderBook"
        },
        []
    ],
    [
        "marketsim.gen._out.math._ew.EW_IObservableFloatFloat",
        [
            "marketsim.gen._out.math._ew.EW_IObservableFloatFloat"
        ]
    ],
    [
        "marketsim.gen._out.strategy.price._marketdata.MarketData_StringStringStringFloatFloat",
        [
            "marketsim.gen._out.strategy.price._marketdata.MarketData_StringStringStringFloatFloat"
        ]
    ]
]