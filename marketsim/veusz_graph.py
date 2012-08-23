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

   
class CSV(file):
    
    def __init__(self, filename, source, label):
        
        file.__init__(self, filename, 'w')
        self._filename = filename
        self._label = label
        
        self.write('Time'+label+','+label+',\n')
        
        def wakeUp(_):
            x = source.value
            if x is not None:
                self.write(str(world.currentTime) + ',' + str(x) + ',\n')
        
        source.advise(wakeUp)

def randColor():
    h = uniform(0., 1.) 
    s = uniform(0.2, .8)
    v = uniform(0.3, .8)
    
    def toHex(x):
        return hex(int(x*255))[2:]

    r, g, b = hsv_to_rgb(h, s, v)
    
    return toHex(r) + toHex(g) + toHex(b)

graphHeader = """
To(Add('page', name='page_{0}', autoadd=False))
Set('width', u'25cm')
To(Add('graph', name='graph_{0}', autoadd=False))
To(Add('axis', name='x', autoadd=False))
Set('label', u'Time')
To('..')
Add('axis', name='y', autoadd=False)
"""

graphData = """
ImportFileCSV('{0}', linked=True)
To(Add('xy', name='{1}', autoadd=False))
Set('xData', u'Time{1}')
Set('yData', u'{1}')
Set('marker', u'none')
Set('PlotLine/steps', u'left')
Set('PlotLine/color', u'#{2}')
Set('key', u'{1}')
To('..')
"""

graphTrailer = """
Add('key', name='key1', autoadd=False)
To('..')
To('..')
"""
    
class Graph(object):
    
    def __init__(self, name):
        self._name = name
        self._datas = []
        
    def addTimeSerie(self, source):
        label = source.label
        self._datas.append(CSV(myDir()+label+'.csv', source, label))
        
    def exportTo(self, f):
        f.write(graphHeader.format(self._name))

        for ts in self._datas:
            ts.flush()
            f.write(graphData.format(ts._filename, ts._label, randColor()))
            
        f.write(graphTrailer)

def showGraphs(name, graphs):
    with open(myDir() + name+".vsz", "w") as f:
        for g in graphs:
            g.exportTo(f)
    sys.argv = [sys.argv[0], myDir()+name+".vsz"]
    run()
    