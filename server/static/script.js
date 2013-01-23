function all() {
   z = ($.ajax({
     url: 'all',
     dataType: 'json',
     async: false
   }));

   return $.parseJSON(z.responseText);
}

function isInteger (s) {
    var isInteger_re     = /^\s*(\+|-)?\d+\s*$/;
    return String(s).search (isInteger_re) != -1
}

function isFloat (s) {
    var isDecimal_re     = /^\s*(\+|-)?((\d+(\.\d+)?)|(\.\d+))\s*$/;
    return String(s).search (isDecimal_re) != -1
}

function _parseInt(x) {
    if (typeof(x) == "string" && !isInteger(x.trim()))
        return NaN;
    return parseInt(x,10);
}

function _parseFloat(x) {
    if (typeof(x) == "string" && !isFloat(x.trim()))
        return NaN;
    return parseFloat(x);
}

function identity(s) { return s; }

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
	return x.val.editor == INPUT;
}

var EMPTYSTR = "";

function hasChangedSign(x) {
	return x.val.initial != x.val.val() ? "*" : "";
}

function ScalarValue(s, checker) {
	var self = this;
	self.initial = s;
	self.val = ko.observable(s);
	self.editor = INPUT;
	self.convertedValue = ko.computed(function (){
		return checker(self.val());
	});
}

function ArrayValue(s) {
	var self = this;
	self.val = ko.observableArray(map(s, function (x,i) {
					return new Property(i, x);
				}));
	
	self.brief = function () {
		return "...";
	}

	self.expanded = self.val;
	
	self.editor = ARRAY;
}

function ObjectValue(s) {
	var self = this;
	self.val = s;
	
	self.brief = function () {
		return self.val.name;
	}

	self.expanded = ko.computed(function() {
		return self.val.fields;
	});
	
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
				return new ScalarValue(value.substring(1), identity);
			} else {
				return new ScalarValue(value, identity);
			}
		}
	} else if (isArray(value)) {
		return new ArrayValue(map(value, treatAny));
	} else {
		return new ScalarValue(value, _parseFloat);
	}	
}

function Property(name, value) {
	var self = this;
	self.name = name;
	self.val = value;
	
	self.isExpanded = ko.observable(false);

	self.expandedView = ko.computed(function() {
		return self.isExpanded() ? self.val.expanded() : [];
	});
}


function Instance(id, src) {
	var self = this;
	self.id = parseInt(id);
	self.constructor = src[0];
	self.name = src[2];
	self.fields = map(dict2array(src[1]), function (x) { 
		return new Property(x.key, treatAny(x.value)); 
	});
	
	self.changes = ko.computed(function() {
		var result = [];
		for (var i=0; i < self.fields.length; i++) {
			var f = self.fields[i];
			if (f.val.editor == INPUT && f.val.initial != f.val.val()) {
				result.push([self.id, f.name, f.val.convertedValue()]);
			}
		}
		return result;
	});
}

function getObj(id) {
	if (id2obj[id] == undefined) {
		id2obj[id] = new Instance(id, original[id]);
	}
	return id2obj[id];
}


function AppViewModel() {
	var self = this;
	self.all = ko.computed(function () {
		var res = [];
		var src = original;
		for (var i in src) {
			res.push(getObj(i));
		}
		return res;
	})
	self.changes = ko.computed(function(){
		var result = [];
		var all = self.all();
		for (var i=0; i<all.length; i++) {
			var x = all[i].changes();
			for (var j=0; j<x.length; j++) {
				result.push(x[j]);
			}
		}
		return $.toJSON(result);
	})
	self.submitChanges = function() {
		$.getJSON('/update?'+self.changes());
	}
};

viewmodel = new AppViewModel();
