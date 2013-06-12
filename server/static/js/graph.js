/**
 * 	Represents a time serie to be rendered on graph 
 * @param {Instance}    source 	 -- source object for the time serie
 * @param {map<int, list<(float, float)>>} data -- initial data to be rendered 
 */
function TimeSerie(source, initialData) {
	var self = source;
	
	self._data = ko.observable([]);
	
	/**
	 *	Should be the timeserie visible on a graph 
	 */
	self.visible = ko.observable(true);
	
	/**
	 *  Appends updates in the time serie 
 	 *  @param {list<(float, float)>} dataDelta -- list of pair (time, value) to be appended to the time serie
	 */
	self.appendData = function (dataDelta) {
		self._data(self._data().concat(dataDelta));
		self._data.valueHasMutated();
	}

	/**
	 *	Updates time serie from data fetched from server
	 *  @param {map<int, list<(float, float)>>} -- time serie relevant data fetched from server 
	 */	
	self.updateFrom = function (ts_changes) {
		if (ts_changes[self.uniqueId()]) {
			self.appendData(ts_changes[self.uniqueId()]);
		}
	}
	
	self._base_clone = source.clone;
	
	self.clone = function () {
		return TimeSerie(self._base_clone());
	}
	
	if (initialData) {
		self.updateFrom(initialData);
	}
	
	/**
	 *	Resets time serie data 
	 */
	self.resetData = function () {
		self._data([]);
	}
	
	/**
	 *	Returns time serie data to be rendered 
	 */
	self.getData = ko.computed(function () {
		return self._data();
	});
	
	/**
	 *	Returns true iff there is no data to render 
	 */
	self.empty = ko.computed(function () {
		return self._data().length == 0;
	});
	
	self.asFlotr = function () {
		var ts = self;
		var smooth = ts.lookupField("_smooth").impl().serialized() == 1;
		return ts.visible() ? [{ 
			'source' : ts,
			'data' : ts.getData.peek(), 
			'label' : ts.alias.peek(), 
			'name': ts.alias.peek(),
			'volumes' : ts.volumes ? ts.volumes() : undefined,
			'step' : !smooth,
			'type' : smooth ? "spline" : "line",
			'digits':  ts.lookupField('_digits').impl().serialized(),
			'tooltip' : {
				'valueDecimals': ts.lookupField('_digits').impl().serialized()
			}
		}] : [];
	}
	
	return self;
}

var makeTimeSerie = TimeSerie;

function makeVolumeLevels(source, initialData) {
	var self = makeTimeSerie(source, initialData);
	
	self.volumes = function () {
		var vs = self.lookupField("_volumes").impl();
		return map(vs.elements(), function (property) {
			return property.impl().serialized();
		})
	}

	self.asFlotr = function () {
		var ts = self;
		if (!ts.visible()) {
			return [];
		} else {
			var res = [];
			var vs = self.volumes();
			for (var i = 1; i < vs.length; i++) {
				var side_buy = self.lookupField("_isBuy").impl().serialized();
				var rgb = hsvToRgb(side_buy ? 90 : 180, 50, 100 - i / vs.length * 100);
				var c = "#"+(rgb[0]).toString(16)+(rgb[1]).toString(16)+(rgb[2]).toString(16);
				res.push({
					'data' : map(ts.getData.peek(), function (x) {
								return [x[0], x[1][i-1], x[1][i]];
 							 }),
					'name' : ts.alias.peek() + ': ' + vs[i-1] + ' - ' + vs[i],
					'color' : c,
					'type' : 'areasplinerange', 
					'tooltip' : {
						'valueDecimals': ts.lookupField('_digits').impl().serialized()
					}
				});
			}
			return res;
		}
	}
	
	return self;
}

function firstChild(e) {
    for (var j=0; j<e.childNodes.length; j++) {
        if (e.childNodes[j].nodeType == 1) {
            return e.childNodes[j];
        }
    }    
    return undefined;
}

function Graph(source, root) {
	
	var self = source;
	
	/**
	 *	Returns an array of TimeSerie instances held by the graph 
	 */
	self.series = ko.computed(function () {
		var series = [];
		var root_obj = root.root();
		if (root_obj == ""){
			return series;
		}
		function process(fieldName) {
			foreach(root_obj.lookupField(fieldName).impl().elements(), function (trader) {
				foreach(trader.impl().pointee().lookupField("timeseries").impl().elements(), 
				function (timeserie) {
					var graph_id = timeserie.impl().pointee().lookupField('graph').impl().pointee().uniqueId();
					if (graph_id  == self.uniqueId()) {
						series.push(timeserie.impl().pointee());
					}
				})
			})
		}
		process('traders');
		process('orderbooks');
		/*var timeseries = source.lookupField("series").impl().elements();
		return map(timeseries, function (timeserie) {
			return root.id2obj.lookup(timeserie.impl().pointee().uniqueId());
		});*/
		return series;
	});
		
	self.asFlotr = ko.computed(function () {
		var dummy = root.updategraph();
		console.log("asFlotr for " + self.alias());
		return collect(self.series(), function (ts) {
			return ts.asFlotr();
		});		
	})
	
	self.empty = ko.computed(function () {
		return all(self.series(), function (timeserie) {
			return timeserie.empty();
		});
	});
	
	self._base_clone = source.clone;
	
	self.clone = function () {
		return Graph(self._base_clone(), root);
	}
	
	return self;
}

var makeGraph = Graph;

function viewport()
{
	var e = window
	  , a = 'inner';
	if ( !( 'innerWidth' in window ) )
	{
		a = 'client';
		e = document.documentElement || document.body;
	}
	return { width : e[ a+'Width' ] , height : e[ a+'Height' ] }
}

ko.bindingHandlers.flotr = {
    update:function (element, valueAccessor, allBindingsAccessor, viewModel) {
    	
		var data = ko.utils.unwrapObservable(valueAccessor());
		var metrics = viewport();
        
        element.style.width = Math.round(metrics.width*0.89)+'px';
        element.style.height = Math.round(metrics.height*0.9)+'px';
        
        Flotr.draw(element, data, {
            legend : {
                position : 'se',            // Position the legend 'south-east'.
                backgroundColor : '#D2E8FF' // A light blue background color.
            },
            HtmlText : false
        });
    }
}

ko.bindingHandlers.highstocks = {
    update:function (element, valueAccessor, allBindingsAccessor, viewModel) {
    	
		var data = ko.utils.unwrapObservable(valueAccessor());
		
        new Highcharts.StockChart({
        	chart: {
        		renderTo: element.id,
        		type: 'line',
        		animation: false
        	},
	        tooltip: {
	            shared: true,
	            useHTML: true,
	            formatter: function () {
			        var s = '<b>t = '+ this.x.toFixed(2) +'</b><table>';
			
			        $.each(this.points, function(i, point) {
			        	
			            s += '<tr><td style="color: '+point.series.color+'">'+ point.series.name 
			            +'</td><td style="text-align: right"><b> '+
			                point.y.toFixed(point.series.tooltipOptions.valueDecimals) + '</b></td></tr>';
			         });
			         
			         s += "</table>"
			
			        return s;
	            }
	        },
        	series: data,
		    rangeSelector: {
		    	enabled: false
		    },
		    navigator : {
		        xAxis: {        
		            labels: {
		                format: '{value}'
		            }
		        },
		    },	        
	        xAxis: {        
	            labels: {
	                format: '{value}'
	            }
	        },
	        legend: {
	        	enabled: true
	        }, 
	        credits: {
	        	enabled: false
	        },
	        plotOptions: {
	            series: {
                	animation: false
            	},
            	line: {
	        		dataGrouping: {
	        			groupPixelWidth: 2,
	        			approximation: "open"
	        		}
	        	}
	        }	        	
        });
    }
}