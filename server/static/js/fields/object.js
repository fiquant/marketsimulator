/**
 *	Filters availableOptions from parent by current aliaspart
 *  @param {ko.observable(array<Instance>)} parentOptions -- options to be filtered
 *  @param {string} -- initial state of the filter
 *  @param {int} idx -- index of the current filter
 *  @param {ObjectValue} base -- reference to the object value containing this filter
 */
function Filter(optionsMap, aliaspart, idx, base) {
	var self = this;
	
	if (typeof(aliaspart) != 'string'){
		console.log('incorrect alias part type');
	}
	
	if (optionsMap == undefined) {
		console.log("optionsMap should be defined")
	}
	
	self.alive = ko.observable(true);
	
	/**
	 * 	Editable alias part 
	 */
	self.aliaspart = ko.observable(aliaspart);
	
	self.editableAliaspart = ko.observable(aliaspart);

	/**
	 *	Alias has changed iff it isn't equal to the corresponding alias part saved in 'base'  
	 */	
	self.hasChanged = function () {
		return self.aliaspart() != base.alias.peek()[idx];
	}
	
	self.editMode = ko.observable(false);
	
	self.availablePartsEx = [];
	for (var key in optionsMap) {
		self.availablePartsEx.push(key);
	}
	
	/**
	 *  Available choices for the child 
	 */
	self._options = ko.computed(function () {
		if (!self.alive.peek()) {
			return [];
		} else {
			if (optionsMap[self.aliaspart()] == undefined) {
				console.log('incorrent optionsMap');
			}
			return optionsMap[self.aliaspart()];
		}
	})
	
	self._child = ko.computed(function () {
		if (!self.alive.peek()) {
			return null;
		}
		
		if (self['_child'] && self._child()) {
			self._child().dispose();
		}
		
		if (self._options() == {}) {
			return null;			
		}
		var first = undefined;
		if (self.hasChanged()) {
			for (var k in self._options()) {
				first = k;
				break;
			}
		}
		var next_choice = (self.hasChanged() 
							? 	first 
							: 	base.alias.peek()[idx + 1]);
							
		if (next_choice == undefined) {
			return null;
		}
							
		return new Filter(self._options(), next_choice, idx + 1, base);
	})
	
	self.dispose = function () {
		self.alive(false);
		if (self._child()) {
			self._child().dispose();
		}
	}
	
	self.childrenWithMe = ko.computed(function () {
		if (!self.alive.peek()) {
			return null;
		}
		if (self._child() == null) {
			return ko.observableArray([self]);
		} else {
			var r = self._child().childrenWithMe();
			r.unshift(self);
			return r;
		}
	})
	
	self.alias = ko.computed(function () {
		if (!self.alive.peek()) {
			return null;
		}
		var r = [self.aliaspart.peek()].concat(self._child() 
				         			     	 ?   self._child().alias() 
										     :   []);
		return idx == 0 ? $.toJSON(r) : r;
	});
	
	self.editedAlias = function () {
		if (!self.alive.peek()) {
			return null;
		}
		var r = [self.editableAliaspart()].concat(self._child() 
				         			     	 ?   self._child().editedAlias() 
										     :   []);
		return idx == 0 ? $.toJSON(r) : r;
	};
	
	
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

	self.alias = ko.computed(function () {
		return _storage().alias();
	})
		
	self.hint = ko.computed(function () {
		var myTypeinfo = typeinfo[_storage().constructor()];
		return myTypeinfo ? myTypeinfo.description : "";
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
	
	/**
	 *  Prefix tree of aliases suitable for this field 
	 */	
	self._optionsMap = ko.observable({});
	
	/**
	 *  Forces to recalculate options 
	 */
	self.updateOptions = function () {
		var c = root.getCandidateAliases(constraint);
		if ($.toJSON(c) != $.toJSON(self._optionsMap.peek())) {
			self._optionsMap(c);
		}
	}
	
	self.filters = ko.computed(function () {
		self.updateOptions();
		return new Filter(self._optionsMap(), _storage().alias.peek()[0], 0, self);
	})
	
	self.__alias = ko.computed(function () {
		return self.filters().alias();
	})
	
	self.switchTo = function (newAlias) {
		var value = $.toJSON(newAlias);
		if (value != $.toJSON(self.alias())) {
			console.log($.toJSON(self.alias()) + ' -> '  + value);
			var id = root.alias2id[value][0];
			
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
	}
	
	self.__alias.subscribe(function (value) {
		if (value != null && self.alias() != undefined) {
			self.switchTo($.parseJSON(value));
		}
	})
	
	self.exitEditMode = function () {
		var newAlias = self.filters().editedAlias();
		var oldAlias = self.filters().alias();
		if (newAlias != oldAlias) {
			self.filters().dispose();		
			_storage().alias($.parseJSON(newAlias));
			self.updateOptions();
			self._optionsMap.valueHasMutated();
		}
		self.editAliasMode(false);
	}
	

	/**
	 *	Returns Id of the primary object having the same alias as ours 
	 */
	var primaryId = ko.computed(function () {
		return root.alias2id[$.toJSON(self.alias())][0];
	})
	
		
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
