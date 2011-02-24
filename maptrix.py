import pylab as pl
import numpy as np

class Maptrix:
    def __init__(self, x, xlabels=False, ylabels=False, colorbar=True,
            cmap='summer'):
        y = np.zeros(x.shape)
        for i in np.arange(x.shape[0]):
            y[:, i] = x[:, i][:: -1]
        x = ''
        p = pl.pcolor(y, cmap=cmap)
        if colorbar:
            c = pl.colorbar()
        if not xlabels:
            xlabels=['']*y.shape[0]
        self.xticks(xlabels, p)
        if not ylabels:
            ylabels=['']*y.shape[1]
        self.yticks(ylabels, p)
        self.p = p
        self.y = y

    def xticks(self, names, plotobj, empty=False):
        l = [' '] * (len(names)*2 + 1)
        if not empty:
            for i,j in zip(range(0, len(l)-1, 2), range(len(names))):
                l[i+1] = names[j]
        plotobj.axes.xaxis.set_major_locator(pl.MaxNLocator(len(l)+1))
        plotobj.axes.set_xticklabels(l)
        try:
            plotobj.axes.tick_params(length=0, width=0, labelbottom=False,
                labeltop=True)
        except:
            print 'It was not possible to tweak tick parameters'
        return plotobj

    def yticks(self, names, plotobj, empty=False):
        l = [' '] * (len(names)*2 + 1)
        if not empty:
            for i,j in zip(range(0, len(l)-1, 2), range(len(names))):
                l[i+1] = names[j]
        plotobj.axes.yaxis.set_major_locator(pl.MaxNLocator(len(l)+1))
        plotobj.axes.set_yticklabels(l)
        try:
            plotobj.axes.tick_params(length=0, width=0)
        except:
            print 'It was not possible to tweak tick parameters'
        return plotobj

    def show(self):
        pl.show()


