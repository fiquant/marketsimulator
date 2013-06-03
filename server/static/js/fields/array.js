/**
 * Field of array type 
 * @param {list<ArrayValue -> Field>} s -- array of field factories (of scalar, array or object type)
 */

function ArrayValue(fieldFactories) {
	var self = this;
	self.array = function () { return true; }
	
	var fields = map(fieldFactories, function (factory) {
		return factory(self);
	});
	
	self._storage = ko.observableArray(fields);
	
	/**
	 *	Removes an element from the array 
	 */
	self.remove = function (element) {
		self._storage.remove(element);
	}

	/**
	 * 	Returns true iff element can be removed from array
	 */
	self.canBeRemoved = ko.computed(function () {
		return self._storage().length > 1;
	})
		
	/**
	 *	Duplicates an element in the array 
	 */
	self.duplicate = function (element) {
		var idx = self._storage().indexOf(element);
		self._storage.splice(idx, 0, element.clone(self));
		element.context.valueHasMutated();
	}
	
	/**
	 *	Elements of the array 
	 */				
	self.elements = ko.computed(function () {
		return self._storage();
	})
	
	/**
	 *	Clones array field 
	 */
	self.clone = function () {
		return new ArrayValue(map(self._storage(), function (element) { 
			return function (newParentArray) {
				return element.clone(newParentArray); }
			}));
	}

	/**
	 *  Returns serialized representation of the field 
	 */
	self.serialized = ko.computed(function () {
		return map(self.elements(), function (property) {
			return property.impl().serialized();
		});
	});
	
	var _init = self.serialized();
	
	self._initial = ko.observable(_init);
	
	/**
	 *	Returns true if the fields has been changed 
	 */
	self.hasChanged = ko.computed(function() {
		return $.toJSON(self.serialized()) != $.toJSON(self._initial());
	});
	
	self.haveChildrenChanged = ko.computed(function () {
		return any(self.elements(), function (property) {
			return property.hasChangedWithChildren();
		})
	})

	self.dropHistory = function () {
		self._initial(self.serialized());
	}
	
	/**
	 *  For the moment we consider all arrays as value types  
	 */
	self.isReference = function () { return false; }

	/**
	 *  Returns true iff any child has an error 
	 */
	self.hasError = ko.computed(function () {
		return any(self._storage(), function (x) { 
			return x.impl().hasError(); 
		})
	})

	/**
	 *  expanded representation of the array 
	 */
	self.expanded = self._storage;
	
	self.rowsWithChildren = ko.computed(function () {
		return 1 + reduce(self._storage(), function (acc, element) {
			return acc + element.rowsWithChildren();
		})
	})
}

function createArrayValue(s) {
	return new ArrayValue(map(s, function (x) {
						return function (self) {
							return new Property("", x, false, false, self);
						}
				}));
}
