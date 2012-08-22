from marketsim.scheduler import world
from colorsys import hsv_to_rgb
from random import uniform
import sys
from veusz.veusz_main import run
    
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
    
class Graph(object):
    
    def __init__(self, name):
        self._name = name
        self._datas = []
        
    def addTimeSerie(self, source):
        label = source.label
        self._datas.append(CSV(label+'.csv', source, label))
        
    def show(self):
        self.exportToVsz()
        sys.argv = [sys.argv[0], self._name+".vsz"]
        run()
        
    def exportToVsz(self):
        with open(self._name+".vsz", "w") as f:
            f.write("To(Add(\'page\', name=\'page1\', autoadd=False))\n")
            f.write("Set(\'width\', u\'25cm\')\n")
            f.write("To(Add(\'graph\', name=\'graph1\', autoadd=False))\n")
            f.write("To(Add(\'axis\', name=\'x\', autoadd=False))\n")
            f.write("Set(\'label\', u\'Time\')\n")
            f.write("To(\'..\')\n")
            f.write("Add(\'axis\', name=\'y\', autoadd=False)\n")

            for ts in self._datas:
                ts.flush()
                f.write("ImportFileCSV(\'"+ts._filename+"\', linked=True)\n")
                plotname = 'lineplot_' + ts._label
                timename = "Time"+ts._label
                f.write("To(Add(\'xy\', name=\'"+plotname+"\', autoadd=False))\n")
                f.write("Set(\'xData\', u\'"+timename+"\')\n")
                f.write("Set(\'yData\', u\'"+ts._label+"\')\n")
                f.write("Set(\'marker\', u\'none\')\n")
                f.write("Set(\'PlotLine/steps\', u\'left\')\n")
                f.write("Set(\'PlotLine/color\', u\'#"+randColor()+"\')\n")
                f.write("Set(\'key\', u\'"+ts._label+"\')\n")
                f.write("To(\'..\')\n")
                
            f.write("Add(\'key\', name=\'key1\', autoadd=False)\n")

