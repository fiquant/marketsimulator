function all() {
   z = ($.ajax({
     url: 'all',
     dataType: 'json',
     async: false
   }));

   return $.parseJSON(z.responseText);
}

function TeXize(s) {
	return "$$" + s + "$$";
}

var original = all();

var id2obj = {};

function isArray(o) {
  return Object.prototype.toString.call(o) === '[object Array]';
}

function map(elements, f) {
    var res = [];
    for (var i=0; i<elements.length; i++)
        res.push(f(elements[i], i));
    return res;
}

function mapDictionaryToArray(dictionary) {
    var result = [];
    for (var key in dictionary) {
        if (dictionary.hasOwnProperty(key)) {
            result.push({ key: key, value: dictionary[key] }); 
        }  
    }

    return result;
}

var dict2array = mapDictionaryToArray;

var INPUT = 0x1;
var ARRAY = 0x2;
var LISTBOX = 0x4;

function isInput(x) {
	return x.value.editor == INPUT;
}

function StringValue(s) {
	var self = this;
	self.value = ko.observable(s);
	
	self.brief = function () {
		return self.value;
	}
	self.expanded = function () { return []; }
	
	self.editor = INPUT;
}

function NumberValue(s) {
	var self = this;
	self.value = ko.observable(s);
	
	self.brief = function () {
		return self.value;
	}
	self.expanded = function () { return []; }
	
	self.editor = INPUT;
}

function ArrayValue(s) {
	var self = this;
	self.value = s;
	
	self.brief = function () {
		return "...";
	}
	self.expanded = function () { 
		return map(self.value, function (x,i) {
			return {'name' : i, 'value' : x };
		}); 
	}
	
	self.editor = ARRAY;
}

function ObjectValue(s) {
	var self = this;
	self.value = s;
	
	self.brief = function () {
		return self.value.name;
	}
	self.expanded = function() {
		return self.value.fields;
	}
	
	self.editor = LISTBOX;
}

nbsp = "&nbsp;";
spaces = [nbsp];

for (var i=0; i<30; i++) {
	spaces.push(spaces[spaces.length-1]+nbsp);
}

function indentify (s, n) {
	return spaces[n] + s;
} 

function treatAny(value) {
	if (typeof(value) == 'string'){
		if (value.length > 1 && value[0]=='#' && value[1] != "#") {
			return new ObjectValue(getObj(parseInt(value.substring(1))));
		} else {
			if (value.length > 1 && value[0]=='#' && value[1] == "#") {
				return new StringValue(value.substring(1));
			} else {
				return new StringValue(value);
			}
		}
	} else if (isArray(value)) {
		return new ArrayValue(map(value, treatAny));
	} else {
		return new NumberValue(value);
	}	
}

function Property(src) {
	var self = this;
	self.name = src.key;
	self.value = treatAny(src.value);
	self.isArray = function() {
		return isArray(self.value);
	}
	self.isObject = function() {
		return typeof(self.value) == 'object' && !self.isArray();
	}
	self.isString = function() {
		return typeof(self.value) == 'string';
	}
	self.isNumber = function() {
		return typeof(self.value) == 'number';
	}
}


function Instance(id, src) {
	var self = this;
	self.id = id;
	self.constructor = src[0];
	self.name = src[2];
	self.fields = map(dict2array(src[1]), function (x) { return new Property(x); });
	if (self.fields == undefined) { 
		console.log(self);
	}
}

function getObj(id) {
	if (id2obj[id] == undefined) {
		id2obj[id] = new Instance(id, original[id]);
	}
	return id2obj[id];
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
	self.all = ko.computed(function () {
		var res = [];
		var src = original;
		for (var i in src) {
			res.push(getObj(i));
		}
		return res;
	})
};

viewmodel = new AppViewModel();
