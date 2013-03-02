/**
 * Field of array type 
 * @param {list<Field>} s -- array of fields (of scalar, array or object type)
 */

function ArrayValue(s) {
	var self = this;
	self.array = function () { return true; }
	
	self._storage = ko.observableArray(map(s, function (x,i) {
						return new Property(i, x, true);
					}));
	
	/**
	 *	Elements of the array 
	 */				
	self.elements = ko.computed(function () {
		return self._storage();
	})
	
	/**
	 *  For the moment we consider all arrays as value types  
	 */
	self.isReference = function () { return false; }

	/**
	 *  Returns true iff any child has an error 
	 */
	self.hasError = ko.computed(function () {
		return any(self._storage(), function (x) { return x.impl().hasError(); })
	})

	/**
	 *  expanded representation of the array 
	 */
	self.expanded = self._storage;
}

