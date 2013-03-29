/**
 * Represents a property or a field of an object
 * Contains label to display and reference to a concrete field implementation (scalar, array or object)
 * @param {string} name  -- displayable label
 * @param {ObjectValue|ArrayValue|ScalarValue} value -- concrete implementation of the field
 * @param {bool} toplevel -- is this field top-level? (it will be rendered initially as collapsed)
 */
function Property(name, value, toplevel, parentArray) {
	var self = this;
	self.scalar = value.scalar;
	self.array  = value.array;
	self.object = value.object;
	
	// TODO: introduce special array element to handle case with non-trivial parentArray

	/**
	 *	Returns name of the field
	 */
	self.name = ko.observable(name); 
	
	/**
	 * Concrete implementation of the field 
	 */
	self.impl = function (){ return value; }
	
	/**
	 *	Returns true iff the property belongs to an array 
	 */
	self.isArrayElement = function (){ return parentArray != undefined; }
	
	/**
	 *	Removes this field from parent array if any 
	 */
	self._removeFromArray = function () { 
		parentArray.remove(self); 
	}

	self.parentArray = function () {
		return parentArray;
	}	
	
	/**
	 *	Creates a duplicate of this in the parent array if any 
	 */
	self._duplicateInArray = function () {
		parentArray.duplicate(self);	
	}
	
	/**
	 * Error message for the field if any 
	 */
	self.errorMessage = ko.computed(function () {
		return self.scalar ? self.impl().errormsg() : "";
	});
	
	/**
	 *	Returns true if there are changes in the field 
	 */
	self.hasChanged = ko.computed(function () {
		return self.impl().hasChanged();
	});
	
	/**
	 *  Returns changed field mark if there are any changes 
	 */
	self.changedSign = ko.computed(function () {
		return self.hasChanged() ? "*" : "";
	})
	
	/**
	 *	Returns name of the field to render in current language 
	 */
	self.displayName = ko.computed(function () {
		return translate(self.name());
	})
	
	/**
	 *	Property name to display 
	 */
	self.displayLabel = ko.computed(function () { 
		return self.displayName() + self.changedSign(); 
	});
	
	/**
	 *	Returns value to save of the field: (name, value) 
	 */
	self.serialized = function () {
		return [self.name(), self.impl().serialized()];
	}
	
	/**
	 *	Returns true if there any errors in the field 
	 */
	self.hasError = ko.computed(function () {
		return self.impl().hasError();
	});
	
	/**
	 *	Returns true iff field row should be rendered with error style 
	 */
	self.hasErrorStyle = ko.computed(function () {
		return self.scalar && self.hasError();
	})
	
	/**
	 *  Returns true iff the fiels can be expanded 
	 */
	self.expandable = ko.computed(function () {
		return !self.scalar && self.impl().expanded().length;
	});
	
	/**
	 *  Returns true if the field is expanded at the moment 
	 */
	self.isExpanded = ko.observable(!toplevel && self.expandable.peek());
	
	/**
	 *	Returns array of expanded field items if in expanded state 
	 */
	self.expandedView = ko.computed(function() {
		return self.isExpanded() ? self.impl().expanded() : [];
	});
	
	/**
	 *  Clones the property 
	 */
	self.clone = function (newParentArray) {
		return new Property(self.name(), value.clone(), toplevel, newParentArray);
	}
	
	/**
	 * 	Sets new value to the field. At the moment server may update only scalar values
 	 * @param {number|string} newvalue
	 */
	self.set = function (newvalue) {
		assert(self.scalar);
		self.impl().set(newvalue);
	}
	
	self.dropHistory = function () {
		self.impl().dropHistory();
	}
}
