var typeinfo = {
    "marketsim.strategy.adaptive._virtual_market.virtualMarket": {
        "castsTo": [
            {
                "rv": "marketsim.types.IAccount",
                "args": [
                    "marketsim.types.ISingleAssetStrategy"
                ]
            }
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.strategy.v0._mean_reversion.MeanReversion": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy"
        ],
        "properties": {
            "ewma_alpha": {
                "type": "combine(greater_or_equal(0.0), _parseFloat)"
            },
            "creationIntervalDistr": {
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
                            "_parseFloat"
                        ]
                    },
                    "args": [
                        "marketsim.Side"
                    ]
                }
            },
            "volumeDistr": {
                "type": {
                    "rv": "_parseFloat",
                    "args": []
                }
            }
        },
        "description": "<div class=\"document\">\n<p>Mean reversion strategy believes that asset price should return to its average value.\nIt estimates this average using some functional and\nif the current asset price is lower than the average\nit buys the asset and if the price is higher it sells the asset.</p>\n<p>It has following parameters:</p>\n<dl class=\"docutils\">\n<dt><strong>Order factory</strong></dt>\n<dd>order factory function (default: order.Market.T)</dd>\n<dt><strong>Time intervals between two order creations</strong></dt>\n<dd>defines intervals of time between order creation\n(default: exponential distribution with \u03bb = 1)</dd>\n<dt><strong>&amp;alpha; for moving average</strong></dt>\n<dd>\u03b1 for exponentially weighted moving average\n(default: 0.15)</dd>\n<dt><strong>Volume of orders to create</strong></dt>\n<dd>defines volumes of orders to create\n(default: exponential distribution with \u03bb = 1)</dd>\n</dl>\n</div>\n"
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
    "marketsim.order._limit.SidePrice_Factory": {
        "castsTo": [
            {
                "rv": "marketsim.types.IOrderGenerator",
                "args": [
                    "marketsim.types.IFunction_Tag",
                    "marketsim.types.IFunction_float"
                ]
            }
        ],
        "properties": {
            "volume": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.trader._proxy.SingleProxy": {
        "castsTo": [
            "marketsim.types.IAccount",
            "marketsim.types.ISingleAssetTrader",
            "marketsim.types.ITrader"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.observable._average.Fold": {
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
            "folder": {
                "type": "marketsim.types.IUpdatableValue"
            }
        },
        "description": "<div class=\"document\">\n<p>Aggregates (folds) time-dependent data from <em>source</em> using given functional  <em>folder</em> (e.g. moving average)</p>\n<p>For example</p>\n<pre class=\"literal-block\">\nprice_avg = Fold(MidPrice(book_A), ewma(alpha = 0.15))\n</pre>\n<p>creates a observable for a moving average with \u03b1 = 0.15 of mid-price of asset <em>book_A</em></p>\n</div>\n"
    },
    "marketsim.strategy._canceller.Canceller": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy"
        ],
        "properties": {
            "cancellationIntervalDistr": {
                "type": {
                    "rv": "_parseFloat",
                    "args": []
                }
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.order.meta._with_expiry.SidePrice_Factory": {
        "castsTo": [
            {
                "rv": "marketsim.types.IOrderGenerator",
                "args": [
                    "marketsim.types.IFunction_Tag",
                    "marketsim.types.IFunction_float"
                ]
            }
        ],
        "properties": {
            "factory": {
                "type": {
                    "rv": "marketsim.types.IOrderGenerator",
                    "args": [
                        "marketsim.types.IFunction_Tag",
                        "marketsim.types.IFunction_float"
                    ]
                }
            },
            "expiry": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.mathutils.rnd.lognormvariate": {
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
                "type": "combine(greater(0.0), _parseFloat)"
            }
        },
        "description": "<div class=\"document\">\n<p>Log normal distribution. If you take the natural logarithm of this distribution, you'll get a normal distribution with mean \u03bc and standard deviation \u03c3. \u03bc can have any value, and \u03c3 must be greater than zero.</p>\n</div>\n"
    },
    "marketsim.order._market.Side_Factory": {
        "castsTo": [
            {
                "rv": "marketsim.types.IOrderGenerator",
                "args": [
                    "marketsim.types.IFunction_Tag"
                ]
            }
        ],
        "properties": {
            "volume": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
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
    "marketsim.strategy.price._lp_side.LiquidityProviderSide_Generated": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy"
        ],
        "properties": {
            "priceDistr": {
                "type": {
                    "rv": "_parseFloat",
                    "args": []
                }
            },
            "initialValue": {
                "type": "_parseFloat"
            },
            "eventGen": {
                "type": "marketsim.types.IEvent"
            },
            "orderFactory": {
                "type": {
                    "rv": "marketsim.types.IOrderGenerator",
                    "args": [
                        "marketsim.types.IFunction_Tag",
                        "marketsim.types.IFunction_float"
                    ]
                }
            },
            "side": {
                "type": "marketsim.Side"
            }
        },
        "description": "<div class=\"document\">\n<p>Liquidity provider for one side has followng parameters:</p>\n<dl class=\"docutils\">\n<dt><strong>Side</strong></dt>\n<dd>side of orders to create (default: Side.Sell)</dd>\n<dt><strong>Initial value</strong></dt>\n<dd>initial price which is taken if orderBook is empty (default: 100)</dd>\n<dt><strong>Time intervals between two order creations</strong></dt>\n<dd>defines intervals of time between order creation\n(default: exponential distribution with \u03bb = 1)</dd>\n<dt><strong>Price of orders to create as multiplier to the current price</strong></dt>\n<dd>defines multipliers for current asset price when price of\norder to create is calculated (default: log normal distribution with\n\u03bc = 0 and \u03c3 = 0.1)</dd>\n<dt><strong>Volume of orders to create</strong></dt>\n<dd>defines volumes of orders to create\n(default: exponential distribution with \u03bb = 1)</dd>\n</dl>\n<p>It wakes up in moments of time given by <em>creationIntervalDistr</em>, checks\nthe last best price of orders in the corresponding queue, takes <em>initialValue</em>\nif it is empty, multiplies it by a value taken from <em>priceDistr</em> to obtain price\nof the order to create, calculates order volume using <em>volumeDistr</em>, creates\nan order via <em>orderFactoryT(side)</em> and tells the trader to send it.</p>\n</div>\n"
    },
    "marketsim.timeserie.VolumeLevels": {
        "castsTo": [
            "marketsim.timeserie.ToRecord"
        ],
        "properties": {
            "graph": {
                "type": "marketsim.types.IGraph"
            },
            "_digits": {
                "hidden": true,
                "type": "_parseInt"
            },
            "source": {
                "type": "marketsim.types.IObservable_object"
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
            },
            "_smooth": {
                "hidden": true,
                "type": "_parseInt"
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
    "marketsim.ops.Sqrt": {
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
    "marketsim.observable._ma.MA": {
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
    "marketsim.order._limit.Side_Price_Factory": {
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
    "marketsim.observable._trader.PendingVolume": {
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
    "marketsim.ops.Sqr": {
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
    "marketsim.order._limit.AdaptLimit": {
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
            }
        ],
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
    "marketsim.strategy.adaptive.weight.efficiencyTrend": {
        "castsTo": [
            {
                "rv": "marketsim.types.IFunction_float",
                "args": [
                    "marketsim.types.IAccount"
                ]
            }
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.observable._trader.OnTraded": {
        "castsTo": [
            "marketsim.types.IEvent"
        ],
        "properties": {
            "trader": {
                "type": "marketsim.types.ITrader"
            }
        },
        "description": "<div class=\"document\">\n<p>Multicast event that is fired once a trade is done by <em>trader</em></p>\n</div>\n"
    },
    "marketsim.observable._trader.volume_traded": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "trader": {
                "type": "marketsim.types.IAccount"
            }
        },
        "description": "<div class=\"document\">\n<p>Returns trader's position (i.e. number of assets traded)</p>\n</div>\n"
    },
    "marketsim.mathutils.rnd.paretovariate": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "Alpha": {
                "type": "combine(greater(0.0), _parseFloat)"
            }
        },
        "description": "<div class=\"document\">\n<p>Pareto distribution. \u03b1 is the shape parameter.</p>\n</div>\n"
    },
    "marketsim.strategy.v0._rsi.RelativeStrengthIndexSide": {
        "castsTo": [
            {
                "rv": "marketsim.Side",
                "args": []
            }
        ],
        "properties": {
            "threshold": {
                "type": "_parseFloat"
            },
            "rsi": {
                "type": "marketsim.types.IFunction_float"
            },
            "orderBook": {
                "type": "marketsim.types.IOrderBook"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.strategy.v0._two_averages.TwoAverages": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy"
        ],
        "properties": {
            "ewma_alpha2": {
                "type": "combine(greater_or_equal(0.0), _parseFloat)"
            },
            "ewma_alpha1": {
                "type": "combine(greater_or_equal(0.0), _parseFloat)"
            },
            "volumeDistr": {
                "type": {
                    "rv": "_parseFloat",
                    "args": []
                }
            },
            "creationIntervalDistr": {
                "type": {
                    "rv": "_parseFloat",
                    "args": []
                }
            },
            "threshold": {
                "type": "combine(greater_or_equal(0.0), _parseFloat)"
            },
            "orderFactory": {
                "type": {
                    "rv": {
                        "rv": "marketsim.types.IOrder",
                        "args": [
                            "_parseFloat"
                        ]
                    },
                    "args": [
                        "marketsim.Side"
                    ]
                }
            }
        },
        "description": "<div class=\"document\">\n<p>Two averages strategy compares two averages of price of the same asset but\nwith different parameters ('slow' and 'fast' averages) and when\nthe first is greater than the second one it buys,\nwhen the first is lower than the second one it sells</p>\n<p>It has following parameters:</p>\n<dl class=\"docutils\">\n<dt><strong>Average 1</strong></dt>\n<dd>functional used to obtain the first average\n(defaut: expenentially weighted moving average with \u03b1 = 0.15)</dd>\n<dt><strong>&amp;alpha; for moving average 1</strong></dt>\n<dd>parameter \u03b1 for the first exponentially weighted moving average\n(default: 0.15.)</dd>\n<dt><strong>&amp;alpha; for moving average 2</strong></dt>\n<dd>parameter \u03b1 for the second exponentially weighted moving average\n(default: 0.015.)</dd>\n<dt><strong>Threshold</strong></dt>\n<dd>threshold when the trader starts to act (default: 0.)</dd>\n<dt><strong>Volume of orders to create</strong></dt>\n<dd>defines volumes of orders to create\n(default: exponential distribution with \u03bb = 1)</dd>\n<dt><strong>Time intervals between two order creations</strong></dt>\n<dd>defines intervals of time between order creation\n(default: exponential distribution with \u03bb = 1)</dd>\n</dl>\n</div>\n"
    },
    "marketsim.strategy.adaptive._account.account": {
        "castsTo": [
            {
                "rv": "marketsim.types.IAccount",
                "args": [
                    "marketsim.types.ISingleAssetStrategy"
                ]
            }
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.order._market.SignedVolume_Factory": {
        "castsTo": [
            {
                "rv": "marketsim.types.IOrderGenerator",
                "args": [
                    "marketsim.types.IFunction_SignedVolume"
                ]
            }
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.strategy.adaptive.weight.atanpow": {
        "castsTo": [
            {
                "rv": "marketsim.types.IFunction_float",
                "args": [
                    "marketsim.types.IFunction_float"
                ]
            }
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.parts.side._cross_avg.TwoAverages_Generated": {
        "castsTo": [
            {
                "rv": "marketsim.Side",
                "args": []
            },
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_Tag",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "ewma_alpha2": {
                "type": "combine(greater_or_equal(0.0), _parseFloat)"
            },
            "threshold": {
                "type": "combine(greater_or_equal(0.0), _parseFloat)"
            },
            "ewma_alpha1": {
                "type": "combine(greater_or_equal(0.0), _parseFloat)"
            },
            "orderBook": {
                "type": "marketsim.types.IOrderBook"
            },
            "impl": {
                "collapsed": true,
                "type": "marketsim.types.IFunction_Tag"
            }
        },
        "description": "<div class=\"document\">\n<p>Two averages is a signal that compares two averages of price of the same asset but\nwith different parameters ('slow' and 'fast' averages) and when\nthe first is greater than the second one it buys,\nwhen the first is lower than the second one it sells</p>\n<p>It has following parameters:</p>\n<dl class=\"docutils\">\n<dt><strong>&amp;alpha; for moving average 1</strong></dt>\n<dd>parameter \u03b1 for the first exponentially weighted moving average\n(default: 0.15.)</dd>\n<dt><strong>&amp;alpha; for moving average 2</strong></dt>\n<dd>parameter \u03b1 for the second exponentially weighted moving average\n(default: 0.015.)</dd>\n<dt><strong>Threshold</strong></dt>\n<dd>threshold when the trader starts to act (default: 0.)</dd>\n</dl>\n</div>\n"
    },
    "marketsim.order.meta._floating_price.Side_Factory": {
        "castsTo": [
            {
                "rv": "marketsim.types.IOrderGenerator",
                "args": [
                    "marketsim.types.IFunction_Tag"
                ]
            }
        ],
        "properties": {
            "price": {
                "type": "marketsim.types.IObservable_float"
            },
            "factory": {
                "type": "marketsim.types.IFunction_IFunction_IOrderGenerator_IFunction_float_IFunction_Tag"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.observable._orderbook.MidPrice_Generated": {
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
            "orderBook": {
                "type": "marketsim.types.IOrderBook"
            }
        },
        "description": "<div class=\"document\">\n<p>Arithmetic mean of ask and bid price of an asset</p>\n</div>\n"
    },
    "marketsim.observable._orderbook.volume_levels": {
        "castsTo": [
            "marketsim.types.IFunction_IVolumeLevels"
        ],
        "properties": {
            "volumeCount": {
                "type": "_parseInt"
            },
            "side": {
                "type": "marketsim.Side"
            },
            "orderbook": {
                "type": "marketsim.types.IOrderBook"
            },
            "volumeDelta": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.parts.side._mean_reversion.MeanReversion_Generated": {
        "castsTo": [
            {
                "rv": "marketsim.Side",
                "args": []
            },
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_Tag",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "ewma_alpha": {
                "type": "combine(greater_or_equal(0.0), _parseFloat)"
            },
            "orderBook": {
                "type": "marketsim.types.IOrderBook"
            },
            "impl": {
                "collapsed": true,
                "type": "marketsim.types.IFunction_Tag"
            }
        },
        "description": "<div class=\"document\">\n<p>Mean reversion strategy believes that asset price should return to its average value.\nIt estimates this average using some functional and\nif the current asset price is lower than the average\nit buys the asset and if the price is higher it sells the asset.</p>\n<p>It has following parameters:</p>\n<dl class=\"docutils\">\n<dt><strong>&amp;alpha; for moving average</strong></dt>\n<dd>\u03b1 for exponentially weighted moving average\n(default: 0.15)</dd>\n</dl>\n</div>\n"
    },
    "marketsim.orderbook._remote.Remote": {
        "castsTo": [
            "marketsim.types.IOrderBook"
        ],
        "properties": {
            "link": {
                "type": "marketsim.remote.TwoWayLink"
            },
            "orderbook": {
                "type": "marketsim.types.IOrderBook"
            },
            "timeseries": {
                "collapsed": true,
                "type": {
                    "elementType": "marketsim.timeserie.ToRecord"
                }
            }
        },
        "description": "<div class=\"document\">\n<p>Represent an <em>orderbook</em> from point of view of a remote trader connected\nto the market by means of a <em>link</em> that introduces some latency in information propagation</p>\n</div>\n"
    },
    "marketsim.orderbook._proxy.OfTrader": {
        "castsTo": [
            "marketsim.types.IOrderBook"
        ],
        "properties": {
            "Trader": {
                "type": "marketsim.types.ISingleAssetTrader"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.orderbook._proxy.Queue": {
        "castsTo": [
            "marketsim.types.IOrderQueue"
        ],
        "properties": {
            "side": {
                "type": "marketsim.Side"
            },
            "orderbook": {
                "type": "marketsim.types.IOrderBook"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.order.meta._stoploss.SidePrice_Factory": {
        "castsTo": [
            {
                "rv": "marketsim.types.IOrderGenerator",
                "args": [
                    "marketsim.types.IFunction_Tag",
                    "marketsim.types.IFunction_float"
                ]
            }
        ],
        "properties": {
            "maxloss": {
                "type": "marketsim.types.IFunction_float"
            },
            "factory": {
                "type": {
                    "rv": "marketsim.types.IOrderGenerator",
                    "args": [
                        "marketsim.types.IFunction_Tag",
                        "marketsim.types.IFunction_float"
                    ]
                }
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.strategy._array.Array": {
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
    "marketsim.strategy.position._bollinger.Bollinger_linear_Generated": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy"
        ],
        "properties": {
            "alpha": {
                "type": "combine(greater_or_equal(0.0), _parseFloat)"
            },
            "k": {
                "type": "marketsim.types.IFunction_float"
            },
            "orderFactory": {
                "type": {
                    "rv": "marketsim.types.IOrderGenerator",
                    "args": [
                        "marketsim.types.IFunction_SignedVolume"
                    ]
                }
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.ops.identity": {
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
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.ops.Product": {
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
    "marketsim.ops.Max": {
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
        "description": "<div class=\"document\">\n<p>Function max of the operands</p>\n</div>\n"
    },
    "marketsim.strategy.adaptive.weight.efficiency": {
        "castsTo": [
            {
                "rv": "marketsim.types.IFunction_float",
                "args": [
                    "marketsim.types.IAccount"
                ]
            }
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.observable._stddev.MovingVariance": {
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
    "marketsim.strategy.side._rsi.RSIbis_Generated": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy"
        ],
        "properties": {
            "threshold": {
                "type": "combine(greater_or_equal(0.0), _parseFloat)"
            },
            "alpha": {
                "type": "combine(greater_or_equal(0.0), _parseFloat)"
            },
            "eventGen": {
                "type": "marketsim.types.IEvent"
            },
            "orderFactory": {
                "type": {
                    "rv": "marketsim.types.IOrderGenerator",
                    "args": [
                        "marketsim.types.IFunction_Tag"
                    ]
                }
            },
            "timeframe": {
                "type": "combine(greater_or_equal(0.0), _parseFloat)"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.strategy.v0._noise.Noise": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy"
        ],
        "properties": {
            "sideDistr": {
                "type": {
                    "rv": "_parseInt",
                    "args": []
                }
            },
            "creationIntervalDistr": {
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
                            "_parseFloat"
                        ]
                    },
                    "args": [
                        "marketsim.Side"
                    ]
                }
            },
            "volumeDistr": {
                "type": {
                    "rv": "_parseFloat",
                    "args": []
                }
            }
        },
        "description": "<div class=\"document\">\n<p>Noise strategy is a quite dummy strategy that randomly creates an order\nand sends it to the order book.</p>\n<p>It has following parameters:</p>\n<dl class=\"docutils\">\n<dt><strong>Order factory</strong></dt>\n<dd>order factory function (default: order.Market.T)</dd>\n<dt><strong>Time intervals between two order creations</strong></dt>\n<dd>defines intervals of time between order creation\n(default: exponential distribution with \u03bb = 1)</dd>\n<dt><strong>Function to choose side of order to create</strong></dt>\n<dd>side of orders to create\n(default: discrete uniform distribution P(Sell)=P(Buy)=.5)</dd>\n</dl>\n</div>\n"
    },
    "marketsim.observable._macd.histogram_Generated": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "slow": {
                "type": "combine(greater(0.0), _parseFloat)"
            },
            "fast": {
                "type": "combine(greater(0.0), _parseFloat)"
            },
            "source": {
                "type": "marketsim.types.IObservable_float"
            },
            "timeframe": {
                "type": "combine(greater(0.0), _parseFloat)"
            },
            "updateInterval": {
                "type": "combine(greater(0.0), _parseFloat)"
            },
            "impl": {
                "collapsed": true,
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>Moving average convergence/divergence histogram</p>\n</div>\n"
    },
    "marketsim.orderbook._proxy.Proxy": {
        "castsTo": [
            "marketsim.types.IOrderBook"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.order.meta._ioc.Side_Factory": {
        "castsTo": [
            {
                "rv": "marketsim.types.IOrderGenerator",
                "args": [
                    "marketsim.types.IFunction_Tag"
                ]
            }
        ],
        "properties": {
            "factory": {
                "type": {
                    "rv": "marketsim.types.IOrderGenerator",
                    "args": [
                        "marketsim.types.IFunction_Tag"
                    ]
                }
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.strategy.v0._lp_side.LiquidityProviderSide": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy"
        ],
        "properties": {
            "priceDistr": {
                "type": {
                    "rv": "_parseFloat",
                    "args": []
                }
            },
            "defaultValue": {
                "type": "_parseFloat"
            },
            "orderFactoryT": {
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
            },
            "creationIntervalDistr": {
                "type": {
                    "rv": "_parseFloat",
                    "args": []
                }
            },
            "volumeDistr": {
                "type": {
                    "rv": "_parseFloat",
                    "args": []
                }
            },
            "side": {
                "type": "marketsim.Side"
            }
        },
        "description": "<div class=\"document\">\n<p>Liquidity provider for one side has followng parameters:</p>\n<dl class=\"docutils\">\n<dt><strong>Side</strong></dt>\n<dd>side of orders to create (default: Side.Sell)</dd>\n<dt><strong>Order factory</strong></dt>\n<dd>order factory function (default: order.Limit.T)</dd>\n<dt><strong>Initial value</strong></dt>\n<dd>initial price which is taken if orderBook is empty (default: 100)</dd>\n<dt><strong>Time intervals between two order creations</strong></dt>\n<dd>defines intervals of time between order creation\n(default: exponential distribution with \u03bb = 1)</dd>\n<dt><strong>Price of orders to create as multiplier to the current price</strong></dt>\n<dd>defines multipliers for current asset price when price of\norder to create is calculated (default: log normal distribution with\n\u03bc = 0 and \u03c3 = 0.1)</dd>\n<dt><strong>Volume of orders to create</strong></dt>\n<dd>defines volumes of orders to create\n(default: exponential distribution with \u03bb = 1)</dd>\n</dl>\n<p>It wakes up in moments of time given by <em>creationIntervalDistr</em>, checks\nthe last best price of orders in the corresponding queue, takes <em>initialValue</em>\nif it is empty, multiplies it by a value taken from <em>priceDistr</em> to obtain price\nof the order to create, calculates order volume using <em>volumeDistr</em>, creates\nan order via <em>orderFactoryT(side)</em> and tells the trader to send it.</p>\n</div>\n"
    },
    "marketsim.strategy.side._signal.Signal_Generated": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy"
        ],
        "properties": {
            "threshold": {
                "type": "combine(greater_or_equal(0.0), _parseFloat)"
            },
            "signal": {
                "type": "marketsim.types.IFunction_float"
            },
            "eventGen": {
                "type": "marketsim.types.IEvent"
            },
            "orderFactory": {
                "type": {
                    "rv": "marketsim.types.IOrderGenerator",
                    "args": [
                        "marketsim.types.IFunction_Tag"
                    ]
                }
            }
        },
        "description": "<div class=\"document\">\n<p>Signal strategy listens to some discrete signal\nand when the signal becomes more than some threshold the strategy starts to buy.\nWhen the signal gets lower than -threshold the strategy starts to sell.</p>\n<p>It has following parameters:</p>\n<dl class=\"docutils\">\n<dt><strong>Signal</strong></dt>\n<dd>signal to be listened to (default: RandomWalk)</dd>\n<dt><strong>Threshold</strong></dt>\n<dd>threshold when the trader starts to act (default: 0.7)</dd>\n<dt><strong>Volume of orders to create</strong></dt>\n<dd>defines volumes of orders to create\n(default: exponential distribution with \u03bb = 1)</dd>\n</dl>\n</div>\n"
    },
    "marketsim.observable._orderbook.price_at_volume": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "side": {
                "type": "marketsim.Side"
            },
            "orderbook": {
                "type": "marketsim.types.IOrderBook"
            },
            "volumeAt": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.observable._orderbook.LastTradePrice": {
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
            "orderbook": {
                "type": "marketsim.types.IOrderBook"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.ops.Min": {
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
        "description": "<div class=\"document\">\n<p>Function min of the operands</p>\n</div>\n"
    },
    "marketsim.strategy.v0._periodic.Periodic": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy"
        ],
        "properties": {
            "sideFunc": {
                "type": {
                    "rv": "marketsim.Side",
                    "args": []
                }
            },
            "orderFactory": {
                "type": {
                    "rv": {
                        "rv": "marketsim.types.IOrder",
                        "args": [
                            "_parseFloat"
                        ]
                    },
                    "args": [
                        "marketsim.Side"
                    ]
                }
            },
            "eventGen": {
                "type": "marketsim.types.IEvent"
            },
            "volumeFunc": {
                "type": {
                    "rv": "_parseFloat",
                    "args": []
                }
            }
        },
        "description": "<div class=\"document\">\n<p>Generic periodic strategy that wakes up on events given by <em>eventGen</em>,\nchooses side of order to create using <em>sideFunc</em> and its volume by <em>volumeFunc</em>,\ncreates an order via <em>orderFactory</em> and sends the order to the market using its trader</p>\n<p>Parameters:</p>\n<blockquote>\n<dl class=\"docutils\">\n<dt><strong>Order factory</strong></dt>\n<dd>order factory function (default: order.Limit.T)</dd>\n<dt><strong>Action trigger</strong></dt>\n<dd>Event source making the strategy to wake up</dd>\n<dt><strong>Volume</strong></dt>\n<dd>defines volumes of orders to create\n(default: exponential distribution with \u03bb = 1)</dd>\n<dt><strong>Side</strong></dt>\n<dd>function choosing side of order to create (default: randomSide)</dd>\n</dl>\n</blockquote>\n</div>\n"
    },
    "marketsim.mathutils.rnd.weibullvariate": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "Alpha": {
                "type": "combine(greater(0.0), _parseFloat)"
            },
            "Beta": {
                "type": "combine(greater(0.0), _parseFloat)"
            }
        },
        "description": "<div class=\"document\">\n<p>Weibull distribution. \u03b1 is the scale parameter and \u03b2 is the shape parameter.</p>\n</div>\n"
    },
    "marketsim.strategy.side._trend.TrendFollower_Generated": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy"
        ],
        "properties": {
            "threshold": {
                "type": "combine(greater_or_equal(0.0), _parseFloat)"
            },
            "ewma_alpha": {
                "type": "combine(greater_or_equal(0.0), _parseFloat)"
            },
            "eventGen": {
                "type": "marketsim.types.IEvent"
            },
            "orderFactory": {
                "type": {
                    "rv": "marketsim.types.IOrderGenerator",
                    "args": [
                        "marketsim.types.IFunction_Tag"
                    ]
                }
            }
        },
        "description": "<div class=\"document\">\n<p>Trend follower can be considered as a sort of a signal strategy\nwhere the <em>signal</em> is a trend of the asset.\nUnder trend we understand the first derivative of some moving average of asset prices.\nIf the derivative is positive, the trader buys; if negative - it sells.\nSince moving average is a continuously changing signal, we check its\nderivative at random moments of time given by <em>creationIntervalDistr</em>.</p>\n<p>It has following parameters:</p>\n<dl class=\"docutils\">\n<dt><strong>&amp;alpha; for moving average</strong></dt>\n<dd>parameter \u03b1 for exponentially weighted moving average\n(default: 0.15.)</dd>\n<dt><strong>Threshold</strong></dt>\n<dd>threshold when the trader starts to act (default: 0.)</dd>\n<dt><strong>Time intervals between two order creations</strong></dt>\n<dd>defines intervals of time between order creation\n(default: exponential distribution with \u03bb = 1)</dd>\n<dt><strong>Volume of orders to create</strong></dt>\n<dd>defines volumes of orders to create\n(default: exponential distribution with \u03bb = 1)</dd>\n</dl>\n</div>\n"
    },
    "marketsim.mathutils._average.ewma": {
        "castsTo": [
            "marketsim.types.IUpdatableValue"
        ],
        "properties": {
            "alpha": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n<p>Exponentially weighted moving average</p>\n</div>\n"
    },
    "marketsim.ops.Derivative": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "source": {
                "type": "marketsim.types.IDifferentiable"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.ops.Constant_Tag": {
        "castsTo": [
            {
                "rv": "marketsim.Side",
                "args": []
            },
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
    "marketsim.strategy.side._dependency.Dependency_Generated": {
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
                "type": {
                    "rv": "marketsim.types.IOrderGenerator",
                    "args": [
                        "marketsim.types.IFunction_Tag"
                    ]
                }
            },
            "factor": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n<p>Dependent price strategy believes that the fair price of an asset <em>A</em>\nis completely correlated with price of another asset <em>B</em> and the following relation\nshould be held: <em>PriceA</em> = <em>kPriceB</em>, where <em>k</em> is some factor.\nIt may be considered as a variety of a fundamental value strategy\nwith the exception that it is invoked every the time price of another\nasset <em>B</em> changes.</p>\n<p>It has following parameters:</p>\n<dl class=\"docutils\">\n<dt><strong>Asset to depend on</strong></dt>\n<dd>reference to order book for another asset used to evaluate fair price of our asset</dd>\n<dt><strong>Factor</strong></dt>\n<dd>multiplier to obtain fair asset price from the reference asset price</dd>\n<dt><strong>Volume of orders to create</strong></dt>\n<dd>defines volumes of orders to create\n(default: exponential distribution with \u03bb = 1)</dd>\n</dl>\n</div>\n"
    },
    "marketsim.strategy.adaptive.weight.unit": {
        "castsTo": [
            {
                "rv": "marketsim.types.IFunction_float",
                "args": [
                    "marketsim.types.IAccount"
                ]
            }
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.order._limit.Side_Factory": {
        "castsTo": [
            {
                "rv": "marketsim.types.IOrderGenerator",
                "args": [
                    "marketsim.types.IFunction_Tag"
                ]
            }
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
    "marketsim.parts.side._fv.FundamentalValue_Generated": {
        "castsTo": [
            {
                "rv": "marketsim.Side",
                "args": []
            },
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_Tag",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "fundamentalValue": {
                "type": "marketsim.types.IFunction_float"
            },
            "orderBook": {
                "type": "marketsim.types.IOrderBook"
            },
            "impl": {
                "collapsed": true,
                "type": "marketsim.types.IFunction_Tag"
            }
        },
        "description": "<div class=\"document\">\n<p>If <em>fundamentalValue</em> &gt; bid price then sells,\nif <em>fundamentalValue</em> &lt; ask price then buys</p>\n</div>\n"
    },
    "marketsim.observable._deltalag.DownMovements": {
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
    "marketsim.observable._macd.signal_Generated": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "slow": {
                "type": "combine(greater(0.0), _parseFloat)"
            },
            "fast": {
                "type": "combine(greater(0.0), _parseFloat)"
            },
            "source": {
                "type": "marketsim.types.IObservable_float"
            },
            "timeframe": {
                "type": "combine(greater(0.0), _parseFloat)"
            },
            "updateInterval": {
                "type": "combine(greater(0.0), _parseFloat)"
            },
            "impl": {
                "collapsed": true,
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>Moving average convergence/divergence signal</p>\n</div>\n"
    },
    "marketsim.order._market.MarketFactory": {
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
            }
        ],
        "properties": {},
        "description": "<div class=\"document\">\n<p>Market order of given <em>side</em> and <em>volume</em></p>\n</div>\n"
    },
    "marketsim.observable._efficiency.Efficiency": {
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
        "description": "<div class=\"document\">\n<p>Observes trader's balance as if was cleared (trader's balance if its position was cleared).\nCan be None if there is not enough assets on the market to clear the position.\nThis observable is updated when trader position is changed\n(which is not fair since the asset price change influences on this parameter also)</p>\n</div>\n"
    },
    "marketsim.observable._minmax_eps.MaxEpsilon": {
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
            "epsilon": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>Observable that fires if underlying source value becomes greater previous maximum plus some epsilon</p>\n</div>\n"
    },
    "marketsim.ops.negate": {
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
    "marketsim.observable._stddev.Variance": {
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
    "marketsim.parts.side._signal.Signal_Generated": {
        "castsTo": [
            {
                "rv": "marketsim.Side",
                "args": []
            },
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_Tag",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "threshold": {
                "type": "combine(greater_or_equal(0.0), _parseFloat)"
            },
            "source": {
                "type": "marketsim.types.IFunction_float"
            },
            "impl": {
                "collapsed": true,
                "type": "marketsim.types.IFunction_Tag"
            }
        },
        "description": "<div class=\"document\">\n<p>If <em>signal</em> &gt; <em>threshold</em> buys, if <em>signal</em> &lt; -<em>threshold</em> sells</p>\n</div>\n"
    },
    "marketsim.ops.Less_float": {
        "castsTo": [
            {
                "rv": "__builtin__.bool",
                "args": []
            },
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
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.order.meta._fixed_budget.Factory": {
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
    "marketsim.side_._BuySide": {
        "castsTo": [
            "marketsim.Side"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.observable._orderbook.Spread_Generated": {
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
            "orderBook": {
                "type": "marketsim.types.IOrderBook"
            }
        },
        "description": "<div class=\"document\">\n<p>Difference between ask and bid asset's price</p>\n</div>\n"
    },
    "marketsim.order.meta._iceberg.Side_Factory": {
        "castsTo": [
            {
                "rv": "marketsim.types.IOrderGenerator",
                "args": [
                    "marketsim.types.IFunction_Tag"
                ]
            }
        ],
        "properties": {
            "lotSize": {
                "type": "marketsim.types.IFunction_float"
            },
            "factory": {
                "type": {
                    "rv": "marketsim.types.IOrderGenerator",
                    "args": [
                        "marketsim.types.IFunction_Tag"
                    ]
                }
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.strategy.v0._fv.FundamentalValue": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy"
        ],
        "properties": {
            "creationIntervalDistr": {
                "type": {
                    "rv": "_parseFloat",
                    "args": []
                }
            },
            "fundamentalValue": {
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
                            "_parseFloat"
                        ]
                    },
                    "args": [
                        "marketsim.Side"
                    ]
                }
            },
            "volumeDistr": {
                "type": {
                    "rv": "_parseFloat",
                    "args": []
                }
            }
        },
        "description": "<div class=\"document\">\n<p>Fundamental value strategy believes that an asset should have some specific price\n(<em>fundamental value</em>) and if the current asset price is lower than the fundamental value\nit starts to buy the asset and if the price is higher it starts to sell the asset.</p>\n<p>It has following parameters:</p>\n<dl class=\"docutils\">\n<dt><strong>Order factory</strong></dt>\n<dd>order factory function (default: order.Market.T)</dd>\n<dt><strong>Time intervals between two order creations</strong></dt>\n<dd>defines intervals of time between order creation\n(default: exponential distribution with \u03bb = 1)</dd>\n<dt><strong>Fundamental value</strong></dt>\n<dd>defines fundamental value (default: constant 100)</dd>\n<dt><strong>Volume of orders to create</strong></dt>\n<dd>defines volumes of orders to create\n(default: exponential distribution with \u03bb = 1)</dd>\n</dl>\n</div>\n"
    },
    "marketsim.trader._sa.SingleAsset": {
        "castsTo": [
            "marketsim.types.IAccount",
            "marketsim.types.ISingleAssetTrader",
            "marketsim.types.ITrader"
        ],
        "properties": {
            "amount": {
                "type": "_parseFloat"
            },
            "orderBook": {
                "type": "marketsim.types.IOrderBook"
            },
            "PnL": {
                "type": "_parseFloat"
            },
            "timeseries": {
                "collapsed": true,
                "type": {
                    "elementType": "marketsim.timeserie.ToRecord"
                }
            },
            "strategy": {
                "type": "marketsim.types.ISingleAssetStrategy"
            }
        },
        "description": "<div class=\"document\">\n<p>A trader that trades a single asset on a single market.</p>\n<p>Parameters:</p>\n<dl class=\"docutils\">\n<dt><strong>orderBook</strong></dt>\n<dd>order book for the asset being traded</dd>\n<dt><strong>strategies</strong></dt>\n<dd>array of strategies run by the trader</dd>\n<dt><strong>amount</strong></dt>\n<dd>current position of the trader (number of assets that it owns)</dd>\n<dt><strong>PnL</strong></dt>\n<dd>current trader balance (number of money units that it owns)</dd>\n</dl>\n</div>\n"
    },
    "marketsim.mathutils.rnd.normalvariate": {
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
        "description": "<div class=\"document\">\n<p>Normal distribution. \u03bc is the mean, and \u03c3 is the standard deviation.</p>\n</div>\n"
    },
    "marketsim.ops.Atan": {
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
    "marketsim.strategy.adaptive.weight.chooseTheBest": {
        "castsTo": [
            {
                "rv": {
                    "elementType": "_parseFloat"
                },
                "args": [
                    {
                        "elementType": "_parseFloat"
                    }
                ]
            }
        ],
        "properties": {},
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
    "marketsim.mathutils.rnd.betavariate": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "Alpha": {
                "type": "combine(greater(0.0), _parseFloat)"
            },
            "Beta": {
                "type": "combine(greater(0.0), _parseFloat)"
            }
        },
        "description": "<div class=\"document\">\n<p>Beta distribution. Conditions on the parameters are \u03b1 &gt; 0 and \u03b2 &gt; 0. Returned values range between 0 and 1.</p>\n</div>\n"
    },
    "marketsim.observable._orderbook.TickSize": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "orderbook": {
                "type": "marketsim.types.IOrderBook"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.order.meta._iceberg.SidePrice_Factory": {
        "castsTo": [
            {
                "rv": "marketsim.types.IOrderGenerator",
                "args": [
                    "marketsim.types.IFunction_Tag",
                    "marketsim.types.IFunction_float"
                ]
            }
        ],
        "properties": {
            "lotSize": {
                "type": "marketsim.types.IFunction_float"
            },
            "factory": {
                "type": {
                    "rv": "marketsim.types.IOrderGenerator",
                    "args": [
                        "marketsim.types.IFunction_Tag",
                        "marketsim.types.IFunction_float"
                    ]
                }
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.observable._minmax.Min": {
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
    "marketsim.observable._ewma.EWMA": {
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
        "description": "<div class=\"document\">\n<p>Exponentially weighted moving average</p>\n</div>\n"
    },
    "marketsim.observable._macd.MACD_Generated": {
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
            "slow": {
                "type": "combine(greater(0.0), _parseFloat)"
            },
            "fast": {
                "type": "combine(greater(0.0), _parseFloat)"
            },
            "impl": {
                "collapsed": true,
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>Moving average convergence/divergence</p>\n</div>\n"
    },
    "marketsim.strategy.position._rsi.RSI_linear_Generated": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy"
        ],
        "properties": {
            "alpha": {
                "type": "combine(greater_or_equal(0.0), _parseFloat)"
            },
            "k": {
                "type": "marketsim.types.IFunction_float"
            },
            "orderFactory": {
                "type": {
                    "rv": "marketsim.types.IOrderGenerator",
                    "args": [
                        "marketsim.types.IFunction_SignedVolume"
                    ]
                }
            },
            "timeframe": {
                "type": "combine(greater_or_equal(0.0), _parseFloat)"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.ops.Exp": {
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
    "marketsim.parts.signed_volume._bollinger.Bollinger_linear_Generated": {
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
                "type": "combine(greater_or_equal(0.0), _parseFloat)"
            },
            "k": {
                "type": "marketsim.types.IFunction_float"
            },
            "trader": {
                "type": "marketsim.types.ISingleAssetTrader"
            },
            "impl": {
                "collapsed": true,
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.observable._orderbook.QueueLastTradePrice": {
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
            "orderqueue": {
                "type": "marketsim.types.IOrderQueue"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.strategy.adaptive.weight.clamp0": {
        "castsTo": [
            {
                "rv": "marketsim.types.IFunction_float",
                "args": [
                    "marketsim.types.IFunction_float"
                ]
            }
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.ops.Sub": {
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
    "marketsim.strategy.side._mean_reversion.MeanReversion_Generated": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy"
        ],
        "properties": {
            "ewma_alpha": {
                "type": "combine(greater_or_equal(0.0), _parseFloat)"
            },
            "eventGen": {
                "type": "marketsim.types.IEvent"
            },
            "orderFactory": {
                "type": {
                    "rv": "marketsim.types.IOrderGenerator",
                    "args": [
                        "marketsim.types.IFunction_Tag"
                    ]
                }
            }
        },
        "description": "<div class=\"document\">\n<p>Mean reversion strategy believes that asset price should return to its average value.\nIt estimates this average using some functional and\nif the current asset price is lower than the average\nit buys the asset and if the price is higher it sells the asset.</p>\n<p>It has following parameters:</p>\n<dl class=\"docutils\">\n<dt><strong>Time intervals between two order creations</strong></dt>\n<dd>defines intervals of time between order creation\n(default: exponential distribution with \u03bb = 1)</dd>\n<dt><strong>&amp;alpha; for moving average</strong></dt>\n<dd>\u03b1 for exponentially weighted moving average\n(default: 0.15)</dd>\n<dt><strong>Volume of orders to create</strong></dt>\n<dd>defines volumes of orders to create\n(default: exponential distribution with \u03bb = 1)</dd>\n</dl>\n</div>\n"
    },
    "marketsim.signal.RandomWalk": {
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
            }
        },
        "description": "<div class=\"document\">\n<p>A discrete signal with user-defined increments.</p>\n<p>Parameters:</p>\n<dl class=\"docutils\">\n<dt><strong>initialValue</strong></dt>\n<dd>initial value of the signal (default: 0)</dd>\n<dt><strong>deltaDistr</strong></dt>\n<dd>increment function (default: normal distribution with \u03bc = 0, \u03c3 = 1)</dd>\n<dt><strong>intervalDistr</strong></dt>\n<dd>defines intervals between signal updates\n(default: exponential distribution with \u03bb = 1)</dd>\n</dl>\n</div>\n"
    },
    "marketsim.order.meta._with_expiry.Side_Factory": {
        "castsTo": [
            {
                "rv": "marketsim.types.IOrderGenerator",
                "args": [
                    "marketsim.types.IFunction_Tag"
                ]
            }
        ],
        "properties": {
            "factory": {
                "type": {
                    "rv": "marketsim.types.IOrderGenerator",
                    "args": [
                        "marketsim.types.IFunction_Tag"
                    ]
                }
            },
            "expiry": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.ops.Sum": {
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
    "marketsim.strategy._market_data.MarketData_Generated": {
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
                "type": "combine(greater(0.0), _parseFloat)"
            }
        },
        "description": "<div class=\"document\">\n<p>A Strategy that allows to drive the asset price based on historical market data\nby creating large volume orders for the given price.</p>\n<p>Every time step of 1 in the simulation corresponds to a 1 day in the market data.</p>\n<p>At each time step the previous Limit Buy/Sell orders are cancelled and new ones\nare created based on the next price of the market data.</p>\n<dl class=\"docutils\">\n<dt><a href=\"#id1\"><span class=\"problematic\" id=\"id2\">|ticker|</span></a></dt>\n<dd>Ticker of the asset</dd>\n<dt><a href=\"#id3\"><span class=\"problematic\" id=\"id4\">|start|</span></a></dt>\n<dd>Start date in DD-MM-YYYY format</dd>\n<dt><a href=\"#id5\"><span class=\"problematic\" id=\"id6\">|end|</span></a></dt>\n<dd>End date in DD-MM-YYYY format</dd>\n<dt>\u03b4</dt>\n<dd>Price difference between orders placed and underlying quotes</dd>\n<dt><a href=\"#id7\"><span class=\"problematic\" id=\"id8\">|volume|</span></a></dt>\n<dd>Volume of Buy/Sell orders. Should be large compared to the volumes of other traders.</dd>\n</dl>\n<div class=\"system-messages section\">\n<h1>Docutils System Messages</h1>\n<div class=\"system-message\" id=\"id1\">\n<p class=\"system-message-title\">System Message: ERROR/3 (<tt class=\"docutils\">&lt;string&gt;</tt>, line 118); <em><a href=\"#id2\">backlink</a></em></p>\nUndefined substitution referenced: &quot;ticker&quot;.</div>\n<div class=\"system-message\" id=\"id3\">\n<p class=\"system-message-title\">System Message: ERROR/3 (<tt class=\"docutils\">&lt;string&gt;</tt>, line 121); <em><a href=\"#id4\">backlink</a></em></p>\nUndefined substitution referenced: &quot;start&quot;.</div>\n<div class=\"system-message\" id=\"id5\">\n<p class=\"system-message-title\">System Message: ERROR/3 (<tt class=\"docutils\">&lt;string&gt;</tt>, line 124); <em><a href=\"#id6\">backlink</a></em></p>\nUndefined substitution referenced: &quot;end&quot;.</div>\n<div class=\"system-message\" id=\"id7\">\n<p class=\"system-message-title\">System Message: ERROR/3 (<tt class=\"docutils\">&lt;string&gt;</tt>, line 129); <em><a href=\"#id8\">backlink</a></em></p>\nUndefined substitution referenced: &quot;volume&quot;.</div>\n</div>\n</div>\n"
    },
    "marketsim.strategy._generic.Generic": {
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
        "description": "<div class=\"document\">\n<p>Generic strategy that wakes up on events given by <em>eventGen</em>,\ncreates an order via <em>orderFactory</em> and sends the order to the market using its trader</p>\n<p>Parameters:</p>\n<blockquote>\n<dl class=\"docutils\">\n<dt><strong>Order factory</strong></dt>\n<dd>order factory function (default: order.Limit.T)</dd>\n<dt><strong>Action trigger</strong></dt>\n<dd>Event source making the strategy to wake up</dd>\n</dl>\n</blockquote>\n</div>\n"
    },
    "marketsim.remote.Link": {
        "castsTo": [
            "marketsim.remote.Link"
        ],
        "properties": {
            "latency": {
                "type": {
                    "rv": "_parseFloat",
                    "args": []
                }
            }
        },
        "description": "<div class=\"document\">\n<p>Represents latency in information propagation from one agent to another one\n(normally between a trader and a market).\nEnsures that sending packets via a link preserves their order.</p>\n<p>Parameters:</p>\n<dl class=\"docutils\">\n<dt><strong>latency</strong></dt>\n<dd>function called for each packet in order to determine\nwhen it will appear at the destination point</dd>\n</dl>\n</div>\n"
    },
    "marketsim.observable._minmax.Max": {
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
    "marketsim.parts.signed_volume._rsi.RSI_linear_Generated": {
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
                "type": "combine(greater_or_equal(0.0), _parseFloat)"
            },
            "k": {
                "type": "marketsim.types.IFunction_float"
            },
            "trader": {
                "type": "marketsim.types.ISingleAssetTrader"
            },
            "impl": {
                "collapsed": true,
                "type": "marketsim.types.IFunction_float"
            },
            "timeframe": {
                "type": "combine(greater_or_equal(0.0), _parseFloat)"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.strategy.v0._dependency.Dependency": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy"
        ],
        "properties": {
            "volumeDistr": {
                "type": {
                    "rv": "_parseFloat",
                    "args": []
                }
            },
            "bookToDependOn": {
                "type": "marketsim.types.IOrderBook"
            },
            "orderFactory": {
                "type": {
                    "rv": {
                        "rv": "marketsim.types.IOrder",
                        "args": [
                            "_parseFloat"
                        ]
                    },
                    "args": [
                        "marketsim.Side"
                    ]
                }
            },
            "factor": {
                "type": "combine(greater(0.0), _parseFloat)"
            }
        },
        "description": "<div class=\"document\">\n<p>Dependent price strategy believes that the fair price of an asset <em>A</em>\nis completely correlated with price of another asset <em>B</em> and the following relation\nshould be held: <em>PriceA</em> = <em>kPriceB</em>, where <em>k</em> is some factor.\nIt may be considered as a variety of a fundamental value strategy\nwith the exception that it is invoked every the time price of another\nasset <em>B</em> changes.</p>\n<p>It has following parameters:</p>\n<dl class=\"docutils\">\n<dt><strong>Order factory</strong></dt>\n<dd>order factory function (default: order.Market.T)</dd>\n<dt><strong>Asset to depend on</strong></dt>\n<dd>reference to order book for another asset used to evaluate fair price of our asset</dd>\n<dt><strong>Factor</strong></dt>\n<dd>multiplier to obtain fair asset price from the reference asset price</dd>\n<dt><strong>Volume of orders to create</strong></dt>\n<dd>defines volumes of orders to create\n(default: exponential distribution with \u03bb = 1)</dd>\n</dl>\n</div>\n"
    },
    "marketsim.observable._orderbook.QueueLastTradeVolume": {
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
            "orderqueue": {
                "type": "marketsim.types.IOrderQueue"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.strategy.side._two_averages.TwoAverages_Generated": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy"
        ],
        "properties": {
            "ewma_alpha2": {
                "type": "combine(greater_or_equal(0.0), _parseFloat)"
            },
            "threshold": {
                "type": "combine(greater_or_equal(0.0), _parseFloat)"
            },
            "ewma_alpha1": {
                "type": "combine(greater_or_equal(0.0), _parseFloat)"
            },
            "eventGen": {
                "type": "marketsim.types.IEvent"
            },
            "orderFactory": {
                "type": {
                    "rv": "marketsim.types.IOrderGenerator",
                    "args": [
                        "marketsim.types.IFunction_Tag"
                    ]
                }
            }
        },
        "description": "<div class=\"document\">\n<p>Two averages strategy compares two averages of price of the same asset but\nwith different parameters ('slow' and 'fast' averages) and when\nthe first is greater than the second one it buys,\nwhen the first is lower than the second one it sells</p>\n<p>It has following parameters:</p>\n<dl class=\"docutils\">\n<dt><strong>&amp;alpha; for moving average 1</strong></dt>\n<dd>parameter \u03b1 for the first exponentially weighted moving average\n(default: 0.15.)</dd>\n<dt><strong>&amp;alpha; for moving average 2</strong></dt>\n<dd>parameter \u03b1 for the second exponentially weighted moving average\n(default: 0.015.)</dd>\n<dt><strong>Threshold</strong></dt>\n<dd>threshold when the trader starts to act (default: 0.)</dd>\n<dt><strong>Volume of orders to create</strong></dt>\n<dd>defines volumes of orders to create\n(default: exponential distribution with \u03bb = 1)</dd>\n<dt><strong>Time intervals between two order creations</strong></dt>\n<dd>defines intervals of time between order creation\n(default: exponential distribution with \u03bb = 1)</dd>\n</dl>\n</div>\n"
    },
    "marketsim.mathutils.rnd.vonmisesvariate": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "Mu": {
                "type": "combine(less(6.28318530718), combine(greater_or_equal(0.0), _parseFloat))"
            },
            "Kappa": {
                "type": "combine(greater_or_equal(0.0), _parseFloat)"
            }
        },
        "description": "<div class=\"document\">\n<p>\u03bc is the mean angle, expressed in radians between 0 and 2|pi|, and \u03ba is the concentration parameter, which must be greater than or equal to zero. If \u03ba is equal to zero, this distribution reduces to a uniform random angle over the range 0 to 2|pi|</p>\n</div>\n"
    },
    "marketsim.strategy.v0._lp.LiquidityProvider": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy"
        ],
        "properties": {
            "priceDistr": {
                "type": {
                    "rv": "_parseFloat",
                    "args": []
                }
            },
            "defaultValue": {
                "type": "_parseFloat"
            },
            "creationIntervalDistr": {
                "type": {
                    "rv": "_parseFloat",
                    "args": []
                }
            },
            "orderFactoryT": {
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
            },
            "volumeDistr": {
                "type": {
                    "rv": "_parseFloat",
                    "args": []
                }
            }
        },
        "description": "<div class=\"document\">\n<p>Liquidity provider is a combination of two LiquidityProviderSide traders\nwith the same parameters but different trading sides.</p>\n<p>It has followng parameters:</p>\n<dl class=\"docutils\">\n<dt><strong>Order factory</strong></dt>\n<dd>order factory function (default: order.Limit.T)</dd>\n<dt><strong>Initial value</strong></dt>\n<dd>initial price which is taken if orderBook is empty (default: 100)</dd>\n<dt><strong>Time intervals between two order creations</strong></dt>\n<dd>defines intervals of time between order creation\n(default: exponential distribution with \u03bb = 1)</dd>\n<dt><strong>Price of orders to create as multiplier to the current price</strong></dt>\n<dd>defines multipliers for current asset price when price of\norder to create is calculated (default: log normal distribution with\n\u03bc = 0 and \u03c3 = 0.1)</dd>\n<dt><strong>Volume of orders to create</strong></dt>\n<dd>defines volumes of orders to create\n(default: exponential distribution with \u03bb = 1)</dd>\n</dl>\n</div>\n"
    },
    "marketsim.ops.Greater_float": {
        "castsTo": [
            {
                "rv": "__builtin__.bool",
                "args": []
            },
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
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.parts.side._trend.TrendFollower_Generated": {
        "castsTo": [
            {
                "rv": "marketsim.Side",
                "args": []
            },
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_Tag",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "threshold": {
                "type": "combine(greater_or_equal(0.0), _parseFloat)"
            },
            "ewma_alpha": {
                "type": "combine(greater_or_equal(0.0), _parseFloat)"
            },
            "orderBook": {
                "type": "marketsim.types.IOrderBook"
            },
            "impl": {
                "collapsed": true,
                "type": "marketsim.types.IFunction_Tag"
            }
        },
        "description": "<div class=\"document\">\n<p>Trend follower can be considered as a sort of a signal\nwhere the <em>signal</em> is a trend of the asset.\nUnder trend we understand the first derivative of some moving average of asset prices.\nIf the derivative is positive, the trader buys; if negative - it sells.\nSince moving average is a continuously changing signal, we check its\nderivative at random moments of time given by <em>creationIntervalDistr</em>.</p>\n<p>It has following parameters:</p>\n<dl class=\"docutils\">\n<dt><strong>&amp;alpha; for moving average</strong></dt>\n<dd>parameter \u03b1 for exponentially weighted moving average\n(default: 0.15.)</dd>\n<dt><strong>Threshold</strong></dt>\n<dd>threshold when the trader starts to act (default: 0.)</dd>\n</dl>\n</div>\n"
    },
    "marketsim.strategy._basic.Empty": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.strategy._market_data.BreaksAtChanges": {
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
    "marketsim.strategy.adaptive._choose_best.ChooseTheBest": {
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
                "type": {
                    "rv": "marketsim.types.IAccount",
                    "args": [
                        "marketsim.types.ISingleAssetStrategy"
                    ]
                }
            },
            "performance": {
                "type": {
                    "rv": "marketsim.types.IFunction_float",
                    "args": [
                        "marketsim.types.IAccount"
                    ]
                }
            }
        },
        "description": "<div class=\"document\">\n<p>A composite strategy initialized with an array of strategies.\nIn some moments of time the most effective strategy\nis chosen and made running; other strategies are suspended.</p>\n<p>Parameters:</p>\n<blockquote>\n<dl class=\"docutils\">\n<dt><strong>strategies</strong></dt>\n<dd>original strategies that can be suspended</dd>\n<dt><strong>Efficiency evaluation function</strong></dt>\n<dd>function estimating is the strategy efficient or not</dd>\n</dl>\n</blockquote>\n</div>\n"
    },
    "marketsim.strategy.adaptive._trade_if_profitable.TradeIfProfitable_Generated": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy"
        ],
        "properties": {
            "performance": {
                "type": {
                    "rv": "marketsim.types.IFunction_float",
                    "args": [
                        "marketsim.types.IAccount"
                    ]
                }
            },
            "account": {
                "type": {
                    "rv": "marketsim.types.IAccount",
                    "args": [
                        "marketsim.types.ISingleAssetStrategy"
                    ]
                }
            },
            "inner": {
                "type": "marketsim.types.ISingleAssetStrategy"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.observable._quote.Quote": {
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
    "marketsim.observable._candlestick.CandleSticks": {
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
    "marketsim.ops.Pow": {
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
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.order.meta._peg.Side_Factory": {
        "castsTo": [
            {
                "rv": "marketsim.types.IOrderGenerator",
                "args": [
                    "marketsim.types.IFunction_Tag"
                ]
            }
        ],
        "properties": {
            "factory": {
                "type": "marketsim.types.IFunction_IFunction_IOrderGenerator_IFunction_float_IFunction_Tag"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.ops.Div": {
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
    "marketsim.parts.side._dependency.Dependency_Generated": {
        "castsTo": [
            {
                "rv": "marketsim.Side",
                "args": []
            },
            "marketsim.types.IEvent",
            "marketsim.types.IFunction_Tag",
            "marketsim.types.IObservable_object"
        ],
        "properties": {
            "bookToDependOn": {
                "type": "marketsim.types.IOrderBook"
            },
            "orderBook": {
                "type": "marketsim.types.IOrderBook"
            },
            "impl": {
                "collapsed": true,
                "type": "marketsim.types.IFunction_Tag"
            },
            "factor": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n<p>Dependent price strategy believes that the fair price of an asset <em>A</em>\nis completely correlated with price of another asset <em>B</em> and the following relation\nshould be held: <em>PriceA</em> = <em>kPriceB</em>, where <em>k</em> is some factor.\nIt may be considered as a variety of a fundamental value strategy\nwith the exception that it is invoked every the time price of another\nasset <em>B</em> changes.</p>\n<p>It has following parameters:</p>\n<dl class=\"docutils\">\n<dt><strong>Asset to depend on</strong></dt>\n<dd>reference to order book for another asset used to evaluate fair price of our asset</dd>\n<dt><strong>Factor</strong></dt>\n<dd>multiplier to obtain fair asset price from the reference asset price</dd>\n</dl>\n</div>\n"
    },
    "marketsim.orderbook._local.Local": {
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
            "timeseries": {
                "collapsed": true,
                "type": {
                    "elementType": "marketsim.timeserie.ToRecord"
                }
            }
        },
        "description": "<div class=\"document\">\n<p>Order book for a single asset in a market.\nMaintains two order queues for orders of different sides</p>\n</div>\n"
    },
    "marketsim.ops.Constant_float": {
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
    "marketsim.strategy.adaptive._multiarmed_bandit.MultiarmedBandit2": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy"
        ],
        "properties": {
            "corrector": {
                "type": {
                    "rv": {
                        "elementType": "_parseFloat"
                    },
                    "args": [
                        {
                            "elementType": "_parseFloat"
                        }
                    ]
                }
            },
            "strategies": {
                "type": {
                    "elementType": "marketsim.types.ISingleAssetStrategy"
                }
            },
            "account": {
                "type": {
                    "rv": "marketsim.types.IAccount",
                    "args": [
                        "marketsim.types.ISingleAssetStrategy"
                    ]
                }
            },
            "normalizer": {
                "type": {
                    "rv": "marketsim.types.IFunction_float",
                    "args": [
                        "marketsim.types.IFunction_float"
                    ]
                }
            },
            "weight": {
                "type": {
                    "rv": "marketsim.types.IFunction_float",
                    "args": [
                        "marketsim.types.IAccount"
                    ]
                }
            }
        },
        "description": "<div class=\"document\">\n<p>A composite strategy initialized with an array of strategies.\nIn some moments of time the most effective strategy\nis chosen and made running; other strategies are suspended.\nThe choice is made randomly among the strategies that have\na positive efficiency trend, weighted by the efficiency value.</p>\n<p>Parameters:</p>\n<blockquote>\n<dl class=\"docutils\">\n<dt><strong>Weight function</strong></dt>\n<dd>weighting scheme for choosing strategies</dd>\n<dt><strong>strategies</strong></dt>\n<dd>original strategies that can be suspended</dd>\n<dt><strong>Efficiency evaluation function</strong></dt>\n<dd>function estimating is the strategy efficient or not</dd>\n<dt><strong>Function creating a strategy used to estimate the original one</strong></dt>\n<dd>function creating phantom strategy used for efficiency estimation</dd>\n</dl>\n</blockquote>\n</div>\n"
    },
    "marketsim.ops._None_Tag": {
        "castsTo": [
            {
                "rv": "marketsim.Side",
                "args": []
            },
            "marketsim.types.IFunction_Tag"
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
        "description": "<div class=\"document\">\n<p>Return a random floating point number <em>N</em> such that <em>low</em> &lt;= <em>N</em> &lt;= <em>high</em> and with the specified <em>mode</em> between those bounds. The <em>low</em> and <em>high</em> bounds default to zero and one. The <em>mode</em> argument defaults to the midpoint between the bounds, giving a symmetric distribution.</p>\n</div>\n"
    },
    "marketsim.order.meta._fixed_budget.Side_Factory": {
        "castsTo": [
            {
                "rv": "marketsim.types.IOrderGenerator",
                "args": [
                    "marketsim.types.IFunction_Tag"
                ]
            }
        ],
        "properties": {
            "budget": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.observable._orderbook.QueueLastPrice": {
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
    "marketsim.remote.TwoWayLink": {
        "castsTo": [
            "marketsim.remote.TwoWayLink"
        ],
        "properties": {
            "down": {
                "type": "marketsim.remote.Link"
            },
            "up": {
                "type": "marketsim.remote.Link"
            }
        },
        "description": "<div class=\"document\">\n<p>Represents latency in information propagation between two agents\n(normally between a trader and a market).\nEnsures that sending packets via links preserves their order.\nHolds two one-way links in opposite directions.</p>\n<p>Parameters:</p>\n<dl class=\"docutils\">\n<dt><strong>up</strong></dt>\n<dd>Forward link (normally from a trader to a market)</dd>\n<dt><strong>down</strong></dt>\n<dd>Backward link (normally from a market to a trader)</dd>\n</dl>\n</div>\n"
    },
    "marketsim.ops.Condition_float": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "ifpart": {
                "type": {
                    "rv": "_parseFloat",
                    "args": []
                }
            },
            "elsepart": {
                "type": {
                    "rv": "_parseFloat",
                    "args": []
                }
            },
            "cond": {
                "type": {
                    "rv": "__builtin__.bool",
                    "args": []
                }
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.mathutils.rnd.randint": {
        "castsTo": [
            {
                "rv": "_parseInt",
                "args": []
            }
        ],
        "properties": {
            "High": {
                "type": "_parseInt"
            },
            "Low": {
                "type": "_parseInt"
            }
        },
        "description": "<div class=\"document\">\n<p>Return a random integer <em>N</em> such that <em>a</em> &lt;= <em>N</em> &lt;= <em>b</em>.</p>\n</div>\n"
    },
    "marketsim.strategy.v0._rsi.RSIEx_Generated": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy"
        ],
        "properties": {
            "threshold": {
                "type": "combine(greater_or_equal(0.0), _parseFloat)"
            },
            "alpha": {
                "type": "combine(greater_or_equal(0.0), _parseFloat)"
            },
            "creationIntervalDistr": {
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
                            "_parseFloat"
                        ]
                    },
                    "args": [
                        "marketsim.Side"
                    ]
                }
            },
            "volumeDistr": {
                "type": {
                    "rv": "_parseFloat",
                    "args": []
                }
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.ops.Equal_float": {
        "castsTo": [
            {
                "rv": "__builtin__.bool",
                "args": []
            },
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
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.mathutils.rnd.gammavariate": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "Alpha": {
                "type": "combine(greater(0.0), _parseFloat)"
            },
            "Beta": {
                "type": "combine(greater(0.0), _parseFloat)"
            }
        },
        "description": "<div class=\"document\">\n<p>Gamma distribution. Conditions on the parameters are \u03b1 &gt; 0 and \u03b2 &gt; 0.</p>\n<p>The probability distribution function is:</p>\n<pre class=\"literal-block\">\n          x ** (alpha - 1) * math.exp(-x / beta)\npdf(x) =  --------------------------------------\n             math.gamma(alpha) * beta ** alpha\n</pre>\n</div>\n"
    },
    "marketsim.js.Graph": {
        "castsTo": [
            "marketsim.types.IGraph"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n<p>Generic 2D graph to be rendered by means of javascript libraries</p>\n</div>\n"
    },
    "marketsim.strategy.v0._signal.Signal": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy"
        ],
        "properties": {
            "threshold": {
                "type": "combine(greater_or_equal(0.0), _parseFloat)"
            },
            "signal": {
                "type": "marketsim.types.IObservable_float"
            },
            "orderFactory": {
                "type": {
                    "rv": {
                        "rv": "marketsim.types.IOrder",
                        "args": [
                            "_parseFloat"
                        ]
                    },
                    "args": [
                        "marketsim.Side"
                    ]
                }
            },
            "volumeDistr": {
                "type": {
                    "rv": "_parseFloat",
                    "args": []
                }
            }
        },
        "description": "<div class=\"document\">\n<p>Signal strategy listens to some discrete signal\nand when the signal becomes more than some threshold the strategy starts to buy.\nWhen the signal gets lower than -threshold the strategy starts to sell.</p>\n<p>It has following parameters:</p>\n<dl class=\"docutils\">\n<dt><strong>Signal</strong></dt>\n<dd>signal to be listened to (default: RandomWalk)</dd>\n<dt><strong>Order factory</strong></dt>\n<dd>order factory function (default: order.Market.T)</dd>\n<dt><strong>Threshold</strong></dt>\n<dd>threshold when the trader starts to act (default: 0.7)</dd>\n<dt><strong>Volume of orders to create</strong></dt>\n<dd>defines volumes of orders to create\n(default: exponential distribution with \u03bb = 1)</dd>\n</dl>\n</div>\n"
    },
    "marketsim.mathutils.rnd.uniform": {
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
        "description": "<div class=\"document\">\n<p>Return a random floating point number <em>N</em> such that <em>a</em> &lt;= <em>N</em> &lt;= <em>b</em> for <em>a</em> &lt;= <em>b</em> and <em>b</em> &lt;= <em>N</em> &lt;= <em>a</em> for <em>b</em> &lt; <em>a</em>.\nThe end-point value <em>b</em> may or may not be included in the range depending on floating-point rounding in the equation <em>a</em> + (<em>b</em>-<em>a</em>) * <em>random()</em>.</p>\n</div>\n"
    },
    "marketsim.observable._cma.CMA": {
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
    "marketsim.observable._rsi.RSI_Generated": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "alpha": {
                "type": "combine(greater(0.0), _parseFloat)"
            },
            "orderBook": {
                "type": "marketsim.types.IOrderBook"
            },
            "impl": {
                "collapsed": true,
                "type": "marketsim.types.IFunction_float"
            },
            "timeframe": {
                "type": "combine(greater_or_equal(0.0), _parseFloat)"
            }
        },
        "description": "<div class=\"document\">\n<p>Relative strength index</p>\n</div>\n"
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
    "marketsim.observable._trader.profit_and_loss": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "trader": {
                "type": "marketsim.types.IAccount"
            }
        },
        "description": "<div class=\"document\">\n<p>Returns balance of the given <em>trader</em></p>\n</div>\n"
    },
    "marketsim.ops._None_float": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IFunction_float"
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.observable._computed.IndicatorBaseT_float": {
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
            "eventSource": {
                "type": "marketsim.types.IEvent"
            },
            "dataSource": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.observable._deltalag.DeltaLag": {
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
    "marketsim.parts.price._lp.LiquidityProvider_Generated": {
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
                "type": {
                    "rv": "_parseFloat",
                    "args": []
                }
            },
            "initialValue": {
                "type": "_parseFloat"
            },
            "orderBook": {
                "type": "marketsim.types.IOrderBook"
            },
            "side": {
                "type": "marketsim.Side"
            },
            "impl": {
                "collapsed": true,
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>Liquidity provider for one side has followng parameters:</p>\n<dl class=\"docutils\">\n<dt><strong>Side</strong></dt>\n<dd>side of orders to create (default: Side.Sell)</dd>\n<dt><strong>Initial value</strong></dt>\n<dd>initial price which is taken if orderBook is empty (default: 100)</dd>\n<dt><strong>Price of orders to create as multiplier to the current price</strong></dt>\n<dd>defines multipliers for current asset price when price of\norder to create is calculated (default: log normal distribution with\n\u03bc = 0 and \u03c3 = 0.1)</dd>\n</dl>\n<p>It checks the last best price of orders in the corresponding queue, takes <em>initialValue</em>\nif it is empty, multiplies it by a value taken from <em>priceDistr</em> to obtain price\nof the order to create</p>\n</div>\n"
    },
    "marketsim.observable._deltalag.UpMovements": {
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
    "marketsim.strategy._market_maker.MarketMaker_Generated": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy"
        ],
        "properties": {
            "volume": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n<dl class=\"docutils\">\n<dt><a href=\"#id1\"><span class=\"problematic\" id=\"id2\">|volume|</span></a></dt>\n<dd>Volume of Buy/Sell orders. Should be large compared to the volumes of other traders.</dd>\n</dl>\n<div class=\"system-messages section\">\n<h1>Docutils System Messages</h1>\n<div class=\"system-message\" id=\"id1\">\n<p class=\"system-message-title\">System Message: ERROR/3 (<tt class=\"docutils\">&lt;string&gt;</tt>, line 109); <em><a href=\"#id2\">backlink</a></em></p>\nUndefined substitution referenced: &quot;volume&quot;.</div>\n</div>\n</div>\n"
    },
    "marketsim.strategy.price._lp.LiquidityProvider_Generated": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy"
        ],
        "properties": {
            "priceDistr": {
                "type": {
                    "rv": "_parseFloat",
                    "args": []
                }
            },
            "defaultValue": {
                "type": "_parseFloat"
            },
            "eventGen": {
                "type": "marketsim.types.IEvent"
            },
            "orderFactory": {
                "type": {
                    "rv": "marketsim.types.IOrderGenerator",
                    "args": [
                        "marketsim.types.IFunction_Tag",
                        "marketsim.types.IFunction_float"
                    ]
                }
            }
        },
        "description": "<div class=\"document\">\n<p>Liquidity provider is a combination of two LiquidityProviderSide traders\nwith the same parameters but different trading sides.</p>\n<p>It has followng parameters:</p>\n<dl class=\"docutils\">\n<dt><strong>Initial value</strong></dt>\n<dd>initial price which is taken if orderBook is empty (default: 100)</dd>\n<dt><strong>Time intervals between two order creations</strong></dt>\n<dd>defines intervals of time between order creation\n(default: exponential distribution with \u03bb = 1)</dd>\n<dt><strong>Price of orders to create as multiplier to the current price</strong></dt>\n<dd>defines multipliers for current asset price when price of\norder to create is calculated (default: log normal distribution with\n\u03bc = 0 and \u03c3 = 0.1)</dd>\n<dt><strong>Volume of orders to create</strong></dt>\n<dd>defines volumes of orders to create\n(default: exponential distribution with \u03bb = 1)</dd>\n</dl>\n</div>\n"
    },
    "marketsim.ops.Log": {
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
    "marketsim.order.meta._iceberg.Side_Price_Factory": {
        "castsTo": [
            "marketsim.types.IFunction_IFunction_IOrderGenerator_IFunction_float_IFunction_Tag"
        ],
        "properties": {
            "lotSize": {
                "type": "marketsim.types.IFunction_float"
            },
            "factory": {
                "type": "marketsim.types.IFunction_IFunction_IOrderGenerator_IFunction_float_IFunction_Tag"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.ops.Condition_Tag": {
        "castsTo": [
            {
                "rv": "marketsim.Side",
                "args": []
            },
            "marketsim.types.IFunction_Tag"
        ],
        "properties": {
            "ifpart": {
                "type": {
                    "rv": "marketsim.Side",
                    "args": []
                }
            },
            "elsepart": {
                "type": {
                    "rv": "marketsim.Side",
                    "args": []
                }
            },
            "cond": {
                "type": {
                    "rv": "__builtin__.bool",
                    "args": []
                }
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.observable._orderbook.QueueWeightedPrice_Generated": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "alpha": {
                "type": "combine(greater(0.0), _parseFloat)"
            },
            "impl": {
                "collapsed": true,
                "type": "marketsim.types.IFunction_float"
            },
            "orderqueue": {
                "type": "marketsim.types.IOrderQueue"
            }
        },
        "description": "<div class=\"document\">\n<p>Moving average of trade prices weighted by volumes of an order queue</p>\n</div>\n"
    },
    "marketsim.order.meta._stoploss.Side_Factory": {
        "castsTo": [
            {
                "rv": "marketsim.types.IOrderGenerator",
                "args": [
                    "marketsim.types.IFunction_Tag"
                ]
            }
        ],
        "properties": {
            "maxloss": {
                "type": "marketsim.types.IFunction_float"
            },
            "factory": {
                "type": {
                    "rv": "marketsim.types.IOrderGenerator",
                    "args": [
                        "marketsim.types.IFunction_Tag"
                    ]
                }
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.observable._minmax_eps.MinEpsilon": {
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
            "epsilon": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>Observable that fires if underlying source value becomes less than previous minimum minus some epsilon</p>\n</div>\n"
    },
    "marketsim.strategy.adaptive.weight.identity": {
        "castsTo": [
            {
                "rv": {
                    "elementType": "_parseFloat"
                },
                "args": [
                    {
                        "elementType": "_parseFloat"
                    }
                ]
            },
            {
                "rv": "marketsim.types.IFunction_float",
                "args": [
                    "marketsim.types.IFunction_float"
                ]
            }
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.parts.signed_volume._desired_position.DesiredPosition_Generated": {
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
                "type": "marketsim.types.IFunction_float"
            },
            "trader": {
                "type": "marketsim.types.ISingleAssetTrader"
            },
            "impl": {
                "collapsed": true,
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.strategy.side._noise.Noise_Generated": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy"
        ],
        "properties": {
            "eventGen": {
                "type": "marketsim.types.IEvent"
            },
            "orderFactory": {
                "type": {
                    "rv": "marketsim.types.IOrderGenerator",
                    "args": [
                        "marketsim.types.IFunction_Tag"
                    ]
                }
            }
        },
        "description": "<div class=\"document\">\n<p>Noise strategy is a quite dummy strategy that randomly creates an order\nand sends it to the order book.</p>\n<p>It has following parameters:</p>\n<dl class=\"docutils\">\n<dt><strong>Time intervals between two order creations</strong></dt>\n<dd>defines intervals of time between order creation\n(default: exponential distribution with \u03bb = 1)</dd>\n<dt><strong>Volume of orders to create</strong></dt>\n<dd>defines volumes of orders to create\n(default: exponential distribution with \u03bb = 1)</dd>\n</dl>\n</div>\n"
    },
    "marketsim.order._market.Factory": {
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
    "marketsim.timeserie.ToRecord": {
        "castsTo": [
            "marketsim.timeserie.ToRecord"
        ],
        "properties": {
            "source": {
                "type": "marketsim.types.IObservable_object"
            },
            "_digits": {
                "hidden": true,
                "type": "_parseInt"
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
    "marketsim.observable._orderbook.QueuePrice": {
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
            "orderqueue": {
                "type": "marketsim.types.IOrderQueue"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.strategy.adaptive.weight.score": {
        "castsTo": [
            {
                "rv": "marketsim.types.IFunction_float",
                "args": [
                    "marketsim.types.IAccount"
                ]
            }
        ],
        "properties": {},
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.strategy.v0._trend.TrendFollower": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy"
        ],
        "properties": {
            "threshold": {
                "type": "combine(greater_or_equal(0.0), _parseFloat)"
            },
            "ewma_alpha": {
                "type": "combine(greater_or_equal(0.0), _parseFloat)"
            },
            "creationIntervalDistr": {
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
                            "_parseFloat"
                        ]
                    },
                    "args": [
                        "marketsim.Side"
                    ]
                }
            },
            "volumeDistr": {
                "type": {
                    "rv": "_parseFloat",
                    "args": []
                }
            }
        },
        "description": "<div class=\"document\">\n<p>Trend follower can be considered as a sort of a signal strategy\nwhere the <em>signal</em> is a trend of the asset.\nUnder trend we understand the first derivative of some moving average of asset prices.\nIf the derivative is positive, the trader buys; if negative - it sells.\nSince moving average is a continuously changing signal, we check its\nderivative at random moments of time given by <em>creationIntervalDistr</em>.</p>\n<p>It has following parameters:</p>\n<dl class=\"docutils\">\n<dt><strong>&amp;alpha; for moving average</strong></dt>\n<dd>parameter \u03b1 for exponentially weighted moving average\n(default: 0.15.)</dd>\n<dt><strong>Order factory</strong></dt>\n<dd>order factory function (default: order.Market.T)</dd>\n<dt><strong>Threshold</strong></dt>\n<dd>threshold when the trader starts to act (default: 0.)</dd>\n<dt><strong>Time intervals between two order creations</strong></dt>\n<dd>defines intervals of time between order creation\n(default: exponential distribution with \u03bb = 1)</dd>\n<dt><strong>Volume of orders to create</strong></dt>\n<dd>defines volumes of orders to create\n(default: exponential distribution with \u03bb = 1)</dd>\n</dl>\n</div>\n"
    },
    "marketsim.observable._stddev.EWMV": {
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
    "marketsim.reference.Reference": {
        "castsTo": [],
        "properties": {
            "name": {
                "type": "identity"
            }
        },
        "description": "<div class=\"document\">\n</div>\n"
    },
    "marketsim.event.Every": {
        "castsTo": [
            "marketsim.types.IEvent"
        ],
        "properties": {
            "intervalFunc": {
                "type": "marketsim.types.IFunction_float"
            }
        },
        "description": "<div class=\"document\">\n<p>Represents a repeating action.</p>\n<p>Parameters:</p>\n<dl class=\"docutils\">\n<dt><em>intervalFunc</em></dt>\n<dd>intervals of time between moments when subscribed listeners are to be called</dd>\n</dl>\n</div>\n"
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
    "marketsim.mathutils._rsi.rsi": {
        "castsTo": [
            "marketsim.types.IUpdatableValue"
        ],
        "properties": {
            "alpha": {
                "type": "_parseFloat"
            }
        },
        "description": "<div class=\"document\">\n<p>Relative strength index</p>\n</div>\n"
    },
    "marketsim.parts.side._random.Random_Generated": {
        "castsTo": [
            {
                "rv": "marketsim.Side",
                "args": []
            },
            "marketsim.types.IFunction_Tag"
        ],
        "properties": {
            "impl": {
                "collapsed": true,
                "type": "marketsim.types.IFunction_Tag"
            }
        },
        "description": "<div class=\"document\">\n<p>Chooses Sell or Buy side with equal probability</p>\n</div>\n"
    },
    "marketsim.mathutils.rnd.expovariate": {
        "castsTo": [
            {
                "rv": "_parseFloat",
                "args": []
            },
            "marketsim.types.IFunction_float"
        ],
        "properties": {
            "Lambda": {
                "type": "combine(greater(0.0), _parseFloat)"
            }
        },
        "description": "<div class=\"document\">\n<p>Exponential distribution. \u03bb is 1.0 divided by the desired mean. It should be greater zero. Returned values range from 0 to positive infinity</p>\n</div>\n"
    },
    "marketsim.strategy.side._fv.FundamentalValue_Generated": {
        "castsTo": [
            "marketsim.types.ISingleAssetStrategy"
        ],
        "properties": {
            "fundamentalValue": {
                "type": {
                    "rv": "_parseFloat",
                    "args": []
                }
            },
            "eventGen": {
                "type": "marketsim.types.IEvent"
            },
            "orderFactory": {
                "type": {
                    "rv": "marketsim.types.IOrderGenerator",
                    "args": [
                        "marketsim.types.IFunction_Tag"
                    ]
                }
            }
        },
        "description": "<div class=\"document\">\n<p>Fundamental value strategy believes that an asset should have some specific price\n(<em>fundamental value</em>) and if the current asset price is lower than the fundamental value\nit starts to buy the asset and if the price is higher it starts to sell the asset.</p>\n<p>It has following parameters:</p>\n<dl class=\"docutils\">\n<dt><strong>Time intervals between two order creations</strong></dt>\n<dd>defines intervals of time between order creation\n(default: exponential distribution with \u03bb = 1)</dd>\n<dt><strong>Fundamental value</strong></dt>\n<dd>defines fundamental value (default: constant 100)</dd>\n<dt><strong>Volume of orders to create</strong></dt>\n<dd>defines volumes of orders to create\n(default: exponential distribution with \u03bb = 1)</dd>\n</dl>\n</div>\n"
    }
}
var interfaces = [
    [
        "_parseInt",
        []
    ],
    [
        {
            "rv": "_parseInt",
            "args": []
        },
        [
            "marketsim.mathutils.rnd.randint"
        ]
    ],
    [
        "marketsim.types.IUpdatableValue",
        [
            "marketsim.mathutils._average.ewma",
            "marketsim.mathutils._rsi.rsi"
        ]
    ],
    [
        {
            "rv": {
                "elementType": "_parseFloat"
            },
            "args": [
                {
                    "elementType": "_parseFloat"
                }
            ]
        },
        [
            "marketsim.strategy.adaptive.weight.identity",
            "marketsim.strategy.adaptive.weight.chooseTheBest"
        ]
    ],
    [
        {
            "rv": "marketsim.types.IOrderGenerator",
            "args": [
                "marketsim.types.IFunction_SignedVolume"
            ]
        },
        [
            "marketsim.order._market.SignedVolume_Factory"
        ]
    ],
    [
        "marketsim.types.IOrderGenerator",
        [
            "marketsim.order._market.Factory",
            "marketsim.order.meta._fixed_budget.Factory"
        ]
    ],
    [
        {
            "elementType": "_parseFloat"
        },
        []
    ],
    [
        "marketsim.types.IAccount",
        [
            "marketsim.trader._proxy.SingleProxy",
            "marketsim.trader._sa.SingleAsset"
        ]
    ],
    [
        "marketsim.types.IFunction_IVolumeLevels",
        [
            "marketsim.observable._computed.IndicatorBaseT_IVolumeLevels",
            "marketsim.observable._orderbook.volume_levels"
        ]
    ],
    [
        "marketsim.types.ISingleAssetTrader",
        [
            "marketsim.trader._proxy.SingleProxy",
            "marketsim.trader._sa.SingleAsset"
        ]
    ],
    [
        {
            "rv": "marketsim.types.IFunction_float",
            "args": [
                "marketsim.types.IFunction_float"
            ]
        },
        [
            "marketsim.strategy.adaptive.weight.clamp0",
            "marketsim.strategy.adaptive.weight.identity",
            "marketsim.strategy.adaptive.weight.atanpow"
        ]
    ],
    [
        "marketsim.remote.Link",
        [
            "marketsim.remote.Link"
        ]
    ],
    [
        {
            "rv": "__builtin__.bool",
            "args": []
        },
        [
            "marketsim.ops.Equal_float",
            "marketsim.ops.Less_float",
            "marketsim.ops.Greater_float"
        ]
    ],
    [
        {
            "elementType": "marketsim.types.IOrderBook"
        },
        []
    ],
    [
        {
            "rv": "marketsim.Side",
            "args": []
        },
        [
            "marketsim.parts.side._signal.Signal_Generated",
            "marketsim.ops._None_Tag",
            "marketsim.parts.side._fv.FundamentalValue_Generated",
            "marketsim.parts.side._cross_avg.TwoAverages_Generated",
            "marketsim.ops.Condition_Tag",
            "marketsim.parts.side._trend.TrendFollower_Generated",
            "marketsim.parts.side._dependency.Dependency_Generated",
            "marketsim.strategy.v0._rsi.RelativeStrengthIndexSide",
            "marketsim.parts.side._mean_reversion.MeanReversion_Generated",
            "marketsim.parts.side._random.Random_Generated",
            "marketsim.ops.Constant_Tag"
        ]
    ],
    [
        {
            "rv": "marketsim.types.IOrderGenerator",
            "args": [
                "marketsim.types.IFunction_Tag"
            ]
        },
        [
            "marketsim.order.meta._ioc.Side_Factory",
            "marketsim.order.meta._stoploss.Side_Factory",
            "marketsim.order._limit.Side_Factory",
            "marketsim.order.meta._with_expiry.Side_Factory",
            "marketsim.order.meta._fixed_budget.Side_Factory",
            "marketsim.order.meta._peg.Side_Factory",
            "marketsim.order.meta._iceberg.Side_Factory",
            "marketsim.order.meta._floating_price.Side_Factory",
            "marketsim.order._market.Side_Factory"
        ]
    ],
    [
        "marketsim.types.IObservable_object",
        [
            "marketsim.observable._orderbook.QueueLastPrice",
            "marketsim.observable._computed.IndicatorBaseT_IVolumeLevels",
            "marketsim.observable._minmax.Min",
            "marketsim.ops.Product",
            "marketsim.ops.Max",
            "marketsim.observable.fold._two_point.TwoPoint",
            "marketsim.ops.Exp",
            "marketsim.parts.signed_volume._bollinger.Bollinger_linear_Generated",
            "marketsim.observable._orderbook.QueueLastTradePrice",
            "marketsim.observable._computed.IndicatorBaseT_float",
            "marketsim.ops.Sub",
            "marketsim.observable._deltalag.DeltaLag",
            "marketsim.signal.RandomWalk",
            "marketsim.ops.Sqrt",
            "marketsim.ops.Sum",
            "marketsim.observable._deltalag.UpMovements",
            "marketsim.observable._orderbook.LastTradePrice",
            "marketsim.ops.Min",
            "marketsim.ops.Log",
            "marketsim.observable._trader.PendingVolume",
            "marketsim.observable._minmax.Max",
            "marketsim.parts.signed_volume._rsi.RSI_linear_Generated",
            "marketsim.ops.Sqr",
            "marketsim.ops.Constant_Tag",
            "marketsim.observable._minmax_eps.MinEpsilon",
            "marketsim.parts.price._lp.LiquidityProvider_Generated",
            "marketsim.parts.side._fv.FundamentalValue_Generated",
            "marketsim.observable._deltalag.DownMovements",
            "marketsim.ops.Greater_float",
            "marketsim.parts.signed_volume._desired_position.DesiredPosition_Generated",
            "marketsim.parts.side._trend.TrendFollower_Generated",
            "marketsim.observable._efficiency.Efficiency",
            "marketsim.observable._minmax_eps.MaxEpsilon",
            "marketsim.strategy._market_data.BreaksAtChanges",
            "marketsim.ops.Equal_float",
            "marketsim.observable._quote.Quote",
            "marketsim.parts.side._signal.Signal_Generated",
            "marketsim.ops.Less_float",
            "marketsim.order.meta._fixed_budget.Factory",
            "marketsim.observable._orderbook.QueuePrice",
            "marketsim.observable._orderbook.Spread_Generated",
            "marketsim.parts.side._cross_avg.TwoAverages_Generated",
            "marketsim.ops.Pow",
            "marketsim.observable._orderbook.QueueLastTradeVolume",
            "marketsim.ops.Div",
            "marketsim.parts.side._dependency.Dependency_Generated",
            "marketsim.observable._orderbook.MidPrice_Generated",
            "marketsim.ops.Atan",
            "marketsim.ops.Constant_float",
            "marketsim.parts.side._mean_reversion.MeanReversion_Generated",
            "marketsim.order._market.Factory",
            "marketsim.observable._candlestick.CandleSticks"
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
        "marketsim.types.IFunction_Tag",
        [
            "marketsim.parts.side._signal.Signal_Generated",
            "marketsim.ops._None_Tag",
            "marketsim.parts.side._fv.FundamentalValue_Generated",
            "marketsim.parts.side._cross_avg.TwoAverages_Generated",
            "marketsim.ops.Condition_Tag",
            "marketsim.parts.side._trend.TrendFollower_Generated",
            "marketsim.parts.side._dependency.Dependency_Generated",
            "marketsim.parts.side._mean_reversion.MeanReversion_Generated",
            "marketsim.parts.side._random.Random_Generated",
            "marketsim.ops.Constant_Tag"
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
        "marketsim.types.ISingleAssetStrategy",
        [
            "marketsim.strategy.v0._mean_reversion.MeanReversion",
            "marketsim.strategy._array.Array",
            "marketsim.strategy.position._bollinger.Bollinger_linear_Generated",
            "marketsim.strategy.v0._lp.LiquidityProvider",
            "marketsim.strategy.v0._signal.Signal",
            "marketsim.strategy.side._rsi.RSIbis_Generated",
            "marketsim.strategy._canceller.Canceller",
            "marketsim.strategy.v0._noise.Noise",
            "marketsim.strategy.price._lp_side.LiquidityProviderSide_Generated",
            "marketsim.strategy.side._mean_reversion.MeanReversion_Generated",
            "marketsim.strategy.v0._lp_side.LiquidityProviderSide",
            "marketsim.strategy.side._signal.Signal_Generated",
            "marketsim.strategy.position._rsi.RSI_linear_Generated",
            "marketsim.strategy._market_data.MarketData_Generated",
            "marketsim.strategy._market_maker.MarketMaker_Generated",
            "marketsim.strategy.v0._periodic.Periodic",
            "marketsim.strategy.v0._rsi.RSIEx_Generated",
            "marketsim.strategy.side._trend.TrendFollower_Generated",
            "marketsim.strategy._basic.Empty",
            "marketsim.strategy.v0._dependency.Dependency",
            "marketsim.strategy.adaptive._multiarmed_bandit.MultiarmedBandit2",
            "marketsim.strategy.side._dependency.Dependency_Generated",
            "marketsim.strategy.side._two_averages.TwoAverages_Generated",
            "marketsim.strategy.price._lp.LiquidityProvider_Generated",
            "marketsim.strategy._generic.Generic",
            "marketsim.strategy.v0._two_averages.TwoAverages",
            "marketsim.strategy.side._noise.Noise_Generated",
            "marketsim.strategy.adaptive._choose_best.ChooseTheBest",
            "marketsim.strategy.adaptive._trade_if_profitable.TradeIfProfitable_Generated",
            "marketsim.strategy.v0._trend.TrendFollower",
            "marketsim.strategy.v0._fv.FundamentalValue",
            "marketsim.strategy.side._fv.FundamentalValue_Generated"
        ]
    ],
    [
        {
            "elementType": "marketsim.types.IGraph"
        },
        []
    ],
    [
        "marketsim.types.IDifferentiable",
        [
            "marketsim.observable._ma.MA",
            "marketsim.observable._cma.CMA",
            "marketsim.observable._ewma.EWMA"
        ]
    ],
    [
        {
            "rv": "marketsim.types.IAccount",
            "args": [
                "marketsim.types.ISingleAssetStrategy"
            ]
        },
        [
            "marketsim.strategy.adaptive._virtual_market.virtualMarket",
            "marketsim.strategy.adaptive._account.account"
        ]
    ],
    [
        "_parseFloat",
        []
    ],
    [
        "marketsim.remote.TwoWayLink",
        [
            "marketsim.remote.TwoWayLink"
        ]
    ],
    [
        "marketsim.types.IObservable_float",
        [
            "marketsim.observable._orderbook.QueueLastPrice",
            "marketsim.observable._minmax.Min",
            "marketsim.ops.Product",
            "marketsim.ops.Max",
            "marketsim.observable.fold._two_point.TwoPoint",
            "marketsim.ops.Exp",
            "marketsim.parts.signed_volume._bollinger.Bollinger_linear_Generated",
            "marketsim.observable._orderbook.QueueLastTradePrice",
            "marketsim.ops.Sub",
            "marketsim.observable._deltalag.DeltaLag",
            "marketsim.signal.RandomWalk",
            "marketsim.ops.Sqrt",
            "marketsim.ops.Sum",
            "marketsim.observable._deltalag.UpMovements",
            "marketsim.observable._orderbook.LastTradePrice",
            "marketsim.ops.Min",
            "marketsim.ops.Log",
            "marketsim.observable._trader.PendingVolume",
            "marketsim.observable._minmax.Max",
            "marketsim.parts.signed_volume._rsi.RSI_linear_Generated",
            "marketsim.ops.Sqr",
            "marketsim.observable._minmax_eps.MinEpsilon",
            "marketsim.parts.price._lp.LiquidityProvider_Generated",
            "marketsim.observable._deltalag.DownMovements",
            "marketsim.ops.Greater_float",
            "marketsim.parts.signed_volume._desired_position.DesiredPosition_Generated",
            "marketsim.observable._efficiency.Efficiency",
            "marketsim.observable._minmax_eps.MaxEpsilon",
            "marketsim.strategy._market_data.BreaksAtChanges",
            "marketsim.ops.Equal_float",
            "marketsim.observable._quote.Quote",
            "marketsim.ops.Less_float",
            "marketsim.observable._orderbook.QueuePrice",
            "marketsim.observable._orderbook.Spread_Generated",
            "marketsim.ops.Pow",
            "marketsim.observable._orderbook.QueueLastTradeVolume",
            "marketsim.ops.Div",
            "marketsim.observable._computed.IndicatorBaseT_float",
            "marketsim.observable._orderbook.MidPrice_Generated",
            "marketsim.ops.Atan",
            "marketsim.ops.Constant_float"
        ]
    ],
    [
        "marketsim.types.IGraph",
        [
            "marketsim.js.Graph"
        ]
    ],
    [
        {
            "rv": "marketsim.types.IOrderGenerator",
            "args": [
                "marketsim.types.IFunction_Tag",
                "marketsim.types.IFunction_float"
            ]
        },
        [
            "marketsim.order.meta._stoploss.SidePrice_Factory",
            "marketsim.order._limit.SidePrice_Factory",
            "marketsim.order.meta._with_expiry.SidePrice_Factory",
            "marketsim.order.meta._iceberg.SidePrice_Factory"
        ]
    ],
    [
        "marketsim.timeserie.ToRecord",
        [
            "marketsim.timeserie.ToRecord",
            "marketsim.timeserie.VolumeLevels"
        ]
    ],
    [
        {
            "rv": "marketsim.types.IFunction_float",
            "args": [
                "marketsim.types.IAccount"
            ]
        },
        [
            "marketsim.strategy.adaptive.weight.efficiency",
            "marketsim.strategy.adaptive.weight.efficiencyTrend",
            "marketsim.strategy.adaptive.weight.unit",
            "marketsim.strategy.adaptive.weight.score"
        ]
    ],
    [
        {
            "elementType": "marketsim.types.ITrader"
        },
        []
    ],
    [
        "marketsim.types.IOrderBook",
        [
            "marketsim.orderbook._proxy.Proxy",
            "marketsim.orderbook._remote.Remote",
            "marketsim.orderbook._local.Local",
            "marketsim.orderbook._proxy.OfTrader"
        ]
    ],
    [
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
        [
            "marketsim.order._market.MarketFactory",
            "marketsim.order._limit.AdaptLimit"
        ]
    ],
    [
        {
            "elementType": "marketsim.types.ISingleAssetStrategy"
        },
        []
    ],
    [
        "combine(greater(0.0), _parseFloat)",
        []
    ],
    [
        "combine(greater_or_equal(0.0), _parseFloat)",
        []
    ],
    [
        "marketsim.types.IEvent",
        [
            "marketsim.observable._orderbook.QueueLastPrice",
            "marketsim.observable._computed.IndicatorBaseT_IVolumeLevels",
            "marketsim.observable._minmax.Min",
            "marketsim.ops.Product",
            "marketsim.ops.Max",
            "marketsim.observable.fold._two_point.TwoPoint",
            "marketsim.ops.Exp",
            "marketsim.parts.signed_volume._bollinger.Bollinger_linear_Generated",
            "marketsim.observable._orderbook.QueueLastTradePrice",
            "marketsim.observable._computed.IndicatorBaseT_float",
            "marketsim.ops.Sub",
            "marketsim.observable._deltalag.DeltaLag",
            "marketsim.event.Every",
            "marketsim.signal.RandomWalk",
            "marketsim.ops.Sqrt",
            "marketsim.ops.Sum",
            "marketsim.observable._deltalag.UpMovements",
            "marketsim.observable._orderbook.LastTradePrice",
            "marketsim.ops.Min",
            "marketsim.ops.Log",
            "marketsim.observable._trader.PendingVolume",
            "marketsim.observable._minmax.Max",
            "marketsim.parts.signed_volume._rsi.RSI_linear_Generated",
            "marketsim.ops.Sqr",
            "marketsim.ops.Constant_Tag",
            "marketsim.observable._minmax_eps.MinEpsilon",
            "marketsim.parts.price._lp.LiquidityProvider_Generated",
            "marketsim.parts.side._fv.FundamentalValue_Generated",
            "marketsim.observable._deltalag.DownMovements",
            "marketsim.observable._trader.OnTraded",
            "marketsim.ops.Greater_float",
            "marketsim.parts.signed_volume._desired_position.DesiredPosition_Generated",
            "marketsim.parts.side._trend.TrendFollower_Generated",
            "marketsim.observable._efficiency.Efficiency",
            "marketsim.observable._minmax_eps.MaxEpsilon",
            "marketsim.strategy._market_data.BreaksAtChanges",
            "marketsim.ops.Equal_float",
            "marketsim.observable._quote.Quote",
            "marketsim.parts.side._signal.Signal_Generated",
            "marketsim.ops.Less_float",
            "marketsim.order.meta._fixed_budget.Factory",
            "marketsim.observable._orderbook.QueuePrice",
            "marketsim.observable._orderbook.Spread_Generated",
            "marketsim.parts.side._cross_avg.TwoAverages_Generated",
            "marketsim.ops.Pow",
            "marketsim.observable._orderbook.QueueLastTradeVolume",
            "marketsim.ops.Div",
            "marketsim.parts.side._dependency.Dependency_Generated",
            "marketsim.observable._orderbook.MidPrice_Generated",
            "marketsim.ops.Atan",
            "marketsim.ops.Constant_float",
            "marketsim.parts.side._mean_reversion.MeanReversion_Generated",
            "marketsim.order._market.Factory",
            "marketsim.observable._candlestick.CandleSticks"
        ]
    ],
    [
        "marketsim.types.IFunction_float",
        [
            "marketsim.observable._orderbook.TickSize",
            "marketsim.observable._orderbook.QueueLastPrice",
            "marketsim.ops.Greater_float",
            "marketsim.observable._minmax.Min",
            "marketsim.observable._ma.MA",
            "marketsim.observable.fold._last.Last",
            "marketsim.ops.identity",
            "marketsim.ops.Product",
            "marketsim.ops.Max",
            "marketsim.observable.fold._two_point.TwoPoint",
            "marketsim.mathutils.rnd.uniform",
            "marketsim.observable._cma.CMA",
            "marketsim.observable._stddev.MovingVariance",
            "marketsim.ops.Exp",
            "marketsim.observable._rsi.RSI_Generated",
            "marketsim.strategy._market_data.BreaksAtChanges",
            "marketsim.parts.signed_volume._bollinger.Bollinger_linear_Generated",
            "marketsim.ops.Condition_float",
            "marketsim.observable._orderbook.QueueLastTradePrice",
            "marketsim.mathutils.rnd.lognormvariate",
            "marketsim.observable._macd.MACD_Generated",
            "marketsim.observable._average.Fold",
            "marketsim.observable._computed.IndicatorBaseT_float",
            "marketsim.ops.Sub",
            "marketsim.observable._trader.profit_and_loss",
            "marketsim.observable._deltalag.DeltaLag",
            "marketsim.ops.Derivative",
            "marketsim.signal.RandomWalk",
            "marketsim.observable._orderbook.price_at_volume",
            "marketsim.ops.Sqrt",
            "marketsim.observable._ewma.EWMA",
            "marketsim.ops.Sum",
            "marketsim.observable._deltalag.UpMovements",
            "marketsim.observable._orderbook.LastTradePrice",
            "marketsim.ops.Min",
            "marketsim.mathutils.rnd.weibullvariate",
            "marketsim.ops._None_float",
            "marketsim.ops.Log",
            "marketsim.observable._trader.PendingVolume",
            "marketsim.observable._minmax.Max",
            "marketsim.parts.signed_volume._rsi.RSI_linear_Generated",
            "marketsim.ops.Sqr",
            "marketsim.observable._orderbook.QueueWeightedPrice_Generated",
            "marketsim.observable._macd.histogram_Generated",
            "marketsim.mathutils.rnd.gammavariate",
            "marketsim.observable._minmax_eps.MinEpsilon",
            "marketsim.mathutils.rnd.vonmisesvariate",
            "marketsim.observable._trader.volume_traded",
            "marketsim.observable._deltalag.DownMovements",
            "marketsim.observable._macd.signal_Generated",
            "marketsim.mathutils.rnd.paretovariate",
            "marketsim.parts.signed_volume._desired_position.DesiredPosition_Generated",
            "marketsim.parts.price._lp.LiquidityProvider_Generated",
            "marketsim.observable._efficiency.Efficiency",
            "marketsim.observable._minmax_eps.MaxEpsilon",
            "marketsim.ops.negate",
            "marketsim.ops.Equal_float",
            "marketsim.observable._quote.Quote",
            "marketsim.observable._stddev.Variance",
            "marketsim.ops.Less_float",
            "marketsim.observable._orderbook.QueuePrice",
            "marketsim.observable._orderbook.Spread_Generated",
            "marketsim.ops.Pow",
            "marketsim.observable._orderbook.QueueLastTradeVolume",
            "marketsim.ops.Div",
            "marketsim.observable._stddev.EWMV",
            "marketsim.mathutils.rnd.normalvariate",
            "marketsim.observable._orderbook.MidPrice_Generated",
            "marketsim.ops.Atan",
            "marketsim.ops.Constant_float",
            "marketsim.mathutils.rnd.expovariate",
            "marketsim.mathutils.rnd.triangular",
            "marketsim.mathutils.rnd.betavariate"
        ]
    ],
    [
        {
            "rv": "_parseFloat",
            "args": []
        },
        [
            "marketsim.observable._orderbook.TickSize",
            "marketsim.observable._orderbook.QueueLastPrice",
            "marketsim.ops.Greater_float",
            "marketsim.observable._minmax.Min",
            "marketsim.observable._ma.MA",
            "marketsim.observable.fold._last.Last",
            "marketsim.ops.identity",
            "marketsim.ops.Product",
            "marketsim.ops.Max",
            "marketsim.observable.fold._two_point.TwoPoint",
            "marketsim.mathutils.rnd.uniform",
            "marketsim.observable._cma.CMA",
            "marketsim.observable._stddev.MovingVariance",
            "marketsim.ops.Exp",
            "marketsim.observable._rsi.RSI_Generated",
            "marketsim.strategy._market_data.BreaksAtChanges",
            "marketsim.parts.signed_volume._bollinger.Bollinger_linear_Generated",
            "marketsim.ops.Condition_float",
            "marketsim.observable._orderbook.QueueLastTradePrice",
            "marketsim.mathutils.rnd.lognormvariate",
            "marketsim.observable._macd.MACD_Generated",
            "marketsim.observable._average.Fold",
            "marketsim.observable._computed.IndicatorBaseT_float",
            "marketsim.ops.Sub",
            "marketsim.observable._trader.profit_and_loss",
            "marketsim.observable._deltalag.DeltaLag",
            "marketsim.ops.Derivative",
            "marketsim.signal.RandomWalk",
            "marketsim.observable._orderbook.price_at_volume",
            "marketsim.ops.Sqrt",
            "marketsim.observable._ewma.EWMA",
            "marketsim.ops.Sum",
            "marketsim.observable._deltalag.UpMovements",
            "marketsim.observable._orderbook.LastTradePrice",
            "marketsim.ops.Min",
            "marketsim.mathutils.rnd.weibullvariate",
            "marketsim.ops._None_float",
            "marketsim.ops.Log",
            "marketsim.observable._trader.PendingVolume",
            "marketsim.observable._minmax.Max",
            "marketsim.parts.signed_volume._rsi.RSI_linear_Generated",
            "marketsim.ops.Sqr",
            "marketsim.observable._orderbook.QueueWeightedPrice_Generated",
            "marketsim.observable._macd.histogram_Generated",
            "marketsim.mathutils.rnd.gammavariate",
            "marketsim.observable._minmax_eps.MinEpsilon",
            "marketsim.mathutils.rnd.vonmisesvariate",
            "marketsim.observable._trader.volume_traded",
            "marketsim.observable._deltalag.DownMovements",
            "marketsim.observable._macd.signal_Generated",
            "marketsim.mathutils.rnd.paretovariate",
            "marketsim.parts.signed_volume._desired_position.DesiredPosition_Generated",
            "marketsim.parts.price._lp.LiquidityProvider_Generated",
            "marketsim.observable._efficiency.Efficiency",
            "marketsim.observable._minmax_eps.MaxEpsilon",
            "marketsim.ops.negate",
            "marketsim.ops.Equal_float",
            "marketsim.observable._quote.Quote",
            "marketsim.observable._stddev.Variance",
            "marketsim.ops.Less_float",
            "marketsim.observable._orderbook.QueuePrice",
            "marketsim.observable._orderbook.Spread_Generated",
            "marketsim.ops.Pow",
            "marketsim.observable._orderbook.QueueLastTradeVolume",
            "marketsim.ops.Div",
            "marketsim.observable._stddev.EWMV",
            "marketsim.mathutils.rnd.normalvariate",
            "marketsim.observable._orderbook.MidPrice_Generated",
            "marketsim.ops.Atan",
            "marketsim.ops.Constant_float",
            "marketsim.mathutils.rnd.expovariate",
            "marketsim.mathutils.rnd.triangular",
            "marketsim.mathutils.rnd.betavariate"
        ]
    ],
    [
        "marketsim.types.ITrader",
        [
            "marketsim.trader._proxy.SingleProxy",
            "marketsim.trader._sa.SingleAsset"
        ]
    ],
    [
        {
            "elementType": "marketsim.timeserie.ToRecord"
        },
        []
    ],
    [
        "marketsim.types.IOrderQueue",
        [
            "marketsim.orderbook._proxy.Queue"
        ]
    ],
    [
        "identity",
        []
    ],
    [
        "marketsim.types.IFunction_IFunction_IOrderGenerator_IFunction_float_IFunction_Tag",
        [
            "marketsim.order._limit.Side_Price_Factory",
            "marketsim.order.meta._iceberg.Side_Price_Factory"
        ]
    ],
    [
        "combine(less(6.28318530718), combine(greater_or_equal(0.0), _parseFloat))",
        []
    ]
]