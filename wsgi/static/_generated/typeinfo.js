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
        "description": "<div class=\"document\">\n<p><strong>Moving average convergence/divergence signal</strong></p>\n<p>Parameters are:</p>\n<p><strong>x</strong></p>\n<dl class=\"docutils\">\n<dt><strong>timeframe</strong></dt>\n<dd>signal period</dd>\n<dt><strong>step</strong></dt>\n<dd>discretization step</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Returns traders eficiency. Under efficiency we understand trader balance if trader position was cleared</strong></p>\n<p>Parameters are:</p>\n<p><strong>trader</strong></p>\n</div>\n"
    },
    "marketsim.gen._out.ops._condition.Condition_BooleanBooleanBoolean": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool",
            "marketsim.gen._out._iobservable._iobservablebool.IObservablebool",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "ifpart": {
                "type": "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool"
            },
            "elsepart": {
                "type": "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool"
            },
            "cond": {
                "type": "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool"
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
        "description": "<div class=\"document\">\n<p><strong>Returns naive approximation of price for best orders of total volume *depth*</strong></p>\n<blockquote>\n<p>by taking into account prices only for the best order</p>\n<p>Negative <em>depth</em> correponds to will buy assets\nPositive <em>depth</em> correponds to will sell assets</p>\n</blockquote>\n<p>Parameters are:</p>\n<p><strong>book</strong></p>\n<p><strong>depth</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Factory creating StopLoss orders</strong></p>\n<blockquote>\nStopLoss order is initialised by an underlying order and a maximal acceptable loss factor.\nIt keeps track of position and balance change induced by trades of the underlying order and\nif losses from keeping the position exceed certain limit (given by maximum loss factor),\nthe meta order clears its position.</blockquote>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>proto</strong></dt>\n<dd>underlying orders to create</dd>\n<dt><strong>maxloss</strong></dt>\n<dd>maximal acceptable loss factor</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Returns price for best orders of total volume *depth*</strong></p>\n<blockquote>\n<p>In other words cumulative price corresponds to trader balance change\nif a market order of volume <em>depth</em> is completely matched</p>\n<p>Negative <em>depth</em> correponds to will buy assets\nPositive <em>depth</em> correponds to will sell assets</p>\n</blockquote>\n<p>Parameters are:</p>\n<p><strong>book</strong></p>\n<p><strong>depth</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Factory creating limit orders</strong></p>\n<blockquote>\nLimit orders ask to buy or sell some asset at price better than some limit price.\nIf a limit order is not competely fulfilled\nit remains in an order book waiting to be matched with another order.</blockquote>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>price</strong></dt>\n<dd>function defining price of orders to create</dd>\n<dt><strong>volume</strong></dt>\n<dd>function defining volume of orders to create</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>A trader that trades different assets</strong></p>\n<blockquote>\nIt can be considered as a composition of single asset traders and multi asset strategies\nAt the moment there is no way to instruct a multi asset strategy to trade only on subset of the assets</blockquote>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>traders</strong></dt>\n<dd>defines accounts for every asset to trade</dd>\n<dt><strong>strategy</strong></dt>\n<dd>multi asset strategy run by the trader</dd>\n</dl>\n<p><strong>name</strong></p>\n<dl class=\"docutils\">\n<dt><strong>PnL</strong></dt>\n<dd>current trader balance (number of money units that it owns)</dd>\n<dt><strong>timeseries</strong></dt>\n<dd>defines what data should be gathered for the trader</dd>\n</dl>\n</div>\n"
    },
    "marketsim.gen._out.ops._condition.Condition_IObservableBooleanIObservableBooleanIObservableBoolean": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool",
            "marketsim.gen._out._iobservable._iobservablebool.IObservablebool",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "ifpart": {
                "type": "marketsim.gen._out._iobservable._iobservablebool.IObservablebool"
            },
            "elsepart": {
                "type": "marketsim.gen._out._iobservable._iobservablebool.IObservablebool"
            },
            "cond": {
                "type": "marketsim.gen._out._iobservable._iobservablebool.IObservablebool"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
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
    "marketsim.gen._out.ops._condition.Condition_BooleanIObservableBooleanBoolean": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool",
            "marketsim.gen._out._iobservable._iobservablebool.IObservablebool",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "ifpart": {
                "type": "marketsim.gen._out._iobservable._iobservablebool.IObservablebool"
            },
            "elsepart": {
                "type": "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool"
            },
            "cond": {
                "type": "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool"
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
        "description": "<div class=\"document\">\n<p><strong>Square root of *x*</strong></p>\n<p>Parameters are:</p>\n<p><strong>x</strong></p>\n</div>\n"
    },
    "marketsim.gen._out._observablefalse.observableFalse_": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool",
            "marketsim.gen._out._iobservable._iobservablebool.IObservablebool",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n<p><strong>Trivial observable always returning *False*</strong></p>\n<p>Parameters are:</p>\n</div>\n"
    },
    "marketsim.gen._out.side._observablesell.observableSell_": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionside.IFunctionSide",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject",
            "marketsim.gen._out._iobservable._iobservableside.IObservableSide"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n<p><strong>Observable always equal to Sell side</strong></p>\n<p>Parameters are:</p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Number of money owned by trader</strong></p>\n<p>Parameters are:</p>\n<p><strong>trader</strong></p>\n</div>\n"
    },
    "marketsim.gen._out.ops._or.Or_BooleanIObservableBoolean": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool",
            "marketsim.gen._out._iobservable._iobservablebool.IObservablebool",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "y": {
                "type": "marketsim.gen._out._iobservable._iobservablebool.IObservablebool"
            },
            "x": {
                "type": "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool"
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
        "description": "<div class=\"document\">\n<p><strong>Returns first derivative of a moving average of the trader efficiency</strong></p>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>trader</strong></dt>\n<dd>account in question</dd>\n<dt><strong>alpha</strong></dt>\n<dd>parameter alpha for the moving average</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Function returning minimum of two functions *x* and *y*.</strong></p>\n<blockquote>\nIf <em>x</em> or/and <em>y</em> are observables, <em>Min</em> is also observable</blockquote>\n<p>Parameters are:</p>\n<p><strong>x</strong></p>\n<p><strong>y</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Function returning minimum of two functions *x* and *y*.</strong></p>\n<blockquote>\nIf <em>x</em> or/and <em>y</em> are observables, <em>Min</em> is also observable</blockquote>\n<p>Parameters are:</p>\n<p><strong>x</strong></p>\n<p><strong>y</strong></p>\n</div>\n"
    },
    "marketsim.gen._out.ops._or.Or_BooleanBoolean": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool",
            "marketsim.gen._out._iobservable._iobservablebool.IObservablebool",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "y": {
                "type": "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool"
            },
            "x": {
                "type": "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Graph to render at Veusz. Time series are added to it automatically in their constructor</strong></p>\n<p>Parameters are:</p>\n<p><strong>name</strong></p>\n</div>\n"
    },
    "marketsim.gen._out.ops._condition.Condition_IObservableBooleanBooleanIObservableBoolean": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool",
            "marketsim.gen._out._iobservable._iobservablebool.IObservablebool",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "ifpart": {
                "type": "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool"
            },
            "elsepart": {
                "type": "marketsim.gen._out._iobservable._iobservablebool.IObservablebool"
            },
            "cond": {
                "type": "marketsim.gen._out._iobservable._iobservablebool.IObservablebool"
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
        "description": "<div class=\"document\">\n<p><strong>Simple moving variance</strong></p>\n<p>Parameters are:</p>\n<p><strong>x</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Identity function for an array of floats</strong></p>\n<p>Parameters are:</p>\n<p><strong>array</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Function returning an array of length *len(array)*</strong></p>\n<blockquote>\nhaving 1 at the index of the maximal element and 0 are at the rest</blockquote>\n<p>Parameters are:</p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>scaling function = max(0, f(x)) + 1</strong></p>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>f</strong></dt>\n<dd>function to scale</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Triangular distribution</strong></p>\n<blockquote>\n<dl class=\"docutils\">\n<dt>Return a random floating point number <em>N</em> such that <em>low</em> &lt;= <em>N</em> &lt;= <em>high</em> and</dt>\n<dd>with the specified <em>mode</em> between those bounds.\nThe <em>low</em> and <em>high</em> bounds default to zero and one.\nThe <em>mode</em> argument defaults to the midpoint between the bounds,\ngiving a symmetric distribution.</dd>\n</dl>\n</blockquote>\n<p>Parameters are:</p>\n<p><strong>Low</strong></p>\n<p><strong>High</strong></p>\n<p><strong>Mode</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Generic strategy that wakes up on events given by *eventGen*,</strong></p>\n<blockquote>\ncreates an order via <em>orderFactory</em> and sends the order to the market using its trader</blockquote>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>orderFactory</strong></dt>\n<dd>order factory function</dd>\n<dt><strong>eventGen</strong></dt>\n<dd>Event source making the strategy to wake up</dd>\n</dl>\n</div>\n"
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
    "marketsim.gen._out.strategy.price._stoploss.StopLoss_ISuspendableStrategyIObservableFloat": {
        "castsTo": [
            "marketsim.gen._out._isingleassetstrategy.ISingleAssetStrategy"
        ],
        "properties": {
            "lossFactor": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
            },
            "inner": {
                "type": "marketsim.gen._out._isuspendablestrategy.ISuspendableStrategy"
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
        "description": "<div class=\"document\">\n<p><strong>Returns naive approximation of price for best orders of total volume *depth*</strong></p>\n<blockquote>\n<p>by taking into account prices only for the best order</p>\n<p>Negative <em>depth</em> correponds to will buy assets\nPositive <em>depth</em> correponds to will sell assets</p>\n</blockquote>\n<p>Parameters are:</p>\n<p><strong>book</strong></p>\n<p><strong>depth</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Factory creating limit orders</strong></p>\n<blockquote>\nLimit orders ask to buy or sell some asset at price better than some limit price.\nIf a limit order is not competely fulfilled\nit remains in an order book waiting to be matched with another order.</blockquote>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>volume</strong></dt>\n<dd>function defining volume of orders to create</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Adaptive strategy that evaluates *inner* strategy efficiency</strong></p>\n<blockquote>\nand if it is considered as good, sends orders</blockquote>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>inner</strong></dt>\n<dd>wrapped strategy</dd>\n<dt><strong>account</strong></dt>\n<dd>defines how strategy trades are booked:\nactually traded amount or virtual market orders are\nused in order to estimate how the strategy would have traded\nif all its orders appeared at market</dd>\n<dt><strong>performance</strong></dt>\n<dd>given a trading account tells\nshould it be considered as effective or not</dd>\n</dl>\n</div>\n"
    },
    "marketsim.gen._out.trader._pershareprice.PerSharePrice_IAccount": {
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
    "marketsim.gen._out.strategy.price._stoploss.StopLoss_ISuspendableStrategyFloat": {
        "castsTo": [
            "marketsim.gen._out._isingleassetstrategy.ISingleAssetStrategy"
        ],
        "properties": {
            "lossFactor": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
            },
            "inner": {
                "type": "marketsim.gen._out._isuspendablestrategy.ISuspendableStrategy"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Function always returning *True*</strong></p>\n<p>Parameters are:</p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Factory creating Peg orders</strong></p>\n<blockquote>\nA peg order is a particular case of the floating price order\nwith the price better at one tick than the best price of the order queue.\nIt implies that if several peg orders are sent to the same order queue\nthey start to race until being matched against the counterparty orders.</blockquote>\n<p>Parameters are:</p>\n<p><strong>proto</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Function returning maximum of two functions *x* and *y*.</strong></p>\n<blockquote>\nIf <em>x</em> or/and <em>y</em> are observables, <em>Min</em> is also observable</blockquote>\n<p>Parameters are:</p>\n<p><strong>x</strong></p>\n<p><strong>y</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Event that fires every *intervalFunc* moments of time</strong></p>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>intervalFunc</strong></dt>\n<dd>interval of time between two events</dd>\n</dl>\n</div>\n"
    },
    "marketsim.gen._out.strategy._arbitrage.Arbitrage_": {
        "castsTo": [
            "marketsim.gen._out._imultiassetstrategy.IMultiAssetStrategy"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n<p><strong>Strategy for a multi asset trader.</strong></p>\n<blockquote>\nIt believes that these assets represent a single asset traded on different venues\nOnce an ask at one venue becomes lower than a bid at another venue\nit sends market sell and buy orders in order to exploit this arbitrage possibility</blockquote>\n<p>Parameters are:</p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Returns first derivative of a moving average of the trader efficiency</strong></p>\n<p>Parameters are:</p>\n<p><strong>trader</strong></p>\n<p><strong>alpha</strong></p>\n</div>\n"
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
    "marketsim.gen._out.ops._condition.Condition_IObservableBooleanBooleanBoolean": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool",
            "marketsim.gen._out._iobservable._iobservablebool.IObservablebool",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "ifpart": {
                "type": "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool"
            },
            "elsepart": {
                "type": "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool"
            },
            "cond": {
                "type": "marketsim.gen._out._iobservable._iobservablebool.IObservablebool"
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
        "description": "<div class=\"document\">\n<p><strong>Factory creating limit orders</strong></p>\n<blockquote>\nLimit orders ask to buy or sell some asset at price better than some limit price.\nIf a limit order is not competely fulfilled\nit remains in an order book waiting to be matched with another order.</blockquote>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>side</strong></dt>\n<dd>function defining side of orders to create</dd>\n<dt><strong>volume</strong></dt>\n<dd>function defining volume of orders to create</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Factory creating Peg orders</strong></p>\n<blockquote>\nA peg order is a particular case of the floating price order\nwith the price better at one tick than the best price of the order queue.\nIt implies that if several peg orders are sent to the same order queue\nthey start to race until being matched against the counterparty orders.</blockquote>\n<p>Parameters are:</p>\n<p><strong>proto</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>A discrete signal with user-defined increments.</strong></p>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>initialValue</strong></dt>\n<dd>initial value of the signal</dd>\n<dt><strong>deltaDistr</strong></dt>\n<dd>increment function</dd>\n<dt><strong>intervalDistr</strong></dt>\n<dd>intervals between signal updates</dd>\n</dl>\n<p><strong>name</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Factory creating Immediate-Or-Cancel orders</strong></p>\n<blockquote>\nImmediate-Or-Cancel order sends an underlying order to the market and\nimmediately sends a cancel request for it.\nIt allows to combine market and limit order behaviour:\nthe order is either executed immediately\nat price equal or better than given one\neither it is cancelled (and consequently never stored in the order queue).</blockquote>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>proto</strong></dt>\n<dd>factory for underlying orders</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>scaling function = atan(base^f(x))</strong></p>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>f</strong></dt>\n<dd>function to scale</dd>\n<dt><strong>base</strong></dt>\n<dd>base for power function</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Associated with a strategy account that tracks</strong></p>\n<blockquote>\nhow orders sent by the strategy have been actually traded</blockquote>\n<p>Parameters are:</p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Standard deviation</strong></p>\n<p>Parameters are:</p>\n<p><strong>x</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Von Mises distribution</strong></p>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>Mu</strong></dt>\n<dd>\u03bc is the mean angle, expressed in radians between 0 and 2|pi|</dd>\n<dt><strong>Kappa</strong></dt>\n<dd><dl class=\"first last docutils\">\n<dt>\u03ba is the concentration parameter, which must be greater than or equal to zero.</dt>\n<dd>If \u03ba is equal to zero, this distribution reduces\nto a uniform random angle over the range 0 to 2|pi|</dd>\n</dl>\n</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Square of *x*</strong></p>\n<p>Parameters are:</p>\n<p><strong>x</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Factory creating Immediate-Or-Cancel orders</strong></p>\n<blockquote>\nImmediate-Or-Cancel order sends an underlying order to the market and\nimmediately sends a cancel request for it.\nIt allows to combine market and limit order behaviour:\nthe order is either executed immediately\nat price equal or better than given one\neither it is cancelled (and consequently never stored in the order queue).</blockquote>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>proto</strong></dt>\n<dd>factory for underlying orders</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Observable always equal to None of type Side</strong></p>\n<p>Parameters are:</p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Moving average convergence/divergence</strong></p>\n<p>Parameters are:</p>\n<p><strong>x</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Observable that adds a lag to an observable data source</strong></p>\n<blockquote>\nso Lagged(x, dt)(t0+dt) == x(t0)</blockquote>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>source</strong></dt>\n<dd>observable data source</dd>\n<dt><strong>timeframe</strong></dt>\n<dd>lag size</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Factory creating Immediate-Or-Cancel orders</strong></p>\n<blockquote>\nImmediate-Or-Cancel order sends an underlying order to the market and\nimmediately sends a cancel request for it.\nIt allows to combine market and limit order behaviour:\nthe order is either executed immediately\nat price equal or better than given one\neither it is cancelled (and consequently never stored in the order queue).</blockquote>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>proto</strong></dt>\n<dd>factory for underlying orders</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Returns buy side order queue for *book*</strong></p>\n<p>Parameters are:</p>\n<p><strong>book</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Cumulative average</strong></p>\n<p>Parameters are:</p>\n<p><strong>x</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>scaling function = atan(base^f(x))</strong></p>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>base</strong></dt>\n<dd>base for power function</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Cumulative minimum of a function with positive tolerance.</strong></p>\n<blockquote>\nIt fires updates only if <em>source</em> value becomes less than the old value minus <em>epsilon</em></blockquote>\n<p>Parameters are:</p>\n<p><strong>x</strong></p>\n<p><strong>epsilon</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Factory creating iceberg orders</strong></p>\n<blockquote>\nIceberg order is initialized by an underlying order and a lot size.\nIt sends consequently pieces of the underlying order of size equal or less to the lot size\nthus maximum lot size volume is visible at the market at any moment.</blockquote>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>proto</strong></dt>\n<dd>underlying orders to create</dd>\n<dt><strong>lotSize</strong></dt>\n<dd>maximal size of order to send</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Factory creating Peg orders</strong></p>\n<blockquote>\nA peg order is a particular case of the floating price order\nwith the price better at one tick than the best price of the order queue.\nIt implies that if several peg orders are sent to the same order queue\nthey start to race until being matched against the counterparty orders.</blockquote>\n<p>Parameters are:</p>\n<p><strong>proto</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Cumulative volume of orders sent to the market but haven't matched yet</strong></p>\n<p>Parameters are:</p>\n<p><strong>trader</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Function always returning Buy side</strong></p>\n<p>Parameters are:</p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Represents latency in information propagation between two agents</strong></p>\n<blockquote>\n(normally between a trader and a market).\nEnsures that sending packets via links preserves their order.\nHolds two one-way links in opposite directions.</blockquote>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>up</strong></dt>\n<dd>Forward link (normally from a trader to a market)</dd>\n<dt><strong>down</strong></dt>\n<dd>Backward link (normally from a market to a trader)</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Factory creating StopLoss orders</strong></p>\n<blockquote>\nStopLoss order is initialised by an underlying order and a maximal acceptable loss factor.\nIt keeps track of position and balance change induced by trades of the underlying order and\nif losses from keeping the position exceed certain limit (given by maximum loss factor),\nthe meta order clears its position.</blockquote>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>proto</strong></dt>\n<dd>underlying orders to create</dd>\n<dt><strong>maxloss</strong></dt>\n<dd>maximal acceptable loss factor</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Returns traders naive approximation of trader eficiency.</strong></p>\n<blockquote>\nIt takes into account only the best price of the order queue</blockquote>\n<p>Parameters are:</p>\n<p><strong>trader</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Uniform distribution</strong></p>\n<blockquote>\nReturn a random floating point number <em>N</em> such that\n<em>a</em> &lt;= <em>N</em> &lt;= <em>b</em> for <em>a</em> &lt;= <em>b</em> and <em>b</em> &lt;= <em>N</em> &lt;= <em>a</em> for <em>b</em> &lt; <em>a</em>.\nThe end-point value <em>b</em> may or may not be included in the range depending on\nfloating-point rounding in the equation <em>a</em> + (<em>b</em>-<em>a</em>) * <em>random()</em>.</blockquote>\n<p>Parameters are:</p>\n<p><strong>Low</strong></p>\n<p><strong>High</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Strategy that listens to all orders sent by a trader to the market</strong></p>\n<blockquote>\nand in some moments of time it randomly chooses an order and cancels it\nNote: a similar effect can be obtained using order.WithExpiry meta orders</blockquote>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>cancellationIntervalDistr</strong></dt>\n<dd>intervals between order cancellations</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Returns *x* if defined and *elsePart* otherwise</strong></p>\n<p>Parameters are:</p>\n<p><strong>x</strong></p>\n<dl class=\"docutils\">\n<dt><strong>elsePart</strong></dt>\n<dd>function to take values from when <em>x</em> is undefined</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Order book for a single asset in a market.</strong></p>\n<blockquote>\nMaintains two order queues for orders of different sides</blockquote>\n<p>Parameters are:</p>\n<p><strong>name</strong></p>\n<p><strong>tickSize</strong></p>\n<p><strong>_digitsToShow</strong></p>\n<p><strong>timeseries</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>A composite strategy initialized with an array of strategies.</strong></p>\n<blockquote>\nIn some moments of time the most effective strategy\nis chosen and made running; other strategies are suspended.\nIt can be considered as a particular case for MultiArmedBandit strategy with\n<em>corrector</em> parameter set to <em>chooseTheBest</em></blockquote>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>strategies</strong></dt>\n<dd>original strategies that can be suspended</dd>\n<dt><strong>account</strong></dt>\n<dd>function creating phantom strategy used for efficiency estimation</dd>\n<dt><strong>performance</strong></dt>\n<dd>function estimating is the strategy efficient or not</dd>\n</dl>\n</div>\n"
    },
    "marketsim.gen._out.side._sell.Sell_": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionside.IFunctionSide"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n<p><strong>Function always returning Sell side</strong></p>\n<p>Parameters are:</p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Factory creating fixed budget orders</strong></p>\n<blockquote>\nFixed budget order acts like a market order\nbut the volume is implicitly given by a budget available for trades.\nInternally first it sends request.EvalVolumesForBudget\nto estimate volumes and prices of orders to sent and\nthen sends a sequence of order.ImmediateOrCancel to be sure that\ncumulative price of trades to be done won't exceed the given budget.</blockquote>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>budget</strong></dt>\n<dd>function defining budget on which it may send orders at one time</dd>\n</dl>\n</div>\n"
    },
    "marketsim.gen._out._false.false_": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n<p><strong>Function always returning *False*</strong></p>\n<p>Parameters are:</p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Trivial observable always returning *undefined* or *None* value</strong></p>\n<p>Parameters are:</p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Factory creating orders with floating price</strong></p>\n<blockquote>\nFloating price order is initialized by an order having a price and an observable that generates new prices.\nWhen the observable value changes the order is cancelled and\na new order with new price is created and sent to the order book.</blockquote>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>proto</strong></dt>\n<dd>underlying orders to create</dd>\n<dt><strong>floatingPrice</strong></dt>\n<dd>observable defining price of orders to create</dd>\n</dl>\n</div>\n"
    },
    "marketsim.gen._out.event._createscheduler.createScheduler_Float": {
        "castsTo": [],
        "properties": {
            "currentTime": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n<p><strong>Scheduler that manages the future event set.</strong></p>\n<blockquote>\nMust be a singleton</blockquote>\n<p>Parameters are:</p>\n<p><strong>currentTime</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>identity scaling = f(x)</strong></p>\n<p>Parameters are:</p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Returns best price if defined, otherwise last price</strong></p>\n<blockquote>\nand <em>defaultValue</em> if there haven't been any trades</blockquote>\n<p>Parameters are:</p>\n<p><strong>queue</strong></p>\n<dl class=\"docutils\">\n<dt><strong>defaultValue</strong></dt>\n<dd>price to be used if there haven't been any trades</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Factory creating market orders</strong></p>\n<blockquote>\nMarket order intructs buy or sell given volume immediately</blockquote>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>side</strong></dt>\n<dd>function defining side of orders to create</dd>\n<dt><strong>volume</strong></dt>\n<dd>function defining volume of orders to create</dd>\n</dl>\n</div>\n"
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
    "marketsim.gen._out.js._graph.Graph_String": {
        "castsTo": [
            "marketsim.gen._out._igraph.IGraph"
        ],
        "properties": {
            "name": {
                "type": "identity"
            }
        },
        "description": "<div class=\"document\">\n<p><strong>Graph to render at Veusz. Time series are added to it automatically in their constructor</strong></p>\n<p>Parameters are:</p>\n<p><strong>name</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Returns first derivative of a moving average of the trader efficiency</strong></p>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>alpha</strong></dt>\n<dd>parameter alpha for the moving average</dd>\n</dl>\n</div>\n"
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
    "marketsim.gen._out.orderbook._lasttradeimpl.LastTradeImpl_": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {},
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
        "description": "<div class=\"document\">\n<p><strong>Factory creating WithExpiry orders</strong></p>\n<blockquote>\nWithExpiry orders can be viewed as ImmediateOrCancel orders\nwhere cancel order is sent not immediately but after some delay</blockquote>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>proto</strong></dt>\n<dd>underlying orders to create</dd>\n<dt><strong>expiry</strong></dt>\n<dd>expiration period for orders</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Running maximum of a function</strong></p>\n<p>Parameters are:</p>\n<p><strong>x</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Factory creating WithExpiry orders</strong></p>\n<blockquote>\nWithExpiry orders can be viewed as ImmediateOrCancel orders\nwhere cancel order is sent not immediately but after some delay</blockquote>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>proto</strong></dt>\n<dd>underlying orders to create</dd>\n<dt><strong>expiry</strong></dt>\n<dd>expiration period for orders</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Factory creating StopLoss orders</strong></p>\n<blockquote>\nStopLoss order is initialised by an underlying order and a maximal acceptable loss factor.\nIt keeps track of position and balance change induced by trades of the underlying order and\nif losses from keeping the position exceed certain limit (given by maximum loss factor),\nthe meta order clears its position.</blockquote>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>proto</strong></dt>\n<dd>underlying orders to create</dd>\n<dt><strong>maxloss</strong></dt>\n<dd>maximal acceptable loss factor</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Returns position of the trader</strong></p>\n<blockquote>\nIt is negative if trader has sold more assets than has bought and\npositive otherwise</blockquote>\n<p>Parameters are:</p>\n<p><strong>trader</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Observable that downloads closing prices for every day from *start* to *end* for asset given by *ticker*</strong></p>\n<blockquote>\nand follows the price in scale 1 model unit of time = 1 real day</blockquote>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>ticker</strong></dt>\n<dd>defines quotes to download</dd>\n<dt><strong>start</strong></dt>\n<dd>defines first day to download in form YYYY-MM-DD</dd>\n<dt><strong>end</strong></dt>\n<dd>defines last day to download in form YYYY-MM-DD</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Standard deviation</strong></p>\n<p>Parameters are:</p>\n<p><strong>x</strong></p>\n</div>\n"
    },
    "marketsim.gen._out.event._event.Event_": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent"
        ],
        "properties": {},
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
        "description": "<div class=\"document\">\n<p><strong>Arc tangent of x, in radians.</strong></p>\n<p>Parameters are:</p>\n<p><strong>x</strong></p>\n</div>\n"
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
    "marketsim.gen._out.ops._condition.Condition_IObservableBooleanIObservableBooleanBoolean": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool",
            "marketsim.gen._out._iobservable._iobservablebool.IObservablebool",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "ifpart": {
                "type": "marketsim.gen._out._iobservable._iobservablebool.IObservablebool"
            },
            "elsepart": {
                "type": "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool"
            },
            "cond": {
                "type": "marketsim.gen._out._iobservable._iobservablebool.IObservablebool"
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
        "description": "<div class=\"document\">\n<p><strong>Returns tick size for the order *book*</strong></p>\n<p>Parameters are:</p>\n<p><strong>book</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Function returning maximum of two functions *x* and *y*.</strong></p>\n<blockquote>\nIf <em>x</em> or/and <em>y</em> are observables, <em>Min</em> is also observable</blockquote>\n<p>Parameters are:</p>\n<p><strong>x</strong></p>\n<p><strong>y</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Log normal distribution</strong></p>\n<blockquote>\n<dl class=\"docutils\">\n<dt>If you take the natural logarithm of this distribution,</dt>\n<dd>you'll get a normal distribution with mean \u03bc and standard deviation \u03c3.\n\u03bc can have any value, and \u03c3 must be greater than zero.</dd>\n</dl>\n</blockquote>\n<p>Parameters are:</p>\n<p><strong>Mu</strong></p>\n<p><strong>Sigma</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Exponentially weighted moving variance</strong></p>\n<p>Parameters are:</p>\n<p><strong>x</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Factory creating Peg orders</strong></p>\n<blockquote>\nA peg order is a particular case of the floating price order\nwith the price better at one tick than the best price of the order queue.\nIt implies that if several peg orders are sent to the same order queue\nthey start to race until being matched against the counterparty orders.</blockquote>\n<p>Parameters are:</p>\n<p><strong>proto</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Standard deviation</strong></p>\n<p>Parameters are:</p>\n<p><strong>x</strong></p>\n</div>\n"
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
    "marketsim.gen._out.orderbook._proxy.Proxy_": {
        "castsTo": [
            "marketsim.gen._out._iorderbook.IOrderBook"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n<p><strong>Phantom orderbook that is used to refer to the current order book</strong></p>\n<blockquote>\nMay be used only in objects held by orderbooks (so it is normally used in orderbook properties)</blockquote>\n<p>Parameters are:</p>\n</div>\n"
    },
    "marketsim.gen._out.ops._or.Or_IObservableBooleanBoolean": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool",
            "marketsim.gen._out._iobservable._iobservablebool.IObservablebool",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "y": {
                "type": "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool"
            },
            "x": {
                "type": "marketsim.gen._out._iobservable._iobservablebool.IObservablebool"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.ops._and.And_IObservableBooleanBoolean": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool",
            "marketsim.gen._out._iobservable._iobservablebool.IObservablebool",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "y": {
                "type": "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool"
            },
            "x": {
                "type": "marketsim.gen._out._iobservable._iobservablebool.IObservablebool"
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
        "description": "<div class=\"document\">\n<p><strong>Returns *x* if defined and *elsePart* otherwise</strong></p>\n<p>Parameters are:</p>\n<p><strong>x</strong></p>\n<dl class=\"docutils\">\n<dt><strong>elsePart</strong></dt>\n<dd>function to take values from when <em>x</em> is undefined</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Function returning an array of length *len(array)*</strong></p>\n<blockquote>\nhaving 1 at the index of the maximal element and 0 are at the rest</blockquote>\n<p>Parameters are:</p>\n<p><strong>array</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Factory creating Peg orders</strong></p>\n<blockquote>\nA peg order is a particular case of the floating price order\nwith the price better at one tick than the best price of the order queue.\nIt implies that if several peg orders are sent to the same order queue\nthey start to race until being matched against the counterparty orders.</blockquote>\n<p>Parameters are:</p>\n<p><strong>proto</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Creates a strategy combining an array of strategies</strong></p>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>strategies</strong></dt>\n<dd>strategies to combine</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Moving average convergence/divergence histogram</strong></p>\n<p>Parameters are:</p>\n<p><strong>x</strong></p>\n<dl class=\"docutils\">\n<dt><strong>timeframe</strong></dt>\n<dd>signal period</dd>\n<dt><strong>step</strong></dt>\n<dd>discretization step</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Relative standard deviation</strong></p>\n<p>Parameters are:</p>\n<p><strong>x</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Function always returning *x*</strong></p>\n<p>Parameters are:</p>\n<p><strong>x</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Function always returning None of type Side</strong></p>\n<p>Parameters are:</p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Function returning minimum of two functions *x* and *y*.</strong></p>\n<blockquote>\nIf <em>x</em> or/and <em>y</em> are observables, <em>Min</em> is also observable</blockquote>\n<p>Parameters are:</p>\n<p><strong>x</strong></p>\n<p><strong>y</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Factory creating limit orders</strong></p>\n<blockquote>\nLimit orders ask to buy or sell some asset at price better than some limit price.\nIf a limit order is not competely fulfilled\nit remains in an order book waiting to be matched with another order.</blockquote>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>side</strong></dt>\n<dd>function defining side of orders to create</dd>\n<dt><strong>price</strong></dt>\n<dd>function defining price of orders to create</dd>\n<dt><strong>volume</strong></dt>\n<dd>function defining volume of orders to create</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Function always returning *x*</strong></p>\n<p>Parameters are:</p>\n<p><strong>x</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Trivial observable always returning *x*</strong></p>\n<p>Parameters are:</p>\n<p><strong>x</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Trivial observable always returning *x*</strong></p>\n<p>Parameters are:</p>\n<p><strong>x</strong></p>\n</div>\n"
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
    "marketsim.gen._out.ops._and.And_IObservableBooleanIObservableBoolean": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool",
            "marketsim.gen._out._iobservable._iobservablebool.IObservablebool",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "y": {
                "type": "marketsim.gen._out._iobservable._iobservablebool.IObservablebool"
            },
            "x": {
                "type": "marketsim.gen._out._iobservable._iobservablebool.IObservablebool"
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
        "description": "<div class=\"document\">\n<p><strong>Associated with a strategy account that tracks</strong></p>\n<blockquote>\nhow orders sent by the strategy have been actually traded</blockquote>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>inner</strong></dt>\n<dd>strategy to track</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Unit function. Used to simulate uniform random choice of a strategy</strong></p>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>trader</strong></dt>\n<dd>account in question</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Factory creating Immediate-Or-Cancel orders</strong></p>\n<blockquote>\nImmediate-Or-Cancel order sends an underlying order to the market and\nimmediately sends a cancel request for it.\nIt allows to combine market and limit order behaviour:\nthe order is either executed immediately\nat price equal or better than given one\neither it is cancelled (and consequently never stored in the order queue).</blockquote>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>proto</strong></dt>\n<dd>factory for underlying orders</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Returns *x* if defined and *elsePart* otherwise</strong></p>\n<p>Parameters are:</p>\n<p><strong>x</strong></p>\n<dl class=\"docutils\">\n<dt><strong>elsePart</strong></dt>\n<dd>function to take values from when <em>x</em> is undefined</dd>\n</dl>\n</div>\n"
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
    "marketsim.gen._out.math._timeframe.Timeframe_mathMoving": {
        "castsTo": [],
        "properties": {
            "x": {
                "type": "marketsim.gen._out.math._moving.Moving_IObservableFloatFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Function returning maximum of two functions *x* and *y*.</strong></p>\n<blockquote>\nIf <em>x</em> or/and <em>y</em> are observables, <em>Min</em> is also observable</blockquote>\n<p>Parameters are:</p>\n<p><strong>x</strong></p>\n<p><strong>y</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Returns best order price of *queue*</strong></p>\n<blockquote>\nReturns None is <em>queue</em> is empty</blockquote>\n<p>Parameters are:</p>\n<p><strong>queue</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Returns price of the last trade at *queue*</strong></p>\n<blockquote>\nReturns None if there haven't been any trades</blockquote>\n<p>Parameters are:</p>\n<p><strong>queue</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Factory creating orders with floating price</strong></p>\n<blockquote>\nFloating price order is initialized by an order having a price and an observable that generates new prices.\nWhen the observable value changes the order is cancelled and\na new order with new price is created and sent to the order book.</blockquote>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>proto</strong></dt>\n<dd>underlying orders to create</dd>\n<dt><strong>floatingPrice</strong></dt>\n<dd>observable defining price of orders to create</dd>\n</dl>\n</div>\n"
    },
    "marketsim.gen._out.event._scheduler.Scheduler_": {
        "castsTo": [],
        "properties": {},
        "description": "<div class=\"document\">\n<p><strong>Returns reference to the instance of the scheduler</strong></p>\n<p>Parameters are:</p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Simple moving average</strong></p>\n<p>Parameters are:</p>\n<p><strong>x</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Associated with a strategy account that evaluates for every order sent by the strategy</strong></p>\n<blockquote>\nhow it would be traded by sending request.evalMarketOrder\n(note: orders sent by a strategy wrapped into an adaptive strategy may not come to the market\nbut we want evaluate in any case would it be profitable or not)</blockquote>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>inner</strong></dt>\n<dd>strategy to track</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Returns moving average of trade prices weighted by their volumes</strong></p>\n<p>Parameters are:</p>\n<p><strong>queue</strong></p>\n<dl class=\"docutils\">\n<dt><strong>alpha</strong></dt>\n<dd>parameter alpha for the moving average</dd>\n</dl>\n</div>\n"
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
    "marketsim.gen._out.ops._and.And_BooleanIObservableBoolean": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool",
            "marketsim.gen._out._iobservable._iobservablebool.IObservablebool",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "y": {
                "type": "marketsim.gen._out._iobservable._iobservablebool.IObservablebool"
            },
            "x": {
                "type": "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool"
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
        "description": "<div class=\"document\">\n<p><strong>Phantom orderbook used to refer to the order book associated with a single asset trader</strong></p>\n<blockquote>\nMay be used only in objects that are held by traders (so it is used in trader properties and strategies)</blockquote>\n<p>Parameters are:</p>\n<p><strong>Trader</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Factory creating StopLoss orders</strong></p>\n<blockquote>\nStopLoss order is initialised by an underlying order and a maximal acceptable loss factor.\nIt keeps track of position and balance change induced by trades of the underlying order and\nif losses from keeping the position exceed certain limit (given by maximum loss factor),\nthe meta order clears its position.</blockquote>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>proto</strong></dt>\n<dd>underlying orders to create</dd>\n<dt><strong>maxloss</strong></dt>\n<dd>maximal acceptable loss factor</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Time serie to store and render it after on a graph</strong></p>\n<blockquote>\nUsed to specify what data should be collected about order books and traders</blockquote>\n<p>Parameters are:</p>\n<p><strong>source</strong></p>\n<p><strong>graph</strong></p>\n<p><strong>_digitsToShow</strong></p>\n<p><strong>_smooth</strong></p>\n</div>\n"
    },
    "marketsim.gen._out.strategy.weight.trader._trader_score.trader_Score_": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionifunctionfloat_from_iaccount.IFunctionIFunctionfloat_from_IAccount"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n<p><strong>Calculates how many times efficiency of trader went up and went down</strong></p>\n<blockquote>\n<p>Returns difference between them.</p>\n<p>TODO: should be UpScore(timeframe, Efficiency(trader)) - DownScore(timeframe, Efficiency(trader))</p>\n</blockquote>\n<p>Parameters are:</p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Calculates how many times efficiency of trader went up and went down</strong></p>\n<blockquote>\n<p>Returns difference between them.</p>\n<p>TODO: should be UpScore(timeframe, Efficiency(trader)) - DownScore(timeframe, Efficiency(trader))</p>\n</blockquote>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>trader</strong></dt>\n<dd>account in question</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>scaling function = max(0, f(x)) + 1</strong></p>\n<p>Parameters are:</p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Factory creating Immediate-Or-Cancel orders</strong></p>\n<blockquote>\nImmediate-Or-Cancel order sends an underlying order to the market and\nimmediately sends a cancel request for it.\nIt allows to combine market and limit order behaviour:\nthe order is either executed immediately\nat price equal or better than given one\neither it is cancelled (and consequently never stored in the order queue).</blockquote>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>proto</strong></dt>\n<dd>factory for underlying orders</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Identity function for an array of floats</strong></p>\n<p>Parameters are:</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy.price._ladder.Ladder_SideFloatIObservableIOrderIntSide": {
        "castsTo": [
            "marketsim.gen._out._isingleassetstrategy.ISingleAssetStrategy"
        ],
        "properties": {
            "initialSize": {
                "type": "_parseInt"
            },
            "side": {
                "type": "marketsim.gen._out._ifunction._ifunctionside.IFunctionSide"
            },
            "orderFactory": {
                "type": "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionsideifunctionfloat.IFunctionIObservableIOrder_from_IFunctionSideIFunctionfloat"
            }
        },
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
        "description": "<div class=\"document\">\n<p><strong>Empty strategy doing nothing</strong></p>\n<p>Parameters are:</p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Factory creating limit orders</strong></p>\n<blockquote>\nLimit orders ask to buy or sell some asset at price better than some limit price.\nIf a limit order is not competely fulfilled\nit remains in an order book waiting to be matched with another order.</blockquote>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>volume</strong></dt>\n<dd>function defining volume of orders to create</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Returns positive movements of some observable *source* with lag *timeframe*</strong></p>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>source</strong></dt>\n<dd>observable data source</dd>\n<dt><strong>timeframe</strong></dt>\n<dd>lag size</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Square of *x*</strong></p>\n<p>Parameters are:</p>\n<p><strong>x</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Factory creating market orders</strong></p>\n<blockquote>\nMarket order intructs buy or sell given volume immediately</blockquote>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>volume</strong></dt>\n<dd>function defining volume of orders to create</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Exponent of *x*</strong></p>\n<p>Parameters are:</p>\n<p><strong>x</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Returns traders eficiency. Under efficiency we understand trader balance if trader position was cleared</strong></p>\n<p>Parameters are:</p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Strategy that wraps another strategy and passes its orders only if *predicate* is true</strong></p>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>inner</strong></dt>\n<dd>wrapped strategy</dd>\n<dt><strong>predicate</strong></dt>\n<dd>predicate to evaluate</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Function returning maximum of two functions *x* and *y*.</strong></p>\n<blockquote>\nIf <em>x</em> or/and <em>y</em> are observables, <em>Min</em> is also observable</blockquote>\n<p>Parameters are:</p>\n<p><strong>x</strong></p>\n<p><strong>y</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Function returning minimum of two functions *x* and *y*.</strong></p>\n<blockquote>\nIf <em>x</em> or/and <em>y</em> are observables, <em>Min</em> is also observable</blockquote>\n<p>Parameters are:</p>\n<p><strong>x</strong></p>\n<p><strong>y</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>A composite strategy initialized with an array of strategies.</strong></p>\n<blockquote>\nIn some moments of time the efficiency of the strategies is evaluated\nThese efficiencies are mapped into weights using <em>weight</em> and <em>normilizer</em>\nfunctions per every strategy and <em>corrector</em> for the whole collection of weights\nThese weights are used to choose randomly a strategy to run for the next quant of time.\nAll other strategies are suspended</blockquote>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>strategies</strong></dt>\n<dd>original strategies that can be suspended</dd>\n<dt><strong>account</strong></dt>\n<dd>function creating a virtual account used\nto estimate efficiency of the strategy itself</dd>\n<dt><strong>weight</strong></dt>\n<dd>function estimating is the strategy efficient or not</dd>\n<dt><strong>normalizer</strong></dt>\n<dd>function that maps trader efficiency to its weight\nthat will be used for random choice</dd>\n<dt><strong>corrector</strong></dt>\n<dd>given array of strategy weights corrects them.\nfor example it may set to 0 all weights except the maximal one</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Relative standard deviation</strong></p>\n<p>Parameters are:</p>\n<p><strong>x</strong></p>\n</div>\n"
    },
    "marketsim.gen._out.strategy.price._laddermm.LadderMM_SideFloatIObservableIOrderInt": {
        "castsTo": [
            "marketsim.gen._out._iladderstrategy.ILadderStrategy",
            "marketsim.gen._out._isingleassetstrategy.ISingleAssetStrategy",
            "marketsim.gen._out._isuspendablestrategy.ISuspendableStrategy"
        ],
        "properties": {
            "initialSize": {
                "type": "_parseInt"
            },
            "orderFactory": {
                "type": "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionsideifunctionfloat.IFunctionIObservableIOrder_from_IFunctionSideIFunctionfloat"
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
        "description": "<div class=\"document\">\n<p><strong>Trivial observable always returning *True*</strong></p>\n<p>Parameters are:</p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Gamma distribution</strong></p>\n<blockquote>\n<p>Conditions on the parameters are \u03b1 &gt; 0 and \u03b2 &gt; 0.</p>\n<p>The probability distribution function is:</p>\n<pre class=\"literal-block\">\n          x ** (alpha - 1) * math.exp(-x / beta)\npdf(x) =  --------------------------------------\n             math.gamma(alpha) * beta ** alpha\n</pre>\n</blockquote>\n<p>Parameters are:</p>\n<p><strong>Alpha</strong></p>\n<p><strong>Beta</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Returns last defined price at *queue*</strong></p>\n<blockquote>\nReturns None is <em>queue</em> has been always empty</blockquote>\n<p>Parameters are:</p>\n<p><strong>queue</strong></p>\n</div>\n"
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
    "marketsim.gen._out.strategy.account.inner._inner_virtualmarket.inner_VirtualMarket_": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctioniaccount_from_isingleassetstrategy.IFunctionIAccount_from_ISingleAssetStrategy"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n<p><strong>Associated with a strategy account that evaluates for every order sent by the strategy</strong></p>\n<blockquote>\nhow it would be traded by sending request.evalMarketOrder\n(note: orders sent by a strategy wrapped into an adaptive strategy may not come to the market\nbut we want evaluate in any case would it be profitable or not)</blockquote>\n<p>Parameters are:</p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Relative standard deviation</strong></p>\n<p>Parameters are:</p>\n<p><strong>x</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Running minimum of a function</strong></p>\n<p>Parameters are:</p>\n<p><strong>x</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Normal distribution</strong></p>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>Mu</strong></dt>\n<dd>\u03bc is the mean</dd>\n<dt><strong>Sigma</strong></dt>\n<dd>\u03c3 is the standard deviation</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Factory creating limit orders</strong></p>\n<blockquote>\nLimit orders ask to buy or sell some asset at price better than some limit price.\nIf a limit order is not competely fulfilled\nit remains in an order book waiting to be matched with another order.</blockquote>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>signedVolume</strong></dt>\n<dd>signed volume</dd>\n<dt><strong>price</strong></dt>\n<dd>function defining price of orders to create</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Observable listening to *source*</strong></p>\n<blockquote>\nWhen <em>source</em> changes it inserts <em>undefined</em> value and then immidiately becomes equal to <em>source</em> value</blockquote>\n<p>Parameters are:</p>\n<p><strong>source</strong></p>\n</div>\n"
    },
    "marketsim.gen._out.ops._condition.Condition_BooleanIObservableBooleanIObservableBoolean": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool",
            "marketsim.gen._out._iobservable._iobservablebool.IObservablebool",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "ifpart": {
                "type": "marketsim.gen._out._iobservable._iobservablebool.IObservablebool"
            },
            "elsepart": {
                "type": "marketsim.gen._out._iobservable._iobservablebool.IObservablebool"
            },
            "cond": {
                "type": "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Returns arrays of levels for given volumes [i*volumeDelta for i in range(0, volumeCount)]</strong></p>\n<blockquote>\nLevel of volume V is a price at which cumulative volume of better orders is V</blockquote>\n<p>Parameters are:</p>\n<p><strong>queue</strong></p>\n<dl class=\"docutils\">\n<dt><strong>volumeDelta</strong></dt>\n<dd>distance between two volumes</dd>\n<dt><strong>volumeCount</strong></dt>\n<dd>number of volume levels to track</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Returns negative movements of some observable *source* with lag *timeframe*</strong></p>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>source</strong></dt>\n<dd>observable data source</dd>\n<dt><strong>timeframe</strong></dt>\n<dd>lag size</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Cumulative variance</strong></p>\n<p>Parameters are:</p>\n<p><strong>x</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Factory creating iceberg orders</strong></p>\n<blockquote>\nIceberg order is initialized by an underlying order and a lot size.\nIt sends consequently pieces of the underlying order of size equal or less to the lot size\nthus maximum lot size volume is visible at the market at any moment.</blockquote>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>proto</strong></dt>\n<dd>underlying orders to create</dd>\n<dt><strong>lotSize</strong></dt>\n<dd>maximal size of order to send</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>MidPrice of order *book*</strong></p>\n<p>Parameters are:</p>\n<p><strong>book</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Discretizes function *x* at even time steps *dt*</strong></p>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>x</strong></dt>\n<dd>function to discretize</dd>\n<dt><strong>dt</strong></dt>\n<dd>time discretization step</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Factory creating orders with floating price</strong></p>\n<blockquote>\nFloating price order is initialized by an order having a price and an observable that generates new prices.\nWhen the observable value changes the order is cancelled and\na new order with new price is created and sent to the order book.</blockquote>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>proto</strong></dt>\n<dd>underlying orders to create</dd>\n<dt><strong>floatingPrice</strong></dt>\n<dd>observable defining price of orders to create</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Creates a strategy combining two strategies</strong></p>\n<blockquote>\nCan be considered as a particular case of Array strategy</blockquote>\n<p>Parameters are:</p>\n<p><strong>A</strong></p>\n<p><strong>B</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Observable returning at the end of every *timeframe*</strong></p>\n<blockquote>\nopen/close/min/max price, its average and standard deviation</blockquote>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>source</strong></dt>\n<dd>observable data source considered as asset price</dd>\n<dt><strong>timeframe</strong></dt>\n<dd>size of timeframe</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>identity scaling = f(x)</strong></p>\n<p>Parameters are:</p>\n<p><strong>f</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Returns traders eficiency. Under efficiency we understand trader balance if trader position was cleared</strong></p>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>trader</strong></dt>\n<dd>account in question</dd>\n</dl>\n</div>\n"
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
    "marketsim.gen._out.strategy.price._suspend.Suspend_ISuspendableStrategyBoolean": {
        "castsTo": [
            "marketsim.gen._out._isingleassetstrategy.ISingleAssetStrategy",
            "marketsim.gen._out._isuspendablestrategy.ISuspendableStrategy"
        ],
        "properties": {
            "predicate": {
                "type": "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool"
            },
            "inner": {
                "type": "marketsim.gen._out._isuspendablestrategy.ISuspendableStrategy"
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
        "description": "<div class=\"document\">\n<p><strong>Exponential distribution</strong></p>\n<blockquote>\nReturned values range from 0 to positive infinity</blockquote>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>Lambda</strong></dt>\n<dd>\u03bb is 1.0 divided by the desired mean. It should be greater zero.</dd>\n</dl>\n</div>\n"
    },
    "marketsim.gen._out.trader._singleproxy.SingleProxy_": {
        "castsTo": [
            "marketsim.gen._out._iaccount.IAccount",
            "marketsim.gen._out._isingleassettrader.ISingleAssetTrader",
            "marketsim.gen._out._itrader.ITrader"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n<p><strong>Phantom trader that is used to refer to the current trader</strong></p>\n<blockquote>\n(normally it is used to define trader properties and strategies)</blockquote>\n<p>Parameters are:</p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Time serie holding volume levels of an asset</strong></p>\n<blockquote>\nLevel of volume V is a price at which cumulative volume of better orders is V</blockquote>\n<p>Parameters are:</p>\n<p><strong>source</strong></p>\n<p><strong>graph</strong></p>\n<p><strong>_digitsToShow</strong></p>\n<p><strong>_smooth</strong></p>\n<p><strong>_volumes</strong></p>\n<p><strong>_isBuy</strong></p>\n</div>\n"
    },
    "marketsim.gen._out.strategy.weight.trader._trader_unit.trader_Unit_": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctionifunctionfloat_from_iaccount.IFunctionIFunctionfloat_from_IAccount"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n<p><strong>Unit function. Used to simulate uniform random choice of a strategy</strong></p>\n<p>Parameters are:</p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Returns *x* if defined and *elsePart* otherwise</strong></p>\n<p>Parameters are:</p>\n<p><strong>x</strong></p>\n<dl class=\"docutils\">\n<dt><strong>elsePart</strong></dt>\n<dd>function to take values from when <em>x</em> is undefined</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Factory creating StopLoss orders</strong></p>\n<blockquote>\nStopLoss order is initialised by an underlying order and a maximal acceptable loss factor.\nIt keeps track of position and balance change induced by trades of the underlying order and\nif losses from keeping the position exceed certain limit (given by maximum loss factor),\nthe meta order clears its position.</blockquote>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>proto</strong></dt>\n<dd>underlying orders to create</dd>\n<dt><strong>maxloss</strong></dt>\n<dd>maximal acceptable loss factor</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Factory creating WithExpiry orders</strong></p>\n<blockquote>\nWithExpiry orders can be viewed as ImmediateOrCancel orders\nwhere cancel order is sent not immediately but after some delay</blockquote>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>proto</strong></dt>\n<dd>underlying orders to create</dd>\n<dt><strong>expiry</strong></dt>\n<dd>expiration period for orders</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Log returns</strong></p>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>x</strong></dt>\n<dd>observable data source</dd>\n<dt><strong>timeframe</strong></dt>\n<dd>lag size</dd>\n</dl>\n</div>\n"
    },
    "marketsim.gen._out.strategy.price._islosstoohigh.isLossTooHigh_Float": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool",
            "marketsim.gen._out._iobservable._iobservablebool.IObservablebool",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "lossFactor": {
                "type": "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat"
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
        "description": "<div class=\"document\">\n<p><strong>Factory creating limit orders</strong></p>\n<blockquote>\nLimit orders ask to buy or sell some asset at price better than some limit price.\nIf a limit order is not competely fulfilled\nit remains in an order book waiting to be matched with another order.</blockquote>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>price</strong></dt>\n<dd>function defining price of orders to create</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Factory creating WithExpiry orders</strong></p>\n<blockquote>\nWithExpiry orders can be viewed as ImmediateOrCancel orders\nwhere cancel order is sent not immediately but after some delay</blockquote>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>proto</strong></dt>\n<dd>underlying orders to create</dd>\n<dt><strong>expiry</strong></dt>\n<dd>expiration period for orders</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Factory creating fixed budget orders</strong></p>\n<blockquote>\nFixed budget order acts like a market order\nbut the volume is implicitly given by a budget available for trades.\nInternally first it sends request.EvalVolumesForBudget\nto estimate volumes and prices of orders to sent and\nthen sends a sequence of order.ImmediateOrCancel to be sure that\ncumulative price of trades to be done won't exceed the given budget.</blockquote>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>side</strong></dt>\n<dd>function defining side of orders to create</dd>\n<dt><strong>budget</strong></dt>\n<dd>function defining budget on which it may send orders at one time</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Factory creating market orders</strong></p>\n<blockquote>\nMarket order intructs buy or sell given volume immediately</blockquote>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>signedVolume</strong></dt>\n<dd>signed volume</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Pareto distribution</strong></p>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>Alpha</strong></dt>\n<dd>\u03b1 is the shape parameter</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Spread of order *book*</strong></p>\n<p>Parameters are:</p>\n<p><strong>book</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Cumulative maximum of a function with positive tolerance.</strong></p>\n<blockquote>\nIt fires updates only if <em>source</em> value becomes greater than the old value plus <em>epsilon</em></blockquote>\n<p>Parameters are:</p>\n<p><strong>x</strong></p>\n<p><strong>epsilon</strong></p>\n</div>\n"
    },
    "marketsim.gen._out.ops._condition.Condition_BooleanBooleanIObservableBoolean": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool",
            "marketsim.gen._out._iobservable._iobservablebool.IObservablebool",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "ifpart": {
                "type": "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool"
            },
            "elsepart": {
                "type": "marketsim.gen._out._iobservable._iobservablebool.IObservablebool"
            },
            "cond": {
                "type": "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Returns volume of the last trade at *queue*</strong></p>\n<blockquote>\nReturns None if there haven't been any trades</blockquote>\n<p>Parameters are:</p>\n<p><strong>queue</strong></p>\n</div>\n"
    },
    "marketsim.gen._out.ops._or.Or_IObservableBooleanIObservableBoolean": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool",
            "marketsim.gen._out._iobservable._iobservablebool.IObservablebool",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "y": {
                "type": "marketsim.gen._out._iobservable._iobservablebool.IObservablebool"
            },
            "x": {
                "type": "marketsim.gen._out._iobservable._iobservablebool.IObservablebool"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.price._clearable.Clearable_ISuspendableStrategyBoolean": {
        "castsTo": [
            "marketsim.gen._out._isingleassetstrategy.ISingleAssetStrategy",
            "marketsim.gen._out._isuspendablestrategy.ISuspendableStrategy"
        ],
        "properties": {
            "predicate": {
                "type": "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool"
            },
            "inner": {
                "type": "marketsim.gen._out._isuspendablestrategy.ISuspendableStrategy"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Absolute value for Relative Strength Index</strong></p>\n<p>Parameters are:</p>\n<p><strong>x</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Exponentially weighted moving average</strong></p>\n<p>Parameters are:</p>\n<p><strong>x</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Beta distribution</strong></p>\n<blockquote>\nConditions on the parameters are \u03b1 &gt; 0 and \u03b2 &gt; 0.\nReturned values range between 0 and 1.</blockquote>\n<p>Parameters are:</p>\n<p><strong>Alpha</strong></p>\n<p><strong>Beta</strong></p>\n</div>\n"
    },
    "marketsim.gen._out.ops._and.And_BooleanBoolean": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool",
            "marketsim.gen._out._iobservable._iobservablebool.IObservablebool",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "y": {
                "type": "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool"
            },
            "x": {
                "type": "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
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
    "marketsim.gen._out._currenttime.CurrentTime_": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionfloat.IFunctionfloat",
            "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.order._curried._signedvolume_marketsigned.signedVolume_MarketSigned_": {
        "castsTo": [
            "marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionfloat.IFunctionIObservableIOrder_from_IFunctionfloat"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n<p><strong>Factory creating market orders</strong></p>\n<blockquote>\nMarket order intructs buy or sell given volume immediately</blockquote>\n<p>Parameters are:</p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>A trader that trades a single asset on a single market</strong></p>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>orderBook</strong></dt>\n<dd>order book for the asset being traded</dd>\n<dt><strong>strategy</strong></dt>\n<dd>strategy run by the trader</dd>\n</dl>\n<p><strong>name</strong></p>\n<dl class=\"docutils\">\n<dt><strong>amount</strong></dt>\n<dd>current position of the trader (number of assets that it owns)</dd>\n<dt><strong>PnL</strong></dt>\n<dd>current trader balance (number of money units that it owns)</dd>\n<dt><strong>timeseries</strong></dt>\n<dd>defines what data should be gathered for the trader</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Factory creating iceberg orders</strong></p>\n<blockquote>\nIceberg order is initialized by an underlying order and a lot size.\nIt sends consequently pieces of the underlying order of size equal or less to the lot size\nthus maximum lot size volume is visible at the market at any moment.</blockquote>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>proto</strong></dt>\n<dd>underlying orders to create</dd>\n<dt><strong>lotSize</strong></dt>\n<dd>maximal size of order to send</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Factory creating orders with floating price</strong></p>\n<blockquote>\nFloating price order is initialized by an order having a price and an observable that generates new prices.\nWhen the observable value changes the order is cancelled and\na new order with new price is created and sent to the order book.</blockquote>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>proto</strong></dt>\n<dd>underlying orders to create</dd>\n<dt><strong>floatingPrice</strong></dt>\n<dd>observable defining price of orders to create</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Function returning first derivative on time of *x*</strong></p>\n<blockquote>\n<em>x</em> should provide <em>derivative</em> member</blockquote>\n<p>Parameters are:</p>\n<p><strong>x</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Weibull distribution</strong></p>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>Alpha</strong></dt>\n<dd>\u03b1 is the scale parameter</dd>\n<dt><strong>Beta</strong></dt>\n<dd>\u03b2 is the shape parameter</dd>\n</dl>\n</div>\n"
    },
    "marketsim.gen._out.strategy.price._ladderbalancer.LadderBalancer_ILadderStrategyInt": {
        "castsTo": [
            "marketsim.gen._out._iladderstrategy.ILadderStrategy",
            "marketsim.gen._out._isingleassetstrategy.ISingleAssetStrategy",
            "marketsim.gen._out._isuspendablestrategy.ISuspendableStrategy"
        ],
        "properties": {
            "inner": {
                "type": "marketsim.gen._out._iladderstrategy.ILadderStrategy"
            },
            "maximalSize": {
                "type": "_parseInt"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Returns best price if defined, otherwise last price</strong></p>\n<blockquote>\nand <em>defaultValue</em> if there haven't been any trades</blockquote>\n<p>Parameters are:</p>\n<p><strong>queue</strong></p>\n<dl class=\"docutils\">\n<dt><strong>defaultValue</strong></dt>\n<dd>price to be used if there haven't been any trades</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Event that once at *delay*</strong></p>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>delay</strong></dt>\n<dd>when the event should be fired</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Factory creating iceberg orders</strong></p>\n<blockquote>\nIceberg order is initialized by an underlying order and a lot size.\nIt sends consequently pieces of the underlying order of size equal or less to the lot size\nthus maximum lot size volume is visible at the market at any moment.</blockquote>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>proto</strong></dt>\n<dd>underlying orders to create</dd>\n<dt><strong>lotSize</strong></dt>\n<dd>maximal size of order to send</dd>\n</dl>\n</div>\n"
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
    "marketsim.gen._out.strategy.price._islosstoohigh.isLossTooHigh_IObservableFloat": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool",
            "marketsim.gen._out._iobservable._iobservablebool.IObservablebool",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject"
        ],
        "properties": {
            "lossFactor": {
                "type": "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat"
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
        "description": "<div class=\"document\">\n<p><strong>Represent an *orderbook* from point of view of a remote trader connected</strong></p>\n<blockquote>\nto the market by means of a <em>link</em> that introduces some latency in information propagation</blockquote>\n<p>Parameters are:</p>\n<p><strong>orderbook</strong></p>\n<p><strong>link</strong></p>\n<p><strong>timeseries</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Returns order queue of order *book* for trade *side*</strong></p>\n<p>Parameters are:</p>\n<p><strong>book</strong></p>\n<p><strong>side</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Factory creating orders with floating price</strong></p>\n<blockquote>\nFloating price order is initialized by an order having a price and an observable that generates new prices.\nWhen the observable value changes the order is cancelled and\na new order with new price is created and sent to the order book.</blockquote>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>proto</strong></dt>\n<dd>underlying orders to create</dd>\n<dt><strong>floatingPrice</strong></dt>\n<dd>observable defining price of orders to create</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Factory creating iceberg orders</strong></p>\n<blockquote>\nIceberg order is initialized by an underlying order and a lot size.\nIt sends consequently pieces of the underlying order of size equal or less to the lot size\nthus maximum lot size volume is visible at the market at any moment.</blockquote>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>proto</strong></dt>\n<dd>underlying orders to create</dd>\n<dt><strong>lotSize</strong></dt>\n<dd>maximal size of order to send</dd>\n</dl>\n</div>\n"
    },
    "marketsim.gen._out.side._observablebuy.observableBuy_": {
        "castsTo": [
            "marketsim.gen._out._ievent.IEvent",
            "marketsim.gen._out._ifunction._ifunctionside.IFunctionSide",
            "marketsim.gen._out._iobservable._iobservableobject.IObservableobject",
            "marketsim.gen._out._iobservable._iobservableside.IObservableSide"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n<p><strong>Observable always equal to Buy side</strong></p>\n<p>Parameters are:</p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Return *x* raised to the power *y*.</strong></p>\n<blockquote>\nExceptional cases follow Annex F of the C99 standard as far as possible.\nIn particular, <tt class=\"docutils literal\">pow(1.0, x)</tt> and <tt class=\"docutils literal\">pow(x, 0.0)</tt> always return 1.0,\neven when <em>x</em> is a zero or a NaN.\nIf both <em>x</em> and <em>y</em> are finite, <em>x</em> is negative, and <em>y</em> is not an integer then\n<tt class=\"docutils literal\">pow(x, y)</tt> is undefined, and raises <tt class=\"docutils literal\">ValueError</tt>.</blockquote>\n<p>Parameters are:</p>\n<p><strong>base</strong></p>\n<p><strong>power</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Represents latency in information propagation from one agent to another one</strong></p>\n<blockquote>\n(normally between a trader and a market).\nEnsures that sending packets via a link preserves their order.</blockquote>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>latency</strong></dt>\n<dd>function called for each packet in order to determine\nwhen it will appear at the end point</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Factory creating WithExpiry orders</strong></p>\n<blockquote>\nWithExpiry orders can be viewed as ImmediateOrCancel orders\nwhere cancel order is sent not immediately but after some delay</blockquote>\n<p>Parameters are:</p>\n<dl class=\"docutils\">\n<dt><strong>proto</strong></dt>\n<dd>underlying orders to create</dd>\n<dt><strong>expiry</strong></dt>\n<dd>expiration period for orders</dd>\n</dl>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Natural logarithm of *x* (to base e)</strong></p>\n<p>Parameters are:</p>\n<p><strong>x</strong></p>\n</div>\n"
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
        "description": "<div class=\"document\">\n<p><strong>Returns sell side order queue for *book*</strong></p>\n<p>Parameters are:</p>\n<p><strong>book</strong></p>\n</div>\n"
    }
}
var interfaces = [
    [
        "_parseInt",
        []
    ],
    [
        "marketsim.gen._out.strategy.side._rsibis.RSIbis_FloatFloatFloat",
        [
            "marketsim.gen._out.strategy.side._rsibis.RSIbis_FloatFloatFloat"
        ]
    ],
    [
        "marketsim.gen._out._igraph.IGraph",
        [
            "marketsim.gen._out.js._graph.Graph_String",
            "marketsim.gen._out.veusz._graph.Graph_String"
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
        "marketsim.gen._out.strategy.position._bollinger_linear.Bollinger_linear_FloatIObservableFloatISingleAssetTrader",
        [
            "marketsim.gen._out.strategy.position._bollinger_linear.Bollinger_linear_FloatIObservableFloatISingleAssetTrader"
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
        "marketsim.gen._out.strategy.side._pairtrading.PairTrading_IOrderBookFloat",
        [
            "marketsim.gen._out.strategy.side._pairtrading.PairTrading_IOrderBookFloat"
        ]
    ],
    [
        {
            "elementType": "_parseFloat"
        },
        []
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
            "marketsim.gen._out.ops._condition.Condition_BooleanBooleanBoolean",
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
            "marketsim.gen._out.ops._and.And_IObservableBooleanIObservableBoolean",
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanIObservableBooleanIObservableBoolean",
            "marketsim.gen._out.ops._greaterequal.GreaterEqual_IObservableFloatFloat",
            "marketsim.gen._out.trader._pendingvolume.PendingVolume_IAccount",
            "marketsim.gen._out.ops._condition.Condition_BooleanIObservableBooleanIObservableBoolean",
            "marketsim.gen._out.ops._condition.Condition_BooleanIObservableBooleanBoolean",
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
            "marketsim.gen._out.ops._or.Or_BooleanIObservableBoolean",
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanIObservableSideSide",
            "marketsim.gen._out.math._min.Min_IObservableFloatFloat",
            "marketsim.gen._out.ops._mul.Mul_FloatIObservableFloat",
            "marketsim.gen._out.trader._roughpnl.RoughPnL_IAccount",
            "marketsim.gen._out.ops._or.Or_BooleanBoolean",
            "marketsim.gen._out.strategy.side._fundamental_value.Fundamental_Value_strategysidePairTrading",
            "marketsim.gen._out._candlesticks.CandleSticks_IObservableFloatFloat",
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanBooleanIObservableBoolean",
            "marketsim.gen._out._ifdefined.IfDefined_FloatFloat",
            "marketsim.gen._out.ops._lessequal.LessEqual_IObservableFloatIObservableFloat",
            "marketsim.gen._out.ops._and.And_IObservableBooleanBoolean",
            "marketsim.gen._out.ops._lessequal.LessEqual_IObservableFloatFloat",
            "marketsim.gen._out._ifdefined.IfDefined_FloatIObservableFloat",
            "marketsim.gen._out.order._limitsigned.LimitSigned_FloatFloat",
            "marketsim.gen._out.ops._less.Less_IObservableFloatFloat",
            "marketsim.gen._out.ops._div.Div_IObservableFloatIObservableFloat",
            "marketsim.gen._out._test.in1.in2._o.O_IObservableFloat",
            "marketsim.gen._out.math._max.Max_FloatIObservableFloat",
            "marketsim.gen._out.trader._efficiency.Efficiency_IAccount",
            "marketsim.gen._out.ops._condition.Condition_BooleanFloatIObservableFloat",
            "marketsim.gen._out._ifdefined.IfDefined_IObservableFloatIObservableFloat",
            "marketsim.gen._out.math._min.Min_FloatFloat",
            "marketsim.gen._out.strategy.position._desiredposition.DesiredPosition_strategypositionBollinger_linear",
            "marketsim.gen._out.ops._greaterequal.GreaterEqual_FloatIObservableFloat",
            "marketsim.gen._out.strategy.price._islosstoohigh.isLossTooHigh_Float",
            "marketsim.gen._out.ops._div.Div_IObservableFloatFloat",
            "marketsim.gen._out.orderbook._lasttradeprice.LastTradePrice_IOrderQueue",
            "marketsim.gen._out.ops._notequal.NotEqual_IObservableFloatFloat",
            "marketsim.gen._out.order._fixedbudget.FixedBudget_SideFloat",
            "marketsim.gen._out.order._marketsigned.MarketSigned_Float",
            "marketsim.gen._out.strategy.side._side.Side_strategysideMeanReversion",
            "marketsim.gen._out.trader._pershareprice.PerSharePrice_IAccount",
            "marketsim.gen._out.order._limit.Limit_SideFloatFloat",
            "marketsim.gen._out.strategy.side._side.Side_strategysidePairTrading",
            "marketsim.gen._out.ops._greater.Greater_IObservableFloatFloat",
            "marketsim.gen._out.ops._greaterequal.GreaterEqual_FloatFloat",
            "marketsim.gen._out.ops._sub.Sub_FloatFloat",
            "marketsim.gen._out.ops._condition.Condition_BooleanFloatFloat",
            "marketsim.gen._out.math._maxepsilon.MaxEpsilon_mathCumulativeFloat",
            "marketsim.gen._out.orderbook._safesideprice.SafeSidePrice_IOrderQueueFloat",
            "marketsim.gen._out.ops._condition.Condition_BooleanBooleanIObservableBoolean",
            "marketsim.gen._out.orderbook._naivecumulativeprice.NaiveCumulativePrice_IOrderBookIObservableFloat",
            "marketsim.gen._out.ops._and.And_BooleanIObservableBoolean",
            "marketsim.gen._out.order._market.Market_SideFloat",
            "marketsim.gen._out.ops._div.Div_FloatFloat",
            "marketsim.gen._out.ops._less.Less_FloatFloat",
            "marketsim.gen._out.ops._condition.Condition_BooleanIObservableSideSide",
            "marketsim.gen._out.orderbook._lasttradevolume.LastTradeVolume_IOrderQueue",
            "marketsim.gen._out.ops._condition.Condition_BooleanIObservableFloatFloat",
            "marketsim.gen._out.ops._or.Or_IObservableBooleanIObservableBoolean",
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
            "marketsim.gen._out.orderbook._lasttradeimpl.LastTradeImpl_",
            "marketsim.gen._out.order._withexpiry.WithExpiry_IObservableIOrderFloat",
            "marketsim.gen._out.math._maximum.Maximum_mathMoving",
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanBooleanBoolean",
            "marketsim.gen._out.ops._mul.Mul_IObservableFloatIObservableFloat",
            "marketsim.gen._out.ops._equal.Equal_FloatIObservableFloat",
            "marketsim.gen._out.ops._and.And_BooleanBoolean",
            "marketsim.gen._out.ops._sub.Sub_IObservableFloatFloat",
            "marketsim.gen._out.trader._position.Position_IAccount",
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanSideIObservableSide",
            "marketsim.gen._out.ops._greater.Greater_IObservableFloatIObservableFloat",
            "marketsim.gen._out.observable._quote.Quote_StringStringString",
            "marketsim.gen._out.order._peg.Peg_FloatIObservableIOrder",
            "marketsim.gen._out.ops._equal.Equal_IObservableFloatIObservableFloat",
            "marketsim.gen._out._currenttime.CurrentTime_",
            "marketsim.gen._out.math._atan.Atan_Float",
            "marketsim.gen._out.math._pow.Pow_FloatFloat",
            "marketsim.gen._out.math._upmovements.UpMovements_IObservableFloatFloat",
            "marketsim.gen._out.ops._condition.Condition_BooleanSideIObservableSide",
            "marketsim.gen._out.math._sqr.Sqr_IObservableFloat",
            "marketsim.gen._out.ops._notequal.NotEqual_FloatFloat",
            "marketsim.gen._out.math._randomwalk.RandomWalk_FloatFloatFloatString",
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanIObservableBooleanBoolean",
            "marketsim.gen._out.ops._sub.Sub_FloatIObservableFloat",
            "marketsim.gen._out.ops._greater.Greater_FloatFloat",
            "marketsim.gen._out.ops._lessequal.LessEqual_FloatFloat",
            "marketsim.gen._out.ops._notequal.NotEqual_FloatIObservableFloat",
            "marketsim.gen._out.math._max.Max_FloatFloat",
            "marketsim.gen._out.math._exp.Exp_Float",
            "marketsim.gen._out.ops._add.Add_FloatIObservableFloat",
            "marketsim.gen._out.orderbook._safesideprice.SafeSidePrice_IOrderQueueIObservableFloat",
            "marketsim.gen._out.ops._add.Add_FloatFloat",
            "marketsim.gen._out.observable._breaksatchanges.BreaksAtChanges_IObservableFloat",
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanSideSide",
            "marketsim.gen._out.strategy.price._price.Price_strategypriceLiquidityProviderSide",
            "marketsim.gen._out.ops._less.Less_IObservableFloatIObservableFloat",
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanFloatIObservableFloat",
            "marketsim.gen._out.ops._notequal.NotEqual_IObservableFloatIObservableFloat",
            "marketsim.gen._out.math._sqr.Sqr_Float",
            "marketsim.gen._out.ops._condition.Condition_BooleanIObservableFloatIObservableFloat",
            "marketsim.gen._out.strategy.price._islosstoohigh.isLossTooHigh_IObservableFloat",
            "marketsim.gen._out.ops._or.Or_IObservableBooleanBoolean",
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
        "marketsim.gen._out._ifunction._ifunctioniaccount_from_isingleassetstrategy.IFunctionIAccount_from_ISingleAssetStrategy",
        [
            "marketsim.gen._out.strategy.account.inner._inner_virtualmarket.inner_VirtualMarket_",
            "marketsim.gen._out.strategy.account.inner._inner_real.inner_Real_"
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
        "marketsim.gen._out.strategy.side._crossingaverages.CrossingAverages_FloatFloatFloatIOrderBook",
        [
            "marketsim.gen._out.strategy.side._crossingaverages.CrossingAverages_FloatFloatFloatIOrderBook"
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
        "marketsim.gen._out.strategy.price._marketmaker.MarketMaker_FloatFloat",
        [
            "marketsim.gen._out.strategy.price._marketmaker.MarketMaker_FloatFloat"
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
        "marketsim.gen._out.math._ew.EW_IObservableFloatFloat",
        [
            "marketsim.gen._out.math._ew.EW_IObservableFloatFloat"
        ]
    ],
    [
        "marketsim.gen._out.strategy.side._trendfollower.TrendFollower_FloatFloatIOrderBook",
        [
            "marketsim.gen._out.strategy.side._trendfollower.TrendFollower_FloatFloatIOrderBook"
        ]
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
            "marketsim.gen._out.strategy.price._suspend.Suspend_ISuspendableStrategyBoolean",
            "marketsim.gen._out.strategy.price._ladderbalancer.LadderBalancer_ILadderStrategyInt",
            "marketsim.gen._out.strategy.price._clearable.Clearable_ISuspendableStrategyBoolean",
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
            "marketsim.gen._out.strategy.price._stoploss.StopLoss_ISuspendableStrategyIObservableFloat",
            "marketsim.gen._out.strategy.price._onesidestrategy.OneSideStrategy_strategypriceLiquidityProviderIEventSideFloatIObservableIOrderIObservableSide",
            "marketsim.gen._out.strategy.side._strategy.Strategy_strategysideNoiseIEventSideIObservableIOrder",
            "marketsim.gen._out.strategy.price._oneside.OneSide_strategypriceMarketMakerSideFloat",
            "marketsim.gen._out.strategy.side._strategy.Strategy_strategysideTrendFollowerIEventSideIObservableIOrder",
            "marketsim.gen._out.strategy.position._strategy.Strategy_strategypositionBollinger_linearFloatIObservableIOrder",
            "marketsim.gen._out.strategy.side._strategy.Strategy_strategysideRSIbisIEventSideIObservableIOrder",
            "marketsim.gen._out.strategy._tradeifprofitable.TradeIfProfitable_ISingleAssetStrategyISingleAssetStrategyIAccountIAccountFloat",
            "marketsim.gen._out.strategy._multiarmedbandit.MultiArmedBandit_ListISingleAssetStrategyISingleAssetStrategyIAccountIAccountFloatFloatFloatListFloatListFloat",
            "marketsim.gen._out.strategy.side._strategy.Strategy_strategysideSignalIEventSideIObservableIOrder",
            "marketsim.gen._out.strategy.price._stoploss.StopLoss_ISuspendableStrategyFloat",
            "marketsim.gen._out.strategy._empty.Empty_",
            "marketsim.gen._out.strategy.price._oneside.OneSide_strategypriceMarketMakerIObservableSideFloat",
            "marketsim.gen._out.strategy.price._laddermm.LadderMM_SideFloatIObservableIOrderInt",
            "marketsim.gen._out.strategy._array.Array_ListISingleAssetStrategy",
            "marketsim.gen._out.strategy.price._ladder.Ladder_SideFloatIObservableIOrderIntSide"
        ]
    ],
    [
        "marketsim.gen._out._iobservable._iobservablebool.IObservablebool",
        [
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanBooleanIObservableBoolean",
            "marketsim.gen._out.ops._greater.Greater_IObservableFloatIObservableFloat",
            "marketsim.gen._out._observabletrue.observableTrue_",
            "marketsim.gen._out.ops._and.And_BooleanIObservableBoolean",
            "marketsim.gen._out.ops._lessequal.LessEqual_IObservableFloatIObservableFloat",
            "marketsim.gen._out.ops._lessequal.LessEqual_FloatIObservableFloat",
            "marketsim.gen._out.ops._equal.Equal_IObservableFloatFloat",
            "marketsim.gen._out.ops._less.Less_FloatFloat",
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanIObservableBooleanBoolean",
            "marketsim.gen._out.ops._greater.Greater_FloatFloat",
            "marketsim.gen._out.ops._lessequal.LessEqual_IObservableFloatFloat",
            "marketsim.gen._out.ops._lessequal.LessEqual_FloatFloat",
            "marketsim.gen._out.ops._notequal.NotEqual_FloatIObservableFloat",
            "marketsim.gen._out.ops._or.Or_IObservableBooleanIObservableBoolean",
            "marketsim.gen._out.ops._notequal.NotEqual_FloatFloat",
            "marketsim.gen._out.ops._less.Less_IObservableFloatFloat",
            "marketsim.gen._out.ops._condition.Condition_BooleanBooleanBoolean",
            "marketsim.gen._out.ops._greaterequal.GreaterEqual_IObservableFloatIObservableFloat",
            "marketsim.gen._out.ops._less.Less_IObservableFloatIObservableFloat",
            "marketsim.gen._out.ops._equal.Equal_FloatFloat",
            "marketsim.gen._out.ops._less.Less_FloatIObservableFloat",
            "marketsim.gen._out.ops._notequal.NotEqual_IObservableFloatIObservableFloat",
            "marketsim.gen._out.ops._greaterequal.GreaterEqual_FloatIObservableFloat",
            "marketsim.gen._out.ops._greater.Greater_FloatIObservableFloat",
            "marketsim.gen._out.strategy.price._islosstoohigh.isLossTooHigh_Float",
            "marketsim.gen._out.ops._and.And_IObservableBooleanBoolean",
            "marketsim.gen._out.ops._and.And_IObservableBooleanIObservableBoolean",
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanBooleanBoolean",
            "marketsim.gen._out.ops._notequal.NotEqual_IObservableFloatFloat",
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanIObservableBooleanIObservableBoolean",
            "marketsim.gen._out.ops._greaterequal.GreaterEqual_IObservableFloatFloat",
            "marketsim.gen._out.strategy.price._islosstoohigh.isLossTooHigh_IObservableFloat",
            "marketsim.gen._out.ops._condition.Condition_BooleanIObservableBooleanIObservableBoolean",
            "marketsim.gen._out.ops._condition.Condition_BooleanIObservableBooleanBoolean",
            "marketsim.gen._out.ops._equal.Equal_FloatIObservableFloat",
            "marketsim.gen._out.ops._and.And_BooleanBoolean",
            "marketsim.gen._out._observablefalse.observableFalse_",
            "marketsim.gen._out.ops._greater.Greater_IObservableFloatFloat",
            "marketsim.gen._out.ops._greaterequal.GreaterEqual_FloatFloat",
            "marketsim.gen._out.ops._or.Or_IObservableBooleanBoolean",
            "marketsim.gen._out.ops._or.Or_BooleanIObservableBoolean",
            "marketsim.gen._out.ops._or.Or_BooleanBoolean",
            "marketsim.gen._out.ops._condition.Condition_BooleanBooleanIObservableBoolean",
            "marketsim.gen._out.ops._equal.Equal_IObservableFloatIObservableFloat"
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
        "marketsim.gen._out.math._macd.macd_IObservableFloatFloatFloat",
        [
            "marketsim.gen._out.math._macd.macd_IObservableFloatFloatFloat"
        ]
    ],
    [
        "marketsim.gen._out.strategy.price._marketdata.MarketData_StringStringStringFloatFloat",
        [
            "marketsim.gen._out.strategy.price._marketdata.MarketData_StringStringStringFloatFloat"
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
        "marketsim.gen._out.strategy.side._meanreversion.MeanReversion_Float",
        [
            "marketsim.gen._out.strategy.side._meanreversion.MeanReversion_Float"
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
        "marketsim.gen._out._iobservable._iobservablefloat.IObservablefloat",
        [
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanIObservableFloatFloat",
            "marketsim.gen._out.math._relstddev.RelStdDev_mathEW",
            "marketsim.gen._out.orderbook._lastprice.LastPrice_IOrderQueue",
            "marketsim.gen._out._test.in1.in2._intobs.IntObs_",
            "marketsim.gen._out.ops._negate.Negate_Float",
            "marketsim.gen._out._ifdefined.IfDefined_IObservableFloatIObservableFloat",
            "marketsim.gen._out.math._min.Min_FloatIObservableFloat",
            "marketsim.gen._out.orderbook._naivecumulativeprice.NaiveCumulativePrice_IOrderBookFloat",
            "marketsim.gen._out._const.const_Int",
            "marketsim.gen._out.math._minepsilon.MinEpsilon_mathCumulativeFloat",
            "marketsim.gen._out._const.const_Float",
            "marketsim.gen._out.orderbook._cumulativeprice.CumulativePrice_IOrderBookFloat",
            "marketsim.gen._out.math._relstddev.RelStdDev_mathCumulative",
            "marketsim.gen._out.math._max.Max_IObservableFloatIObservableFloat",
            "marketsim.gen._out.observable._breaksatchanges.BreaksAtChanges_IObservableFloat",
            "marketsim.gen._out.trader._pendingvolume.PendingVolume_IAccount",
            "marketsim.gen._out.ops._div.Div_FloatIObservableFloat",
            "marketsim.gen._out.math._downmovements.DownMovements_IObservableFloatFloat",
            "marketsim.gen._out.orderbook._bestprice.BestPrice_IOrderQueue",
            "marketsim.gen._out.math._sqrt.Sqrt_Float",
            "marketsim.gen._out.orderbook._midprice.MidPrice_IOrderBook",
            "marketsim.gen._out.observable._oneverydt.OnEveryDt_FloatFloat",
            "marketsim.gen._out.trader._balance.Balance_IAccount",
            "marketsim.gen._out.math._min.Min_FloatFloat",
            "marketsim.gen._out.math._min.Min_IObservableFloatFloat",
            "marketsim.gen._out.ops._mul.Mul_FloatIObservableFloat",
            "marketsim.gen._out.trader._roughpnl.RoughPnL_IAccount",
            "marketsim.gen._out.strategy.side._fundamental_value.Fundamental_Value_strategysidePairTrading",
            "marketsim.gen._out._ifdefined.IfDefined_FloatFloat",
            "marketsim.gen._out._ifdefined.IfDefined_FloatIObservableFloat",
            "marketsim.gen._out.ops._div.Div_IObservableFloatIObservableFloat",
            "marketsim.gen._out._test.in1.in2._o.O_IObservableFloat",
            "marketsim.gen._out._currenttime.CurrentTime_",
            "marketsim.gen._out.trader._efficiency.Efficiency_IAccount",
            "marketsim.gen._out.ops._condition.Condition_BooleanFloatIObservableFloat",
            "marketsim.gen._out.strategy.position._position.Position_strategypositionRSI_linear",
            "marketsim.gen._out.strategy.position._desiredposition.DesiredPosition_strategypositionBollinger_linear",
            "marketsim.gen._out.ops._div.Div_IObservableFloatFloat",
            "marketsim.gen._out.orderbook._lasttradeprice.LastTradePrice_IOrderQueue",
            "marketsim.gen._out.orderbook._naivecumulativeprice.NaiveCumulativePrice_IOrderBookIObservableFloat",
            "marketsim.gen._out.trader._pershareprice.PerSharePrice_IAccount",
            "marketsim.gen._out.orderbook._spread.Spread_IOrderBook",
            "marketsim.gen._out.ops._sub.Sub_FloatFloat",
            "marketsim.gen._out.ops._condition.Condition_BooleanFloatFloat",
            "marketsim.gen._out.math._maxepsilon.MaxEpsilon_mathCumulativeFloat",
            "marketsim.gen._out.orderbook._safesideprice.SafeSidePrice_IOrderQueueFloat",
            "marketsim.gen._out.orderbook._lasttradevolume.LastTradeVolume_IOrderQueue",
            "marketsim.gen._out.ops._condition.Condition_BooleanIObservableFloatFloat",
            "marketsim.gen._out.ops._negate.Negate_IObservableFloat",
            "marketsim.gen._out.math._max.Max_IObservableFloatFloat",
            "marketsim.gen._out.ops._sub.Sub_IObservableFloatIObservableFloat",
            "marketsim.gen._out.ops._mul.Mul_IObservableFloatFloat",
            "marketsim.gen._out.ops._add.Add_IObservableFloatFloat",
            "marketsim.gen._out.ops._div.Div_FloatFloat",
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanIObservableFloatIObservableFloat",
            "marketsim.gen._out.orderbook._lasttradeimpl.LastTradeImpl_",
            "marketsim.gen._out.math._maximum.Maximum_mathMoving",
            "marketsim.gen._out.ops._mul.Mul_IObservableFloatIObservableFloat",
            "marketsim.gen._out.ops._sub.Sub_IObservableFloatFloat",
            "marketsim.gen._out.trader._position.Position_IAccount",
            "marketsim.gen._out.observable._quote.Quote_StringStringString",
            "marketsim.gen._out.math._max.Max_FloatIObservableFloat",
            "marketsim.gen._out.math._atan.Atan_Float",
            "marketsim.gen._out.math._minimum.Minimum_mathMoving",
            "marketsim.gen._out.math._upmovements.UpMovements_IObservableFloatFloat",
            "marketsim.gen._out.math._sqr.Sqr_IObservableFloat",
            "marketsim.gen._out.math._randomwalk.RandomWalk_FloatFloatFloatString",
            "marketsim.gen._out.ops._sub.Sub_FloatIObservableFloat",
            "marketsim.gen._out.math._max.Max_FloatFloat",
            "marketsim.gen._out.math._exp.Exp_Float",
            "marketsim.gen._out.ops._add.Add_FloatIObservableFloat",
            "marketsim.gen._out.orderbook._safesideprice.SafeSidePrice_IOrderQueueIObservableFloat",
            "marketsim.gen._out.ops._add.Add_FloatFloat",
            "marketsim.gen._out.strategy.price._price.Price_strategypriceLiquidityProviderSide",
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanFloatIObservableFloat",
            "marketsim.gen._out.math._sqr.Sqr_Float",
            "marketsim.gen._out.ops._condition.Condition_BooleanIObservableFloatIObservableFloat",
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanFloatFloat",
            "marketsim.gen._out._ifdefined.IfDefined_IObservableFloatFloat",
            "marketsim.gen._out.ops._mul.Mul_FloatFloat",
            "marketsim.gen._out.strategy.position._desiredposition.DesiredPosition_strategypositionRSI_linear",
            "marketsim.gen._out.math._pow.Pow_FloatFloat",
            "marketsim.gen._out.math._min.Min_IObservableFloatIObservableFloat",
            "marketsim.gen._out.ops._add.Add_IObservableFloatIObservableFloat",
            "marketsim.gen._out.math._relstddev.RelStdDev_mathMoving",
            "marketsim.gen._out.math._lagged.Lagged_IObservableFloatFloat",
            "marketsim.gen._out.strategy.position._position.Position_strategypositionBollinger_linear",
            "marketsim.gen._out.math._log.Log_Float"
        ]
    ],
    [
        "marketsim.gen._out.math._moving.Moving_IObservableFloatFloat",
        [
            "marketsim.gen._out.math._moving.Moving_IObservableFloatFloat"
        ]
    ],
    [
        {
            "elementType": "marketsim.gen._out._itrader.ITrader"
        },
        []
    ],
    [
        "_parseFloat",
        []
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
        "marketsim.gen._out._iladderstrategy.ILadderStrategy",
        [
            "marketsim.gen._out.strategy.price._ladderbalancer.LadderBalancer_ILadderStrategyInt",
            "marketsim.gen._out.strategy.price._laddermm.LadderMM_SideFloatIObservableIOrderInt"
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
        {
            "elementType": "marketsim.gen._out._iorderbook.IOrderBook"
        },
        []
    ],
    [
        "marketsim.gen._out._ifunction._ifunctionbool.IFunctionbool",
        [
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanBooleanIObservableBoolean",
            "marketsim.gen._out._true.true_",
            "marketsim.gen._out._observabletrue.observableTrue_",
            "marketsim.gen._out.ops._and.And_BooleanIObservableBoolean",
            "marketsim.gen._out.ops._lessequal.LessEqual_IObservableFloatIObservableFloat",
            "marketsim.gen._out.ops._lessequal.LessEqual_FloatIObservableFloat",
            "marketsim.gen._out.ops._equal.Equal_IObservableFloatFloat",
            "marketsim.gen._out.ops._less.Less_FloatFloat",
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanIObservableBooleanBoolean",
            "marketsim.gen._out.ops._greater.Greater_FloatFloat",
            "marketsim.gen._out.ops._lessequal.LessEqual_IObservableFloatFloat",
            "marketsim.gen._out.ops._lessequal.LessEqual_FloatFloat",
            "marketsim.gen._out.ops._notequal.NotEqual_FloatIObservableFloat",
            "marketsim.gen._out.ops._or.Or_IObservableBooleanIObservableBoolean",
            "marketsim.gen._out.ops._notequal.NotEqual_FloatFloat",
            "marketsim.gen._out.ops._less.Less_IObservableFloatFloat",
            "marketsim.gen._out.ops._condition.Condition_BooleanBooleanBoolean",
            "marketsim.gen._out.ops._greaterequal.GreaterEqual_IObservableFloatIObservableFloat",
            "marketsim.gen._out.ops._less.Less_IObservableFloatIObservableFloat",
            "marketsim.gen._out.ops._equal.Equal_FloatFloat",
            "marketsim.gen._out.ops._less.Less_FloatIObservableFloat",
            "marketsim.gen._out.ops._notequal.NotEqual_IObservableFloatIObservableFloat",
            "marketsim.gen._out.ops._greaterequal.GreaterEqual_FloatIObservableFloat",
            "marketsim.gen._out.ops._greater.Greater_FloatIObservableFloat",
            "marketsim.gen._out.strategy.price._islosstoohigh.isLossTooHigh_Float",
            "marketsim.gen._out.ops._and.And_IObservableBooleanBoolean",
            "marketsim.gen._out.ops._and.And_IObservableBooleanIObservableBoolean",
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanBooleanBoolean",
            "marketsim.gen._out.ops._notequal.NotEqual_IObservableFloatFloat",
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanIObservableBooleanIObservableBoolean",
            "marketsim.gen._out.ops._greaterequal.GreaterEqual_IObservableFloatFloat",
            "marketsim.gen._out.strategy.price._islosstoohigh.isLossTooHigh_IObservableFloat",
            "marketsim.gen._out.ops._condition.Condition_BooleanIObservableBooleanIObservableBoolean",
            "marketsim.gen._out.ops._condition.Condition_BooleanIObservableBooleanBoolean",
            "marketsim.gen._out._false.false_",
            "marketsim.gen._out.ops._equal.Equal_FloatIObservableFloat",
            "marketsim.gen._out.ops._and.And_BooleanBoolean",
            "marketsim.gen._out._observablefalse.observableFalse_",
            "marketsim.gen._out.ops._greater.Greater_IObservableFloatIObservableFloat",
            "marketsim.gen._out.ops._greater.Greater_IObservableFloatFloat",
            "marketsim.gen._out.ops._greaterequal.GreaterEqual_FloatFloat",
            "marketsim.gen._out.ops._or.Or_IObservableBooleanBoolean",
            "marketsim.gen._out.ops._or.Or_BooleanIObservableBoolean",
            "marketsim.gen._out.ops._or.Or_BooleanBoolean",
            "marketsim.gen._out.ops._condition.Condition_BooleanBooleanIObservableBoolean",
            "marketsim.gen._out.ops._equal.Equal_IObservableFloatIObservableFloat"
        ]
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
        "marketsim.gen._out.strategy.side._signal.Signal_FloatFloat",
        [
            "marketsim.gen._out.strategy.side._signal.Signal_FloatFloat"
        ]
    ],
    [
        {
            "elementType": "marketsim.gen._out._igraph.IGraph"
        },
        []
    ],
    [
        "marketsim.gen._out._isuspendablestrategy.ISuspendableStrategy",
        [
            "marketsim.gen._out.strategy.price._suspend.Suspend_ISuspendableStrategyBoolean",
            "marketsim.gen._out.strategy.price._laddermm.LadderMM_SideFloatIObservableIOrderInt",
            "marketsim.gen._out.strategy.price._ladderbalancer.LadderBalancer_ILadderStrategyInt",
            "marketsim.gen._out.strategy.price._clearable.Clearable_ISuspendableStrategyBoolean"
        ]
    ],
    [
        {
            "elementType": "marketsim.gen._out._itimeserie.ITimeSerie"
        },
        []
    ],
    [
        "marketsim.gen._out._itwowaylink.ITwoWayLink",
        [
            "marketsim.gen._out.orderbook._twowaylink.TwoWayLink_ILinkILink"
        ]
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
            "marketsim.gen._out.ops._condition.Condition_BooleanBooleanBoolean",
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
            "marketsim.gen._out.ops._and.And_IObservableBooleanIObservableBoolean",
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanIObservableBooleanIObservableBoolean",
            "marketsim.gen._out.ops._greaterequal.GreaterEqual_IObservableFloatFloat",
            "marketsim.gen._out.trader._pendingvolume.PendingVolume_IAccount",
            "marketsim.gen._out.ops._condition.Condition_BooleanIObservableBooleanIObservableBoolean",
            "marketsim.gen._out.ops._condition.Condition_BooleanIObservableBooleanBoolean",
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
            "marketsim.gen._out.ops._or.Or_BooleanIObservableBoolean",
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanIObservableSideSide",
            "marketsim.gen._out.math._min.Min_IObservableFloatFloat",
            "marketsim.gen._out.ops._mul.Mul_FloatIObservableFloat",
            "marketsim.gen._out.trader._roughpnl.RoughPnL_IAccount",
            "marketsim.gen._out.ops._or.Or_BooleanBoolean",
            "marketsim.gen._out.strategy.side._fundamental_value.Fundamental_Value_strategysidePairTrading",
            "marketsim.gen._out._candlesticks.CandleSticks_IObservableFloatFloat",
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanBooleanIObservableBoolean",
            "marketsim.gen._out._ifdefined.IfDefined_FloatFloat",
            "marketsim.gen._out.ops._lessequal.LessEqual_IObservableFloatIObservableFloat",
            "marketsim.gen._out.ops._and.And_IObservableBooleanBoolean",
            "marketsim.gen._out.ops._lessequal.LessEqual_IObservableFloatFloat",
            "marketsim.gen._out._ifdefined.IfDefined_FloatIObservableFloat",
            "marketsim.gen._out.order._limitsigned.LimitSigned_FloatFloat",
            "marketsim.gen._out.ops._less.Less_IObservableFloatFloat",
            "marketsim.gen._out.ops._div.Div_IObservableFloatIObservableFloat",
            "marketsim.gen._out._test.in1.in2._o.O_IObservableFloat",
            "marketsim.gen._out.event._event.Event_",
            "marketsim.gen._out.trader._efficiency.Efficiency_IAccount",
            "marketsim.gen._out.ops._condition.Condition_BooleanFloatIObservableFloat",
            "marketsim.gen._out._ifdefined.IfDefined_IObservableFloatIObservableFloat",
            "marketsim.gen._out.math._min.Min_FloatFloat",
            "marketsim.gen._out.strategy.position._desiredposition.DesiredPosition_strategypositionBollinger_linear",
            "marketsim.gen._out.ops._greaterequal.GreaterEqual_FloatIObservableFloat",
            "marketsim.gen._out.strategy.price._islosstoohigh.isLossTooHigh_Float",
            "marketsim.gen._out.ops._div.Div_IObservableFloatFloat",
            "marketsim.gen._out.orderbook._lasttradeprice.LastTradePrice_IOrderQueue",
            "marketsim.gen._out.ops._notequal.NotEqual_IObservableFloatFloat",
            "marketsim.gen._out.order._fixedbudget.FixedBudget_SideFloat",
            "marketsim.gen._out.order._marketsigned.MarketSigned_Float",
            "marketsim.gen._out.strategy.side._side.Side_strategysideMeanReversion",
            "marketsim.gen._out.trader._pershareprice.PerSharePrice_IAccount",
            "marketsim.gen._out.order._limit.Limit_SideFloatFloat",
            "marketsim.gen._out.strategy.side._side.Side_strategysidePairTrading",
            "marketsim.gen._out.ops._sub.Sub_FloatIObservableFloat",
            "marketsim.gen._out.ops._greaterequal.GreaterEqual_FloatFloat",
            "marketsim.gen._out.ops._sub.Sub_FloatFloat",
            "marketsim.gen._out.ops._condition.Condition_BooleanFloatFloat",
            "marketsim.gen._out.math._maxepsilon.MaxEpsilon_mathCumulativeFloat",
            "marketsim.gen._out.orderbook._safesideprice.SafeSidePrice_IOrderQueueFloat",
            "marketsim.gen._out.ops._condition.Condition_BooleanBooleanIObservableBoolean",
            "marketsim.gen._out.orderbook._naivecumulativeprice.NaiveCumulativePrice_IOrderBookIObservableFloat",
            "marketsim.gen._out.ops._and.And_BooleanIObservableBoolean",
            "marketsim.gen._out.order._market.Market_SideFloat",
            "marketsim.gen._out.ops._div.Div_FloatFloat",
            "marketsim.gen._out.ops._less.Less_FloatFloat",
            "marketsim.gen._out.ops._condition.Condition_BooleanIObservableSideSide",
            "marketsim.gen._out.orderbook._lasttradevolume.LastTradeVolume_IOrderQueue",
            "marketsim.gen._out.ops._condition.Condition_BooleanIObservableFloatFloat",
            "marketsim.gen._out.ops._or.Or_IObservableBooleanIObservableBoolean",
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
            "marketsim.gen._out.orderbook._lasttradeimpl.LastTradeImpl_",
            "marketsim.gen._out.order._withexpiry.WithExpiry_IObservableIOrderFloat",
            "marketsim.gen._out.event._every.Every_Float",
            "marketsim.gen._out.math._maximum.Maximum_mathMoving",
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanBooleanBoolean",
            "marketsim.gen._out.ops._mul.Mul_IObservableFloatIObservableFloat",
            "marketsim.gen._out.ops._equal.Equal_FloatIObservableFloat",
            "marketsim.gen._out.ops._and.And_BooleanBoolean",
            "marketsim.gen._out.ops._sub.Sub_IObservableFloatFloat",
            "marketsim.gen._out.trader._position.Position_IAccount",
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanSideIObservableSide",
            "marketsim.gen._out.ops._greater.Greater_IObservableFloatIObservableFloat",
            "marketsim.gen._out.observable._quote.Quote_StringStringString",
            "marketsim.gen._out.order._peg.Peg_FloatIObservableIOrder",
            "marketsim.gen._out.ops._equal.Equal_IObservableFloatIObservableFloat",
            "marketsim.gen._out._currenttime.CurrentTime_",
            "marketsim.gen._out.math._atan.Atan_Float",
            "marketsim.gen._out.math._pow.Pow_FloatFloat",
            "marketsim.gen._out.math._upmovements.UpMovements_IObservableFloatFloat",
            "marketsim.gen._out.ops._condition.Condition_BooleanSideIObservableSide",
            "marketsim.gen._out.math._sqr.Sqr_IObservableFloat",
            "marketsim.gen._out.ops._notequal.NotEqual_FloatFloat",
            "marketsim.gen._out.math._randomwalk.RandomWalk_FloatFloatFloatString",
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanIObservableBooleanBoolean",
            "marketsim.gen._out.ops._greater.Greater_IObservableFloatFloat",
            "marketsim.gen._out.ops._greater.Greater_FloatFloat",
            "marketsim.gen._out.ops._lessequal.LessEqual_FloatFloat",
            "marketsim.gen._out.ops._notequal.NotEqual_FloatIObservableFloat",
            "marketsim.gen._out.math._max.Max_FloatFloat",
            "marketsim.gen._out.math._exp.Exp_Float",
            "marketsim.gen._out.ops._add.Add_FloatIObservableFloat",
            "marketsim.gen._out.math._max.Max_FloatIObservableFloat",
            "marketsim.gen._out.orderbook._safesideprice.SafeSidePrice_IOrderQueueIObservableFloat",
            "marketsim.gen._out.event._after.After_Float",
            "marketsim.gen._out.ops._add.Add_FloatFloat",
            "marketsim.gen._out.observable._breaksatchanges.BreaksAtChanges_IObservableFloat",
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanSideSide",
            "marketsim.gen._out.strategy.price._price.Price_strategypriceLiquidityProviderSide",
            "marketsim.gen._out.ops._less.Less_IObservableFloatIObservableFloat",
            "marketsim.gen._out.ops._condition.Condition_IObservableBooleanFloatIObservableFloat",
            "marketsim.gen._out.ops._notequal.NotEqual_IObservableFloatIObservableFloat",
            "marketsim.gen._out.math._sqr.Sqr_Float",
            "marketsim.gen._out.ops._condition.Condition_BooleanIObservableFloatIObservableFloat",
            "marketsim.gen._out.strategy.price._islosstoohigh.isLossTooHigh_IObservableFloat",
            "marketsim.gen._out.ops._or.Or_IObservableBooleanBoolean",
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
            "marketsim.gen._out._currenttime.CurrentTime_",
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
            "marketsim.gen._out.trader._pershareprice.PerSharePrice_IAccount",
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
            "marketsim.gen._out.orderbook._lasttradeimpl.LastTradeImpl_",
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
        "marketsim.gen._out.strategy.position._rsi_linear.RSI_linear_FloatIObservableFloatFloatISingleAssetTrader",
        [
            "marketsim.gen._out.strategy.position._rsi_linear.RSI_linear_FloatIObservableFloatFloatISingleAssetTrader"
        ]
    ],
    [
        "marketsim.gen._out.strategy.price._liquidityprovider.LiquidityProvider_FloatFloatIOrderBook",
        [
            "marketsim.gen._out.strategy.price._liquidityprovider.LiquidityProvider_FloatFloatIOrderBook"
        ]
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
        "marketsim.gen._out._imultiassetstrategy.IMultiAssetStrategy",
        [
            "marketsim.gen._out.strategy._arbitrage.Arbitrage_"
        ]
    ],
    [
        "marketsim.gen._out.strategy.side._noise.Noise_Float",
        [
            "marketsim.gen._out.strategy.side._noise.Noise_Float"
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
        "marketsim.gen._out.math._cumulative.Cumulative_IObservableFloat",
        [
            "marketsim.gen._out.math._cumulative.Cumulative_IObservableFloat"
        ]
    ],
    [
        {
            "elementType": "marketsim.gen._out._isingleassettrader.ISingleAssetTrader"
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
        {
            "elementType": "marketsim.gen._out._isingleassetstrategy.ISingleAssetStrategy"
        },
        []
    ],
    [
        "marketsim.gen._out._ilink.ILink",
        [
            "marketsim.gen._out.orderbook._link.Link_IObservableFloat"
        ]
    ],
    [
        "marketsim.gen._out.math._rsi.RSI_IObservableFloatFloatFloat",
        [
            "marketsim.gen._out.math._rsi.RSI_IObservableFloatFloatFloat"
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
        "identity",
        [
            "marketsim.gen._out._test.in1.in2._s2.S2_",
            "marketsim.gen._out._test.in1.in2._s1.S1_String"
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
    ]
]