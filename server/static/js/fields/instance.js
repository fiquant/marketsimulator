/**
 * 	Returns true iff the type should be considered as a reference type 
 * @param {string} typename
 */
function isReferenceType(typename) {
	if (typename.indexOf("._proxy.") > 0) {
		return false;
	}
	return (typename.indexOf("marketsim.orderbook.") == 0 ||
			typename.indexOf("marketsim.scheduler.Scheduler") == 0 ||
			typename.indexOf("marketsim.js.Graph") == 0 ||
			typename.indexOf("marketsim.trader.") == 0);
}

/**
 * Creates an object instance 
 * @param {int} id  -- unique identifier for the object
 * @param {(string, List<(string, (JsonValue, IType), IType, string)>)} src --
 * 			(python constructor, [(field_name, (field_value, field_constraint))], static_type, alias)
 * @param {AppViewModel} root -- reference to the root viewmodel
 */
function Instance(id, constructor, fields, typeinfo, alias, root) {
	var self = this;

	/**
	 *	Unique id of the instance. should be root.id2obj.lookup(self.uniqueId()) == self 
	 */
	self.uniqueId = function () { return id; }
	
	/**
	 *	String telling how to construct corresponding Python type (to be moved to types)
	 */
	self.constructor = function () { return constructor; }
	
	/**
	 *	'Static' type of the field (should be removed and calculated from constructor) 
	 */
	self.typeinfo = function () { return typeinfo; }
	
	/**
	 *	Array of fields. 
	 */
	self.fields = ko.observableArray(fields);
	
	/**
	 *	Stores alias for the instance. Private.
	 */
	self.alias_back = ko.observable(alias);
	
	var strAlias = $.toJSON(alias);
	if (root.alias2id[strAlias] == undefined) {
		root.alias2id[strAlias] = [];
	}
	root.alias2id[strAlias].push(id);
	
	self._initial_alias = ko.observable($.toJSON(alias));
	
	self.alias = ko.computed({
		read: function () {
			foreach(self.alias_back(), function (v) {
				if (typeof(v) != 'string') {
					console.log('incorrect alias type');
				}
			})
			return self.alias_back();
		},
		write: function (newvalue) {
			var strNew = $.toJSON(newvalue);
			var strOld = $.toJSON(self.alias_back());
			
			if (strNew != strOld) {
				var oldids = root.alias2id[strOld];
				oldids.splice(oldids.indexOf(id), 1);
				
				if (root.alias2id[strNew] == undefined) {
					root.alias2id[strNew] = [];
				}
				root.alias2id[strNew].push(id);
				self.alias_back(newvalue);
			}
		}
	})
		
	/**
	 *	Returns true iff this instance should be considered as of reference type
	 */
	self.isReference = function () {
		return isReferenceType(self.constructor());
	}
	
	self._generateNewAlias = function () {
		if (self.isReference()) {
			for (var i = 0; true; i++) {
				var copy = self.alias().slice();
				var idx = copy.length - 1;
				copy[idx] = copy[idx].concat('.' + i);
				if (root.alias2id[$.toJSON(copy)] == undefined) {
					return copy;
				}
			}
		} else {
			return self.alias();
		}
	}

	/**
	 *	Makes a deep clone of the object 
	 */
	self.clone = function () {
		var fields_cloned = map(self.fields(), function (field) { 
								return field.clone(); 
						});
						
		return root.createObj(function (id) {
			return new Instance(id, 
								constructor, 
								fields_cloned, 
								typeinfo, 
								self._generateNewAlias(), 
								root);
		});
	}
	
	/**
	 *	Returns JSON representation for a freshly created object 
	 */
	self.serialized = function () {
		return [self.constructor(), 
				dictOf(map(self.fields(), function (field) {
					return field.serialized(); })), 
				[self.alias()]];
	}
	
	/**
	 * 	Returns true iff this instance is primary with respect to the alias 
	 */
	self.isPrimary = ko.computed(function () {
		return root.alias2id[$.toJSON(self.alias())][0] == self.uniqueId();
	});
	
	/**
	 * 	Returns true iff this instance is secondary with respect to the alias (to be removed)
	 */
	self.notPrimary = ko.computed(function () {
		return !self.isPrimary();
	});
	
	self._aliasChanged = ko.computed(function () {
		return $.toJSON(self.alias()) != self._initial_alias();
	})
	
	/**
	 *	Returns true iff some fields have changed 
	 */
	self.hasChanged = ko.computed(function () {
		return any(self.fields(), function (field) { 
			return field.hasChanged(); }) || self._aliasChanged();
	});
	
	self.hasChangedWithChildren = ko.computed(function () {
		return any(self.fields(), function (field) { 
			return field.hasChangedWithChildren(); }) || self._aliasChanged();
	})
	
	/**
	 *	Returns list of tuples (instance_id, field_name, new_value) of modified fields
	 */
	self.changedFields = function() {
		return map_opt(self.fields(), function (f) {
			return (f.hasChanged()
					?	[self.uniqueId()].concat(f.serialized())
					:   undefined);
		}).concat(self._aliasChanged() ? [[self.uniqueId(), "_alias", self.alias()]] : []);
	};	
	
	/**
	 *	Returns a reference to the field with given name 
	 */
	self.lookupField = function (fieldName) {
		return findFirst(self.fields(), function (f) {
			return f.name() == fieldName;
		})
	}
	
	/**
	 * 	Returns true if there are any errors in the fields 
	 */
	self.hasError = ko.computed(function () {
		return any(self.fields(), function (field) { 
			return field.hasError(); 
		});
	})
	
	/**
	 *	After fields changes have been sent to server we may drop history 
	 */
	self.dropHistory = function () {
		self._initial_alias($.toJSON(self.alias()));
		foreach(self.fields(), function (f) { 
			f.dropHistory(); 
		});
	}

}

function createInstance(id, src, root) {
	var ctor = src[0];
	var myTypeinfo = typeinfo[ctor];
	var fields = map(dict2array(src[1]), function (x) { 
		return new Property(x.key, treatAny(x.value, myTypeinfo[1][x.key], root)); 
	});
	var alias = src[2];
	if (ctor == OrderBookProxyType) {
		alias = ["$(OrderBook)"];
	}
	var created = new Instance(id, ctor, fields, myTypeinfo[0], alias, root);
	if (ctor == "marketsim.js.TimeSerie") {
		created = makeTimeSerie(created, root.response().ts_changes);
	} else if (ctor == "marketsim.js.VolumeLevels") {
		created = makeVolumeLevels(created, root.response().ts_changes);
	} else if (ctor == "marketsim.js.Graph") {
		created = makeGraph(created, root);
	}
	return created;
}
