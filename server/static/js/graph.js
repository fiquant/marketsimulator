/**
 * 	Represents a time serie to be rendered on graph 
 * @param {Instance}    source 	 -- source object for the time serie
 * @param {map<int, list<(float, float)>>} data -- initial data to be rendered 
 */
function TimeSerie(source, initialData) {
	var self = source;
	
	self._data = [];
	
	/**
	 *  Appends updates in the time serie 
 	 *  @param {list<(float, float)>} dataDelta -- list of pair (time, value) to be appended to the time serie
	 */
	self.appendData = function (dataDelta) {
		self._data = self._data.concat(dataDelta);
	}

	/**
	 *	Updates time serie from data fetched from server
	 *  @param {map<int, list<(float, float)>>} -- time serie relevant data fetched from server 
	 */	
	self.updateFrom = function (ts_changes) {
		if (ts_changes[self.uniqueId()]) {
			self.appendData(ts_changes[self.uniqueId()]);
		}
	}
	
	if (initialData) {
		self.updateFrom(initialData);
	}
	
	/**
	 *	Resets time serie data 
	 */
	self.resetData = function () {
		self._data = [];
	}
	
	/**
	 *	Returns time serie data to be rendered 
	 */
	self.getData = function () {
		return self._data;
	};
	
	return self;
}

var makeTimeSerie = TimeSerie;

function Graph(label, timeseries) {
	var self = this;
	self.label = label;
	self.data = timeseries;
	
	self.empty = function () {
		for (var i in self.data) {
			if (self.data[i] == undefined) {
				var a = 12;
			}
			if (self.data[i].getData().length > 0) {
				return false;
			}
		}
		return true;
	}
	
	self.render = function (elem) {
		var graph = self;
		
    	if (graph.empty()) {
    		return;
    	}
    	
		var data = map(graph.data, function (ts) {
			return { 'data' : ts.getData(), 'label' : ts.alias() };
		});
        
        for (var i=0; i<elem.length; i++) {
            var e = elem[i];
            if (e.nodeType==1) {
                var ee = firstChild(firstChild(firstChild(firstChild(e))));
                ee.style.width = '1700px'; //self.graphSizeX()+'px';
                ee.style.height = '800px'; //self.graphSizeY()+'px';
                Flotr.draw(ee, data, {
                    legend : {
                        position : 'se',            // Position the legend 'south-east'.
                        backgroundColor : '#D2E8FF' // A light blue background color.
                    },
                    HtmlText : false
                });
            }
        }
		
	}
}

function firstChild(e) {
    for (var j=0; j<e.childNodes.length; j++) {
        if (e.childNodes[j].nodeType == 1) {
            return e.childNodes[j];
        }
    }    
    return undefined;
}
