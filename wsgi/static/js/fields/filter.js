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
