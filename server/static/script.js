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

function isReferenceType(typename) {
	return (typename.indexOf("marketsim.orderbook.") == 0 ||
			typename.indexOf("marketsim.scheduler.") == 0 ||
			typename.indexOf("marketsim.js.Graph") == 0 ||
			typename.indexOf("marketsim.trader.") == 0 ||
			typename.indexOf("marketsim.js.TimeSerie") == 0);
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
        throw "should be an integer value";
    return parseInt(x,10);
}

function _parseFloat(x) {
    if (typeof(x) == "string" && !isFloat(x.trim()))
        throw "should be a floating point value";
    return parseFloat(x);
}

function less(y) {
    return function (x) {
    	if (!(x < y)) {
    		throw "should be less than " + y;
    	}
        return x;
    }
}

function less_or_equal(y) {
    return function (x) {
    	if (!(x <= y)) {
    		throw "should be less or equal to " + y;
    	}
        return x;
    }
}

function greater(y) {
    return function (x) {
    	if (!(x > y)) {
    		throw "should be greater than " + y;
    	}
        return x;
    }
}

function greater_or_equal(y) {
    return function (x) {
    	if (!(x >= y)) {
    		throw "should be greater or equal to " + y;
    	}
        return x;
    }
}

function combine(f,g) {
    return function (x) {
        return f(g(x));
    }
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
	return x.val.initial() != x.val.val() ? "*" : "";
}

function isnan(x) {
	return typeof(x) != "string" && isNaN(x);
}

function ScalarValue(s, checker) {
	var self = this;
	self.initial = ko.observable(s);
	self.val = ko.observable(s);
	self.editor = INPUT;
	self.errormsg = ko.observable("");
	self.convertedValue = ko.computed(function (){
		try {
			var r = checker(self.val());
			self.errormsg("");
			return r;
		} catch (err) {
			self.errormsg(err);
			return NaN;
		}
	});
	self.hasError = ko.computed(function () {
		return isnan(self.convertedValue());
	})
}

function ArrayValue(s) {
	var self = this;
	self.val = ko.observableArray(map(s, function (x,i) {
					return new Property(i, x, true);
				}));
	
	self.brief = function () {
		return "...";
	}
	
	self.isReference = function () { return false; }

	self.hasError = ko.computed(function () {
		var elements = self.val();
		for (var i in elements) {
			if (elements[i].val.hasError()) {
				return true;
			}
		}
		return false;
	})

	self.expanded = self.val;
	
	self.editor = ARRAY;
}

function ObjectValue(s, constraint, root, expandReference) {
	var self = this;
	self.pointee = ko.observable(s);
	self.root = root;
	self.constraint = constraint == undefined ? "" : constraint;
	
	self._dummy = ko.observable(false);
	
	self.options = ko.computed(function (){
		self._dummy();
		var myAlias = self.pointee().alias();
		var candidates = self.root.getCandidates(self.constraint);
		console.log('updating options for ' + myAlias);
		
		for (var i in candidates) {
			var c = candidates[i];
			if (c.alias.peek() == myAlias) {
				candidates[i] = self.pointee();
			}
		}
		return candidates;
	});
	
	self.updateOptions = function () {
		self._dummy(!self._dummy());
	}
	
	self.currentOption = ko.observable(self.pointee().uniqueId());
	
	self.pointee.subscribe(function (new_pointee) {
		self.currentOption(new_pointee.uniqueId());
	})
	
	self._lock = false;
	
	function updateCurrentOption(id) {
		if (self._lock) {
			return;
		}
		self._lock = true;
		
		console.log('option changed: ' + id);
		var options = self.options();
		for (var i in options) { // it is better to have a true mapping
			if (options[i].uniqueId() == id) {
				var freshly_created = root.getObj(options[i].uniqueId());
				console.log('created: ' + freshly_created.uniqueId() + '/' + i);
				self.pointee(freshly_created);
			}
		}
		
		self._lock = false;
	}
	
	self.currentOption.subscribe(updateCurrentOption);	

	self.expanded = ko.computed(function() {
		return (self.pointee().isReference() && !expandReference) ? [] : self.pointee().fields;
	});
	
	self.hasError = ko.computed(function () {
		var fields = self.pointee().fields;
		for (var i in fields) {
			if (fields[i].val.hasError()) {
				return true;
			}
		}
		return false;
	})
	
	
	self.editor = LISTBOX;
	self.objectref = true;
}

nbsp = "&nbsp;";
spaces = [nbsp];

for (var i=0; i<30; i++) {
	spaces.push(spaces[spaces.length-1]+nbsp);
}

function indentify (s, n) {
	return spaces[n] + s;
} 

function treatAny(value, constraint, root) {
	if (typeof(value) == 'string'){
		if (value.length > 1 && value[0]=='#' && value[1] != "#") {
			return new ObjectValue(root.getObj(parseInt(value.substring(1))), constraint, root, false);
		} else {
			if (value.length > 1 && value[0]=='#' && value[1] == "#") {
				return new ScalarValue(value.substring(1), identity);
			} else {
				return new ScalarValue(value, identity);
			}
		}
	} else if (isArray(value)) {
		var elementType = constraint.elementType;
		return new ArrayValue(map(value, function (x) { return treatAny(x, elementType, root); }));
	} else {
		//console.log(constraint);
		var s = eval(constraint);
		return new ScalarValue(value, s);
	}	
}

function Property(name, value, expanded) {
	var self = this;
	self.name = name;
	self.val = value;
	
	var expandable = value.editor != INPUT && value.expanded().length;
	self.isExpanded = ko.observable(expandable && expanded);

	self.expandedView = ko.computed(function() {
		return self.isExpanded() ? self.val.expanded() : [];
	});
	
	self.hasError = ko.computed(function () {
		return self.val.hasError();
	})
}


function Instance(id, src, root) {
	var self = this;
	var _uniqueId = parseInt(id);
	self.uniqueId = function () { return _uniqueId; }
	
	self.constructor = src[0];
	self.name = src[3];
	self.typeinfo = src[2];
	var alias2id = root.alias2id;
	
	self.withId = function (idex) {
		return new Instance(idex, src, root);
	}
	
	self.alias_back = ko.observable(src[3]);
	self.alias = ko.computed(function () {
		var newvalue = self.alias_back();
		//console.log(newvalue + '@' + id);
		if (self._savedAlias) {
			delete alias2id[self._savedAlias];
		}
		if (alias2id[newvalue] == undefined) {
			self._savedAlias = newvalue;
			alias2id[newvalue] = self.uniqueId();
		}
		return newvalue;
	});
	
	self.isReference = function () {
		return isReferenceType(self.constructor);
	}

	self.fields = map(dict2array(src[1]), function (x) { 
		return new Property(x.key, treatAny(x.value[0], x.value[1], root), true); 
	});
	
	self.isPrimary = ko.computed(function () {
		return alias2id[self.alias()] == self.uniqueId();
	});
	
	self.notPrimary = ko.computed(function () {
		return !self.isPrimary();
	});
	
	self.changes = ko.computed(function() {
		var result = [];
		for (var i=0; i < self.fields.length; i++) {
			var f = self.fields[i];
			if (f.val.editor == INPUT && f.val.initial() != f.val.val()) {
				result.push([self.id, f.name, f.val.convertedValue()]);
			}
		}
		return result;
	});
	
	self.changesSubmitted = function () {
		for (var i=0; i < self.fields.length; i++) {
			var f = self.fields[i];
			if (f.val.editor == INPUT) {
				f.val.initial(f.val.val());
			} 
		}
	}
}

function TimeSerie(id, label, data) {
	var self = this;
	self.id = id;
	self.label = ko.observable(label);
	self.data = data;
}

function Graph(label, timeseries) {
	var self = this;
	self.label = label;
	self.data = timeseries;
	
	self.empty = function () {
		for (var i in self.data) {
			if (self.data[i] == undefined) {
				var a = 12;
			}
			if (self.data[i].data.length > 0) {
				return false;
			}
		}
		return true;
	}
	
	self.render = function (elem) {
		var graph = self;
		
    	if (graph.empty()) {
    		return;
    	}
    	
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

/*
 * We will create observables tree only when 
 *   -- initialization
 *   -- user refreshes the page
 * In these cases we will explicitly construct all the data structures
 * (not implicitely in functional style)
 * id2obj -- it is not an obsevable
 * traders -- observableArray
 * orderbooks -- observableArray
 * graphs -- observableArray
 * scheduler.currentTime -- observable
 * scalar fields -- observable
 * options list -- computed (???). yes it is computed since once a new type added
 * we'll need to reflect this in all options lists involved
 * We seriously rely on fact that data passed from server are mainly deltas 
 * otherwise we'll have to re-render the view every time
 * It is essential that server can only send messages about scalar value attribute changes
 * and time series expansion
 * Model structure cannot changed by the server -- it can only be done by user in browser
 *  
 * first, we should provide change sets at server side and then we'll process them client side
 * 
 * changeset -- it is a difference between state of the server before and after request execution
 * to implement this we'll store for every object it fields and then compare them with current values
 * also we should check that only scalar fields may change
 */

function assert(cond) {
	if (!cond) {
		var a = 11;
	}
}

function Ids2Objs() {
	var self = this;
	var _id2obj = {};

	self.contains = function (id) {
		return _id2obj[id] != undefined;
	}
	
	self.lookup = function (id) {
		assert(!self.contains());
		return _id2obj[id];
	}
	
	self.insert = function (anInstance) {
		var id = anInstance.uniqueId();
		assert(!self.contains());
		_id2obj[id] = anInstance;
		return anInstance;
	} 
	
	self.foreach = function (F) {
		for (var i in _id2obj) {
			F(_id2obj[i]);
		}
	}
}

function AppViewModel() {
	var self = this;
	self.advance = ko.observable(500);
	self.response = ko.observable("");
	self.response(all());

	self.id2obj = new Ids2Objs();	
	
	self.biggestId = -1;
	for (var i in self.response().objects) {
		var ii = parseInt(i);
		if (ii > self.biggestId) {
			self.biggestId = ii;
		}
	}
	self.traders = [];
	self.timeseries = {};
	self._graphs = [];
	self.updateInterval = ko.observable(1);
	
	self.alias2id = {};
	
	self.getCandidates = function (constraint) {
		var candidates = [];
		var jsc = $.toJSON(constraint);
		
		self.id2obj.foreach(function (x) {
			var myId = x.uniqueId();

			if (true || x.isPrimary.peek()) {
				var typeinfo = $.toJSON(x.typeinfo);
				if (typeinfo == jsc) {
					candidates.push(x);
				}
			}
		});
		return candidates;
	}
	
	self.filteredViewEx = function(startsWith) {
		var result = [];
		self.id2obj.foreach(function (x){
			if (x.constructor.indexOf(startsWith) == 0) {
				result.push(x);
			}
		});
		return result;		
	}
	
	self.filteredView = function(startsWith) {
		// to implement through filteredViewEx
		var result = [];
		self.id2obj.foreach(function (x) {
			if (x.constructor.indexOf(startsWith) == 0) {
				result.push(new Property("", new ObjectValue(x, "--", self, true), false));
			}
		});
		return result;		
	}
	
	// главная идея в том, чтобы getObj всегда, 
	// за исключением ссылочных типов выдавал новые объекты.
	// В таком случае для доступа к существующему объекту
	// мы будем использовать id2obj, для клонирования существующих getObj
	// Способ определения ссылочного типа: 
	// если этот id еще не обрабатывался, то мы смотрим на тип в response
	// если обрабатывался - на constructor
	
	self.getObj = function (id) {
		id = parseInt(id);
		if (!self.id2obj.contains(id)) {
			var created = new Instance(id, self.response().objects[id], self);
			if (id > self.biggestId) {
				self.biggestId = id;
			}
			self.id2obj.insert(created);
			return created;
		}
		var obj = self.id2obj.lookup(id);
		if (!obj.isReference()) {
			var newid = self.biggestId + 1;
			var clone = obj.withId(newid);
			self.biggestId = newid;
			self.id2obj.insert(clone);
			return clone;
		}
		return obj;
	}
	
	
	self.parsed = ko.computed(function () {
		var response = self.response();
		
		self.currentTime = response.currentTime;
		
		//----------- building new objects
		if (response.objects) {
			var id2obj = {};
			var original = response.objects;
			
			for (var i in original) {
				id2obj[i] = self.getObj(i);
			}
		}
		
		var asfield = function (id, constraint) {
			var fields = self.id2obj.lookup(id).fields;
			var label = "";
			for (var i in fields) {
				var f = fields[i];
				if (f.name == 'label') {
					label = f.val.val;
				}
			}
			return new Property(label, 
								new ObjectValue(self.id2obj.lookup(id), constraint, self, true), 
								false);
		}
		
		//-------------- traders
		if (response.traders) {
			var src_traders = self.response().traders;
			self.traders = map(src_traders, function (id) {
				return asfield(id,  "marketsim.types.ISingleAssetTrader");
			});
		}
		
		//----------------- graphs
		var rawtimeseries = self.filteredViewEx("marketsim.js.TimeSerie");
		var ts_data = alltimeseries();
		
		var timeseries = {};
		
		for (var i in rawtimeseries) {
			var t = rawtimeseries[i];
			var ts = new TimeSerie(t.uniqueId(), t.name, ts_data[t.uniqueId()]);
			timeseries[ts.id] = ts;		
		}
		
		self.timeseries = timeseries;
		
		return [id2obj];		
	})
	
	self.hasError = ko.computed(function () {
		for (var i in self.traders) {
			if (self.traders[i].hasError()) {
				return true;
			}
		}
		return false;
	})
	
	self.updategraph = ko.observable(false);
	
	self.processResponse = function (data, reset) {
		self.currentTime = data.currentTime;
		
		//------------------------ update properties
		var changes = data.changes;
		for (var i in changes) {
			var ch = changes[i];
			var id = ch[0];
			var pname = ch[1];
			var value = ch[2];
			var obj = self.id2obj.lookup(id);
			for (var j in obj.fields) {
				var field = obj.fields[j];
				if (field.name == pname) {
					var x = field.val;
					x.initial(value);
					x.val(value);
				}
			}
		}
		// -------------------- update timeseries
		if (reset) {
			for (var i in self.timeseries) {
				self.timeseries[i].data = [];
			}	
		} else {
			var ts_changes = data.ts_changes;
			for (var i in ts_changes) {
				var src = ts_changes[i];
				var dst = self.timeseries[i];
				for (var j in src) {
					dst.data.push(src[j]);
				}
			}
		}
		self.updategraph(!self.updategraph());
	}

	
	self.all = ko.computed(function () {
		var dummy = self.parsed();
		var res = [];
		self.id2obj.foreach(function (x) { res.push(x); });
		return res;
	})

	self.graphs = ko.computed(function () {
		var dummy = self.updategraph();
		var rawgraphs = self.filteredViewEx("marketsim.js.Graph");
		return map(rawgraphs, function (g) {
			var tss = g.fields[0].val.val();
			var res = [];
			for (var i in tss) {
				var ts = tss[i].val.pointee(); 
				if (self.timeseries[ts.uniqueId()] == undefined) {
					var a = 11;
				}
				res.push(self.timeseries[ts.uniqueId()]);
			}
			return new Graph(g.name, res);
		})
	})
	
	self.entities = ko.computed(function () {
		var dummy = self.parsed();
		return [
			["Traders" , "model", self.traders],
			["Order books", "option", self.filteredView("marketsim.orderbook.")],
			["Scheduler", "pricing_method", self.filteredView("marketsim.scheduler.")],
			["Graphs", "pricing_method", self.filteredView("marketsim.js.Graph")],
		];
	})
	
	self.limitTime = ko.observable(500);
	
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
						 'timeout' : _parseFloat(self.updateInterval()),
						 'limitTime' : self.limitTime()});
	});
	
	self.running = ko.observable(0);
	self.enabled = ko.computed(function () {
		return self.running() == 0 && !self.hasError();
	})
	self.toBeStopped = false;
	
	
    self.renderGraph1d = function (elem, graph) { graph.render(elem); }
    
    self.changesSubmitted = function () {
		var all = self.all();
		for (var i=0; i<all.length; i++) {
			all[i].changesSubmitted();
		}
    }
    
	self.submitChanges = function() {
		self.limitTime(_parseFloat(self.advance()) + self.currentTime);
		function run() {
			self.running(self.running() + 1);
			var changes = self.changes();
			self.changesSubmitted();
			$.post('/update?'+changes, function (data) {
				var response = $.parseJSON(data);
				self.processResponse(response, false); 
				//console.log(response.currentTime + "...." + self.limitTime());
				if (self.toBeStopped) {
					self.toBeStopped = false;
				} else if (response.currentTime < self.limitTime()) {
					run();
				}
				self.running(self.running() - 1);
			});
		}
		run();
	}
	self.reset = function() {
		$.post('/reset', function (data) {
			self.processResponse($.parseJSON(data), true); 
		});
	}
};

viewmodel = new AppViewModel();
