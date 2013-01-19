function all() {
   z = ($.ajax({
     url: 'all',
     dataType: 'json',
     async: false
   }));

   return $.parseJSON(z.responseText);
}

function AppViewModel() {
	var self = this;
	self.raw_source = all();
	self.source = ko.computed(function () {
		var res = [];
		var src = self.raw_source;
		for (var i in src) {
			res.push([i, src[i]]);
		}
		return res;
	})
};

viewmodel = new AppViewModel();
