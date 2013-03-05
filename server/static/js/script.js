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

			if (x.isPrimary.peek()) {
				var typeinfo = $.toJSON(x.typeinfo());
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
			if (x.constructor().indexOf(startsWith) == 0) {
				result.push(x);
			}
		});
		return result;		
	}
	
	self.filteredView = function(startsWith) {
		// to implement through filteredViewEx
		var result = [];
		self.id2obj.foreach(function (x) {
			if (x.constructor().indexOf(startsWith) == 0) {
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
			var created = createInstance(id, self.response().objects[id], self);
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
	
	self.createObj = function (factory) {
		self.biggestId++;
		var id = self.biggestId;
		var obj = factory(id);
		//console.log("inserting " + obj.alias() + "with id " + id);
		assert(!self.id2obj.contains(id));
		self.id2obj.insert(obj);
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
			var fields = self.id2obj.lookup(id).fields();
			var label = "";
			for (var i in fields) {
				var f = fields[i];
				if (f.name == 'label') {
					label = f.impl().val;
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
			for (var j in obj.fields()) {
				var field = obj.fields()[j];
				if (field.name == pname) {
					field.set(value);
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
			var tss = g.fields()[0].impl().pointee().fields();
			var res = [];
			for (var i in tss) {
				var ts = tss[i].impl().pointee(); 
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
			var x = all[i].changedFields();
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
