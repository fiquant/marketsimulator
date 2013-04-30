/**
 * 	Returns true iff the type should be considered as a reference type 
 * @param {string} typename
 */
function isReferenceType(typename) {
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
		
	self._initial_alias = ko.observable($.toJSON(alias));
	
	/**
	 *	Read only alias for the instance. Public 
	 */
	self.alias = ko.computed(function () {
		var newvalue = self.alias_back();
		// remove old alias from alias registry
		if (self._savedAlias) {
			delete root.alias2id[$.toJSON(self._savedAlias)];
		}
		// update mapping (todo: instroduce AliasRegistry that will manage this mapping)
		if (root.alias2id[$.toJSON(newvalue)] == undefined) {
			self._savedAlias = newvalue;
			root.alias2id[$.toJSON(newvalue)] = self.uniqueId();
		}
		return newvalue;
	});
	
	/**
	 *	Returns true iff this instance should be considered as of reference type
	 */
	self.isReference = function () {
		return isReferenceType(self.constructor());
	}
	
	self._generateNewAlias = function () {
		if (self.isReference()) {
			for (var i = 0; true; i++) {
				var s = self.alias() + '.' + i;
				if (root.alias2id[$.toJSON(s)] == undefined) {
					return s;
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
		return root.alias2id[$.toJSON(self.alias())] == self.uniqueId();
	});
	
	/**
	 * 	Returns true iff this instance is secondary with respect to the alias (to be removed)
	 */
	self.notPrimary = ko.computed(function () {
		return !self.isPrimary();
	});
	
	self._aliasChanged = ko.computed(function () {
		return $.toJSON(self.alias_back()) != self._initial_alias();
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
		self._initial_alias($.toJSON(self.alias_back()));
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
	var created = new Instance(id, ctor, fields, myTypeinfo[0], src[2], root);
	if (ctor == "marketsim.js.TimeSerie") {
		created = makeTimeSerie(created, root.response().ts_changes);
	} else if (ctor == "marketsim.js.Graph") {
		created = makeGraph(created, root);
	}
	return created;
}
