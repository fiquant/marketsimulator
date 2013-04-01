function alldata() {
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

function arrayController(array) {
	return {
		remove : function (element) {
			array.remove(element);
		},
		canBeRemoved : ko.computed(function () {
			return array().length > 1;
		}),
		duplicate : function (element) {
			array.push(element.clone(this));
		}
	}
}



function AppViewModel() {
	var self = this;
	self.advance = ko.observable(500);
	self.response = ko.observable("");
	self.response(alldata());

	self.id2obj = new Ids2Objs();	
	
	self.biggestId = -1;
	for (var i in self.response().objects) {
		var ii = parseInt(i);
		if (ii > self.biggestId) {
			self.biggestId = ii;
		}
	}
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
		
	self.getObj = function (sid) {
		var id = parseInt(sid);
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
		
		self.root = ko.observable(self.id2obj.lookup(response.root));
		
		return [id2obj];		
	})
	
	self.hasError = ko.computed(function () { 
		return self.root().hasError();
	})
	
	self.updategraph = ko.observable(false);
	
	self.processResponse = function (data, reset) {
		self.currentTime = data.currentTime;
		
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
		self.updategraph(!self.updategraph());
	}

	
	self.all = ko.computed(function () {
		var dummy = self.parsed();
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
		var parsed = self.parsed();
		function getTopLevelArray(fieldName) {
			var arrayField = self.root().lookupField(fieldName);
			foreach(arrayField.impl().elements(), function (element) {
				element.impl().makeTopLevel();
			});
			return arrayField;
		}
		return [
			["Traders" , "model", getTopLevelArray('traders')],
			["Order books", "option", getTopLevelArray('orderbooks')],
			["Graphs", "pricing_method", getTopLevelArray('graphs')],
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
		return $.toJSON({'updates' : updates,
						 'created' : created, 
						 'timeout' : _parseFloat(self.updateInterval()),
						 'limitTime' : self.limitTime()});
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
    
    self.errorMessage = ko.observable('');
    
	self.submitChanges = function() {
		self.limitTime(_parseFloat(self.advance()) + self.currentTime);
		function run() {
			self.running(self.running() + 1);
			var changes = self.changes();
			var changes_parsed = $.parseJSON(changes);
			self.dropHistory();
			$.post('/update', changes, function (data) {
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
};

viewmodel = new AppViewModel();
