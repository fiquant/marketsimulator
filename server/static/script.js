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
	self.source = ko.computed(function () {
		var res = [];
		var src = all();
		for (var i in src) {
			res.push([i, src[i]]);
		}
		return res;
	})
};

viewmodel = new AppViewModel();
