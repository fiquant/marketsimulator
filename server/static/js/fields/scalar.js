/**
 * @typeparam T -- either number or string
 * @param {T} s - initial value of the scalar field
 * @param {string -> T} checker - function to check correctness of the current value
 *                                              it throws an exception if there is an error
 */

function ScalarValue(s, checker) {
	var self = this;
	self.scalar = function () { return true; }

	self._initial = ko.observable(s);
	self._storage = ko.observable(s);
	
	/**
	 *	Clones scalar field 
	 */
	self.clone = function () {
		return new ScalarValue(s, checker);
	}
	
	/**
	 *	Returns 'true' iff fields has changes 
	 */
	self.hasChanged = ko.computed(function () {
		return self._storage() != self._initial();
	})
	
	/**
	 * Changes current value of the field and drops his history
 	 * @param {T} newvalue -- new value to be set
	 */
	self.set = function (newvalue) {
		self._initial(newvalue);
		self._storage(newvalue);
	}

	/**
	 *  Drops field history 
	 */	
	self.dropHistory = function () {
		if (self.hasChanged()) {
			self.set(self._storage());
		}
	}
	
	/**
	 *	Contains error message for the field if any 
	 */
	self.errormsg = ko.observable("");
	
	/**
	 *  Contains validated field value or NaN if errors 
	 */
	self.serialized = ko.computed(function (){
		try {
			var r = checker(self._storage());
			self.errormsg("");
			return r;
		} catch (err) {
			self.errormsg(err);
			return NaN;
		}
	});
	
	/**
	 *	Returns true iff there are any errors 
	 */
	self.hasError = ko.computed(function () {
		return isnan(self.serialized());
	})
}
