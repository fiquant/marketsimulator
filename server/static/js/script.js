function alldata() {
   z = ($.ajax({
     url: 'all',
     dataType: 'json',
     async: false
   }));

   return $.parseJSON(z.responseText);
}

var createFromPossibilites = $.parseJSON($.ajax({
	     url: 'common',
	     dataType: 'json',
	     async: false
	   }).responseText);
	   
function alltimeseries() {
   z = ($.ajax({
     url: 'alltimeseries',
     dataType: 'json',
     async: false
   }));

   return $.parseJSON(z.responseText);
}

var southeast = '&#9698;';
var east = '&#9654;';

var OrderBookProxyType = "marketsim.orderbook._proxy.Proxy";

ko.bindingHandlers.withProperties = {
    init: function(element, valueAccessor, allBindingsAccessor, viewModel, bindingContext) {
        // Make a modified binding context, with a extra properties, and apply it to descendant elements
        var newProperties = valueAccessor(),
            innerBindingContext = bindingContext.extend(newProperties);
        ko.applyBindingsToDescendants(innerBindingContext, element);
 
        // Also tell KO *not* to bind the descendants itself, otherwise they will be bound twice
        return { controlsDescendantBindings: true };
    }
};

xlats = {};

/**
 *	Translates string 's' to the active language (only english for the moment) 
 */
function translate(s) {
	xlats[s] = s;
	return translations_en[s] || s;
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
		alert('assertion');
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
	
	self.items = function () {
		return _id2obj;
	} 
	
	self.foreach = function (F) {
		for (var i in _id2obj) {
			F(_id2obj[i]);
		}
	}
}

function types_equal(a, b) {
	if (typeof(a) == "string" && typeof(b) == "string") {
		return a == b;
	} 
	if (a.rv &&  b.rv && a.args.length == b.args.length) {
		for (var i in a.args) {
			if (!types_equal(a.args[i], b.args[i])) {
				return false
			}
		}
		return types_equal(a.rv, b.rv);
	}
	if (a.elementType && b.elementType) {
		return types_equal(a.elementType, b.elementType);
	}
	return false;
}

function AppViewModel() {
	var self = this;
	self.updategraph = ko.observable(false);
	
	self.advance = ko.observable(500);
	
	self.graphRenderers = ["Flotr2", "HighStocks"];
	self.currentRenderer = ko.observable(self.graphRenderers[1]);

	self.updateInterval = ko.observable(1);
	self.showOptions = ko.observable(false);
	
	self.getCandidates = function (constraint) {
		var candidates = [];
		var jsc = $.toJSON(constraint);
		
		self.id2obj.foreach(function (x) {
			var myId = x.uniqueId();

			if (x.isPrimary.peek() || true) {
				if (any(x.castsTo(), function (typeinfo) {
					return types_equal(typeinfo, constraint);
				})) {
					candidates.push(x);
				}
			}
		});
		if (candidates.length == 0) {
			console.log("empty candidates for " + jsc);
		}
		return candidates;
	}
	
	self.getCandidateAliases = function (constraint) {
		var candidates = self.getCandidates(constraint);
		var mapping = {};
		foreach(candidates, function (instance) {
			var alias = instance.alias.peek();
			var current = mapping;
			for (var i in alias) {
				if (current[alias[i]] == undefined) {
					current[alias[i]] = {}
				}
				current = current[alias[i]];
			}
		})
		return mapping;
	}
	
	self.filteredViewEx = function(startsWith) {
		var result = [];
		self.id2obj.foreach(function (x){
			if (x.constructor().indexOf(startsWith) == 0) {
				result.push(x);
			}
		});
		return result;		
	}
		
	self.getObj = function (sid) {
		var id = parseInt(sid);
		if (!self.id2obj.contains(id)) {
			var created = createInstance(id, self.response.peek().objects[id], self);
			if (id > self.biggestId) {
				self.biggestId = id;
			}
			self.id2obj.insert(created);
			return self.id2obj.lookup(id);
		}
		return self.id2obj.lookup(id);
	}
	
	self.getNextId = function () {
		self.biggestId++;
		return self.biggestId;
	}
	
	self._createdObjects = {};
	
	self.createObj = function (factory) {
		self.biggestId++;
		var id = self.biggestId;
		var obj = factory(id);
		console.log("inserting " + obj.alias() + " with id " + id);
		assert(!self.id2obj.contains(id));
		self.id2obj.insert(obj);
		self._createdObjects[id] = true;
		return obj;
	}
	
	
	self.originalmodel = ko.observable("");
	self.response = ko.observable("");
	self.root = ko.observable('');
	self.simulations = ko.observableArray();
	self.filename = ko.observable("");
	self.currentTime = ko.observable(0);
	
	function init_model() {
		self.response(alldata());
		var response = self.response.peek();
		self.id2obj = new Ids2Objs();
		
		self.biggestId = -1;
		for (var i in self.response().objects) {
			var ii = parseInt(i);
			if (ii > self.biggestId) {
				self.biggestId = ii;
			}
		}
	
		self.alias2id = {};
		
		self.currentTime(response.currentTime);
		
		//----------- building new objects
		if (response.objects) {
			var id2obj = {};
			var original = response.objects;
			
			for (var i in original) {
				id2obj[i] = self.getObj(i);
			}
			
			for (var i in id2obj) {
				foreach (id2obj[i].fields(), function (f) {
					if (f.impl().object) {
						f.impl().updateOptions();
					}
				});
			}
		}
		self.root(self.id2obj.lookup(self.response.peek().root));
		
		

		self.simulations(response.simulations);
		if (!response.simulations.length) {
			self.simulations.push(response.name);
		}
		self.filename(response.name);
	
		self.originalmodel.valueHasMutated();
	}
	
	init_model();
	
	self.hasChanged = ko.computed(function () {
		return self.root().hasChangedWithChildren();
	})
			
	self.hasError = ko.computed(function () { 
		return self.root().hasError();
	})
	
	self.processResponse = function (data, reset) {
		//------------------------ update properties
		foreach(data.changes, function (ch) {
			self.id2obj.lookup(ch[0]).lookupField(ch[1]).set(ch[2]);
		});
		// -------------------- update timeseries
		var ts_changes = data.ts_changes;
		foreach(ts_changes, function (newData, idx) {
			var target = self.id2obj.lookup(idx);
			if (reset) {
				target.resetData();
			} else {
				target.appendData(newData);
			}
		});
		
		self.currentTime(data.currentTime);
		self.updategraph(!self.updategraph());
	}

	
	self.all = ko.computed(function () {
		var dummy = self.originalmodel();
		var res = [];
		self.id2obj.foreach(function (x) { res.push(x); });
		return res;
	})
	
	self.graphs = ko.computed(function () {
		var fieldGraphs = self.root().lookupField('graphs');
		return map(fieldGraphs.impl().elements(), function (g) {
			return g.impl().pointee();
		});
	})
	
	self.entities = ko.computed(function () {
		var dummy = self.originalmodel();
		function getTopLevelArray(fieldName) {
			var arrayField = self.root().lookupField(fieldName);
			foreach(arrayField.impl().elements(), function (element) {
				element.impl().makeTopLevel();
			});
			return arrayField;
		}
		return [
			["Traders" , "model", getTopLevelArray('traders'), ko.observable(0)],
			["Order books", "option", getTopLevelArray('orderbooks'), ko.observable(0)],
			["Graphs", "pricing_method", getTopLevelArray('graphs'), ko.observable(0)],
		];
	})
	
	self.limitTime = ko.observable(500);
	
	self.changes = function(){
		var created = [];
		for (var id in self._createdObjects) {
			var obj = self.id2obj.lookup(id);
			created.push([id, obj.serialized()]);
		}

		var updates = collect(self.id2obj.items(), function (obj) { 
						return obj.changedFields(); 
					});
		return {'updates' : updates,
				'created' : created};
	};
	
	self.running = ko.observable(0);
	self.enabled = ko.computed(function () {
		return self.running() == 0 && !self.hasError();
	})
	self.toBeStopped = false;
	
	self.stop = function () {
		$.post('/stop');
		self.toBeStopped = true;
	}
	
	
    self.renderGraph1d = function (elem, graph) { graph().render(elem); }
    
    self.dropHistory = function () {
    	self._createdObjects = {};
    	self.id2obj.foreach(function (obj) { obj.dropHistory(); });
    }
    
	self.submitChanges = function() {
		self.limitTime(_parseFloat(self.advance()) + self.currentTime());
		function run() {
			self.running(self.running() + 1);
			var changes = self.changes();
			changes.timeout = _parseFloat(self.updateInterval());
			changes.limitTime = self.limitTime();
			$.post('/update', $.toJSON(changes), function (data) {
				self.dropHistory();
				var response = $.parseJSON(data);
				self.processResponse(response, false); 
				//console.log(response.currentTime + "...." + self.limitTime());
				if (self.toBeStopped) {
					self.toBeStopped = false;
				} else if (response.currentTime < self.limitTime()) {
					run();
				}
				self.running(self.running() - 1);
			}).fail(function (data) { 
				document.documentElement.innerHTML = data.responseText; 
			});
		}
		run();
	}
	self.reset = function() {
		$.post('/reset', function (data) {
			self.processResponse($.parseJSON(data), true); 
		}).fail(function (data) { 
			document.documentElement.innerHTML = data.responseText; 
		});
	}
	
	self.errorMessage = ko.observable('');
	
	self.forkName = ko.observable('');

	self.forkNameValid = function () {
		return self.simulations.indexOf(self.forkName()) < 0;
	}
	
	function updateForkName () {
		var filename = self.filename();
		for (var i=0; true; i++) {
			var suggestion = filename + '.' + i;
			if (self.simulations.indexOf(suggestion) < 0) {
				self.forkName(suggestion);
				return;
			}			
		}
	}
	
	
	updateForkName();
	
	self.filename.subscribe(updateForkName);
	self.simulations.subscribe(updateForkName);
	
	self.commit = function () {
		if (self.hasChanged()) {
			$.post('/update', $.toJSON(self.changes()), function (data) {
				self.dropHistory();
			});
		}
	}
	
	self.createFromOptions = createFromPossibilites
	   
	self.currentCreateFrom = ko.observable(self.createFromOptions[0]);

	self.createFrom = function () {
		self.commit();
		$.post('/createFrom', $.toJSON({'createFrom': self.currentCreateFrom()}), 
				function (data) {init_model();});
	}

	self.createFromEx = function (filename) {
		self.commit();
		$.post('/createFrom', $.toJSON({'createFrom': filename}), 
				function (data) {init_model();});
	}
		
	self.load = function () {
		self.commit();
		$.post('/load', $.toJSON({'loadFrom': self.filename()}), function (data) {
			init_model();
		});
	}
	
	self.loadEx = function (filename) {
		self.commit();
		$.post('/load', $.toJSON({'loadFrom': filename }), function (data) {
			init_model();
		});
	}
	
	self.remove = function () {
		$.post('/remove', function (data) {
			init_model();
		});
	}

	self.fork = function () {
		self.commit();
		var forkName = self.forkName();
		$.post('/fork', $.toJSON({'forkAs': forkName}), function (data) {
			self.simulations.push(forkName);
			self.filename(forkName);
		});
	}
	
	self.showGraphs = ko.observable(false);
	self.currentGraph = ko.observable(0);
	self.currentEntity = ko.observable(0);
	
	self.currentGraph.subscribe(function () {
		self.showGraphs(true);
		self.showOptions(false);
	})
	
	self.currentEntity.subscribe(function () {
		self.showGraphs(false);
		self.showOptions(false);
	})
	
	self.currentEntityElements = ko.computed(function () {
		return self.entities()[self.currentEntity()][2].impl().elements();
	})
	
	self.currentEntityChoice = ko.computed({
		read: function () { return self.entities()[self.currentEntity()][3](); },
		write: function (value) {
			self.entities()[self.currentEntity()][3](value);
		}
	})
	
	self.graphs.subscribe(function (value) {
		if (value[self.currentGraph()] == undefined || value[self.currentGraph()].empty()) {
			var t = 0;
			for (var i in value) {
				if (!value[i].empty()) {
					t = i;
				}
			}
			self.currentGraph(t);
		}
	})
	
	self.hasGraphs = ko.computed(function () {
		return any(self.graphs(), function (graph) {
			return !graph.empty();
		})
	})
	
	self.hasGraphs.subscribe(function (value) {
		self.showGraphs(value);
	})
};

/**
 *	We will have some workspaces
 *  User can switch between them
 *  Workspaces try to be synchronized with server
 *  Current workspace can be forked
 *  Default suggestion for forked workspace name is current workspace + . + id
 *  where id is first natural number that name.id is unused 
 * 
 *  TODO: 
 *  1. we need to save current workspace before and after running simulation
 *  2. Commit button sends current state to server
 *     It is enabled if there are any changes in client
 *  3. Fork button is enabled if fork name doesn't conflict with other names
 *  4. If server is restarted we try to load saved workspace with given name
 *     It means that at server side we should save current work
 */

viewmodel = new AppViewModel();

/*
function initmenu(){
	var e=document.getElementById("menuV2"),
		i=e.offsetHeight,
		b=e.getElementsByTagName("ul"),
		for(var a=0;a<b.length;a++){
			var c=b[a].parentNode;
			c.getElementsByTagName("a")[0].className+=" arrow";
			b[a].style.left=c.offsetWidth+"px";
			b[a].style.top=c.offsetTop+"px";
		}
		for(var a=b.length-1;a>-1;a--)
			b[a].style.display="none"
	}
	if(window.addEventListener)
		window.addEventListener("load",initmenu,false);
	else 
		window.attachEvent&&window.attachEvent("onload",initmenu)
*/