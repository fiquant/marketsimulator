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
								alias, 
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
				self.alias()];
	}
	
	/**
	 *	Stores alias for the instance. Private.
	 */
	self.alias_back = ko.observable(alias);
	
	/**
	 *	Read only alias for the instance. Public 
	 */
	self.alias = ko.computed(function () {
		var newvalue = self.alias_back();
		// remove old alias from alias registry
		if (self._savedAlias) {
			delete root.alias2id[self._savedAlias];
		}
		// update mapping (todo: instroduce AliasRegistry that will manage this mapping)
		if (root.alias2id[newvalue] == undefined) {
			self._savedAlias = newvalue;
			root.alias2id[newvalue] = self.uniqueId();
		}
		return newvalue;
	});
	
	/**
	 *	Returns true iff this instance should be considered as of reference type
	 */
	self.isReference = function () {
		return isReferenceType(self.constructor());
	}

	/**
	 * 	Returns true iff this instance is primary with respect to the alias 
	 */
	self.isPrimary = ko.computed(function () {
		return root.alias2id[self.alias()] == self.uniqueId();
	});
	
	/**
	 * 	Returns true iff this instance is secondary with respect to the alias (to be removed)
	 */
	self.notPrimary = ko.computed(function () {
		return !self.isPrimary();
	});
	
	/**
	 *	Returns true iff some fields have changed 
	 */
	self.hasChanged = function () {
		return any(self.fields(), function (field) { 
			return field.hasChanged(); });
	}
	
	/**
	 *	Returns list of tuples (instance_id, field_name, new_value) of modified fields
	 */
	self.changedFields = function() {
		return map_opt(self.fields(), function (f) {
			return (f.hasChanged()
					?	[self.uniqueId()].concat(f.serialized())
					:   undefined);
		});
	};	
	
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
		foreach(self.fields(), function (f) { 
			f.dropHistory(); 
		});
	}
}

function createInstance(id, src, root) {
	var fields = map(dict2array(src[1]), function (x) { 
		return new Property(x.key, treatAny(x.value[0], x.value[1], root)); 
	});
	return new Instance(id, src[0], fields, src[2], src[3], root);
}
