from marketsim import bind, types
from marketsim.ops._all import CandleStick
from colorsys import hsv_to_rgb
import subprocess 
import random
import os
import errno
import math
import __main__

from marketsim.gen._out._intrinsic_base.veusz import Graph_Base

def ensure_dir(path):
    """ Ensures that directory given 'path' exists
    """
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

def myDir():
    """ Returns a directory for temporary files with respect to name of main module
    """
    d = r"_output/" + os.path.basename(__main__.__file__)
    ensure_dir(d)
    return d + r"/"

startColors = ['#2f7ed8', '#8bbc21', '#910000', '#1aadce', '#0d233a', '#492970',
               '#f28f43', '#77a1e5', '#c42525', '#a6c96a']
def randColor():
    """ Returns a color randomly chosen from HSV space
    """
    h = 0.3
    v = 0.85
    s = 0.9
    
    for c in startColors:
        yield c

    while True:
        
        def toHex(x):
            return hex(int(x*255))[2:]
    
        r, g, b = hsv_to_rgb(h, s, v)
        
        yield u'#' + toHex(r) + toHex(g) + toHex(b)

        h += 2 / (1+math.sqrt(5))
        h = h - 1 if h > 1 else h
        #v = 1-v

graphDataHeader = """
ImportFileCSV('{0}', linked=True)
To(Add('xy', name='{1}', autoadd=False))
"""

class OutputStream(object):
    
    def __init__(self, filename):
        self._filename = filename
        self._file = None
        
    def reset(self):
        if self._file: 
            self._file.close()
        self._file = file(self._filename, 'w')
        
    def __enter__(self):
        self.reset()
        return self
    
    def __getstate__(self):
        return {'_filename': self._filename}

    def __setstate__(self, dict):
        self._filename = dict['_filename']
        self._file = None
        self.reset()
        
    def write(self, s):
        self._file.write(s)
 
    def flush(self):
        self._file.flush()
        os.fsync(self._file)     
        
    def __exit__(self, type, value, traceback):
        self.flush()

import collections

class TimeserieAttributes(collections.Mapping):
    """ Represents environment for model objects

    Holds references to some outer objects (scheduler, trader in hand, orderbook in hand etc.)
    This class is immutable so its instances can be easily shared.

    """
    def __init__(self, d):
        self._d = d.copy()
        self._hash = None

    def bind_ex(self, ctx):
        pass

    def reset_ex(self, generation):
        pass

    def __getattr__(self, item):
        if item[0:2] != '__':
            return self.__getitem__(item)
        else:
            raise AttributeError

    def __iter__(self):
        return iter(self._d)

    def __len__(self):
        return len(self._d)

    def __getitem__(self, key):
        return self._d[key]

    def __hash__(self):
        if self._hash is None:
            self._hash = 0
            for pair in self.iteritems():
                self._hash ^= hash(pair)
        return self._hash

from marketsim.gen._out._intrinsic_base.veusz import CSV_Base

class CSV_Impl(CSV_Base):
    """ Represents a time serie to be written into a file 
    """
    
    def exportToVsz(self, f, colors):
        """ Exports time serie to Vsz file
        """
        label = self.source.label
        filename = (label+'.csv').replace('\\','_').replace('*', '_').replace("/",'_').replace(">",'_').replace("<",'_')
        fullname = self.directory + filename

        attributes = {
            'xData' : "Time"+label,
            'yData' : label,
            'marker': 'none',
            r'PlotLine/steps': u'left',
            r'PlotLine/color': colors.next(),
            'key' : label,
            }
        for k,v in self.attributes.iteritems():
            attributes[k] = v                

        with OutputStream(fullname) as csv:
    
            csv.write('Time'+label+','+label+',\n')
    
            for (t,x) in self.source.data:
                if type(x) is CandleStick:
                    csv.write(str(t) + ',' + str(x.mean) + ',\n')  
                elif x is not None: 
                    csv.write(str(t) + ',' + str(x) + ',\n')
                else:
                    csv.write(str(t) + ',' + "nan" + ',\n')
            
        
        f.write(graphDataHeader.format(filename, label))
        for k,v in attributes.iteritems():
            f.write("Set('{0}', {1})\n".format(k,repr(v)))
        f.write("To('..')\n")

graphHeader = """
To(Add('page', name='page_{0}', autoadd=False))
Set('width', u'25cm')
To(Add('graph', name='graph_{0}', autoadd=False))
To(Add('axis', name='x', autoadd=False))
Set('label', u'Time')
To('..')
Add('axis', name='y', autoadd=False)
"""

graphTrailer = """
Add('key', name='key1', autoadd=False)
To('..')
To('..')
"""
# Export(r'{0}.png', page={1})

def translateAttributes(src):
    """ Translates abstract attributes to Veusz graph attributes
    """
    res = {}
    if 'smooth' in src and src['smooth']:
        res[r'PlotLine/steps'] = 'off'
    if 'fillBelow' in src and src['fillBelow']:
        res['FillBelow/color'] =  u'#55aaff'
        res['FillBelow/hide'] = False
        res['FillBelow/transparency'] = 90
    if 'fillAbove' in src and src['fillAbove']:
        res['FillAbove/color'] =  u'#aaff7f'
        res['FillAbove/hide'] = False
        res['FillAbove/transparency'] = 90
    if 'transparency' in src:
        res['PlotLine/transparency'] = src["transparency"]
        
    return res

from marketsim.gen._out._intrinsic_base.veusz import VolumeLevelProxy_Base

class VolumeLevelProxy_Impl(VolumeLevelProxy_Base):
    
    @property
    def data(self):
        return [(t, x[self.idx]) for (t,x) in self.source.data]
        
    @property
    def label(self):
        return self.source.label + '{' + str(self.source.source.dataSource.volumes[self.idx]) + '}'
        
    
class Graph_Impl(Graph_Base):
    """ Represents a single Veusz graph
    """
    
    def __init__(self):
        """ Initializes graph with some name
        """
        self._datas = []
        
    @property
    def series(self):
        return self._datas
    
    _internals = ['_datas']
        
    def addTimeSerie(self, source, attributes = {}):
        """ Adds a time serie to the graph
        source should be a source of events (so to have advise method) 
        and have a value property 
        attributes -- veusz specific attributes that will be applied for this time serie  
        """
        from marketsim.gen._out.veusz._csv import CSV

        attr = translateAttributes(source.attributes)
        for k,v in attributes.iteritems():
            attr[k] = v
        if 'volumeLevels' in source.attributes:
            self.processVolumeLevels(source, attr)    
        else:    
            self._datas.append(CSV(myDir(), source, TimeserieAttributes(attr)))
            
    def processVolumeLevels(self, source, attr):
        from marketsim.gen._out.veusz._csv import CSV
        from marketsim.gen._out.veusz._volumelevelproxy import VolumeLevelProxy
        volumes = source.source.dataSource.volumes
        for i in range(len(volumes)):
            proxy = VolumeLevelProxy(source, len(volumes) - i - 1)
            self._datas.append(CSV(myDir(), proxy, TimeserieAttributes(attr)))
        
    def removeTimeSerie(self, source):
        self._datas = [x for x in self._datas if x._source is not source]
        
    def addTimeSeries(self, series):
        for x in series:
            self.addTimeSerie(x)
            
    def __iadd__(self, series):
        self.addTimeSeries(series)
        return self
        
    def exportTo(self, f, idx):
        """ Exports graph to some Vsz file
        """
        f.write(graphHeader.format(self.name))
        
        colors = randColor()

        for ts in self._datas:
            ts.exportToVsz(f, colors)
            
        f.write(graphTrailer.format(self.name, idx))
        
def run(name):
    if not 'VEUSZ_EXE' in os.environ:
        print "Path to Veusz executable is not specified in VEUSZ_EXE environment variable"
        print "Hoping that 'veusz' executable is in standard paths"
        print "You may look also for the results manually in Veusz script: " + myDir()+name+".vsz"
        veusz_exe = 'veusz'
    else:
        veusz_exe = os.environ['VEUSZ_EXE']
    subprocess.call(veusz_exe + ' ' + os.path.abspath(os.path.join(myDir(), name+".vsz")), shell=True)
        

def render(name, graphs):
    """ Draws a sequence of graphs into a Veusz workspace and launches veusz
    """
    name = name.replace(' ', '-')
    with open(os.path.join(myDir(), name+".vsz"), "w") as f:
        idx = 0
        for g in graphs:
            g.exportTo(f, idx)
            idx += 1
    run(name)
    