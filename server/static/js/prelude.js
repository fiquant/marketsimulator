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
        throw "should be an integer value";
    return parseInt(x,10);
}

function _parseFloat(x) {
    if (typeof(x) == "string" && !isFloat(x.trim()))
        throw "should be a floating point value";
    return parseFloat(x);
}

function less(y) {
    return function (x) {
    	if (!(x < y)) {
    		throw "should be less than " + y;
    	}
        return x;
    }
}

function less_or_equal(y) {
    return function (x) {
    	if (!(x <= y)) {
    		throw "should be less or equal to " + y;
    	}
        return x;
    }
}

function greater(y) {
    return function (x) {
    	if (!(x > y)) {
    		throw "should be greater than " + y;
    	}
        return x;
    }
}

function greater_or_equal(y) {
    return function (x) {
    	if (!(x >= y)) {
    		throw "should be greater or equal to " + y;
    	}
        return x;
    }
}

function combine(f,g) {
    return function (x) {
        return f(g(x));
    }
}


function identity(s) { return s; }

function TeXize(s) {
	return "$$" + s + "$$";
}


function isArray(o) {
  return Object.prototype.toString.call(o) === '[object Array]';
}

foreach = ko.utils.arrayForEach;

function any(array, predicate) {
	for (var i in array) {
		if (predicate(array[i])) {
			return true;
		}
	}
	return false;
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

function isnan(x) {
	return typeof(x) != "string" && isNaN(x);
}
