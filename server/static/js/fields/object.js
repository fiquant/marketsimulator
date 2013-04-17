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
		self.editAliasMode(true);
	}

	self.exitEditMode = function () {
		self.editAliasMode(false);
	}
	
	
	self.alias = ko.computed({
		read: function () { return _storage().alias(); },
		write: function (newvalue) {
			_storage().alias_back(newvalue);
		}
	})
	
	/**
	 *	Returns true if the fields has been changed 
	 */
	self.hasChanged = ko.computed(function () {
		return _initial() != _storage();
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
		var deep_cloning = self.toplevel || !self.pointee().isReference();
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
	
	/**
	 *	Returns Id of the primary object having the same alias as ours 
	 */
	var primaryId = ko.computed(function () {
		return root.alias2id[self.pointee().alias()];
	})
	
	/**
	 *	Id of the alias chosen at the moment
	 */
	self._currentOption = ko.computed ({
		read: function () { 
			return primaryId(); 
		},
		write: function (id) {
			if (id != undefined) {
				var source = root.getObj(id);
				// if alias id has changed, let's create a new instance for the chosen alias
				var freshly_created = source.isReference() ? source : source.clone();
				console.log(self.pointee().uniqueId() + ' --> ' + freshly_created.uniqueId() + " @ " + id);
				// and set it as current object
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
	
	/**
	 * Are there any errors in our object? 
	 */
	self.hasError = ko.computed(function () {
		return self.pointee().hasError();
	})
}
