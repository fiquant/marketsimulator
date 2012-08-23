from marketsim.scheduler import world
from colorsys import hsv_to_rgb
from random import uniform
import sys
from veusz.veusz_main import run
import os
import errno
import __main__


def ensure_dir(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

def myDir():
    d = r"_output/" + os.path.basename(__main__.__file__)
    ensure_dir(d)
    return d + r"/"


def randColor():
    h = uniform(0., 1.) 
    s = uniform(0.2, .8)
    v = uniform(0.3, .8)
    
    def toHex(x):
        return hex(int(x*255))[2:]

    r, g, b = hsv_to_rgb(h, s, v)
    
    return toHex(r) + toHex(g) + toHex(b)

graphDataHeader = """
ImportFileCSV('{0}', linked=True)
To(Add('xy', name='{1}', autoadd=False))
"""
   
class CSV(file):
    
    def __init__(self, filename, source, label, attributes={}):
        
        file.__init__(self, filename, 'w')
        self._filename = filename
        self._label = label
        
        self.write('Time'+label+','+label+',\n')
        
        def wakeUp(_):
            x = source.value
            if x is not None:
                self.write(str(world.currentTime) + ',' + str(x) + ',\n')
        
        source.advise(wakeUp)
        
        self._attributes = {
            'xData' : "Time"+label,
            'yData' : label,
            'marker': 'none',
            r'PlotLine/steps': u'left',
            r'PlotLine/color': u'#' + randColor(),
            'key' : label,
            }
        
        for k,v in attributes.iteritems():
            self._attributes[k] = v
        
    def exportToVsz(self, f):
        f.write(graphDataHeader.format(self._filename, self._label))
        for k,v in self._attributes.iteritems():
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

def translateAttributes(src):
    res = {}
    if 'smooth' in src and src['smooth']:
        res[r'PlotLine/steps'] = 'off'
    return res
        
class Graph(object):
    
    def __init__(self, name):
        self._name = name
        self._datas = []
        
    def addTimeSerie(self, source, attributes = {}):
        label = source.label
        attr = translateAttributes(source.attributes)
        for k,v in attributes.iteritems():
            attr[k] = v
        filename = (myDir()+label+'.csv').replace('\\','_')
        self._datas.append(CSV(filename, source, label, attr))
        
    def exportTo(self, f):
        f.write(graphHeader.format(self._name))

        for ts in self._datas:
            ts.exportToVsz(f)
            
        f.write(graphTrailer)

def showGraphs(name, graphs):
    with open(myDir() + name+".vsz", "w") as f:
        for g in graphs:
            g.exportTo(f)
    sys.argv = [sys.argv[0], myDir()+name+".vsz"]
    run()
    