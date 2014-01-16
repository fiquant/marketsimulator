var typeinfo = {
    "marketsim.gen._out.observable.volumefunc._DesiredPosition.DesiredPosition": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
    "marketsim.gen._out.side._Sell.Sell": {
        "castsTo": [
            "marketsim.types.IFunction_Tag"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.observable.sidefunc._TrendFollower.TrendFollower": {
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
    "marketsim.gen._out._Derivative.Derivative": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "x": {
                "type": "marketsim.types.IDifferentiable"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy._ChooseTheBest.ChooseTheBest": {
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
        "description": "<div class=\"document\">\n<p>In some moments of time the most effective strategy\nis chosen and made running; other strategies are suspended.</p>\n</div>\n"
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
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.observable._OnEveryDt.OnEveryDt": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
            },
            "eventSource": {
                "type": "marketsim.types.IEvent"
            },
            "dataSource": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.observable.trader._Balance.Balance": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
    "marketsim.gen._out.observable.orderbook._WeightedPrice.WeightedPrice": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
    "marketsim.gen._out.mathutils.rnd._vonmisesvariate.vonmisesvariate": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
    "marketsim.gen._out.order._curried._side_price_Limit.side_price_Limit": {
        "castsTo": [
            "marketsim.types.IFunction_IFunction_IOrderGenerator_IFunction_float_IFunction_Tag"
        ],
        "properties": {
            "volume": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.observable._Max.Max": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
    "marketsim.side_._SellSide": {
        "castsTo": [
            "marketsim.Side"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n<p>Tag class representing the sell side</p>\n</div>\n"
    },
    "marketsim.gen._out.observable._RSI.RSI": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
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
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.observable.orderbook._BidLastTradePrice.BidLastTradePrice": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
    "marketsim.gen._out.strategy._Combine.Combine": {
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
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.observable.EW._Avg.Avg": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
        "description": "<div class=\"document\">\n</div>\n"
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
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.mathutils.rnd._betavariate.betavariate": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
    "marketsim.observable.fold._last.Last": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "source": {
                "type": "marketsim.types.IObservable_float"
            }
        },
        "description": "<div class=\"document\">\n<dl class=\"docutils\">\n<dt>Aggregates (folds) time-dependent data from <em>source</em> using given</dt>\n<dd>functional  <em>folder</em> (e.g. moving average) defined in derived class</dd>\n</dl>\n<p>For example</p>\n<pre class=\"literal-block\">\nprice_avg = EWMA(MidPrice(book_A), alpha = 0.15)\n</pre>\n<p>creates a observable for a moving average with \u03b1 = 0.15 of mid-price of asset <em>book_A</em></p>\n</div>\n"
    },
    "marketsim.gen._out.strategy._TradeIfProfitable.TradeIfProfitable": {
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
    "marketsim.order._limit.AdaptLimit": {
        "castsTo": [],
        "properties": {
            "priceFunc": {
                "type": {
                    "rv": "_parseFloat",
                    "args": []
                }
            },
            "orderFactory": {
                "type": {
                    "rv": {
                        "rv": "marketsim.types.IOrder",
                        "args": [
                            "_parseFloat",
                            "_parseFloat"
                        ]
                    },
                    "args": [
                        "marketsim.Side"
                    ]
                }
            }
        },
        "description": "<div class=\"document\">\n<p>Adapts limit-like orders for usage where market-like orders are expected.\nUser should provide <em>priceFunc</em> calculating price of order to create</p>\n</div>\n"
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
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.orderbook._Link.Link": {
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
    "marketsim.gen._out.observable.Cumulative._MinEpsilon.MinEpsilon": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.observable.orderbook._TickSize.TickSize": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "book": {
                "type": "marketsim.types.IOrderBook"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out._IfDefined.IfDefined": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.observable.orderbook._OfTrader.OfTrader": {
        "castsTo": [
            "marketsim.types.IOrderBook"
        ],
        "properties": {
            "Trader": {
                "type": "marketsim.types.IAccount"
            }
        },
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
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.ops._arithmetic.Sum": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "rhs": {
                "type": {
                    "rv": "_parseFloat",
                    "args": []
                }
            },
            "lhs": {
                "type": {
                    "rv": "_parseFloat",
                    "args": []
                }
            }
        },
        "description": "<div class=\"document\">\n<p>Function returning Sum of the operands</p>\n</div>\n"
    },
    "marketsim.gen._out.mathops._Pow.Pow": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
    "marketsim.gen._out.side._Nothing.Nothing": {
        "castsTo": [
            "marketsim.types.IFunction_Tag"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.ops._arithmetic.Sub": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "rhs": {
                "type": {
                    "rv": "_parseFloat",
                    "args": []
                }
            },
            "lhs": {
                "type": {
                    "rv": "_parseFloat",
                    "args": []
                }
            }
        },
        "description": "<div class=\"document\">\n<p>Function substructing the right operand from the left one</p>\n</div>\n"
    },
    "marketsim.gen._out.observable.rsi._Raw.Raw": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
    "marketsim.gen._out.observable.Moving._Max.Max": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
    "marketsim.gen._out.order._curried._signedVolume_MarketSigned.signedVolume_MarketSigned": {
        "castsTo": [
            "marketsim.types.IFunction_IOrderGenerator_IFunction_float"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy._Bollinger_linear.Bollinger_linear": {
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
    "marketsim.gen._out._false.false": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_bool",
            "marketsim.types.IObservable_object"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.mathutils.rnd._normalvariate.normalvariate": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
    "marketsim.gen._out.strategy._Signal.Signal": {
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
    "marketsim.gen._out.strategy._Array.Array": {
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
    "marketsim.gen._out.strategy._Arbitrage.Arbitrage": {
        "castsTo": [
            "marketsim.types.IMultiAssetStrategy"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.observable.orderbook._Spread.Spread": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
    "marketsim.gen._out._constant.constant": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "x": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.observable.macd._Signal.Signal": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
    "marketsim.gen._out.mathutils.rnd._expovariate.expovariate": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "Lambda": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n<p>Returned values range from 0 to positive infinity</p>\n</div>\n"
    },
    "marketsim.gen._out.observable.sidefunc._MeanReversion.MeanReversion": {
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
    "marketsim.gen._out.strategy.account._Real.Real": {
        "castsTo": [
            "marketsim.types.IAccount"
        ],
        "properties": {
            "inner": {
                "type": "marketsim.types.ISingleAssetStrategy"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.mathutils.rnd._triangular.triangular": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
    "marketsim.gen._out.order._curried._side_FixedBudget.side_FixedBudget": {
        "castsTo": [
            "marketsim.types.IFunction_IOrderGenerator_IFunction_Tag"
        ],
        "properties": {
            "budget": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.weight._.trader._trader_Efficiency.trader_Efficiency": {
        "castsTo": [
            "marketsim.types.IFunction_IFunction_float_IAccount"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.ops._arithmetic.Div": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "rhs": {
                "type": {
                    "rv": "_parseFloat",
                    "args": []
                }
            },
            "lhs": {
                "type": {
                    "rv": "_parseFloat",
                    "args": []
                }
            }
        },
        "description": "<div class=\"document\">\n<p>Function returning division of the operands</p>\n</div>\n"
    },
    "marketsim.gen._out.strategy.weight._EfficiencyTrend.EfficiencyTrend": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
    "marketsim.gen._out.strategy.account._.inner._inner_Real.inner_Real": {
        "castsTo": [
            "marketsim.types.IFunction_IAccount_ISingleAssetStrategy"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.observable.volumefunc._Bollinger_linear.Bollinger_linear": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
    "marketsim.gen._out.orderbook._TwoWayLink.TwoWayLink": {
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
    "marketsim.gen._out.event._After.After": {
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
    "marketsim.gen._out._const.const": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
    "marketsim.gen._out.strategy._MultiArmedBandit.MultiArmedBandit": {
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
        "description": "<div class=\"document\">\n<p>In some moments of time the most effective strategy\nis chosen and made running; other strategies are suspended.\nThe choice is made randomly among the strategies that have\na positive efficiency trend, weighted by the efficiency value.</p>\n</div>\n"
    },
    "marketsim.gen._out.observable.orderbook._MidPrice.MidPrice": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
    "marketsim.gen._out.order._curried._side_Market.side_Market": {
        "castsTo": [
            "marketsim.types.IFunction_IOrderGenerator_IFunction_Tag"
        ],
        "properties": {
            "volume": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.observable._Sqr.Sqr": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
    "marketsim.gen._out.observable.orderbook._Asks.Asks": {
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
    "marketsim.orderbook._proxy.Proxy": {
        "castsTo": [
            "marketsim.types.IOrderBook"
        ],
        "properties": {},
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
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy._RSIbis.RSIbis": {
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
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.observable.orderbook._VolumeLevels.VolumeLevels": {
        "castsTo": [
            "marketsim.types.IFunction_IVolumeLevels"
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
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.observable.orderbook._AskLastPrice.AskLastPrice": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy._MarketData.MarketData": {
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
    "marketsim.gen._out.observable.orderbook._BestPrice.BestPrice": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
        "description": "<div class=\"document\">\n</div>\n"
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
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.weight._.array._array_IdentityL.array_IdentityL": {
        "castsTo": [
            "marketsim.types.IFunction_listOf_listOf"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.observable._Lagged.Lagged": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
    "marketsim.gen._out.observable.orderbook._AskWeightedPrice.AskWeightedPrice": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
    "marketsim.gen._out.strategy.weight._.trader._trader_Unit.trader_Unit": {
        "castsTo": [
            "marketsim.types.IFunction_IFunction_float_IAccount"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.observable.pricefunc._LiquidityProvider.LiquidityProvider": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
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
    "marketsim.gen._out.observable.macd._MACD.MACD": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
    "marketsim.gen._out.observable.orderbook._LastTradePrice.LastTradePrice": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.mathutils._average.ewma": {
        "castsTo": [],
        "properties": {
            "alpha": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n<p>Exponentially weighted moving average</p>\n</div>\n"
    },
    "marketsim.gen._out.observable.EW._Var.Var": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
    "marketsim.gen._out.strategy._Generic.Generic": {
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
    "marketsim.gen._out.observable.orderbook._BidLastPrice.BidLastPrice": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
    "marketsim.gen._out.strategy._FundamentalValue.FundamentalValue": {
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
    "marketsim.order._market.MarketFactory": {
        "castsTo": [],
        "properties": {},
        "description": "<div class=\"document\">\n<p>Market order of given <em>side</em> and <em>volume</em></p>\n</div>\n"
    },
    "marketsim.observable._computed.IndicatorBaseT_IVolumeLevels": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_IVolumeLevels",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "eventSource": {
                "type": "marketsim.types.IEvent"
            },
            "dataSource": {
                "type": "marketsim.types.IFunction_IVolumeLevels"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.observable.orderbook._Bids.Bids": {
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
    "marketsim.order.meta._with_expiry.WithExpiryFactory": {
        "castsTo": [
            {
                "rv": {
                    "rv": "marketsim.types.IOrder",
                    "args": [
                        "_parseFloat",
                        "_parseFloat"
                    ]
                },
                "args": [
                    "marketsim.Side"
                ]
            }
        ],
        "properties": {
            "expirationDistr": {
                "type": {
                    "rv": "_parseFloat",
                    "args": []
                }
            }
        },
        "description": "<div class=\"document\">\n<p>Limit-like order which is cancelled after given <em>delay</em></p>\n</div>\n"
    },
    "marketsim.gen._out.mathutils.rnd._paretovariate.paretovariate": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "Alpha": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy._MeanReversion.MeanReversion": {
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
    "marketsim.gen._out.strategy.weight._.f._f_AtanPow.f_AtanPow": {
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
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.observable.orderbook._SafeSidePrice.SafeSidePrice": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.weight._.trader._trader_EfficiencyTrend.trader_EfficiencyTrend": {
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
    "marketsim.gen._out.observable.sidefunc._Noise.Noise": {
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
    "marketsim.gen._out.observable.Moving._Min.Min": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
    "marketsim.gen._out.strategy._LiquidityProvider.LiquidityProvider": {
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
    "marketsim.gen._out.observable.Moving._Avg.Avg": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
    "marketsim.gen._out.observable.Cumulative._Var.Var": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "source": {
                "type": "marketsim.types.IObservable_float"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.observable._DownMovements.DownMovements": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
    "marketsim.gen._out.observable.EW._StdDev.StdDev": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
    "marketsim.ops._all.identity": {
        "castsTo": [],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.observable.trader._RoughPnL.RoughPnL": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
    "marketsim.gen._out.observable.trader._PendingVolume.PendingVolume": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
    "marketsim.gen._out.mathops._Atan.Atan": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
    "marketsim.gen._out.observable.orderbook._LastTradeVolume.LastTradeVolume": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy._MarketMaker.MarketMaker": {
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
    "marketsim.gen._out.observable.volumefunc._RSI_linear.RSI_linear": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
    "marketsim.gen._out.event._Every.Every": {
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
    "marketsim.gen._out.observable.orderbook._BidWeightedPrice.BidWeightedPrice": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy._CrossingAverages.CrossingAverages": {
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
    "marketsim.gen._out._true.true": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_bool",
            "marketsim.types.IObservable_object"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.observable.sidefunc._CrossingAverages.CrossingAverages": {
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
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.observable._UpMovements.UpMovements": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
    "marketsim.gen._out.strategy._Canceller.Canceller": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy"
        ],
        "properties": {
            "cancellationIntervalDistr": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.side_._BuySide": {
        "castsTo": [
            "marketsim.Side"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.observable.Moving._Var.Var": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
    "marketsim.gen._out.strategy.weight._.array._array_ChooseTheBest.array_ChooseTheBest": {
        "castsTo": [
            "marketsim.types.IFunction_listOf_listOf"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.observable.macd._Histogram.Histogram": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
    "marketsim.gen._out.observable.Cumulative._MaxEpsilon.MaxEpsilon": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.observable._BreaksAtChanges.BreaksAtChanges": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.observable._CandleSticks.CandleSticks": {
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
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.side._Buy.Buy": {
        "castsTo": [
            "marketsim.types.IFunction_Tag"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.strategy._basic.Empty": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy._RSI_linear.RSI_linear": {
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
    "marketsim.gen._out.observable.sidefunc._PairTrading.PairTrading": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_Tag",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "book": {
                "type": "marketsim.types.IOrderBook"
            },
            "dependee": {
                "type": "marketsim.types.IOrderBook"
            },
            "factor": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.weight._.f._f_IdentityF.f_IdentityF": {
        "castsTo": [
            "marketsim.types.IFunction_IFunction_float_IFunction_float"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.observable.Cumulative._Avg.Avg": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
    "marketsim.gen._out.observable.trader._Position.Position": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
    "marketsim.gen._out.veusz._Graph.Graph": {
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
    "marketsim.gen._out.observable.sidefunc._Signal.Signal": {
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
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.trader._SingleProxy.SingleProxy": {
        "castsTo": [
            "marketsim.types.IAccount",
            "marketsim.types.ISingleAssetTrader",
            "marketsim.types.ITrader"
        ],
        "properties": {},
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
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.mathops._Exp.Exp": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
    "marketsim.gen._out.observable._Quote.Quote": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.observable.EW._RelStdDev.RelStdDev": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
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
    "marketsim.gen._intrinsic.strategy.basic.Empty": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.account._VirtualMarket.VirtualMarket": {
        "castsTo": [
            "marketsim.types.IAccount"
        ],
        "properties": {
            "inner": {
                "type": "marketsim.types.ISingleAssetStrategy"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.orderbook._Local.Local": {
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
    "marketsim.gen._out.orderbook._Remote.Remote": {
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
    "marketsim.gen._out.strategy._PairTrading.PairTrading": {
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
    "marketsim.gen._out.observable.Moving._StdDev.StdDev": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
    "marketsim.gen._out.mathops._Sqrt.Sqrt": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
    "marketsim.gen._out.observable.orderbook._AskLastTradePrice.AskLastTradePrice": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
    "marketsim.gen._out.strategy._Noise.Noise": {
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
    "marketsim.gen._out.observable.orderbook._AskPrice.AskPrice": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
    "marketsim.js.Graph": {
        "castsTo": [
            "marketsim.types.IGraph"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n<p>Generic 2D graph to be rendered by means of javascript libraries</p>\n</div>\n"
    },
    "marketsim.gen._out.mathutils.rnd._lognormvariate.lognormvariate": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
    "marketsim.gen._out._volumeLevels.volumeLevels": {
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
        "description": "<div class=\"document\">\n</div>\n"
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
    "marketsim.gen._out.observable._ObservableSide.ObservableSide": {
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
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy._TrendFollower.TrendFollower": {
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
    "marketsim.gen._out.order._curried._side_Peg.side_Peg": {
        "castsTo": [
            "marketsim.types.IFunction_IOrderGenerator_IFunction_Tag"
        ],
        "properties": {
            "proto": {
                "type": "marketsim.types.IFunction_IFunction_IOrderGenerator_IFunction_float_IFunction_Tag"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.observable.orderbook._CumulativePrice.CumulativePrice": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.observable._Observable.Observable": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
    "marketsim.gen._out._null.null": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.ops._all.negate": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "arg": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>Function returning Product of the operands</p>\n</div>\n"
    },
    "marketsim.gen._out.trader._MultiAsset.MultiAsset": {
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
        "description": "<div class=\"document\">\n</div>\n"
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
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.mathutils.rnd._uniform.uniform": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
    "marketsim.gen._out.strategy.weight._AtanPow.AtanPow": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
    "marketsim.gen._out.strategy._Suspendable.Suspendable": {
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
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.observable.orderbook._BidPrice.BidPrice": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
    "marketsim.gen._out.mathops._Log.Log": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
    "marketsim.order._limit.LimitFactory": {
        "castsTo": [
            {
                "rv": {
                    "rv": "marketsim.types.IOrder",
                    "args": [
                        "_parseFloat",
                        "_parseFloat"
                    ]
                },
                "args": [
                    "marketsim.Side"
                ]
            }
        ],
        "properties": {},
        "description": "<div class=\"document\">\n<p>Limit order of the given <em>side</em>, <em>price</em> and <em>volume</em></p>\n</div>\n"
    },
    "marketsim.ops._arithmetic.Product": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "rhs": {
                "type": {
                    "rv": "_parseFloat",
                    "args": []
                }
            },
            "lhs": {
                "type": {
                    "rv": "_parseFloat",
                    "args": []
                }
            }
        },
        "description": "<div class=\"document\">\n<p>Function returning product of the operands</p>\n</div>\n"
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
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy._LiquidityProviderSide.LiquidityProviderSide": {
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
    "marketsim.gen._out.mathutils.rnd._gammavariate.gammavariate": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
    "marketsim.gen._out.observable.orderbook._NaiveCumulativePrice.NaiveCumulativePrice": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.observable.trader._Efficiency.Efficiency": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
    "marketsim.gen._out.strategy.weight._.f._f_Clamp0.f_Clamp0": {
        "castsTo": [
            "marketsim.types.IFunction_IFunction_float_IFunction_float"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out._TimeSerie.TimeSerie": {
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
        "description": "<div class=\"document\">\n</div>\n"
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
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.ops._all.Constant_float": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "value": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n<p>Constant function returning <strong>value</strong>.</p>\n</div>\n"
    },
    "marketsim.gen._out.observable.sidefunc._FundamentalValue.FundamentalValue": {
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
    "marketsim.ops._all.Constant_Tag": {
        "castsTo": [
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_Tag",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "value": {
                "type": "marketsim.Side"
            }
        },
        "description": "<div class=\"document\">\n<p>Constant function returning <strong>value</strong>.</p>\n</div>\n"
    },
    "marketsim.observable.fold._two_point.TwoPoint": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_float",
            "marketsim.types.IObservable_float",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "source": {
                "type": "marketsim.types.IObservable_float"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.observable._ObservableVolume.ObservableVolume": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
    "marketsim.gen._out.trader._SingleAsset.SingleAsset": {
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
    "marketsim.gen._out.order._curried._pricevolume_Limit.pricevolume_Limit": {
        "castsTo": [],
        "properties": {
            "side": {
                "type": "marketsim.types.IFunction_Tag"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.weight._.trader._trader_Score.trader_Score": {
        "castsTo": [
            "marketsim.types.IFunction_IFunction_float_IAccount"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.mathutils.rnd._weibullvariate.weibullvariate": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.strategy.account._.inner._inner_VirtualMarket.inner_VirtualMarket": {
        "castsTo": [
            "marketsim.types.IFunction_IAccount_ISingleAssetStrategy"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.observable.orderbook._LastPrice.LastPrice": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.mathutils._rsi.rsi": {
        "castsTo": [],
        "properties": {
            "alpha": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n<p>Relative strength index</p>\n</div>\n"
    },
    "marketsim.gen._out.observable._ObservablePrice.ObservablePrice": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
    "marketsim.gen._out.observable.Cumulative._StdDev.StdDev": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "source": {
                "type": "marketsim.types.IObservable_float"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.observable._RandomWalk.RandomWalk": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
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
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.gen._out.observable.orderbook._Queue.Queue": {
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
        "description": "<div class=\"document\">\n</div>\n"
    }
}
var interfaces = [
    [
        "_parseInt",
        []
    ],
    [
        {
            "elementType": "marketsim.types.ISingleAssetStrategy"
        },
        []
    ],
    [
        "marketsim.types.IFunction_IFunction_float_IAccount",
        [
            "marketsim.gen._out.strategy.weight._.trader._trader_Unit.trader_Unit",
            "marketsim.gen._out.strategy.weight._.trader._trader_Efficiency.trader_Efficiency",
            "marketsim.gen._out.strategy.weight._.trader._trader_EfficiencyTrend.trader_EfficiencyTrend",
            "marketsim.gen._out.strategy.weight._.trader._trader_Score.trader_Score"
        ]
    ],
    [
        "marketsim.types.ITimeSerie",
        [
            "marketsim.gen._out._TimeSerie.TimeSerie",
            "marketsim.gen._out._volumeLevels.volumeLevels"
        ]
    ],
    [
        {
            "elementType": "_parseFloat"
        },
        []
    ],
    [
        "marketsim.types.IEvent",
        [
            "marketsim.gen._out.observable._DownMovements.DownMovements",
            "marketsim.gen._out.observable.trader._RoughPnL.RoughPnL",
            "marketsim.gen._out.mathops._Sqrt.Sqrt",
            "marketsim.gen._out.observable.trader._PendingVolume.PendingVolume",
            "marketsim.gen._out.mathops._Atan.Atan",
            "marketsim.gen._out.observable.orderbook._AskLastTradePrice.AskLastTradePrice",
            "marketsim.gen._out.observable.orderbook._AskPrice.AskPrice",
            "marketsim.gen._out.observable.orderbook._LastTradeVolume.LastTradeVolume",
            "marketsim.gen._out.order._FixedBudget.FixedBudget",
            "marketsim.gen._out.observable._OnEveryDt.OnEveryDt",
            "marketsim.gen._out.observable.volumefunc._RSI_linear.RSI_linear",
            "marketsim.gen._out._const.const",
            "marketsim.gen._out.observable.volumefunc._DesiredPosition.DesiredPosition",
            "marketsim.gen._out.observable.orderbook._MidPrice.MidPrice",
            "marketsim.gen._out.observable._ObservableSide.ObservableSide",
            "marketsim.ops._arithmetic.Div",
            "marketsim.ops._all.Constant_float",
            "marketsim.gen._out.observable.trader._Balance.Balance",
            "marketsim.gen._out.observable._Sqr.Sqr",
            "marketsim.gen._out.observable.orderbook._CumulativePrice.CumulativePrice",
            "marketsim.gen._out.observable.orderbook._BidPrice.BidPrice",
            "marketsim.observable._computed.IndicatorBaseT_IVolumeLevels",
            "marketsim.gen._out.order._ImmediateOrCancel.ImmediateOrCancel",
            "marketsim.gen._out.observable._Observable.Observable",
            "marketsim.gen._out.order._WithExpiry.WithExpiry",
            "marketsim.gen._out._null.null",
            "marketsim.gen._out.observable._RSI.RSI",
            "marketsim.gen._out.observable.Cumulative._MaxEpsilon.MaxEpsilon",
            "marketsim.gen._out.observable.orderbook._AskLastPrice.AskLastPrice",
            "marketsim.gen._out.observable._UpMovements.UpMovements",
            "marketsim.gen._out.order._LimitSigned.LimitSigned",
            "marketsim.gen._out.observable.trader._Position.Position",
            "marketsim.gen._out.observable._BreaksAtChanges.BreaksAtChanges",
            "marketsim.gen._out.observable.orderbook._BestPrice.BestPrice",
            "marketsim.gen._out.observable._CandleSticks.CandleSticks",
            "marketsim.gen._out.observable.volumefunc._Bollinger_linear.Bollinger_linear",
            "marketsim.gen._out.order._Market.Market",
            "marketsim.gen._out.observable._Lagged.Lagged",
            "marketsim.gen._out.order._StopLoss.StopLoss",
            "marketsim.gen._out._IfDefined.IfDefined",
            "marketsim.gen._out.mathops._Log.Log",
            "marketsim.gen._out.observable.orderbook._LastPrice.LastPrice",
            "marketsim.gen._out.observable._ObservablePrice.ObservablePrice",
            "marketsim.gen._out.order._FloatingPrice.FloatingPrice",
            "marketsim.gen._out.observable.pricefunc._LiquidityProvider.LiquidityProvider",
            "marketsim.ops._arithmetic.Product",
            "marketsim.gen._out.observable.orderbook._LastTradePrice.LastTradePrice",
            "marketsim.gen._out.observable.Cumulative._MinEpsilon.MinEpsilon",
            "marketsim.gen._out.order._Iceberg.Iceberg",
            "marketsim.gen._out.order._MarketSigned.MarketSigned",
            "marketsim.gen._out.observable.orderbook._BidLastPrice.BidLastPrice",
            "marketsim.observable.fold._two_point.TwoPoint",
            "marketsim.gen._out.observable.trader._Efficiency.Efficiency",
            "marketsim.ops._arithmetic.Sum",
            "marketsim.gen._out.event._After.After",
            "marketsim.gen._out.mathops._Pow.Pow",
            "marketsim.ops._arithmetic.Sub",
            "marketsim.gen._out.observable._Max.Max",
            "marketsim.gen._out.observable.orderbook._BidLastTradePrice.BidLastTradePrice",
            "marketsim.gen._out.observable.sidefunc._FundamentalValue.FundamentalValue",
            "marketsim.gen._out.observable.Moving._Max.Max",
            "marketsim.gen._out.observable.sidefunc._Signal.Signal",
            "marketsim.gen._out.observable._ObservableVolume.ObservableVolume",
            "marketsim.gen._out.observable._RandomWalk.RandomWalk",
            "marketsim.gen._out._false.false",
            "marketsim.gen._out.observable.orderbook._NaiveCumulativePrice.NaiveCumulativePrice",
            "marketsim.gen._out.mathops._Exp.Exp",
            "marketsim.gen._out.observable._Quote.Quote",
            "marketsim.gen._out.event._Every.Every",
            "marketsim.gen._out.order._Limit.Limit",
            "marketsim.gen._out.observable.EW._RelStdDev.RelStdDev",
            "marketsim.gen._out.observable.orderbook._Spread.Spread",
            "marketsim.gen._out.observable.Moving._Min.Min",
            "marketsim.gen._out._true.true",
            "marketsim.gen._out.observable.sidefunc._PairTrading.PairTrading",
            "marketsim.ops._all.Constant_Tag",
            "marketsim.gen._out.observable.orderbook._SafeSidePrice.SafeSidePrice",
            "marketsim.gen._out.order._Peg.Peg"
        ]
    ],
    [
        "marketsim.types.ITrader",
        [
            "marketsim.gen._out.trader._MultiAsset.MultiAsset",
            "marketsim.gen._out.trader._SingleProxy.SingleProxy",
            "marketsim.gen._out.trader._SingleAsset.SingleAsset"
        ]
    ],
    [
        "marketsim.types.IOrderQueue",
        [
            "marketsim.gen._out.observable.orderbook._Bids.Bids",
            "marketsim.gen._out.observable.orderbook._Queue.Queue",
            "marketsim.gen._out.observable.orderbook._Asks.Asks"
        ]
    ],
    [
        "marketsim.types.ISingleAssetTrader",
        [
            "marketsim.gen._out.trader._SingleProxy.SingleProxy",
            "marketsim.gen._out.trader._SingleAsset.SingleAsset"
        ]
    ],
    [
        {
            "rv": {
                "rv": "marketsim.types.IOrder",
                "args": [
                    "_parseFloat",
                    "_parseFloat"
                ]
            },
            "args": [
                "marketsim.Side"
            ]
        },
        [
            "marketsim.order.meta._with_expiry.WithExpiryFactory",
            "marketsim.order._limit.LimitFactory"
        ]
    ],
    [
        "marketsim.types.IFunction_IFunction_float_IFunction_float",
        [
            "marketsim.gen._out.strategy.weight._.f._f_IdentityF.f_IdentityF",
            "marketsim.gen._out.strategy.weight._.f._f_Clamp0.f_Clamp0",
            "marketsim.gen._out.strategy.weight._.f._f_AtanPow.f_AtanPow"
        ]
    ],
    [
        "marketsim.types.IFunction_IOrderGenerator_IFunction_float",
        [
            "marketsim.gen._out.order._curried._volume_Limit.volume_Limit",
            "marketsim.gen._out.order._curried._price_Iceberg.price_Iceberg",
            "marketsim.gen._out.order._curried._signedVolume_MarketSigned.signedVolume_MarketSigned",
            "marketsim.gen._out.order._curried._price_Limit.price_Limit",
            "marketsim.gen._out.order._curried._volume_Market.volume_Market"
        ]
    ],
    [
        "marketsim.Side",
        [
            "marketsim.side_._SellSide",
            "marketsim.side_._BuySide"
        ]
    ],
    [
        "marketsim.types.IOrderGenerator",
        [
            "marketsim.gen._out.order._ImmediateOrCancel.ImmediateOrCancel",
            "marketsim.gen._out.order._WithExpiry.WithExpiry",
            "marketsim.gen._out.order._MarketSigned.MarketSigned",
            "marketsim.gen._out.order._FloatingPrice.FloatingPrice",
            "marketsim.gen._out.order._Limit.Limit",
            "marketsim.gen._out.order._LimitSigned.LimitSigned",
            "marketsim.gen._out.order._FixedBudget.FixedBudget",
            "marketsim.gen._out.order._StopLoss.StopLoss",
            "marketsim.gen._out.order._Market.Market",
            "marketsim.gen._out.order._Peg.Peg",
            "marketsim.gen._out.order._Iceberg.Iceberg"
        ]
    ],
    [
        "marketsim.types.IDifferentiable",
        [
            "marketsim.gen._out.observable.Moving._Avg.Avg",
            "marketsim.gen._out.observable.EW._Avg.Avg",
            "marketsim.gen._out.observable.Cumulative._Avg.Avg"
        ]
    ],
    [
        "marketsim.types.IAccount",
        [
            "marketsim.gen._out.strategy.account._Real.Real",
            "marketsim.gen._out.trader._SingleAsset.SingleAsset",
            "marketsim.gen._out.trader._SingleProxy.SingleProxy",
            "marketsim.gen._out.strategy.account._VirtualMarket.VirtualMarket"
        ]
    ],
    [
        "marketsim.types.IFunction_IFunction_IOrderGenerator_IFunction_float_IFunction_Tag",
        [
            "marketsim.gen._out.order._curried._side_price_Iceberg.side_price_Iceberg",
            "marketsim.gen._out.order._curried._side_price_Limit.side_price_Limit"
        ]
    ],
    [
        {
            "elementType": "marketsim.types.ITimeSerie"
        },
        []
    ],
    [
        "marketsim.types.IFunction_bool",
        [
            "marketsim.gen._out._true.true",
            "marketsim.gen._out._false.false"
        ]
    ],
    [
        "_parseFloat",
        []
    ],
    [
        "marketsim.ILink",
        [
            "marketsim.gen._out.orderbook._Link.Link"
        ]
    ],
    [
        "marketsim.types.IObservable_object",
        [
            "marketsim.gen._out.observable._DownMovements.DownMovements",
            "marketsim.gen._out.observable.trader._RoughPnL.RoughPnL",
            "marketsim.gen._out.mathops._Sqrt.Sqrt",
            "marketsim.gen._out.observable.trader._PendingVolume.PendingVolume",
            "marketsim.gen._out.mathops._Atan.Atan",
            "marketsim.gen._out.observable.orderbook._AskLastTradePrice.AskLastTradePrice",
            "marketsim.gen._out.observable.orderbook._AskPrice.AskPrice",
            "marketsim.gen._out.observable.orderbook._LastTradeVolume.LastTradeVolume",
            "marketsim.gen._out.order._FixedBudget.FixedBudget",
            "marketsim.gen._out.observable._OnEveryDt.OnEveryDt",
            "marketsim.gen._out.observable.volumefunc._RSI_linear.RSI_linear",
            "marketsim.gen._out._const.const",
            "marketsim.gen._out.observable.volumefunc._DesiredPosition.DesiredPosition",
            "marketsim.gen._out.observable.orderbook._MidPrice.MidPrice",
            "marketsim.gen._out.observable._ObservableSide.ObservableSide",
            "marketsim.ops._arithmetic.Div",
            "marketsim.ops._all.Constant_float",
            "marketsim.gen._out.observable.trader._Balance.Balance",
            "marketsim.gen._out.observable._Sqr.Sqr",
            "marketsim.gen._out.observable.orderbook._CumulativePrice.CumulativePrice",
            "marketsim.gen._out.observable.orderbook._BidPrice.BidPrice",
            "marketsim.observable._computed.IndicatorBaseT_IVolumeLevels",
            "marketsim.gen._out.order._ImmediateOrCancel.ImmediateOrCancel",
            "marketsim.gen._out.observable._Observable.Observable",
            "marketsim.gen._out.order._WithExpiry.WithExpiry",
            "marketsim.gen._out._null.null",
            "marketsim.gen._out.observable._RSI.RSI",
            "marketsim.gen._out.observable.Cumulative._MaxEpsilon.MaxEpsilon",
            "marketsim.gen._out.observable.orderbook._AskLastPrice.AskLastPrice",
            "marketsim.gen._out.observable._UpMovements.UpMovements",
            "marketsim.gen._out.order._LimitSigned.LimitSigned",
            "marketsim.gen._out.observable.trader._Position.Position",
            "marketsim.gen._out.observable._BreaksAtChanges.BreaksAtChanges",
            "marketsim.gen._out.observable.orderbook._BestPrice.BestPrice",
            "marketsim.gen._out.observable._CandleSticks.CandleSticks",
            "marketsim.gen._out.observable.volumefunc._Bollinger_linear.Bollinger_linear",
            "marketsim.gen._out.order._Market.Market",
            "marketsim.gen._out.observable._Lagged.Lagged",
            "marketsim.gen._out.order._StopLoss.StopLoss",
            "marketsim.gen._out._IfDefined.IfDefined",
            "marketsim.gen._out.mathops._Log.Log",
            "marketsim.gen._out.observable.orderbook._LastPrice.LastPrice",
            "marketsim.gen._out.observable._ObservablePrice.ObservablePrice",
            "marketsim.gen._out.order._FloatingPrice.FloatingPrice",
            "marketsim.gen._out.observable.pricefunc._LiquidityProvider.LiquidityProvider",
            "marketsim.ops._arithmetic.Product",
            "marketsim.gen._out.observable.orderbook._LastTradePrice.LastTradePrice",
            "marketsim.gen._out.observable.Cumulative._MinEpsilon.MinEpsilon",
            "marketsim.gen._out.order._Iceberg.Iceberg",
            "marketsim.gen._out.order._MarketSigned.MarketSigned",
            "marketsim.gen._out.observable.orderbook._BidLastPrice.BidLastPrice",
            "marketsim.observable.fold._two_point.TwoPoint",
            "marketsim.gen._out.observable.trader._Efficiency.Efficiency",
            "marketsim.ops._arithmetic.Sum",
            "marketsim.gen._out.mathops._Pow.Pow",
            "marketsim.ops._arithmetic.Sub",
            "marketsim.gen._out.observable._Max.Max",
            "marketsim.gen._out.observable.orderbook._BidLastTradePrice.BidLastTradePrice",
            "marketsim.gen._out.observable.sidefunc._FundamentalValue.FundamentalValue",
            "marketsim.gen._out.observable.Moving._Max.Max",
            "marketsim.gen._out.observable.sidefunc._Signal.Signal",
            "marketsim.gen._out.observable._ObservableVolume.ObservableVolume",
            "marketsim.gen._out.observable._RandomWalk.RandomWalk",
            "marketsim.gen._out._false.false",
            "marketsim.gen._out.observable.orderbook._NaiveCumulativePrice.NaiveCumulativePrice",
            "marketsim.gen._out.mathops._Exp.Exp",
            "marketsim.gen._out.observable._Quote.Quote",
            "marketsim.gen._out.order._Limit.Limit",
            "marketsim.gen._out.observable.EW._RelStdDev.RelStdDev",
            "marketsim.gen._out.observable.orderbook._Spread.Spread",
            "marketsim.gen._out.observable.Moving._Min.Min",
            "marketsim.gen._out._true.true",
            "marketsim.gen._out.observable.sidefunc._PairTrading.PairTrading",
            "marketsim.ops._all.Constant_Tag",
            "marketsim.gen._out.observable.orderbook._SafeSidePrice.SafeSidePrice",
            "marketsim.gen._out.order._Peg.Peg"
        ]
    ],
    [
        "marketsim.types.IObservable_float",
        [
            "marketsim.gen._out.observable._DownMovements.DownMovements",
            "marketsim.gen._out.observable.trader._RoughPnL.RoughPnL",
            "marketsim.gen._out.mathops._Sqrt.Sqrt",
            "marketsim.gen._out.observable.trader._PendingVolume.PendingVolume",
            "marketsim.gen._out.mathops._Atan.Atan",
            "marketsim.gen._out.observable.orderbook._AskLastTradePrice.AskLastTradePrice",
            "marketsim.gen._out.observable.orderbook._AskPrice.AskPrice",
            "marketsim.gen._out.observable.orderbook._LastTradeVolume.LastTradeVolume",
            "marketsim.gen._out.observable._OnEveryDt.OnEveryDt",
            "marketsim.gen._out.observable.volumefunc._RSI_linear.RSI_linear",
            "marketsim.gen._out._const.const",
            "marketsim.gen._out.observable.volumefunc._DesiredPosition.DesiredPosition",
            "marketsim.gen._out.observable.orderbook._MidPrice.MidPrice",
            "marketsim.ops._arithmetic.Div",
            "marketsim.ops._all.Constant_float",
            "marketsim.gen._out.observable.trader._Balance.Balance",
            "marketsim.gen._out.observable._Sqr.Sqr",
            "marketsim.gen._out.observable.orderbook._CumulativePrice.CumulativePrice",
            "marketsim.gen._out.observable.orderbook._BidPrice.BidPrice",
            "marketsim.gen._out.observable._Observable.Observable",
            "marketsim.observable.fold._two_point.TwoPoint",
            "marketsim.gen._out.observable._RSI.RSI",
            "marketsim.gen._out.observable.orderbook._AskLastPrice.AskLastPrice",
            "marketsim.gen._out.observable._UpMovements.UpMovements",
            "marketsim.gen._out.observable.Cumulative._MaxEpsilon.MaxEpsilon",
            "marketsim.gen._out.observable.trader._Position.Position",
            "marketsim.gen._out.observable._BreaksAtChanges.BreaksAtChanges",
            "marketsim.gen._out.observable.orderbook._BestPrice.BestPrice",
            "marketsim.gen._out.observable.volumefunc._Bollinger_linear.Bollinger_linear",
            "marketsim.gen._out.observable._Lagged.Lagged",
            "marketsim.gen._out.mathops._Log.Log",
            "marketsim.gen._out.observable.orderbook._LastPrice.LastPrice",
            "marketsim.gen._out.observable.pricefunc._LiquidityProvider.LiquidityProvider",
            "marketsim.ops._arithmetic.Product",
            "marketsim.gen._out.observable.orderbook._LastTradePrice.LastTradePrice",
            "marketsim.gen._out.observable.Cumulative._MinEpsilon.MinEpsilon",
            "marketsim.gen._out._IfDefined.IfDefined",
            "marketsim.gen._out.observable.orderbook._BidLastPrice.BidLastPrice",
            "marketsim.gen._out.observable.orderbook._NaiveCumulativePrice.NaiveCumulativePrice",
            "marketsim.gen._out.observable.trader._Efficiency.Efficiency",
            "marketsim.ops._arithmetic.Sum",
            "marketsim.gen._out.mathops._Pow.Pow",
            "marketsim.ops._arithmetic.Sub",
            "marketsim.gen._out.observable._Max.Max",
            "marketsim.gen._out.observable.orderbook._BidLastTradePrice.BidLastTradePrice",
            "marketsim.gen._out.observable.Moving._Max.Max",
            "marketsim.gen._out.observable._ObservableVolume.ObservableVolume",
            "marketsim.gen._out.observable._RandomWalk.RandomWalk",
            "marketsim.gen._out.mathops._Exp.Exp",
            "marketsim.gen._out.observable._Quote.Quote",
            "marketsim.gen._out._null.null",
            "marketsim.gen._out.observable.EW._RelStdDev.RelStdDev",
            "marketsim.gen._out.observable.orderbook._Spread.Spread",
            "marketsim.gen._out.observable.Moving._Min.Min",
            "marketsim.gen._out.observable._ObservablePrice.ObservablePrice",
            "marketsim.gen._out.observable.orderbook._SafeSidePrice.SafeSidePrice"
        ]
    ],
    [
        "marketsim.types.IFunction_Tag",
        [
            "marketsim.gen._out.observable.sidefunc._Signal.Signal",
            "marketsim.gen._out.side._Nothing.Nothing",
            "marketsim.gen._out.observable._ObservableSide.ObservableSide",
            "marketsim.gen._out.observable.sidefunc._TrendFollower.TrendFollower",
            "marketsim.gen._out.observable.sidefunc._MeanReversion.MeanReversion",
            "marketsim.gen._out.observable.sidefunc._Noise.Noise",
            "marketsim.gen._out.observable.sidefunc._CrossingAverages.CrossingAverages",
            "marketsim.gen._out.side._Sell.Sell",
            "marketsim.gen._out.side._Buy.Buy",
            "marketsim.gen._out.observable.sidefunc._PairTrading.PairTrading",
            "marketsim.gen._out.observable.sidefunc._FundamentalValue.FundamentalValue",
            "marketsim.ops._all.Constant_Tag"
        ]
    ],
    [
        "marketsim.types.ISingleAssetStrategy",
        [
            "marketsim.gen._out.strategy._ChooseTheBest.ChooseTheBest",
            "marketsim.gen._out.strategy._CrossingAverages.CrossingAverages",
            "marketsim.gen._out.strategy._Noise.Noise",
            "marketsim.gen._out.strategy._PairTrading.PairTrading",
            "marketsim.gen._out.strategy._MarketMaker.MarketMaker",
            "marketsim.gen._out.strategy._MultiArmedBandit.MultiArmedBandit",
            "marketsim.gen._out.strategy._Generic.Generic",
            "marketsim.gen._out.strategy._LiquidityProviderSide.LiquidityProviderSide",
            "marketsim.gen._out.strategy._RSIbis.RSIbis",
            "marketsim.gen._out.strategy._MeanReversion.MeanReversion",
            "marketsim.gen._out.strategy._TrendFollower.TrendFollower",
            "marketsim.gen._out.strategy._Combine.Combine",
            "marketsim.gen._out.strategy._MarketData.MarketData",
            "marketsim.gen._out.strategy._Suspendable.Suspendable",
            "marketsim.strategy._basic.Empty",
            "marketsim.gen._out.strategy._TradeIfProfitable.TradeIfProfitable",
            "marketsim.gen._out.strategy._RSI_linear.RSI_linear",
            "marketsim.gen._out.strategy._Bollinger_linear.Bollinger_linear",
            "marketsim.gen._out.strategy._Canceller.Canceller",
            "marketsim.gen._out.strategy._Signal.Signal",
            "marketsim.gen._out.strategy._Array.Array",
            "marketsim.gen._intrinsic.strategy.basic.Empty",
            "marketsim.gen._out.strategy._LiquidityProvider.LiquidityProvider",
            "marketsim.gen._out.strategy._FundamentalValue.FundamentalValue"
        ]
    ],
    [
        "marketsim.types.IFunction_IOrderGenerator_IFunction_Tag_IFunction_float",
        [
            "marketsim.gen._out.order._curried._sideprice_WithExpiry.sideprice_WithExpiry",
            "marketsim.gen._out.order._curried._sideprice_Iceberg.sideprice_Iceberg",
            "marketsim.gen._out.order._curried._sideprice_StopLoss.sideprice_StopLoss",
            "marketsim.gen._out.order._curried._sideprice_Limit.sideprice_Limit"
        ]
    ],
    [
        "marketsim.types.IFunction_IVolumeLevels",
        [
            "marketsim.observable._computed.IndicatorBaseT_IVolumeLevels",
            "marketsim.gen._out.observable.orderbook._VolumeLevels.VolumeLevels"
        ]
    ],
    [
        "marketsim.types.IFunction_listOf_listOf",
        [
            "marketsim.gen._out.strategy.weight._.array._array_IdentityL.array_IdentityL",
            "marketsim.gen._out.strategy.weight._.array._array_ChooseTheBest.array_ChooseTheBest"
        ]
    ],
    [
        "marketsim.types.IFunction_IOrderGenerator_IFunction_Tag",
        [
            "marketsim.gen._out.order._curried._side_Market.side_Market",
            "marketsim.gen._out.order._curried._side_Iceberg.side_Iceberg",
            "marketsim.gen._out.order._curried._side_WithExpiry.side_WithExpiry",
            "marketsim.gen._out.order._curried._side_StopLoss.side_StopLoss",
            "marketsim.gen._out.order._curried._side_Limit.side_Limit",
            "marketsim.gen._out.order._curried._side_Peg.side_Peg",
            "marketsim.gen._out.order._curried._side_FloatingPrice.side_FloatingPrice",
            "marketsim.gen._out.order._curried._side_ImmediateOrCancel.side_ImmediateOrCancel",
            "marketsim.gen._out.order._curried._side_FixedBudget.side_FixedBudget"
        ]
    ],
    [
        "marketsim.types.IFunction_float",
        [
            "marketsim.gen._out.observable.volumefunc._DesiredPosition.DesiredPosition",
            "marketsim.gen._out._Derivative.Derivative",
            "marketsim.gen._out.observable._OnEveryDt.OnEveryDt",
            "marketsim.gen._out.observable.trader._Balance.Balance",
            "marketsim.gen._out.observable.orderbook._WeightedPrice.WeightedPrice",
            "marketsim.gen._out.mathutils.rnd._vonmisesvariate.vonmisesvariate",
            "marketsim.gen._out.observable._RandomWalk.RandomWalk",
            "marketsim.gen._out.observable.Cumulative._Avg.Avg",
            "marketsim.gen._out.observable._RSI.RSI",
            "marketsim.gen._out.observable.trader._Position.Position",
            "marketsim.gen._out.mathutils.rnd._betavariate.betavariate",
            "marketsim.observable.fold._last.Last",
            "marketsim.gen._out.observable.orderbook._BestPrice.BestPrice",
            "marketsim.gen._out.observable.Cumulative._MinEpsilon.MinEpsilon",
            "marketsim.gen._out.observable.orderbook._TickSize.TickSize",
            "marketsim.gen._out._IfDefined.IfDefined",
            "marketsim.gen._out.observable._ObservablePrice.ObservablePrice",
            "marketsim.gen._out.mathops._Pow.Pow",
            "marketsim.ops._arithmetic.Sub",
            "marketsim.gen._out.observable.rsi._Raw.Raw",
            "marketsim.observable.fold._two_point.TwoPoint",
            "marketsim.gen._out.mathutils.rnd._normalvariate.normalvariate",
            "marketsim.gen._out.observable.orderbook._Spread.Spread",
            "marketsim.gen._out._constant.constant",
            "marketsim.gen._out.observable.macd._Signal.Signal",
            "marketsim.gen._out.mathutils.rnd._expovariate.expovariate",
            "marketsim.gen._out.observable.orderbook._SafeSidePrice.SafeSidePrice",
            "marketsim.ops._arithmetic.Div",
            "marketsim.gen._out.strategy.weight._EfficiencyTrend.EfficiencyTrend",
            "marketsim.gen._out.observable.volumefunc._Bollinger_linear.Bollinger_linear",
            "marketsim.gen._out._const.const",
            "marketsim.gen._out.observable.orderbook._MidPrice.MidPrice",
            "marketsim.gen._out.observable.Moving._Max.Max",
            "marketsim.gen._out.observable._Sqr.Sqr",
            "marketsim.gen._out.observable.orderbook._BidPrice.BidPrice",
            "marketsim.gen._out.observable.orderbook._AskLastPrice.AskLastPrice",
            "marketsim.gen._out.observable.volumefunc._RSI_linear.RSI_linear",
            "marketsim.gen._out.observable._Lagged.Lagged",
            "marketsim.gen._out.observable.orderbook._AskWeightedPrice.AskWeightedPrice",
            "marketsim.gen._out.observable.pricefunc._LiquidityProvider.LiquidityProvider",
            "marketsim.gen._out.observable.macd._MACD.MACD",
            "marketsim.gen._out.observable.orderbook._LastTradePrice.LastTradePrice",
            "marketsim.gen._out.observable.EW._Var.Var",
            "marketsim.gen._out.observable.orderbook._BidLastPrice.BidLastPrice",
            "marketsim.gen._out.mathutils.rnd._paretovariate.paretovariate",
            "marketsim.gen._out.observable.Moving._Min.Min",
            "marketsim.gen._out.observable.Moving._Avg.Avg",
            "marketsim.gen._out.observable.Cumulative._Var.Var",
            "marketsim.gen._out.observable._DownMovements.DownMovements",
            "marketsim.gen._out.observable.EW._StdDev.StdDev",
            "marketsim.gen._out.observable.trader._RoughPnL.RoughPnL",
            "marketsim.gen._out.observable.trader._PendingVolume.PendingVolume",
            "marketsim.gen._out.mathops._Atan.Atan",
            "marketsim.gen._out.observable.orderbook._LastTradeVolume.LastTradeVolume",
            "marketsim.gen._out.observable.orderbook._BidWeightedPrice.BidWeightedPrice",
            "marketsim.gen._out.observable._UpMovements.UpMovements",
            "marketsim.gen._out.observable.Moving._Var.Var",
            "marketsim.gen._out.observable.macd._Histogram.Histogram",
            "marketsim.gen._out.observable.Cumulative._MaxEpsilon.MaxEpsilon",
            "marketsim.gen._out.observable._BreaksAtChanges.BreaksAtChanges",
            "marketsim.gen._out.observable._Max.Max",
            "marketsim.gen._out.observable.orderbook._BidLastTradePrice.BidLastTradePrice",
            "marketsim.gen._out.mathops._Exp.Exp",
            "marketsim.gen._out.observable._Quote.Quote",
            "marketsim.gen._out.observable.EW._RelStdDev.RelStdDev",
            "marketsim.gen._out.observable.Moving._StdDev.StdDev",
            "marketsim.gen._out.mathops._Sqrt.Sqrt",
            "marketsim.gen._out.observable.orderbook._AskLastTradePrice.AskLastTradePrice",
            "marketsim.gen._out.observable.orderbook._AskPrice.AskPrice",
            "marketsim.gen._out.mathutils.rnd._lognormvariate.lognormvariate",
            "marketsim.gen._out.observable.orderbook._CumulativePrice.CumulativePrice",
            "marketsim.gen._out.observable._Observable.Observable",
            "marketsim.ops._all.negate",
            "marketsim.gen._out.mathutils.rnd._uniform.uniform",
            "marketsim.gen._out.strategy.weight._AtanPow.AtanPow",
            "marketsim.gen._out.observable.EW._Avg.Avg",
            "marketsim.gen._out.mathops._Log.Log",
            "marketsim.gen._out.mathutils.rnd._triangular.triangular",
            "marketsim.ops._arithmetic.Product",
            "marketsim.gen._out.mathutils.rnd._gammavariate.gammavariate",
            "marketsim.gen._out.observable.orderbook._NaiveCumulativePrice.NaiveCumulativePrice",
            "marketsim.gen._out.observable.trader._Efficiency.Efficiency",
            "marketsim.ops._all.Constant_float",
            "marketsim.gen._out.observable._ObservableVolume.ObservableVolume",
            "marketsim.gen._out.mathutils.rnd._weibullvariate.weibullvariate",
            "marketsim.gen._out._null.null",
            "marketsim.gen._out.observable.orderbook._LastPrice.LastPrice",
            "marketsim.ops._arithmetic.Sum",
            "marketsim.gen._out.observable.Cumulative._StdDev.StdDev"
        ]
    ],
    [
        "marketsim.ITwoWayLink",
        [
            "marketsim.gen._out.orderbook._TwoWayLink.TwoWayLink"
        ]
    ],
    [
        {
            "elementType": "marketsim.types.IOrderBook"
        },
        []
    ],
    [
        "marketsim.types.IFunction_IAccount_ISingleAssetStrategy",
        [
            "marketsim.gen._out.strategy.account._.inner._inner_VirtualMarket.inner_VirtualMarket",
            "marketsim.gen._out.strategy.account._.inner._inner_Real.inner_Real"
        ]
    ],
    [
        "marketsim.types.IGraph",
        [
            "marketsim.js.Graph",
            "marketsim.gen._out.veusz._Graph.Graph"
        ]
    ],
    [
        {
            "elementType": "marketsim.types.IGraph"
        },
        []
    ],
    [
        {
            "rv": "_parseFloat",
            "args": []
        },
        [
            "marketsim.gen._out.observable.volumefunc._DesiredPosition.DesiredPosition",
            "marketsim.gen._out._Derivative.Derivative",
            "marketsim.gen._out.observable._OnEveryDt.OnEveryDt",
            "marketsim.gen._out.observable.trader._Balance.Balance",
            "marketsim.gen._out.observable.orderbook._WeightedPrice.WeightedPrice",
            "marketsim.gen._out.mathutils.rnd._vonmisesvariate.vonmisesvariate",
            "marketsim.gen._out.observable._RandomWalk.RandomWalk",
            "marketsim.gen._out.observable.Cumulative._Avg.Avg",
            "marketsim.gen._out.observable._RSI.RSI",
            "marketsim.gen._out.observable.trader._Position.Position",
            "marketsim.gen._out.mathutils.rnd._betavariate.betavariate",
            "marketsim.observable.fold._last.Last",
            "marketsim.gen._out.observable.orderbook._BestPrice.BestPrice",
            "marketsim.gen._out.observable.Cumulative._MinEpsilon.MinEpsilon",
            "marketsim.gen._out.observable.orderbook._TickSize.TickSize",
            "marketsim.gen._out._IfDefined.IfDefined",
            "marketsim.gen._out.observable._ObservablePrice.ObservablePrice",
            "marketsim.gen._out.mathops._Pow.Pow",
            "marketsim.ops._arithmetic.Sub",
            "marketsim.gen._out.observable.rsi._Raw.Raw",
            "marketsim.observable.fold._two_point.TwoPoint",
            "marketsim.gen._out.mathutils.rnd._normalvariate.normalvariate",
            "marketsim.gen._out.observable.orderbook._Spread.Spread",
            "marketsim.gen._out._constant.constant",
            "marketsim.gen._out.observable.macd._Signal.Signal",
            "marketsim.gen._out.mathutils.rnd._expovariate.expovariate",
            "marketsim.gen._out.observable.orderbook._SafeSidePrice.SafeSidePrice",
            "marketsim.ops._arithmetic.Div",
            "marketsim.gen._out.strategy.weight._EfficiencyTrend.EfficiencyTrend",
            "marketsim.gen._out.observable.volumefunc._Bollinger_linear.Bollinger_linear",
            "marketsim.gen._out._const.const",
            "marketsim.gen._out.observable.orderbook._MidPrice.MidPrice",
            "marketsim.gen._out.observable.Moving._Max.Max",
            "marketsim.gen._out.observable._Sqr.Sqr",
            "marketsim.gen._out.observable.orderbook._BidPrice.BidPrice",
            "marketsim.gen._out.observable.orderbook._AskLastPrice.AskLastPrice",
            "marketsim.gen._out.observable.volumefunc._RSI_linear.RSI_linear",
            "marketsim.gen._out.observable._Lagged.Lagged",
            "marketsim.gen._out.observable.orderbook._AskWeightedPrice.AskWeightedPrice",
            "marketsim.gen._out.observable.pricefunc._LiquidityProvider.LiquidityProvider",
            "marketsim.gen._out.observable.macd._MACD.MACD",
            "marketsim.gen._out.observable.orderbook._LastTradePrice.LastTradePrice",
            "marketsim.gen._out.observable.EW._Var.Var",
            "marketsim.gen._out.observable.orderbook._BidLastPrice.BidLastPrice",
            "marketsim.gen._out.mathutils.rnd._paretovariate.paretovariate",
            "marketsim.gen._out.observable.Moving._Min.Min",
            "marketsim.gen._out.observable.Moving._Avg.Avg",
            "marketsim.gen._out.observable.Cumulative._Var.Var",
            "marketsim.gen._out.observable._DownMovements.DownMovements",
            "marketsim.gen._out.observable.EW._StdDev.StdDev",
            "marketsim.gen._out.observable.trader._RoughPnL.RoughPnL",
            "marketsim.gen._out.observable.trader._PendingVolume.PendingVolume",
            "marketsim.gen._out.mathops._Atan.Atan",
            "marketsim.gen._out.observable.orderbook._LastTradeVolume.LastTradeVolume",
            "marketsim.gen._out.observable.orderbook._BidWeightedPrice.BidWeightedPrice",
            "marketsim.gen._out.observable._UpMovements.UpMovements",
            "marketsim.gen._out.observable.Moving._Var.Var",
            "marketsim.gen._out.observable.macd._Histogram.Histogram",
            "marketsim.gen._out.observable.Cumulative._MaxEpsilon.MaxEpsilon",
            "marketsim.gen._out.observable._BreaksAtChanges.BreaksAtChanges",
            "marketsim.gen._out.observable._Max.Max",
            "marketsim.gen._out.observable.orderbook._BidLastTradePrice.BidLastTradePrice",
            "marketsim.gen._out.mathops._Exp.Exp",
            "marketsim.gen._out.observable._Quote.Quote",
            "marketsim.gen._out.observable.EW._RelStdDev.RelStdDev",
            "marketsim.gen._out.observable.Moving._StdDev.StdDev",
            "marketsim.gen._out.mathops._Sqrt.Sqrt",
            "marketsim.gen._out.observable.orderbook._AskLastTradePrice.AskLastTradePrice",
            "marketsim.gen._out.observable.orderbook._AskPrice.AskPrice",
            "marketsim.gen._out.mathutils.rnd._lognormvariate.lognormvariate",
            "marketsim.gen._out.observable.orderbook._CumulativePrice.CumulativePrice",
            "marketsim.gen._out.observable._Observable.Observable",
            "marketsim.ops._all.negate",
            "marketsim.gen._out.mathutils.rnd._uniform.uniform",
            "marketsim.gen._out.strategy.weight._AtanPow.AtanPow",
            "marketsim.gen._out.observable.EW._Avg.Avg",
            "marketsim.gen._out.mathops._Log.Log",
            "marketsim.gen._out.mathutils.rnd._triangular.triangular",
            "marketsim.ops._arithmetic.Product",
            "marketsim.gen._out.mathutils.rnd._gammavariate.gammavariate",
            "marketsim.gen._out.observable.orderbook._NaiveCumulativePrice.NaiveCumulativePrice",
            "marketsim.gen._out.observable.trader._Efficiency.Efficiency",
            "marketsim.ops._all.Constant_float",
            "marketsim.gen._out.observable._ObservableVolume.ObservableVolume",
            "marketsim.gen._out.mathutils.rnd._weibullvariate.weibullvariate",
            "marketsim.gen._out._null.null",
            "marketsim.gen._out.observable.orderbook._LastPrice.LastPrice",
            "marketsim.ops._arithmetic.Sum",
            "marketsim.gen._out.observable.Cumulative._StdDev.StdDev"
        ]
    ],
    [
        {
            "elementType": "marketsim.types.ISingleAssetTrader"
        },
        []
    ],
    [
        "marketsim.types.IMultiAssetStrategy",
        [
            "marketsim.gen._out.strategy._Arbitrage.Arbitrage"
        ]
    ],
    [
        "identity",
        []
    ],
    [
        "marketsim.types.IOrderBook",
        [
            "marketsim.orderbook._proxy.Proxy",
            "marketsim.gen._out.orderbook._Remote.Remote",
            "marketsim.gen._out.observable.orderbook._OfTrader.OfTrader",
            "marketsim.gen._out.orderbook._Local.Local"
        ]
    ],
    [
        {
            "elementType": "marketsim.types.ITrader"
        },
        []
    ]
]