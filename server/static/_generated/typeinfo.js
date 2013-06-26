var typeinfo = {
    "marketsim.observable._momentum._rsi_label": {
        "castsTo": [
            "marketsim.mathutils._ops.identity",
            "marketsim.mathutils._ops.FloatFunction",
            "marketsim.types.IFloatFunction",
            "marketsim.types.IScalarFunction",
            "marketsim.observable._momentum._rsi_label",
            {
                "rv": "_parseFloat",
                "args": []
            }
        ],
        "properties": {
            "arg": {
                "hidden": false,
                "type": "marketsim.types.IFloatFunction",
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.order._cancel.WithExpiryFactory": {
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
                    "marketsim.Side.Tag"
                ]
            },
            "marketsim.order._cancel.WithExpiryFactory"
        ],
        "properties": {
            "expirationDistr": {
                "hidden": false,
                "type": {
                    "rv": "_parseFloat",
                    "args": []
                },
                "collapsed": false
            },
            "orderFactory": {
                "hidden": false,
                "type": {
                    "rv": {
                        "rv": "marketsim.types.IOrder",
                        "args": [
                            "_parseFloat",
                            "_parseFloat"
                        ]
                    },
                    "args": [
                        "marketsim.Side.Tag"
                    ]
                },
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n<p>Limit-like order which is cancelled after given <em>delay</em></p>\n</div>\n"
    },
    "marketsim.trader._proxy.SingleProxy": {
        "castsTo": [
            "marketsim.trader._proxy.Base",
            "marketsim.trader._proxy.SingleProxyBase",
            "marketsim.types.ISingleAssetTrader",
            "marketsim.types.ITrader",
            "marketsim.trader._proxy.SingleProxy"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.observable._orderbook.bid_price": {
        "castsTo": [
            "marketsim.mathutils._ops.FloatFunction",
            "marketsim.observable._orderbook.bid_price",
            "marketsim.types.IFloatFunction",
            "marketsim.types.IScalarFunction",
            "marketsim.observable._orderbook.side_price",
            {
                "rv": "_parseFloat",
                "args": []
            }
        ],
        "properties": {
            "orderbook": {
                "hidden": false,
                "type": "marketsim.types.IOrderBook",
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.strategy.TrendFollower": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy",
            "marketsim.types.IStrategy",
            "marketsim.strategy._basic.Strategy",
            "marketsim.strategy._basic.Base",
            "marketsim.strategy._trend.TrendFollower",
            "marketsim.strategy._trend._TrendFollower_Impl",
            "marketsim.strategy._signal.SignalBase",
            "marketsim.strategy._two_sides.TwoSides"
        ],
        "properties": {
            "threshold": {
                "hidden": false,
                "type": "combine(greater_or_equal(0.0), _parseFloat)",
                "collapsed": false
            },
            "average": {
                "hidden": false,
                "type": "marketsim.types.IUpdatableValue",
                "collapsed": false
            },
            "creationIntervalDistr": {
                "hidden": false,
                "type": {
                    "rv": "_parseFloat",
                    "args": []
                },
                "collapsed": false
            },
            "orderFactory": {
                "hidden": false,
                "type": {
                    "rv": {
                        "rv": "marketsim.types.IOrder",
                        "args": [
                            "_parseFloat"
                        ]
                    },
                    "args": [
                        "marketsim.Side.Tag"
                    ]
                },
                "collapsed": false
            },
            "volumeDistr": {
                "hidden": false,
                "type": {
                    "rv": "_parseFloat",
                    "args": []
                },
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n<p>Trend follower can be considered as a sort of a signal strategy\nwhere the <em>signal</em> is a trend of the asset.\nUnder trend we understand the first derivative of some moving average of asset prices.\nIf the derivative is positive, the trader buys; if negative - it sells.\nSince moving average is a continuously changing signal, we check its\nderivative at random moments of time given by <em>creationIntervalDistr</em>.</p>\n<p>It has following parameters:</p>\n<dl class=\"docutils\">\n<dt><strong>Average</strong></dt>\n<dd>moving average functional. By default, we use exponentially weighted\nmoving average with \u03b1 = 0.15.</dd>\n<dt><strong>Order factory</strong></dt>\n<dd>order factory function (default: order.Market.T)</dd>\n<dt><strong>Threshold</strong></dt>\n<dd>threshold when the trader starts to act (default: 0.)</dd>\n<dt><strong>Time intervals between two order creations</strong></dt>\n<dd>defines intervals of time between order creation\n(default: exponential distribution with \u03bb = 1)</dd>\n<dt><strong>Volume of orders to create</strong></dt>\n<dd>defines volumes of orders to create\n(default: exponential distribution with \u03bb = 1)</dd>\n</dl>\n</div>\n"
    },
    "marketsim.observable._momentum.TwoPointFold": {
        "castsTo": [
            "marketsim.event.IEvent",
            "marketsim.observable._momentum.TwoPointFold",
            "marketsim.types.Observable",
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IObservable",
            "marketsim.event.Conditional",
            "marketsim.event.Event"
        ],
        "properties": {
            "folder": {
                "hidden": false,
                "type": {
                    "rv": "_parseFloat",
                    "args": [
                        "_parseFloat",
                        "_parseFloat"
                    ]
                },
                "collapsed": false
            },
            "eventSource": {
                "hidden": false,
                "type": "marketsim.event.Event",
                "collapsed": false
            },
            "dataSource": {
                "hidden": false,
                "type": "marketsim.types.IFloatFunction",
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.mathutils.rnd.lognormvariate": {
        "castsTo": [
            "marketsim.mathutils.rnd.lognormvariate",
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IScalarFunction",
            "marketsim.types.IFloatFunction",
            "marketsim.mathutils._ops.FloatFunction"
        ],
        "properties": {
            "Mu": {
                "hidden": false,
                "type": "_parseFloat",
                "collapsed": false
            },
            "Sigma": {
                "hidden": false,
                "type": "combine(greater(0.0), _parseFloat)",
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n<p>Log normal distribution. If you take the natural logarithm of this distribution, you'll get a normal distribution with mean \u03bc and standard deviation \u03c3. \u03bc can have any value, and \u03c3 must be greater than zero.</p>\n</div>\n"
    },
    "marketsim.strategy.weight.TrackRecord": {
        "castsTo": [
            "marketsim.strategy.weight.TrackRecord",
            "marketsim.strategy.weight.Efficiency",
            "marketsim.strategy.weight.Base"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.trader._ma.MultiAsset": {
        "castsTo": [
            "marketsim.trader._base.Base",
            "marketsim.timeserie.Holder",
            "marketsim.trader._ma.MultiAsset",
            "marketsim.types.ITrader"
        ],
        "properties": {
            "traders": {
                "hidden": false,
                "type": {
                    "elementType": "marketsim.types.ISingleAssetTrader"
                },
                "collapsed": false
            },
            "PnL": {
                "hidden": false,
                "type": "_parseFloat",
                "collapsed": false
            },
            "timeseries": {
                "hidden": false,
                "type": {
                    "elementType": "marketsim.timeserie.ToRecord"
                },
                "collapsed": true
            },
            "strategy": {
                "hidden": false,
                "type": "marketsim.types.IMultiAssetStrategy",
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.timeserie.VolumeLevels": {
        "castsTo": [
            "marketsim.timeserie.VolumeLevels",
            "marketsim.types.ITimeSerie",
            "marketsim.timeserie.ToRecord"
        ],
        "properties": {
            "graph": {
                "hidden": false,
                "type": "marketsim.types.IGraph",
                "collapsed": false
            },
            "_digits": {
                "hidden": true,
                "type": "_parseInt",
                "collapsed": false
            },
            "source": {
                "hidden": false,
                "type": "marketsim.types.IObservable",
                "collapsed": false
            },
            "_isBuy": {
                "hidden": true,
                "type": "_parseInt",
                "collapsed": false
            },
            "_volumes": {
                "hidden": true,
                "type": {
                    "elementType": "_parseFloat"
                },
                "collapsed": false
            },
            "_smooth": {
                "hidden": true,
                "type": "_parseInt",
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.strategy._signal.none_side": {
        "castsTo": [
            {
                "rv": "marketsim.Side.Tag",
                "args": []
            },
            "marketsim.strategy._signal.none_side"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.strategy.TradeIfProfitable": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy",
            "marketsim.types.IStrategy",
            "marketsim.strategy._trade_if_profitable.TradeIfProfitable",
            "marketsim.strategy._basic.Strategy",
            "marketsim.strategy._basic.Base",
            "marketsim.strategy._trade_if_profitable.tradeIfProfitable",
            "marketsim.strategy._trade_if_profitable._tradeIfProfitable_Impl"
        ],
        "properties": {
            "efficiency": {
                "hidden": false,
                "type": {
                    "rv": "marketsim.types.ISingleAssetTrader",
                    "args": [
                        "marketsim.types.ISingleAssetTrader"
                    ]
                },
                "collapsed": false
            },
            "estimator": {
                "hidden": false,
                "type": {
                    "rv": "marketsim.types.ISingleAssetStrategy",
                    "args": [
                        "marketsim.types.ISingleAssetStrategy"
                    ]
                },
                "collapsed": false
            },
            "strategy": {
                "hidden": false,
                "type": "marketsim.types.ISingleAssetStrategy",
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n<p>Strategy that estimates efficiency of original <em>strategy</em>\n(normally as derivative of &quot;cleared&quot; balance for its clone sending unit volume orders)</p>\n<p>Parameters:</p>\n<blockquote>\n<dl class=\"docutils\">\n<dt><strong>strategy</strong></dt>\n<dd>original strategy that can be suspended</dd>\n<dt><strong>Efficiency evaluation function</strong></dt>\n<dd>function estimating is the strategy efficient or not</dd>\n<dt><strong>Function creating a strategy used to estimate the original one</strong></dt>\n<dd>function creating phantom strategy used for efficiency estimation</dd>\n</dl>\n</blockquote>\n</div>\n"
    },
    "marketsim.strategy.ChooseTheBest": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy",
            "marketsim.types.IStrategy",
            "marketsim.strategy._choose_best.ChooseTheBest",
            "marketsim.strategy._choose_best._ChooseTheBest_Impl",
            "marketsim.strategy._basic.Strategy",
            "marketsim.strategy._basic.Base"
        ],
        "properties": {
            "strategies": {
                "hidden": false,
                "type": {
                    "elementType": "marketsim.types.ISingleAssetStrategy"
                },
                "collapsed": false
            },
            "estimator": {
                "hidden": false,
                "type": {
                    "rv": "marketsim.types.ISingleAssetStrategy",
                    "args": [
                        "marketsim.types.ISingleAssetStrategy"
                    ]
                },
                "collapsed": false
            },
            "efficiency": {
                "hidden": false,
                "type": {
                    "rv": "marketsim.types.ISingleAssetTrader",
                    "args": [
                        "marketsim.types.ISingleAssetTrader"
                    ]
                },
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n<p>A composite strategy initialized with an array of strategies.\nIn some moments of time the most effective strategy\nis chosen and made running; other strategies are suspended.</p>\n<p>Parameters:</p>\n<blockquote>\n<dl class=\"docutils\">\n<dt><strong>strategies</strong></dt>\n<dd>original strategies that can be suspended</dd>\n<dt><strong>Efficiency evaluation function</strong></dt>\n<dd>function estimating is the strategy efficient or not</dd>\n<dt><strong>Function creating a strategy used to estimate the original one</strong></dt>\n<dd>function creating phantom strategy used for efficiency estimation</dd>\n</dl>\n</blockquote>\n</div>\n"
    },
    "marketsim.order._limit.AdaptLimit": {
        "castsTo": [
            "marketsim.order._limit.AdaptLimit",
            {
                "rv": {
                    "rv": "marketsim.types.IOrder",
                    "args": [
                        "_parseFloat"
                    ]
                },
                "args": [
                    "marketsim.Side.Tag"
                ]
            }
        ],
        "properties": {
            "priceFunc": {
                "hidden": false,
                "type": {
                    "rv": "_parseFloat",
                    "args": []
                },
                "collapsed": false
            },
            "orderFactory": {
                "hidden": false,
                "type": {
                    "rv": {
                        "rv": "marketsim.types.IOrder",
                        "args": [
                            "_parseFloat",
                            "_parseFloat"
                        ]
                    },
                    "args": [
                        "marketsim.Side.Tag"
                    ]
                },
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n<p>Adapts limit-like orders for usage where market-like orders are expected.\nUser should provide <em>priceFunc</em> calculating price of order to create</p>\n</div>\n"
    },
    "marketsim.observable._trader.OnTraded": {
        "castsTo": [
            "marketsim.event.IEvent",
            "marketsim.observable._trader.OnTraded",
            "marketsim.event.Event"
        ],
        "properties": {
            "trader": {
                "hidden": false,
                "type": "marketsim.types.ITrader",
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n<p>Multicast event that is fired once a trade is done by <em>trader</em></p>\n</div>\n"
    },
    "marketsim.observable._trader.volume_traded": {
        "castsTo": [
            "marketsim.observable._trader.volume_traded",
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IScalarFunction",
            "marketsim.types.IFloatFunction",
            "marketsim.mathutils._ops.FloatFunction"
        ],
        "properties": {
            "trader": {
                "hidden": false,
                "type": "marketsim.types.ISingleAssetTrader",
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n<p>Returns trader's position (i.e. number of assets traded)</p>\n</div>\n"
    },
    "marketsim.trader._proxy.MultiProxy": {
        "castsTo": [
            "marketsim.trader._proxy.MultiProxy",
            "marketsim.trader._proxy.Base",
            "marketsim.types.ITrader"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.mathutils.rnd.paretovariate": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IScalarFunction",
            "marketsim.types.IFloatFunction",
            "marketsim.mathutils._ops.FloatFunction",
            "marketsim.mathutils.rnd.paretovariate"
        ],
        "properties": {
            "Alpha": {
                "hidden": false,
                "type": "combine(greater(0.0), _parseFloat)",
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n<p>Pareto distribution. \u03b1 is the shape parameter.</p>\n</div>\n"
    },
    "marketsim.strategy.LiquidityProviderSide": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy",
            "marketsim.types.IStrategy",
            "marketsim.strategy._lp_side.LiquidityProviderSide",
            "marketsim.strategy._lp_side._LiquidityProviderSide_Impl",
            "marketsim.strategy._one_side.OneSide",
            "marketsim.strategy._basic.Strategy",
            "marketsim.strategy._basic.Base"
        ],
        "properties": {
            "priceDistr": {
                "hidden": false,
                "type": {
                    "rv": "_parseFloat",
                    "args": []
                },
                "collapsed": false
            },
            "defaultValue": {
                "hidden": false,
                "type": "_parseFloat",
                "collapsed": false
            },
            "orderFactoryT": {
                "hidden": false,
                "type": {
                    "rv": {
                        "rv": "marketsim.types.IOrder",
                        "args": [
                            "_parseFloat",
                            "_parseFloat"
                        ]
                    },
                    "args": [
                        "marketsim.Side.Tag"
                    ]
                },
                "collapsed": false
            },
            "creationIntervalDistr": {
                "hidden": false,
                "type": {
                    "rv": "_parseFloat",
                    "args": []
                },
                "collapsed": false
            },
            "volumeDistr": {
                "hidden": false,
                "type": {
                    "rv": "_parseFloat",
                    "args": []
                },
                "collapsed": false
            },
            "side": {
                "hidden": false,
                "type": "marketsim.Side.Tag",
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n<p>Liquidity provider for one side has followng parameters:</p>\n<dl class=\"docutils\">\n<dt><strong>Side</strong></dt>\n<dd>side of orders to create (default: Side.Sell)</dd>\n<dt><strong>Order factory</strong></dt>\n<dd>order factory function (default: order.Limit.T)</dd>\n<dt><strong>Initial value</strong></dt>\n<dd>initial price which is taken if orderBook is empty (default: 100)</dd>\n<dt><strong>Time intervals between two order creations</strong></dt>\n<dd>defines intervals of time between order creation\n(default: exponential distribution with \u03bb = 1)</dd>\n<dt><strong>Price of orders to create as multiplier to the current price</strong></dt>\n<dd>defines multipliers for current asset price when price of\norder to create is calculated (default: log normal distribution with\n\u03bc = 0 and \u03c3 = 0.1)</dd>\n<dt><strong>Volume of orders to create</strong></dt>\n<dd>defines volumes of orders to create\n(default: exponential distribution with \u03bb = 1)</dd>\n</dl>\n<p>It wakes up in moments of time given by <em>creationIntervalDistr</em>, checks\nthe last best price of orders in the corresponding queue, takes <em>initialValue</em>\nif it is empty, multiplies it by a value taken from <em>priceDistr</em> to obtain price\nof the order to create, calculates order volume using <em>volumeDistr</em>, creates\nan order via <em>orderFactoryT(side)</em> and tells the trader to send it.</p>\n</div>\n"
    },
    "marketsim.strategy.Dependency": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy",
            "marketsim.types.IStrategy",
            "marketsim.strategy._fv.FundamentalValueBase",
            "marketsim.strategy._basic.Strategy",
            "marketsim.strategy._basic.Base",
            "marketsim.strategy._dependency.Dependency",
            "marketsim.strategy._dependency._Dependency_Impl",
            "marketsim.strategy._signal.SignalBase",
            "marketsim.strategy._two_sides.TwoSides"
        ],
        "properties": {
            "volumeDistr": {
                "hidden": false,
                "type": {
                    "rv": "_parseFloat",
                    "args": []
                },
                "collapsed": false
            },
            "bookToDependOn": {
                "hidden": false,
                "type": "marketsim.types.IOrderBook",
                "collapsed": false
            },
            "orderFactory": {
                "hidden": false,
                "type": {
                    "rv": {
                        "rv": "marketsim.types.IOrder",
                        "args": [
                            "_parseFloat"
                        ]
                    },
                    "args": [
                        "marketsim.Side.Tag"
                    ]
                },
                "collapsed": false
            },
            "factor": {
                "hidden": false,
                "type": "combine(greater(0.0), _parseFloat)",
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n<p>Dependent price strategy believes that the fair price of an asset <em>A</em>\nis completely correlated with price of another asset <em>B</em> and the following relation\nshould be held: <em>PriceA</em> = <em>kPriceB</em>, where <em>k</em> is some factor.\nIt may be considered as a variety of a fundamental value strategy\nwith the exception that it is invoked every the time price of another\nasset <em>B</em> changes.</p>\n<p>It has following parameters:</p>\n<dl class=\"docutils\">\n<dt><strong>Order factory</strong></dt>\n<dd>order factory function (default: order.Market.T)</dd>\n<dt><strong>Asset to depend on</strong></dt>\n<dd>reference to order book for another asset used to evaluate fair price of our asset</dd>\n<dt><strong>Factor</strong></dt>\n<dd>multiplier to obtain fair asset price from the reference asset price</dd>\n<dt><strong>Volume of orders to create</strong></dt>\n<dd>defines volumes of orders to create\n(default: exponential distribution with \u03bb = 1)</dd>\n</dl>\n</div>\n"
    },
    "marketsim.strategy.LiquidityProvider": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy",
            "marketsim.types.IStrategy",
            "marketsim.strategy._lp._LiquidityProvider_Impl",
            "marketsim.strategy._lp.LiquidityProvider",
            "marketsim.strategy._basic.Strategy",
            "marketsim.strategy._basic.Base"
        ],
        "properties": {
            "priceDistr": {
                "hidden": false,
                "type": {
                    "rv": "_parseFloat",
                    "args": []
                },
                "collapsed": false
            },
            "defaultValue": {
                "hidden": false,
                "type": "_parseFloat",
                "collapsed": false
            },
            "creationIntervalDistr": {
                "hidden": false,
                "type": {
                    "rv": "_parseFloat",
                    "args": []
                },
                "collapsed": false
            },
            "orderFactoryT": {
                "hidden": false,
                "type": {
                    "rv": {
                        "rv": "marketsim.types.IOrder",
                        "args": [
                            "_parseFloat",
                            "_parseFloat"
                        ]
                    },
                    "args": [
                        "marketsim.Side.Tag"
                    ]
                },
                "collapsed": false
            },
            "volumeDistr": {
                "hidden": false,
                "type": {
                    "rv": "_parseFloat",
                    "args": []
                },
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n<p>Liquidity provider is a combination of two LiquidityProviderSide traders\nwith the same parameters but different trading sides.</p>\n<p>It has followng parameters:</p>\n<dl class=\"docutils\">\n<dt><strong>Order factory</strong></dt>\n<dd>order factory function (default: order.Limit.T)</dd>\n<dt><strong>Initial value</strong></dt>\n<dd>initial price which is taken if orderBook is empty (default: 100)</dd>\n<dt><strong>Time intervals between two order creations</strong></dt>\n<dd>defines intervals of time between order creation\n(default: exponential distribution with \u03bb = 1)</dd>\n<dt><strong>Price of orders to create as multiplier to the current price</strong></dt>\n<dd>defines multipliers for current asset price when price of\norder to create is calculated (default: log normal distribution with\n\u03bc = 0 and \u03c3 = 0.1)</dd>\n<dt><strong>Volume of orders to create</strong></dt>\n<dd>defines volumes of orders to create\n(default: exponential distribution with \u03bb = 1)</dd>\n</dl>\n</div>\n"
    },
    "marketsim.strategy._signal.less_float": {
        "castsTo": [
            {
                "rv": "__builtin__.bool",
                "args": []
            },
            "marketsim.mathutils._ops.FloatFunction",
            "marketsim.strategy._signal.less_float",
            "marketsim.types.IFloatFunction",
            "marketsim.types.IScalarFunction",
            {
                "rv": "_parseFloat",
                "args": []
            }
        ],
        "properties": {
            "rhs": {
                "hidden": false,
                "type": "marketsim.types.IFloatFunction",
                "collapsed": false
            },
            "lhs": {
                "hidden": false,
                "type": "marketsim.types.IFloatFunction",
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.observable._orderbook.side_price": {
        "castsTo": [
            "marketsim.observable._orderbook.side_price",
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IScalarFunction",
            "marketsim.types.IFloatFunction",
            "marketsim.mathutils._ops.FloatFunction"
        ],
        "properties": {
            "orderbook": {
                "hidden": false,
                "type": "marketsim.types.IOrderBook",
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n<p>Returns <em>orderbook</em> <em>side</em> price</p>\n</div>\n"
    },
    "marketsim.strategy.Noise": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy",
            "marketsim.types.IStrategy",
            "marketsim.strategy._noise.Noise",
            "marketsim.strategy._noise._Noise_Impl",
            "marketsim.strategy._basic.Strategy",
            "marketsim.strategy._basic.Base",
            "marketsim.strategy._two_sides.TwoSides"
        ],
        "properties": {
            "sideDistr": {
                "hidden": false,
                "type": {
                    "rv": "_parseInt",
                    "args": []
                },
                "collapsed": false
            },
            "creationIntervalDistr": {
                "hidden": false,
                "type": {
                    "rv": "_parseFloat",
                    "args": []
                },
                "collapsed": false
            },
            "orderFactory": {
                "hidden": false,
                "type": {
                    "rv": {
                        "rv": "marketsim.types.IOrder",
                        "args": [
                            "_parseFloat"
                        ]
                    },
                    "args": [
                        "marketsim.Side.Tag"
                    ]
                },
                "collapsed": false
            },
            "volumeDistr": {
                "hidden": false,
                "type": {
                    "rv": "_parseFloat",
                    "args": []
                },
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n<p>Noise strategy is a quite dummy strategy that randomly creates an order\nand sends it to the order book.</p>\n<p>It has following parameters:</p>\n<dl class=\"docutils\">\n<dt><strong>Order factory</strong></dt>\n<dd>order factory function (default: order.Market.T)</dd>\n<dt><strong>Time intervals between two order creations</strong></dt>\n<dd>defines intervals of time between order creation\n(default: exponential distribution with \u03bb = 1)</dd>\n<dt><strong>Function to choose side of order to create</strong></dt>\n<dd>side of orders to create\n(default: discrete uniform distribution P(Sell)=P(Buy)=.5)</dd>\n</dl>\n</div>\n"
    },
    "marketsim.strategy.weight.ChooseTheBest": {
        "castsTo": [
            "marketsim.strategy.weight.ChooseTheBest",
            "marketsim.strategy.weight.Efficiency",
            "marketsim.strategy.weight.Base"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.observable._orderbook.volume_levels": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IScalarFunction",
            "marketsim.observable._orderbook.volume_levels",
            "marketsim.types.IFloatFunction",
            "marketsim.mathutils._ops.FloatFunction"
        ],
        "properties": {
            "volumeCount": {
                "hidden": false,
                "type": "_parseInt",
                "collapsed": false
            },
            "side": {
                "hidden": false,
                "type": "marketsim.Side.Tag",
                "collapsed": false
            },
            "orderbook": {
                "hidden": false,
                "type": "marketsim.types.IOrderBook",
                "collapsed": false
            },
            "volumeDelta": {
                "hidden": false,
                "type": "_parseFloat",
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.Side._SellSide": {
        "castsTo": [
            "marketsim.Side._SellSide",
            "marketsim.Side.Tag"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n<p>Tag class representing the sell side</p>\n</div>\n"
    },
    "marketsim.order._always_best.AlwaysBestFactory": {
        "castsTo": [
            "marketsim.order._always_best.AlwaysBestFactory",
            {
                "rv": {
                    "rv": "marketsim.types.IOrder",
                    "args": [
                        "_parseFloat"
                    ]
                },
                "args": [
                    "marketsim.Side.Tag"
                ]
            }
        ],
        "properties": {
            "orderFactory": {
                "hidden": false,
                "type": {
                    "rv": {
                        "rv": "marketsim.types.IOrder",
                        "args": [
                            "_parseFloat",
                            "_parseFloat"
                        ]
                    },
                    "args": [
                        "marketsim.Side.Tag"
                    ]
                },
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n<p>AlwaysBest is a virtual order that ensures that it has the best price in the order book.\nIt is implemented as a limit order which is cancelled\nonce the best price in the order queue has changed\nand is sent again to the order book\nwith a price one tick better than the best price in the book.</p>\n</div>\n"
    },
    "marketsim.observable._computed.IndicatorBase": {
        "castsTo": [
            "marketsim.event.IEvent",
            "marketsim.observable._computed.IndicatorBase",
            "marketsim.types.Observable",
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IObservable",
            "marketsim.event.Conditional",
            "marketsim.event.Event"
        ],
        "properties": {
            "eventSource": {
                "hidden": false,
                "type": "marketsim.event.Event",
                "collapsed": false
            },
            "dataSource": {
                "hidden": false,
                "type": "marketsim.types.IFloatFunction",
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n<p>Observable that stores some scalar value and knows how to update it</p>\n<ul class=\"simple\">\n<li><strong>Source of data</strong> -- function that provides data</li>\n<li><strong>Events when to act</strong> -- events when to act</li>\n</ul>\n</div>\n"
    },
    "marketsim.strategy._signal.ConditionSide": {
        "castsTo": [
            "marketsim.strategy._signal.Condition_Impl",
            {
                "rv": "marketsim.Side.Tag",
                "args": []
            },
            "marketsim.strategy._signal.ConditionSide"
        ],
        "properties": {
            "ifpart": {
                "hidden": false,
                "type": {
                    "rv": "marketsim.Side.Tag",
                    "args": []
                },
                "collapsed": false
            },
            "elsepart": {
                "hidden": false,
                "type": {
                    "rv": "marketsim.Side.Tag",
                    "args": []
                },
                "collapsed": false
            },
            "cond": {
                "hidden": false,
                "type": {
                    "rv": "__builtin__.bool",
                    "args": []
                },
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.strategy._trade_if_profitable.virtualWithUnitVolume": {
        "castsTo": [
            {
                "rv": "marketsim.types.ISingleAssetStrategy",
                "args": [
                    "marketsim.types.ISingleAssetStrategy"
                ]
            },
            "__builtin__.function"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n<p>Creates for a <em>strategy</em> a clone with same parameters but sending virtual market orders of unit volume</p>\n</div>\n"
    },
    "marketsim.observable._orderbook.Price": {
        "castsTo": [
            "marketsim.event.IEvent",
            "marketsim.observable._computed.Proxy",
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IObservable",
            "marketsim.observable._orderbook.Price",
            "marketsim.observable._orderbook.Proxy"
        ],
        "properties": {
            "orderbook": {
                "hidden": false,
                "type": "marketsim.types.IOrderBook",
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.strategy.Signal": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy",
            "marketsim.types.IStrategy",
            "marketsim.strategy._basic.Strategy",
            "marketsim.strategy._basic.Base",
            "marketsim.strategy._signal.Signal",
            "marketsim.strategy._signal._Signal_Impl",
            "marketsim.strategy._signal.SignalBase",
            "marketsim.strategy._two_sides.TwoSides"
        ],
        "properties": {
            "threshold": {
                "hidden": false,
                "type": "combine(greater_or_equal(0.0), _parseFloat)",
                "collapsed": false
            },
            "signal": {
                "hidden": false,
                "type": "marketsim.types.IObservable",
                "collapsed": false
            },
            "orderFactory": {
                "hidden": false,
                "type": {
                    "rv": {
                        "rv": "marketsim.types.IOrder",
                        "args": [
                            "_parseFloat"
                        ]
                    },
                    "args": [
                        "marketsim.Side.Tag"
                    ]
                },
                "collapsed": false
            },
            "volumeDistr": {
                "hidden": false,
                "type": {
                    "rv": "_parseFloat",
                    "args": []
                },
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n<p>Signal strategy listens to some discrete signal\nand when the signal becomes more than some threshold the strategy starts to buy.\nWhen the signal gets lower than -threshold the strategy starts to sell.</p>\n<p>It has following parameters:</p>\n<dl class=\"docutils\">\n<dt><strong>Signal</strong></dt>\n<dd>signal to be listened to (default: RandomWalk)</dd>\n<dt><strong>Order factory</strong></dt>\n<dd>order factory function (default: order.Market.T)</dd>\n<dt><strong>Threshold</strong></dt>\n<dd>threshold when the trader starts to act (default: 0.7)</dd>\n<dt><strong>Volume of orders to create</strong></dt>\n<dd>defines volumes of orders to create\n(default: exponential distribution with \u03bb = 1)</dd>\n</dl>\n</div>\n"
    },
    "marketsim.orderbook._proxy.Proxy": {
        "castsTo": [
            "marketsim.orderbook._proxy.Proxy",
            "marketsim.orderbook._proxy.Base",
            "marketsim.types.IOrderBook"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.mathutils._ops.product": {
        "castsTo": [
            "marketsim.mathutils._ops.product",
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IScalarFunction",
            "marketsim.types.IFloatFunction",
            "marketsim.mathutils._ops.FloatFunction"
        ],
        "properties": {
            "LeftHandSide": {
                "hidden": false,
                "type": "marketsim.types.IFloatFunction",
                "collapsed": false
            },
            "RightHandSide": {
                "hidden": false,
                "type": "marketsim.types.IFloatFunction",
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n<p>Function returning product of the operands</p>\n</div>\n"
    },
    "marketsim.strategy.Canceller": {
        "castsTo": [
            "marketsim.strategy._canceller._Canceller_Impl",
            "marketsim.strategy._canceller.Canceller"
        ],
        "properties": {
            "cancellationIntervalDistr": {
                "hidden": false,
                "type": {
                    "rv": "_parseFloat",
                    "args": []
                },
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.observable._orderbook.ask_price": {
        "castsTo": [
            "marketsim.mathutils._ops.FloatFunction",
            "marketsim.observable._orderbook.ask_price",
            "marketsim.types.IFloatFunction",
            "marketsim.types.IScalarFunction",
            "marketsim.observable._orderbook.side_price",
            {
                "rv": "_parseFloat",
                "args": []
            }
        ],
        "properties": {
            "orderbook": {
                "hidden": false,
                "type": "marketsim.types.IOrderBook",
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.strategy.MeanReversion": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy",
            "marketsim.types.IStrategy",
            "marketsim.strategy._mean_reversion.MeanReversion",
            "marketsim.strategy._fv.FundamentalValueBase",
            "marketsim.strategy._basic.Strategy",
            "marketsim.strategy._basic.Base",
            "marketsim.strategy._signal.SignalBase",
            "marketsim.strategy._two_sides.TwoSides",
            "marketsim.strategy._mean_reversion._MeanReversion_Impl"
        ],
        "properties": {
            "average": {
                "hidden": false,
                "type": "marketsim.types.IUpdatableValue",
                "collapsed": false
            },
            "creationIntervalDistr": {
                "hidden": false,
                "type": {
                    "rv": "_parseFloat",
                    "args": []
                },
                "collapsed": false
            },
            "orderFactory": {
                "hidden": false,
                "type": {
                    "rv": {
                        "rv": "marketsim.types.IOrder",
                        "args": [
                            "_parseFloat"
                        ]
                    },
                    "args": [
                        "marketsim.Side.Tag"
                    ]
                },
                "collapsed": false
            },
            "volumeDistr": {
                "hidden": false,
                "type": {
                    "rv": "_parseFloat",
                    "args": []
                },
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n<p>Mean reversion strategy believes that asset price should return to its average value.\nIt estimates this average using some functional and\nif the current asset price is lower than the average\nit buys the asset and if the price is higher it sells the asset.</p>\n<p>It has following parameters:</p>\n<dl class=\"docutils\">\n<dt><strong>Order factory</strong></dt>\n<dd>order factory function (default: order.Market.T)</dd>\n<dt><strong>Time intervals between two order creations</strong></dt>\n<dd>defines intervals of time between order creation\n(default: exponential distribution with \u03bb = 1)</dd>\n<dt><strong>Average</strong></dt>\n<dd>functional used to calculate the average\n(default: exponentially weighted moving average with \u03b1 = 0.15)</dd>\n<dt><strong>Volume of orders to create</strong></dt>\n<dd>defines volumes of orders to create\n(default: exponential distribution with \u03bb = 1)</dd>\n</dl>\n</div>\n"
    },
    "marketsim.mathutils.rnd.weibullvariate": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IScalarFunction",
            "marketsim.types.IFloatFunction",
            "marketsim.mathutils._ops.FloatFunction",
            "marketsim.mathutils.rnd.weibullvariate"
        ],
        "properties": {
            "Alpha": {
                "hidden": false,
                "type": "combine(greater(0.0), _parseFloat)",
                "collapsed": false
            },
            "Beta": {
                "hidden": false,
                "type": "combine(greater(0.0), _parseFloat)",
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n<p>Weibull distribution. \u03b1 is the scale parameter and \u03b2 is the shape parameter.</p>\n</div>\n"
    },
    "marketsim.observable._orderbook.last_side_price": {
        "castsTo": [
            "marketsim.observable._orderbook.last_side_price",
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IScalarFunction",
            "marketsim.types.IFloatFunction",
            "marketsim.mathutils._ops.FloatFunction"
        ],
        "properties": {
            "orderbook": {
                "hidden": false,
                "type": "marketsim.types.IOrderBook",
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n<p>Returns <em>orderbook</em> last trade <em>side</em> price</p>\n</div>\n"
    },
    "marketsim.mathutils._average.ewma": {
        "castsTo": [
            "marketsim.types.IUpdatableValue",
            "marketsim.mathutils._average.ewma"
        ],
        "properties": {
            "alpha": {
                "hidden": false,
                "type": "_parseFloat",
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n<p>Exponentially weighted moving average</p>\n</div>\n"
    },
    "marketsim.order._market.MarketFactory": {
        "castsTo": [
            "__builtin__.function",
            {
                "rv": {
                    "rv": "marketsim.types.IOrder",
                    "args": [
                        "_parseFloat"
                    ]
                },
                "args": [
                    "marketsim.Side.Tag"
                ]
            }
        ],
        "properties": {},
        "description": "<div class=\"document\">\n<p>Market order of given <em>side</em> and <em>volume</em></p>\n</div>\n"
    },
    "marketsim.observable._average.derivative": {
        "castsTo": [
            "marketsim.types.IUpdatableValue",
            "marketsim.observable._average.derivative"
        ],
        "properties": {
            "source": {
                "hidden": false,
                "type": "marketsim.types.IUpdatableValue",
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n<p>Derivative of some moving average like value.\nUpdated when underlying value is updated.</p>\n</div>\n"
    },
    "marketsim.strategy.TwoAverages": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy",
            "marketsim.types.IStrategy",
            "marketsim.strategy._basic.Strategy",
            "marketsim.strategy._basic.Base",
            "marketsim.strategy._two_averages.TwoAverages",
            "marketsim.strategy._two_averages._TwoAverages_Impl",
            "marketsim.strategy._signal.SignalBase",
            "marketsim.strategy._two_sides.TwoSides"
        ],
        "properties": {
            "volumeDistr": {
                "hidden": false,
                "type": {
                    "rv": "_parseFloat",
                    "args": []
                },
                "collapsed": false
            },
            "creationIntervalDistr": {
                "hidden": false,
                "type": {
                    "rv": "_parseFloat",
                    "args": []
                },
                "collapsed": false
            },
            "average1": {
                "hidden": false,
                "type": "marketsim.types.IUpdatableValue",
                "collapsed": false
            },
            "threshold": {
                "hidden": false,
                "type": "combine(greater_or_equal(0.0), _parseFloat)",
                "collapsed": false
            },
            "average2": {
                "hidden": false,
                "type": "marketsim.types.IUpdatableValue",
                "collapsed": false
            },
            "orderFactory": {
                "hidden": false,
                "type": {
                    "rv": {
                        "rv": "marketsim.types.IOrder",
                        "args": [
                            "_parseFloat"
                        ]
                    },
                    "args": [
                        "marketsim.Side.Tag"
                    ]
                },
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n<p>Two averages strategy compares two averages of price of the same asset but\nwith different parameters ('slow' and 'fast' averages) and when\nthe first is greater than the second one it buys,\nwhen the first is lower than the second one it sells</p>\n<p>It has following parameters:</p>\n<dl class=\"docutils\">\n<dt><strong>Average 1</strong></dt>\n<dd>functional used to obtain the first average\n(defaut: expenentially weighted moving average with \u03b1 = 0.15)</dd>\n<dt><strong>Average 2</strong></dt>\n<dd>functional used to obtain the second average\n(defaut: expenentially weighted moving average with \u03b1 = 0.015)</dd>\n<dt><strong>Order factory</strong></dt>\n<dd>order factory function (default: order.Market.T)</dd>\n<dt><strong>Threshold</strong></dt>\n<dd>threshold when the trader starts to act (default: 0.)</dd>\n<dt><strong>Volume of orders to create</strong></dt>\n<dd>defines volumes of orders to create\n(default: exponential distribution with \u03bb = 1)</dd>\n<dt><strong>Time intervals between two order creations</strong></dt>\n<dd>defines intervals of time between order creation\n(default: exponential distribution with \u03bb = 1)</dd>\n</dl>\n</div>\n"
    },
    "marketsim.trader._sa.SingleAsset": {
        "castsTo": [
            "marketsim.trader._base.Base",
            "marketsim.timeserie.Holder",
            "marketsim.types.ISingleAssetTrader",
            "marketsim.types.ITrader",
            "marketsim.trader._sa.SingleAsset"
        ],
        "properties": {
            "amount": {
                "hidden": false,
                "type": "_parseFloat",
                "collapsed": false
            },
            "orderBook": {
                "hidden": false,
                "type": "marketsim.types.IOrderBook",
                "collapsed": false
            },
            "PnL": {
                "hidden": false,
                "type": "_parseFloat",
                "collapsed": false
            },
            "timeseries": {
                "hidden": false,
                "type": {
                    "elementType": "marketsim.timeserie.ToRecord"
                },
                "collapsed": true
            },
            "strategy": {
                "hidden": false,
                "type": "marketsim.types.ISingleAssetStrategy",
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n<p>A trader that trades a single asset on a single market.</p>\n<p>Parameters:</p>\n<dl class=\"docutils\">\n<dt><strong>orderBook</strong></dt>\n<dd>order book for the asset being traded</dd>\n<dt><strong>strategies</strong></dt>\n<dd>array of strategies run by the trader</dd>\n<dt><strong>amount</strong></dt>\n<dd>current position of the trader (number of assets that it owns)</dd>\n<dt><strong>PnL</strong></dt>\n<dd>current trader balance (number of money units that it owns)</dd>\n</dl>\n</div>\n"
    },
    "marketsim.mathutils.rnd.normalvariate": {
        "castsTo": [
            "marketsim.mathutils.rnd.normalvariate",
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IScalarFunction",
            "marketsim.types.IFloatFunction",
            "marketsim.mathutils._ops.FloatFunction"
        ],
        "properties": {
            "Mu": {
                "hidden": false,
                "type": "_parseFloat",
                "collapsed": false
            },
            "Sigma": {
                "hidden": false,
                "type": "_parseFloat",
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n<p>Normal distribution. \u03bc is the mean, and \u03c3 is the standard deviation.</p>\n</div>\n"
    },
    "marketsim.strategy._periodic.randomSide": {
        "castsTo": [
            "__builtin__.function",
            {
                "rv": "marketsim.Side.Tag",
                "args": []
            }
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.orderbook._proxy.OfTrader": {
        "castsTo": [
            "marketsim.orderbook._proxy.Base",
            "marketsim.types.IOrderBook",
            "marketsim.orderbook._proxy.OfTrader"
        ],
        "properties": {
            "Trader": {
                "hidden": false,
                "type": "marketsim.types.ISingleAssetTrader",
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.mathutils.rnd.betavariate": {
        "castsTo": [
            "marketsim.mathutils.rnd.betavariate",
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IScalarFunction",
            "marketsim.types.IFloatFunction",
            "marketsim.mathutils._ops.FloatFunction"
        ],
        "properties": {
            "Alpha": {
                "hidden": false,
                "type": "combine(greater(0.0), _parseFloat)",
                "collapsed": false
            },
            "Beta": {
                "hidden": false,
                "type": "combine(greater(0.0), _parseFloat)",
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n<p>Beta distribution. Conditions on the parameters are \u03b1 &gt; 0 and \u03b2 &gt; 0. Returned values range between 0 and 1.</p>\n</div>\n"
    },
    "marketsim.observable._orderbook.BidPrice": {
        "castsTo": [
            "marketsim.event.IEvent",
            "marketsim.observable._computed.Proxy",
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IObservable",
            "marketsim.observable._orderbook.BidPrice",
            "marketsim.observable._orderbook.Proxy"
        ],
        "properties": {
            "orderbook": {
                "hidden": false,
                "type": "marketsim.types.IOrderBook",
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.mathutils._ops.sub": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IScalarFunction",
            "marketsim.mathutils._ops.sub",
            "marketsim.types.IFloatFunction",
            "marketsim.mathutils._ops.FloatFunction"
        ],
        "properties": {
            "LeftHandSide": {
                "hidden": false,
                "type": "marketsim.types.IFloatFunction",
                "collapsed": false
            },
            "RightHandSide": {
                "hidden": false,
                "type": "marketsim.types.IFloatFunction",
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n<p>Function substructing the right operand from the left one</p>\n</div>\n"
    },
    "marketsim.strategy._signal.NotNoneFloat": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IScalarFunction",
            "marketsim.types.IFloatFunction",
            "marketsim.mathutils._ops.FloatFunction",
            "marketsim.strategy._signal.NotNoneFloat"
        ],
        "properties": {
            "source": {
                "hidden": false,
                "type": "marketsim.types.IFloatFunction",
                "collapsed": false
            },
            "ifnone": {
                "hidden": false,
                "type": "marketsim.types.IFloatFunction",
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.mathutils._ops.sum": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IScalarFunction",
            "marketsim.types.IFloatFunction",
            "marketsim.mathutils._ops.FloatFunction",
            "marketsim.mathutils._ops.sum"
        ],
        "properties": {
            "LeftHandSide": {
                "hidden": false,
                "type": "marketsim.types.IFloatFunction",
                "collapsed": false
            },
            "RightHandSide": {
                "hidden": false,
                "type": "marketsim.types.IFloatFunction",
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n<p>Function returning sum of the operands</p>\n</div>\n"
    },
    "marketsim.Reference": {
        "castsTo": [
            "marketsim.Reference"
        ],
        "properties": {
            "name": {
                "hidden": false,
                "type": "identity",
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.strategy._rsi.RelativeStrengthIndexSide": {
        "castsTo": [
            "marketsim.strategy._rsi.RelativeStrengthIndexSide",
            {
                "rv": "marketsim.Side.Tag",
                "args": []
            }
        ],
        "properties": {
            "threshold": {
                "hidden": false,
                "type": "_parseFloat",
                "collapsed": false
            },
            "rsi": {
                "hidden": false,
                "type": "marketsim.types.IFloatFunction",
                "collapsed": false
            },
            "orderBook": {
                "hidden": false,
                "type": "marketsim.types.IOrderBook",
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.order._stoploss.StopLossFactory": {
        "castsTo": [
            {
                "rv": {
                    "rv": "marketsim.types.IOrder",
                    "args": [
                        "_parseFloat"
                    ]
                },
                "args": [
                    "marketsim.Side.Tag"
                ]
            },
            "marketsim.order._stoploss.StopLossFactory"
        ],
        "properties": {
            "maxLoss": {
                "hidden": false,
                "type": "_parseFloat",
                "collapsed": false
            },
            "orderFactory": {
                "hidden": false,
                "type": {
                    "rv": {
                        "rv": "marketsim.types.IOrder",
                        "args": [
                            "_parseFloat"
                        ]
                    },
                    "args": [
                        "marketsim.Side.Tag"
                    ]
                },
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.mathutils._ops.negate": {
        "castsTo": [
            "marketsim.mathutils._ops.negate",
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IScalarFunction",
            "marketsim.types.IFloatFunction",
            "marketsim.mathutils._ops.FloatFunction"
        ],
        "properties": {
            "arg": {
                "hidden": false,
                "type": "marketsim.types.IFloatFunction",
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n<p>Function returning product of the operands</p>\n</div>\n"
    },
    "marketsim.signal.RandomWalk": {
        "castsTo": [
            "marketsim.event.IEvent",
            "marketsim.types.Observable",
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IObservable",
            "marketsim.event.Conditional",
            "marketsim.signal.RandomWalk",
            "marketsim.event.Event"
        ],
        "properties": {
            "deltaDistr": {
                "hidden": false,
                "type": "marketsim.types.IFloatFunction",
                "collapsed": false
            },
            "initialValue": {
                "hidden": false,
                "type": "_parseFloat",
                "collapsed": false
            },
            "intervalDistr": {
                "hidden": false,
                "type": "marketsim.types.IFloatFunction",
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n<p>A discrete signal with user-defined increments.</p>\n<p>Parameters:</p>\n<dl class=\"docutils\">\n<dt><strong>initialValue</strong></dt>\n<dd>initial value of the signal (default: 0)</dd>\n<dt><strong>deltaDistr</strong></dt>\n<dd>increment function (default: normal distribution with \u03bc = 0, \u03c3 = 1)</dd>\n<dt><strong>intervalDistr</strong></dt>\n<dd>defines intervals between signal updates\n(default: exponential distribution with \u03bb = 1)</dd>\n</dl>\n</div>\n"
    },
    "marketsim.strategy.MultiarmedBandit": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy",
            "marketsim.types.IStrategy",
            "marketsim.strategy._basic.Strategy",
            "marketsim.strategy._basic.Base",
            "marketsim.strategy._multiarmed_bandit.MultiarmedBandit",
            "marketsim.strategy._multiarmed_bandit._MultiarmedBandit_Impl"
        ],
        "properties": {
            "strategies": {
                "hidden": false,
                "type": {
                    "elementType": "marketsim.types.ISingleAssetStrategy"
                },
                "collapsed": false
            },
            "estimator": {
                "hidden": false,
                "type": {
                    "rv": "marketsim.types.ISingleAssetStrategy",
                    "args": [
                        "marketsim.types.ISingleAssetStrategy"
                    ]
                },
                "collapsed": false
            },
            "weight": {
                "hidden": false,
                "type": "marketsim.strategy.weight.Base",
                "collapsed": false
            },
            "efficiency": {
                "hidden": false,
                "type": {
                    "rv": "marketsim.types.ISingleAssetTrader",
                    "args": [
                        "marketsim.types.ISingleAssetTrader"
                    ]
                },
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n<p>A composite strategy initialized with an array of strategies.\nIn some moments of time the most effective strategy\nis chosen and made running; other strategies are suspended.\nThe choice is made randomly among the strategies that have\na positive efficiency trend, weighted by the efficiency value.</p>\n<p>Parameters:</p>\n<blockquote>\n<dl class=\"docutils\">\n<dt><strong>Weight function</strong></dt>\n<dd>weighting scheme for choosing strategies</dd>\n<dt><strong>strategies</strong></dt>\n<dd>original strategies that can be suspended</dd>\n<dt><strong>Efficiency evaluation function</strong></dt>\n<dd>function estimating is the strategy efficient or not</dd>\n<dt><strong>Function creating a strategy used to estimate the original one</strong></dt>\n<dd>function creating phantom strategy used for efficiency estimation</dd>\n</dl>\n</blockquote>\n</div>\n"
    },
    "marketsim.mathutils._ops.div": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IScalarFunction",
            "marketsim.types.IFloatFunction",
            "marketsim.mathutils._ops.FloatFunction",
            "marketsim.mathutils._ops.div"
        ],
        "properties": {
            "LeftHandSide": {
                "hidden": false,
                "type": "marketsim.types.IFloatFunction",
                "collapsed": false
            },
            "RightHandSide": {
                "hidden": false,
                "type": "marketsim.types.IFloatFunction",
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n<p>Function returning division of the operands</p>\n</div>\n"
    },
    "marketsim.mathutils._ops.identity": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IScalarFunction",
            "marketsim.types.IFloatFunction",
            "marketsim.mathutils._ops.FloatFunction",
            "marketsim.mathutils._ops.identity"
        ],
        "properties": {
            "arg": {
                "hidden": false,
                "type": "marketsim.types.IFloatFunction",
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.order._cancel.LimitMarketFactory": {
        "castsTo": [
            {
                "rv": {
                    "rv": "marketsim.types.IOrder",
                    "args": [
                        "_parseFloat"
                    ]
                },
                "args": [
                    "marketsim.Side"
                ]
            },
            "__builtin__.function"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n<p>This a combination of a limit order and a cancel order sent immediately\nIt works as a market order in sense that it is not put into the order queue\nbut can be matched (as a limit order)\nonly if there are orders with suitable price in the queue</p>\n</div>\n"
    },
    "marketsim.remote.Link": {
        "castsTo": [
            "marketsim.remote.Link"
        ],
        "properties": {
            "latency": {
                "hidden": false,
                "type": {
                    "rv": "_parseFloat",
                    "args": []
                },
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n<p>Represents latency in information propagation from one agent to another one\n(normally between a trader and a market).\nEnsures that sending packets via a link preserves their order.</p>\n<p>Parameters:</p>\n<dl class=\"docutils\">\n<dt><strong>latency</strong></dt>\n<dd>function called for each packet in order to determine\nwhen it will appear at the destination point</dd>\n</dl>\n</div>\n"
    },
    "marketsim.strategy.Periodic": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy",
            "marketsim.strategy._periodic.Periodic",
            "marketsim.strategy._periodic._Periodic_Impl",
            "marketsim.strategy._basic.Strategy",
            "marketsim.strategy._basic.Base",
            "marketsim.types.IStrategy"
        ],
        "properties": {
            "sideFunc": {
                "hidden": false,
                "type": {
                    "rv": "marketsim.Side.Tag",
                    "args": []
                },
                "collapsed": false
            },
            "orderFactory": {
                "hidden": false,
                "type": {
                    "rv": {
                        "rv": "marketsim.types.IOrder",
                        "args": [
                            "_parseFloat"
                        ]
                    },
                    "args": [
                        "marketsim.Side.Tag"
                    ]
                },
                "collapsed": false
            },
            "eventGen": {
                "hidden": false,
                "type": "marketsim.event.Event",
                "collapsed": false
            },
            "volumeFunc": {
                "hidden": false,
                "type": {
                    "rv": "_parseFloat",
                    "args": []
                },
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n<p>Generic periodic strategy that wakes up on events given by <em>eventGen</em>,\nchooses side of order to create using <em>sideFunc</em> and its volume by <em>volumeFunc</em>,\ncreates an order via <em>orderFactory</em> and sends the order to the market using its trader</p>\n<p>Parameters:</p>\n<blockquote>\n<dl class=\"docutils\">\n<dt><strong>Order factory</strong></dt>\n<dd>order factory function (default: order.Limit.T)</dd>\n<dt><strong>Action trigger</strong></dt>\n<dd>Event source making the strategy to wake up</dd>\n<dt><strong>Volume</strong></dt>\n<dd>defines volumes of orders to create\n(default: exponential distribution with \u03bb = 1)</dd>\n<dt><strong>Side</strong></dt>\n<dd>function choosing side of order to create (default: randomSide)</dd>\n</dl>\n</blockquote>\n</div>\n"
    },
    "marketsim.strategy._basic.Empty": {
        "castsTo": [
            "marketsim.strategy._basic.Empty",
            "marketsim.types.ISingleAssetStrategy",
            "marketsim.types.IStrategy",
            "marketsim.strategy._basic.Strategy",
            "marketsim.strategy._basic.Base"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.observable._async.Efficiency": {
        "castsTo": [
            "marketsim.event.IEvent",
            "marketsim.types.Observable",
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IObservable",
            "marketsim.event.Conditional",
            "marketsim.observable._async.Efficiency",
            "marketsim.event.Event"
        ],
        "properties": {
            "trader": {
                "hidden": false,
                "type": "marketsim.types.ISingleAssetTrader",
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n<p>Observes trader's balance as if was cleared (trader's balance if its position was cleared).\nCan be None if there is not enough assets on the market to clear the position.\nThis observable is updated when trader position is changed\n(which is not fair since the asset price change influences on this parameter also)</p>\n</div>\n"
    },
    "marketsim.mathutils.rnd.vonmisesvariate": {
        "castsTo": [
            "marketsim.mathutils.rnd.vonmisesvariate",
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IScalarFunction",
            "marketsim.types.IFloatFunction",
            "marketsim.mathutils._ops.FloatFunction"
        ],
        "properties": {
            "Mu": {
                "hidden": false,
                "type": "combine(less(6.28318530718), combine(greater_or_equal(0.0), _parseFloat))",
                "collapsed": false
            },
            "Kappa": {
                "hidden": false,
                "type": "combine(greater_or_equal(0.0), _parseFloat)",
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n<p>\u03bc is the mean angle, expressed in radians between 0 and 2|pi|, and \u03ba is the concentration parameter, which must be greater than or equal to zero. If \u03ba is equal to zero, this distribution reduces to a uniform random angle over the range 0 to 2|pi|</p>\n</div>\n"
    },
    "marketsim.observable._average.Fold": {
        "castsTo": [
            "marketsim.observable._average.Fold",
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IScalarFunction",
            "marketsim.types.IFloatFunction",
            "marketsim.mathutils._ops.FloatFunction"
        ],
        "properties": {
            "source": {
                "hidden": false,
                "type": "marketsim.types.IObservable",
                "collapsed": false
            },
            "folder": {
                "hidden": false,
                "type": "marketsim.types.IUpdatableValue",
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n<p>Aggregates (folds) time-dependent data from <em>source</em> using given functional  <em>folder</em> (e.g. moving average)</p>\n<p>For example</p>\n<pre class=\"literal-block\">\nprice_avg = Fold(Price(book_A), ewma(alpha = 0.15))\n</pre>\n<p>creates a observable for a moving average with \u03b1 = 0.15 of mid-price of asset <em>book_A</em></p>\n</div>\n"
    },
    "marketsim.strategy._trade_if_profitable.efficiencyTrend": {
        "castsTo": [
            {
                "rv": "marketsim.types.ISingleAssetTrader",
                "args": [
                    "marketsim.types.ISingleAssetTrader"
                ]
            },
            "__builtin__.function"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n<p>Returns derivative of a <em>trader</em>'s &quot;cleared&quot; balance</p>\n</div>\n"
    },
    "marketsim.Side._BuySide": {
        "castsTo": [
            "marketsim.Side._BuySide",
            "marketsim.Side.Tag"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.orderbook._local.Local": {
        "castsTo": [
            "marketsim.timeserie.Holder",
            "marketsim.orderbook._local.Local",
            "marketsim.types.IOrderBook",
            "marketsim.orderbook._base.BookBase"
        ],
        "properties": {
            "_digitsToShow": {
                "hidden": true,
                "type": "_parseInt",
                "collapsed": false
            },
            "tickSize": {
                "hidden": false,
                "type": "_parseFloat",
                "collapsed": false
            },
            "timeseries": {
                "hidden": false,
                "type": {
                    "elementType": "marketsim.timeserie.ToRecord"
                },
                "collapsed": true
            }
        },
        "description": "<div class=\"document\">\n<p>Order book for a single asset in a market.\nMaintains two order queues for orders of different sides</p>\n</div>\n"
    },
    "marketsim.strategy.Arbitrage": {
        "castsTo": [
            "marketsim.types.IStrategy",
            "marketsim.strategy._arbitrage.Arbitrage",
            "marketsim.strategy._arbitrage._Arbitrage_Impl",
            "marketsim.strategy._basic.MultiAssetStrategy",
            "marketsim.strategy._basic.Base",
            "marketsim.types.IMultiAssetStrategy"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.mathutils.rnd.triangular": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IScalarFunction",
            "marketsim.types.IFloatFunction",
            "marketsim.mathutils._ops.FloatFunction",
            "marketsim.mathutils.rnd.triangular"
        ],
        "properties": {
            "High": {
                "hidden": false,
                "type": "_parseFloat",
                "collapsed": false
            },
            "Low": {
                "hidden": false,
                "type": "_parseFloat",
                "collapsed": false
            },
            "Mode": {
                "hidden": false,
                "type": "_parseFloat",
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n<p>Return a random floating point number <em>N</em> such that <em>low</em> &lt;= <em>N</em> &lt;= <em>high</em> and with the specified <em>mode</em> between those bounds. The <em>low</em> and <em>high</em> bounds default to zero and one. The <em>mode</em> argument defaults to the midpoint between the bounds, giving a symmetric distribution.</p>\n</div>\n"
    },
    "marketsim.remote.TwoWayLink": {
        "castsTo": [
            "marketsim.remote.TwoWayLink"
        ],
        "properties": {
            "down": {
                "hidden": false,
                "type": "marketsim.remote.Link",
                "collapsed": false
            },
            "up": {
                "hidden": false,
                "type": "marketsim.remote.Link",
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n<p>Represents latency in information propagation between two agents\n(normally between a trader and a market).\nEnsures that sending packets via links preserves their order.\nHolds two one-way links in opposite directions.</p>\n<p>Parameters:</p>\n<dl class=\"docutils\">\n<dt><strong>up</strong></dt>\n<dd>Forward link (normally from a trader to a market)</dd>\n<dt><strong>down</strong></dt>\n<dd>Backward link (normally from a market to a trader)</dd>\n</dl>\n</div>\n"
    },
    "marketsim.mathutils.rnd.randint": {
        "castsTo": [
            "__builtin__.instance",
            {
                "rv": "_parseInt",
                "args": []
            }
        ],
        "properties": {},
        "description": "<div class=\"document\">\n<p>Return a random integer <em>N</em> such that <em>a</em> &lt;= <em>N</em> &lt;= <em>b</em>.</p>\n</div>\n"
    },
    "marketsim.mathutils.rnd.gammavariate": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IScalarFunction",
            "marketsim.mathutils.rnd.gammavariate",
            "marketsim.types.IFloatFunction",
            "marketsim.mathutils._ops.FloatFunction"
        ],
        "properties": {
            "Alpha": {
                "hidden": false,
                "type": "combine(greater(0.0), _parseFloat)",
                "collapsed": false
            },
            "Beta": {
                "hidden": false,
                "type": "combine(greater(0.0), _parseFloat)",
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n<p>Gamma distribution. Conditions on the parameters are \u03b1 &gt; 0 and \u03b2 &gt; 0.</p>\n<p>The probability distribution function is:</p>\n<pre class=\"literal-block\">\n          x ** (alpha - 1) * math.exp(-x / beta)\npdf(x) =  --------------------------------------\n             math.gamma(alpha) * beta ** alpha\n</pre>\n</div>\n"
    },
    "marketsim.js.Graph": {
        "castsTo": [
            "marketsim.js.Graph",
            "marketsim.types.IGraph"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n<p>Generic 2D graph to be rendered by means of javascript libraries</p>\n</div>\n"
    },
    "marketsim.mathutils.rnd.uniform": {
        "castsTo": [
            "marketsim.mathutils.rnd.uniform",
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IScalarFunction",
            "marketsim.types.IFloatFunction",
            "marketsim.mathutils._ops.FloatFunction"
        ],
        "properties": {
            "High": {
                "hidden": false,
                "type": "_parseFloat",
                "collapsed": false
            },
            "Low": {
                "hidden": false,
                "type": "_parseFloat",
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n<p>Return a random floating point number <em>N</em> such that <em>a</em> &lt;= <em>N</em> &lt;= <em>b</em> for <em>a</em> &lt;= <em>b</em> and <em>b</em> &lt;= <em>N</em> &lt;= <em>a</em> for <em>b</em> &lt; <em>a</em>.\nThe end-point value <em>b</em> may or may not be included in the range depending on floating-point rounding in the equation <em>a</em> + (<em>b</em>-<em>a</em>) * <em>random()</em>.</p>\n</div>\n"
    },
    "marketsim.registry.Simulation": {
        "castsTo": [
            "marketsim.registry.Simulation"
        ],
        "properties": {
            "traders": {
                "hidden": false,
                "type": {
                    "elementType": "marketsim.types.ITrader"
                },
                "collapsed": false
            },
            "graphs": {
                "hidden": false,
                "type": {
                    "elementType": "marketsim.types.IGraph"
                },
                "collapsed": false
            },
            "orderbooks": {
                "hidden": false,
                "type": {
                    "elementType": "marketsim.types.IOrderBook"
                },
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.scheduler.Scheduler": {
        "castsTo": [
            "marketsim.scheduler.Scheduler"
        ],
        "properties": {
            "currentTime": {
                "hidden": false,
                "type": "_parseFloat",
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n<p>Keeps a set of events to be launched in the future</p>\n</div>\n"
    },
    "marketsim.strategy.weight.Uniform": {
        "castsTo": [
            "marketsim.strategy.weight.Base",
            "marketsim.strategy.weight.Uniform"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.order._iceberg.IcebergFactory": {
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
                    "marketsim.Side.Tag"
                ]
            },
            "marketsim.order._iceberg.IcebergFactory"
        ],
        "properties": {
            "volumeLimit": {
                "hidden": false,
                "type": "_parseInt",
                "collapsed": false
            },
            "orderFactory": {
                "hidden": false,
                "type": {
                    "rv": {
                        "rv": "marketsim.types.IOrder",
                        "args": [
                            "_parseFloat",
                            "_parseFloat"
                        ]
                    },
                    "args": [
                        "marketsim.Side.Tag"
                    ]
                },
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n<p>Virtual order that implements iceberg strategy:\nFirst it sends an order for a small potion of its volume to a book and\nonce it is filled resends a new order</p>\n</div>\n"
    },
    "marketsim.observable._trader.profit_and_loss": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IScalarFunction",
            "marketsim.observable._trader.profit_and_loss",
            "marketsim.types.IFloatFunction",
            "marketsim.mathutils._ops.FloatFunction"
        ],
        "properties": {
            "trader": {
                "hidden": false,
                "type": "marketsim.types.ITrader",
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n<p>Returns balance of the given <em>trader</em></p>\n</div>\n"
    },
    "marketsim.observable._momentum.upMovement": {
        "castsTo": [
            "__builtin__.function",
            {
                "rv": "_parseFloat",
                "args": [
                    "_parseFloat",
                    "_parseFloat"
                ]
            }
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.scheduler.Timer": {
        "castsTo": [
            "marketsim.event.IEvent",
            "marketsim.scheduler.Timer",
            "marketsim.event.Event"
        ],
        "properties": {
            "intervalFunc": {
                "hidden": false,
                "type": "marketsim.types.IFloatFunction",
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n<p>Represents a repeating action.</p>\n<p>Parameters:</p>\n<dl class=\"docutils\">\n<dt><em>intervalFunc</em></dt>\n<dd>intervals of time between moments when subscribed listeners are to be called</dd>\n</dl>\n</div>\n"
    },
    "marketsim.observable._momentum.downMovement": {
        "castsTo": [
            "__builtin__.function",
            {
                "rv": "_parseFloat",
                "args": [
                    "_parseFloat",
                    "_parseFloat"
                ]
            }
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.order._virtual.VirtualMarketFactory": {
        "castsTo": [
            "__builtin__.function",
            {
                "rv": {
                    "rv": "marketsim.types.IOrder",
                    "args": [
                        "_parseFloat"
                    ]
                },
                "args": [
                    "marketsim.Side.Tag"
                ]
            }
        ],
        "properties": {},
        "description": "<div class=\"document\">\n<p>Used to evaluates price at which a market order of given volume would be executed\nSince this query might be computationally expensive and done asynchronously,\nwe wrap function OrderQueue.evaluateOrderPrice by this class.\nThe result will returned in on_matched event with empty 'other' field\nTBD: we make use of on_matched machinery since that is supported in RemoteBook\nbut i'm not sure that it is a good design decision.</p>\n</div>\n"
    },
    "marketsim.orderbook._remote.Remote": {
        "castsTo": [
            "marketsim.timeserie.Holder",
            "marketsim.orderbook._remote.Remote",
            "marketsim.types.IOrderBook",
            "marketsim.orderbook._base.BookBase"
        ],
        "properties": {
            "link": {
                "hidden": false,
                "type": "marketsim.remote.TwoWayLink",
                "collapsed": false
            },
            "orderbook": {
                "hidden": false,
                "type": "marketsim.types.IOrderBook",
                "collapsed": false
            },
            "timeseries": {
                "hidden": false,
                "type": {
                    "elementType": "marketsim.timeserie.ToRecord"
                },
                "collapsed": true
            }
        },
        "description": "<div class=\"document\">\n<p>Represent an <em>orderbook</em> from point of view of a remote trader connected\nto the market by means of a <em>link</em> that introduces some latency in information propagation</p>\n</div>\n"
    },
    "marketsim.strategy.weight.EfficiencyAlpha": {
        "castsTo": [
            "marketsim.strategy.weight.EfficiencyAlpha",
            "marketsim.strategy.weight.Efficiency",
            "marketsim.strategy.weight.Base"
        ],
        "properties": {
            "alpha": {
                "hidden": false,
                "type": "combine(less(1.0), combine(greater_or_equal(0.0), _parseFloat))",
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.strategy.FundamentalValue": {
        "castsTo": [
            "marketsim.strategy._fv._FundamentalValue_Impl",
            "marketsim.types.ISingleAssetStrategy",
            "marketsim.types.IStrategy",
            "marketsim.strategy._fv.FundamentalValueBase",
            "marketsim.strategy._basic.Strategy",
            "marketsim.strategy._basic.Base",
            "marketsim.strategy._signal.SignalBase",
            "marketsim.strategy._two_sides.TwoSides",
            "marketsim.strategy._fv.FundamentalValue"
        ],
        "properties": {
            "creationIntervalDistr": {
                "hidden": false,
                "type": {
                    "rv": "_parseFloat",
                    "args": []
                },
                "collapsed": false
            },
            "fundamentalValue": {
                "hidden": false,
                "type": {
                    "rv": "_parseFloat",
                    "args": []
                },
                "collapsed": false
            },
            "orderFactory": {
                "hidden": false,
                "type": {
                    "rv": {
                        "rv": "marketsim.types.IOrder",
                        "args": [
                            "_parseFloat"
                        ]
                    },
                    "args": [
                        "marketsim.Side.Tag"
                    ]
                },
                "collapsed": false
            },
            "volumeDistr": {
                "hidden": false,
                "type": {
                    "rv": "_parseFloat",
                    "args": []
                },
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n<p>Fundamental value strategy believes that an asset should have some specific price\n(<em>fundamental value</em>) and if the current asset price is lower than the fundamental value\nit starts to buy the asset and if the price is higher it starts to sell the asset.</p>\n<p>It has following parameters:</p>\n<dl class=\"docutils\">\n<dt><strong>Order factory</strong></dt>\n<dd>order factory function (default: order.Market.T)</dd>\n<dt><strong>Time intervals between two order creations</strong></dt>\n<dd>defines intervals of time between order creation\n(default: exponential distribution with \u03bb = 1)</dd>\n<dt><strong>Fundamental value</strong></dt>\n<dd>defines fundamental value (default: constant 100)</dd>\n<dt><strong>Volume of orders to create</strong></dt>\n<dd>defines volumes of orders to create\n(default: exponential distribution with \u03bb = 1)</dd>\n</dl>\n</div>\n"
    },
    "marketsim.strategy._lp_side.ConstantSide": {
        "castsTo": [
            "marketsim.strategy._lp_side.ConstantSide",
            {
                "rv": "marketsim.Side.Tag",
                "args": []
            }
        ],
        "properties": {
            "side": {
                "hidden": false,
                "type": "marketsim.Side.Tag",
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n<p>Constant function always returning given <em>side</em>.</p>\n<p>Note: We need it since our type system doesn't support for the moment generic\nConstant: () -&gt; 'a</p>\n</div>\n"
    },
    "marketsim.timeserie.ToRecord": {
        "castsTo": [
            "marketsim.types.ITimeSerie",
            "marketsim.timeserie.ToRecord"
        ],
        "properties": {
            "source": {
                "hidden": false,
                "type": "marketsim.types.IObservable",
                "collapsed": false
            },
            "_digits": {
                "hidden": true,
                "type": "_parseInt",
                "collapsed": false
            },
            "_smooth": {
                "hidden": true,
                "type": "_parseInt",
                "collapsed": false
            },
            "graph": {
                "hidden": false,
                "type": "marketsim.types.IGraph",
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.mathutils._ops.constant": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IScalarFunction",
            "marketsim.types.IFloatFunction",
            "marketsim.mathutils._ops.FloatFunction",
            "marketsim.mathutils._ops.constant"
        ],
        "properties": {
            "value": {
                "hidden": false,
                "type": "_parseFloat",
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n<p>Constant function returning <strong>value</strong>.</p>\n</div>\n"
    },
    "marketsim.strategy.weight.Efficiency": {
        "castsTo": [
            "marketsim.strategy.weight.Efficiency",
            "marketsim.strategy.weight.Base"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.strategy.Array": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy",
            "marketsim.types.IStrategy",
            "marketsim.strategy._array._Array_Impl",
            "marketsim.strategy._basic.Strategy",
            "marketsim.strategy._basic.Base",
            "marketsim.strategy._array.Array"
        ],
        "properties": {
            "strategies": {
                "hidden": false,
                "type": {
                    "elementType": "marketsim.types.ISingleAssetStrategy"
                },
                "collapsed": false
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
                    "marketsim.Side.Tag"
                ]
            },
            "__builtin__.function"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n<p>Limit order of the given <em>side</em>, <em>price</em> and <em>volume</em></p>\n</div>\n"
    },
    "marketsim.mathutils._rsi.rsi": {
        "castsTo": [
            "marketsim.types.IUpdatableValue",
            "marketsim.mathutils._rsi.rsi"
        ],
        "properties": {
            "alpha": {
                "hidden": false,
                "type": "_parseFloat",
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n<p>Relative strength index</p>\n</div>\n"
    },
    "marketsim.mathutils.rnd.expovariate": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IScalarFunction",
            "marketsim.types.IFloatFunction",
            "marketsim.mathutils._ops.FloatFunction",
            "marketsim.mathutils.rnd.expovariate"
        ],
        "properties": {
            "Lambda": {
                "hidden": false,
                "type": "combine(greater(0.0), _parseFloat)",
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n<p>Exponential distribution. \u03bb is 1.0 divided by the desired mean. It should be greater zero. Returned values range from 0 to positive infinity</p>\n</div>\n"
    },
    "marketsim.observable._orderbook.AskPrice": {
        "castsTo": [
            "marketsim.event.IEvent",
            "marketsim.observable._computed.Proxy",
            "marketsim.observable._orderbook.AskPrice",
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IObservable",
            "marketsim.observable._orderbook.Proxy"
        ],
        "properties": {
            "orderbook": {
                "hidden": false,
                "type": "marketsim.types.IOrderBook",
                "collapsed": false
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    }
}