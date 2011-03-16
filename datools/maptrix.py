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

    Methods
    -------
    show        : Displays the figure
    save        : Saves the figure to a file (requires to pass a path). Does
                  not work if 'show' has been initialized
    '''
    def __init__(self, x, xlabels=False, ylabels=False, colorbar=True,
            cmap='summer'):
        y = align_array(x)
        p = pl.pcolor(y, cmap=cmap)
        if colorbar:
            c = pl.colorbar(ticks=np.arange(np.min(y), np.max(y), \
                    (np.max(y) - np.min(y))/8.), format='%0.3f', \
                    spacing='proportional')
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

    def save(self, path):
        pl.savefig(path)
        return path

def align_array(x):
    '''
    Modify the array to display properly in Matplotlib's 'pcolor'
    ...
    
    Arguments
    ---------
    x       : array
             Input array
    Attributes
    ----------
    y       : array
              Modified array in which columns have been reversed
    '''
    y = np.zeros(x.shape)
    for i in np.arange(y.shape[1]):
        y[:, i] = x[:, i][:: -1]
    return y

if __name__ == '__main__':
    z = np.zeros((10, 20))
    z[0, 0] = 100
    z[9, 19] = 10
    m = Maptrix(z).show()
