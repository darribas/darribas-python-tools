import pylab as pl
import numpy as np

class Maptrix:
    '''
    Visualize the values of a matrix in a color scale. Mostly a wrapper from
    matplotlib's 'pcolor'
    ...

    Parameters
    ----------
    x           : array
                  Array with the matrix to visualize
    xlabels     : list
                  List of ticks to put in the matrix's X axis in the middle of
                  each square
    ylabels     : list
                  List of ticks to put in the matrix's Y axis in the middle of
                  each square
    colorbar    : boolean
                  When True (default) adds a scale colorbar to the matrix
    cmap        : string
                  Color set to apply to the matrix. Works as in matplotlib

    Attributes
    ----------
    p           : matplotlib.collections.PolyCollection
                  Plot object
    x           : array
                  Original matrix
    y           : array
                  Matrix reversed so the plot looks as expected
    '''
    def __init__(self, x, xlabels=False, ylabels=False, colorbar=True,
            cmap='summer'):
        y = np.zeros(x.shape)
        for i in np.arange(x.shape[0]):
            y[:, i] = x[:, i][:: -1]
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
        self.x = x
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

