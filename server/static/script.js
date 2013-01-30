function all() {
   z = ($.ajax({
     url: 'all',
     dataType: 'json',
     async: false
   }));

   return $.parseJSON(z.responseText);
}
function alltimeseries() {
   z = ($.ajax({
     url: 'alltimeseries',
     dataType: 'json',
     async: false
   }));

   return $.parseJSON(z.responseText);
}

function isInteger (s) {
    var isInteger_re     = /^\s*(\+|-)?\d+\s*$/;
    return String(s).search (isInteger_re) != -1
}

function isFloat (s) {
    var isDecimal_re     = /^\s*(\+|-)?((\d+(\.\d+)?)|(\.\d+))\s*$/;
    return String(s).search (isDecimal_re) != -1
}

function _parseInt(x) {
    if (typeof(x) == "string" && !isInteger(x.trim()))
        return NaN;
    return parseInt(x,10);
}

function _parseFloat(x) {
    if (typeof(x) == "string" && !isFloat(x.trim()))
        return NaN;
    return parseFloat(x);
}

function identity(s) { return s; }

function TeXize(s) {
	return "$$" + s + "$$";
}


function isArray(o) {
  return Object.prototype.toString.call(o) === '[object Array]';
}

function map(elements, f) {
    var res = [];
    for (var i=0; i<elements.length; i++)
        res.push(f(elements[i], i));
    return res;
}

function mapDictionaryToArray(dictionary) {
    var result = [];
    for (var key in dictionary) {
        if (dictionary.hasOwnProperty(key)) {
            result.push({ key: key, value: dictionary[key] }); 
        }  
    }

    return result;
}

var dict2array = mapDictionaryToArray;

var INPUT = 0x1;
var ARRAY = 0x2;
var LISTBOX = 0x4;

function isInput(x) {
	return x.val.editor == INPUT;
}

var EMPTYSTR = "";

function hasChangedSign(x) {
	return x.val.initial != x.val.val() ? "*" : "";
}

function ScalarValue(s, checker) {
	var self = this;
	self.initial = s;
	self.val = ko.observable(s);
	self.editor = INPUT;
	self.convertedValue = ko.computed(function (){
		return checker(self.val());
	});
}

function ArrayValue(s) {
	var self = this;
	self.val = ko.observableArray(map(s, function (x,i) {
					return new Property(i, x);
				}));
	
	self.brief = function () {
		return "...";
	}

	self.expanded = self.val;
	
	self.editor = ARRAY;
}

function ObjectValue(s) {
	var self = this;
	self.val = s;
	
	self.brief = function () {
		return self.val.name;
	}

	self.expanded = ko.computed(function() {
		return self.val.fields;
	});
	
	self.editor = LISTBOX;
}

nbsp = "&nbsp;";
spaces = [nbsp];

for (var i=0; i<30; i++) {
	spaces.push(spaces[spaces.length-1]+nbsp);
}

function indentify (s, n) {
	return spaces[n] + s;
} 

function treatAny(value, getObj) {
	if (typeof(value) == 'string'){
		if (value.length > 1 && value[0]=='#' && value[1] != "#") {
			return new ObjectValue(getObj(parseInt(value.substring(1))));
		} else {
			if (value.length > 1 && value[0]=='#' && value[1] == "#") {
				return new ScalarValue(value.substring(1), identity);
			} else {
				return new ScalarValue(value, identity);
			}
		}
	} else if (isArray(value)) {
		return new ArrayValue(map(value, function (x) { return treatAny(x, getObj); }));
	} else {
		return new ScalarValue(value, _parseFloat);
	}	
}

function Property(name, value) {
	var self = this;
	self.name = name;
	self.val = value;
	
	self.isExpanded = ko.observable(false);

	self.expandedView = ko.computed(function() {
		return self.isExpanded() ? self.val.expanded() : [];
	});
}


function Instance(id, src, getObj) {
	var self = this;
	self.id = parseInt(id);
	self.constructor = src[0];
	self.name = src[2];
	self.fields = map(dict2array(src[1]), function (x) { 
		return new Property(x.key, treatAny(x.value, getObj)); 
	});
	
	self.changes = ko.computed(function() {
		var result = [];
		for (var i=0; i < self.fields.length; i++) {
			var f = self.fields[i];
			if (f.val.editor == INPUT && f.val.initial != f.val.val()) {
				result.push([self.id, f.name, f.val.convertedValue()]);
			}
		}
		return result;
	});
}

function TimeSerie(id, label, data) {
	var self = this;
	self.id = id;
	self.label = ko.observable(label);
	self.data = data;
/*	self.rawdata = [];
	self.recompute = ko.observable(false);
	self.data = ko.computed(function (){
		var dummy = self.recompute();
		return self.rawdata;
	})
	self.update = function() {
		$.getJSON('/timeserie/' + self.id, function (data) {
			self.rawdata = data; // later 'data' will be just an update
			self.recompute(!self.recompute());
		 	// drop the timeserie from the server
		})
	}
	self.update(); */
}

function Graph(label, timeseries) {
	var self = this;
	self.label = label;
	self.data = timeseries;
}

function firstChild(e) {
    for (var j=0; j<e.childNodes.length; j++) {
        if (e.childNodes[j].nodeType == 1) {
            return e.childNodes[j];
        }
    }    
    return undefined;
}

function dir(object) {
    stuff = [];
    for (s in object) {
        stuff.push(s);
    }
    stuff.sort();
    return stuff;
}

function AppViewModel() {
	var self = this;
	self.advance = ko.observable(500);
	self.response = ko.observable("");
	self.response(all());
	
	self.original = ko.computed(function () {
		return self.response();
	})
	
	self.parsed = ko.computed(function () {
		var id2obj = {};
		//----------- building new objects
		var original = self.original().objects;
		var getObj = function (id) {
			if (id2obj[id] == undefined) {
				id2obj[id] = new Instance(id, original[id], getObj);
			}
			return id2obj[id];
		}
		
		for (var i in original) {
			id2obj[i] = getObj(i);
		}
		
		var result = {
			"id2obj" : id2obj
		}
		//-------------- traders
		var src_traders = self.original().traders;
		
		self._parsed = result;
		return result;		
	})
	
	
	self.id2obj = function () {
		return self.parsed().id2obj;
	}
	
	self.all = ko.computed(function () {
		var res = [];
		var ids = self.id2obj();
		for (var i in ids) {
			res.push(ids[i]);
		}
		return res;
	})

	self.filteredViewEx = function(startsWith) {
		var result = [];
		var ids = self.id2obj();
		for (var i in ids) {
			var x = ids[i];
			if (x.constructor.indexOf(startsWith) == 0) {
				result.push(x);
			}
		}
		return result;		
	}
	
	self.filteredView = function(startsWith) {
		// to implement through filteredViewEx
		var result = [];
		var ids = self.id2obj();
		for (var i in ids) {
			var x = ids[i];
			if (x.constructor.indexOf(startsWith) == 0) {
				result.push(new Property("", new ObjectValue(x)));
			}
		}
		return result;		
	}
	
	self.graphs = ko.computed(function () {
		var rawtimeseries = self.filteredViewEx("marketsim.js.TimeSerie");
		var ts_data = alltimeseries();
		
		var timeseries = {};
		
		for (var i in rawtimeseries) {
			var t = rawtimeseries[i];
			var ts = new TimeSerie(t.id, t.name, ts_data[t.id]);
			timeseries[ts.id] = ts;		
		}
		
		var rawgraphs = self.filteredViewEx("marketsim.js.Graph");
		
		return map(rawgraphs, function (g) {
			var tss = g.fields[0].val.val();
			var res = [];
			for (var i in tss) {
				var ts = tss[i].val.val; 
				res.push(timeseries[ts.id]);
			}
			return new Graph(g.name, res);
		})
	})
	
	self.entities = ko.computed(function () {
		return [
			["Traders" , "model", self.filteredView("marketsim.trader.")],
			["Order books", "option", self.filteredView("marketsim.orderbook.")],
			["Scheduler", "pricing_method", self.filteredView("marketsim.scheduler.")],
			["Graphs", "pricing_method", self.filteredView("marketsim.js.Graph")],
		];
	})
	
	self.changes = ko.computed(function(){
		var updates = [];
		var all = self.all();
		for (var i=0; i<all.length; i++) {
			var x = all[i].changes();
			for (var j=0; j<x.length; j++) {
				updates.push(x[j]);
			}
		}
		return $.toJSON({'updates' : updates, 
						 'advance' : _parseFloat(self.advance())});
	});
	
	
    self.renderGraph1d = function (elem, graph) {
		var data = map(graph.data, function (ts) {
			return { 'data' : ts.data, 'label' : ts.label() };
		});
        
        for (var i=0; i<elem.length; i++) {
            var e = elem[i];
            if (e.nodeType==1) {
                var ee = firstChild(firstChild(firstChild(firstChild(e))));
                ee.style.width = '1700px'; //self.graphSizeX()+'px';
                ee.style.height = '800px'; //self.graphSizeY()+'px';
                Flotr.draw(ee, data, {
                    legend : {
                        position : 'se',            // Position the legend 'south-east'.
                        backgroundColor : '#D2E8FF' // A light blue background color.
                    },
                    HtmlText : false
                });
            }
        }
    } 
	
	self.submitChanges = function() {
		$.post('/update?'+self.changes(), function (data) {
			self.response($.parseJSON(data)); 
		});
	}
};

viewmodel = new AppViewModel();
