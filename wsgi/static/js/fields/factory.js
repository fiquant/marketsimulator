/**
 * 	tries to convert a string into a reference id if has appropriate format
 *  return undefined if fails  
 */
function decodeReferenceToObject(value) {
	return (value.length > 1 && value[0]=='#' && value[1] != "#" 
			? 	parseInt(value.substring(1)) 
			: 	undefined);
}

/**
 *	corrects a string came from server 
 */
function decodeString(value) {
	return (value.length > 1 && value[0]=='#' && value[1] == "#"
			? 	value.substring(1)
			:   value);
}

/** JsonValue = number|string|list<JsonValue>
 * Factory to construct concrete fields (of scalar, array or object type) by raw json data come from server 
 * @param {JsonValue} value -- raw json data containing initial value of the field
 * @param {IType} constraint -- constraint for the field defining set of possible values that the field can contain
 * @param {AppViewModel} root -- reference to the root viewmodel
 */
function treatAny(value, constraint, root) {
    if (typeof(value) == 'string'){
    	var ref_id = decodeReferenceToObject(value);
        return (ref_id != undefined
            	? 	new ObjectValue(root.getObj(ref_id), constraint, root, false)
        		: 	new ScalarValue(decodeString(value), identity));
    } else {
        return (isArray(value) 
        		?	createArrayValue(map(value, function (x) { 
        				return treatAny(x, constraint.elementType, root); 
        			}))
        		:   new ScalarValue(value, eval(constraint)));
    }    
}
