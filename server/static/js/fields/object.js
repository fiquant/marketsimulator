/**
 *	Filters availableOptions from parent by current aliaspart
 *  @param {ko.observable(array<Instance>)} parentOptions -- options to be filtered
 *  @param {string} -- initial state of the filter
 *  @param {int} idx -- index of the current filter
 *  @param {ObjectValue} base -- reference to the object value containing this filter
 */
function Filter(parentOptions, aliaspart, idx, base) {
	var self = this;
	
	if (typeof(aliaspart) != 'string'){
		console.log('incorrect alias part type');
	}
	
	self.alive = ko.observable(true);
	
	/**
	 * 	Editable alias part 
	 */
	self.aliaspart = ko.observable(aliaspart);

	/**
	 *	Alias has changed iff it isn't equal to the corresponding alias part saved in 'base'  
	 */	
	self.hasChanged = function () {
		return self.aliaspart() != base.fullAlias()[idx];
	}
	
	self.editMode = ko.observable(false);
	
	var availableParts = {};
	self.availableParts = [];
	
	foreach(parentOptions(), function (instance) {
		var part = instance.alias()[idx];
		if (typeof(part) != 'string'){
			console.log('incorrect alias part type');
		}
		if (availableParts[part] == undefined) {
			availableParts[part] = true;
			self.availableParts.push(part);
		}
	})
	
	/**
	 *  Available choices for the child 
	 */
	self._options = ko.computed(function () {
		if (!self.alive()) {
			return [];
		} else {
			return filter(parentOptions(), function (instance) {
				return instance.alias()[idx] == self.aliaspart();
			});
		}
	})
	
	self._child = ko.computed(function () {
		if (!self.alive()) {
			return null;
		}
		
		if (self['_child'] && self._child()) {
			self._child().alive(false);
		}
		
		if (self._options().length == 0) {
			console.log('there cannot be empty options');
			return null;			
		}
		var next_choice = (self.hasChanged() 
							? 	self._options()[0].alias()[idx + 1] 
							: 	base.fullAlias()[idx + 1]);
							
		if (next_choice == undefined) {
			return null;
		}
							
		return new Filter(self._options, next_choice, idx + 1, base);
	})
	
	self.childrenWithMe = ko.computed(function () {
		if (self._child() == null) {
			return ko.observableArray([self]);
		} else {
			var r = self._child().childrenWithMe();
			r.unshift(self);
			return r;
		}
	})
	
	self.alias = ko.computed(function () {
		return [self.aliaspart.peek()].concat(self._child() 
				         			     	 ?   self._child().alias() 
										     :   []);
	});
}

/**
 * Creates a value of object type for a field 
 * @param {Instance} s -- reference to an existing object instance
 * @param {Object} constraint -- type representing constraint for the field value
 * @param {AppViewModel} root	-- reference to the root viewmodel object
 * @param {bool} expandReference -- force to expand pointee fields even if it is a reference type
 */
function ObjectValue(s, constraint, root, expandReference) {
	var self = this;
	
	self._expandReference = ko.observable(expandReference);
	self.expandedByDefault = constraint != "marketsim.js.TimeSerie";
	
	self.makeTopLevel = function () {
		self._expandReference(true);
		self.toplevel = function () { return true; }
		self.object = undefined;
	}
	
	if (self._expandReference()) {
		self.makeTopLevel();
	} else {
		self.object = function () { return true; }
	} 

	/**
	 *	Initial value of the field. (synchronized with server) 
	 */
	var _initial = ko.observable(s);
	
	/**
	 *  stored reference to the object 
	 */
	var _storage = ko.observable(s);
	
	self.editAliasMode = ko.observable(false);
	
	self.enterEditMode = function () {
		if (self.toplevel || (!_storage().isReference() && _storage().fields().length)) {
			self.editAliasMode(true);
		}
	}

	self.exitEditMode = function () {
		self.editAliasMode(false);
	}
	
	self.fullAlias = ko.computed(function () {
		return _storage().alias();
	})
	
	
	self.alias = ko.computed({
		read: function () { return _storage().alias()[_storage().alias().length - 1]; },
		write: function (newvalue) {
			_storage().alias_back()[_storage().alias().length - 1] = newvalue;
			_storage().alias_back.valueHasMutated();
		}
	})
	
	self.hint = ko.computed(function () {
		var myTypeinfo = typeinfo[_storage().constructor()];
		return myTypeinfo ? myTypeinfo[2] : "";
	});

	/**
	 *	Returns true if the fields has been changed 
	 */
	self.hasChanged = ko.computed(function () {
		return _initial() != _storage() || _storage()._aliasChanged();
	});
	
	self.haveChildrenChanged = function () {
		return self.pointee().hasChangedWithChildren();
	}
	
	/**
	 *  Drops field history 
	 */	
	self.dropHistory = function () {
		if (self.hasChanged()) {
			_initial(_storage());
		}
	}
	
	/**
	 *  read-only reference to the referenced object
	 */
	self.pointee = ko.computed(function () {
		return _storage();
	})
	
	/**
	 *  Returns serialized representation of the field 
	 */
	self.serialized = function () {
		return "#" + self.pointee().uniqueId();
	}
	
	/**
	 *  Clones object field (if pointee is a reference it is not cloned)
	 */
	self.clone = function () {
		var deep_cloning = self.toplevel || !self.pointee().isReference() && _storage().fields().length;
		return new ObjectValue(deep_cloning ? self.pointee().clone() : self.pointee(), 
								constraint, root, self._expandReference());
	}
	
	// used to recalculate options
	self._dummy = ko.observable(false);
	
	/**
	 *  Array of objects representing available options for the field 
	 */
	self._options = ko.computed(function (){
		self._dummy();
		// we need to recalculate options once our alias has changed
		self.pointee.peek().alias();
		return root.getCandidates(constraint);
	});
	
	/**
	 *  Forces to recalculate options 
	 */
	self.updateOptions = function () {
		self._dummy(!self._dummy());
	}
	
	self.filters = ko.computed(function () {
		return new Filter(self._options, self.fullAlias()[0], 0, self);
	})
	
	self.updateAlias = function () {
		var newAlias = self.filters().alias();
		_storage().alias_back(newAlias);
	}
	

	/**
	 *	Returns Id of the primary object having the same alias as ours 
	 */
	var primaryId = ko.computed(function () {
		return root.alias2id[$.toJSON(self.fullAlias())];
	})
	
	self.filters().alias.subscribe(function (value) {
		var newval = $.toJSON(value);
		if (newval != $.toJSON(self.fullAlias())) {
			console.log('--> ' + newval);
		}
	})
	
	/**
	 *	Id of the alias chosen at the moment
	 */
	self._currentOption = ko.computed ({
		read: function () { 
			return primaryId(); 
		},
		write: function (id) {
			if (id != undefined && id != self.pointee().uniqueId()) {
				var source = root.getObj(id);
				// if alias id has changed, let's create a new instance for the chosen alias
				var freshly_created = !self.toplevel && (
					source.isReference() || _storage().fields().length == 0)
					? 	source 
					: 	source.clone();
					
				console.log(self.pointee().uniqueId() + ' --> ' + freshly_created.uniqueId() + " @ " + id);
				// and set it as current object
				self.updateOptions();
				_storage(freshly_created);
			}
		}	
	});
	
	/**
	 *	List of fields to be rendered in expanded view 
	 */
	self.expanded = ko.computed(function() {
		return (self.pointee().isReference() && !self._expandReference()) ? [] : self.pointee().fields();
	});
	
	self.rowsWithChildren = ko.computed(function () {
		return 1 + reduce(self.expanded(), function (acc, field) {
			return acc + field.rowsWithChildren();
		})
	})
	
	/**
	 * Are there any errors in our object? 
	 */
	self.hasError = ko.computed(function () {
		return self.pointee().hasError();
	})
}
