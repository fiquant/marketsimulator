
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
			var id = root.primaryIdByAlias(constraint, value);
			
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
		return root.primaryIdByAlias(constraint, $.toJSON(self.alias()));
	})
	
		
	/**
	 *	List of fields to be rendered in expanded view 
	 */
	self.expanded = ko.computed({
		read: function() {
				return ((self.pointee().isReference() && !self._expandReference()) 
						? [] : self.pointee().fields());
				},
		deferEvaluation : true
	});
	
	self.expandedLength = ko.computed(function() {
		return (self.pointee().isReference() && !self._expandReference()) ? [] : self.pointee().fieldCount();
	});
	
	self.rowsWithChildren = ko.computed({
		read: function () {
				return 1 + reduce(self.expanded(), function (acc, field) {
					return acc + field.rowsWithChildren();
				})
			},
		deferEvaluation : true
	})
	
	/**
	 * Are there any errors in our object? 
	 */
	self.hasError = ko.computed(function () {
		return self.pointee().hasError();
	})
}
