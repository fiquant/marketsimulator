/**
 * Creates a value of object type for a field 
 * @param {Instance} s -- reference to an existing object instance
 * @param {Object} constraint -- type representing constraint for the field value
 * @param {AppViewModel} root	-- reference to the root viewmodel object
 * @param {bool} expandReference -- force to expand pointee fields even if it is a reference type
 */
function ObjectValue(s, constraint, root, expandReference) {
	var self = this;
	
	/**
	 *  stored reference to the object 
	 */
	var _storage = ko.observable(s);
	
	/**
	 *  read-only reference  
	 */
	self.pointee = ko.computed(function () {
		return _storage();
	})
	
	// used to recalculate options
	self._dummy = ko.observable(false);
	
	/**
	 *  Array of objects representing available options for the field 
	 */
	self.options = ko.computed(function (){
		self._dummy();
		var myAlias = self.pointee().alias();
		return root.getCandidates(constraint);
	});
	
	self.updateOptions = function () {
		self._dummy(!self._dummy());
	}
	
	var primaryId = ko.computed(function () {
		return root.alias2id[self.pointee().alias()];
	})
	
	self.currentOption = ko.observable(primaryId());
	
	primaryId.subscribe(function (newid) {
		self.currentOption(newid);
	})
	
	self._lock = false;
	
	function updateCurrentOption(id) {
		if (self._lock || id == undefined) {
			return;
		}
		self._lock = true;
		
		var freshly_created = root.getObj(id);
		console.log(self.pointee().uniqueId() + ' --> ' + freshly_created.uniqueId());
		_storage(freshly_created);
		
		self._lock = false;
	}
	
	self.currentOption.subscribe(updateCurrentOption);	

	self.expanded = ko.computed(function() {
		return (self.pointee().isReference() && !expandReference) ? [] : self.pointee().fields;
	});
	
	self.hasError = ko.computed(function () {
		var fields = self.pointee().fields;
		for (var i in fields) {
			if (fields[i].val.hasError()) {
				return true;
			}
		}
		return false;
	})
	
	
	self.object = function () { return true; }
}
