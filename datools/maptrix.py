import pylab as pl
import matplotlib as mtl
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
            cmap='summer', draw_pcolor=True, orientation='horizontal'):
        p = None
        y = align_array(x)
        fig = pl.figure()
        ax = fig.add_subplot(111)
        if draw_pcolor:
            p = pl.pcolor(y, cmap=cmap)
            ax.set_xlim(xmax=x.shape[1])
            ax.set_ylim(ymax=x.shape[0])
        if colorbar:
            sep = (np.max(y) - np.min(y))/4.
            ran = np.arange(np.min(y), np.max(y) + sep, sep)
            c = pl.colorbar(p, ticks=ran, format='%0.3f', \
                     orientation=orientation)
        if not xlabels:
            xlabels=['']*y.shape[0]
        '''
        pl.xlabel(xlabels, size='small', rotation=45)
        pl.xticks(xlabels, size='small', rotation=45)
        '''
        if not ylabels:
            ylabels=['']*y.shape[1]

        if draw_pcolor:
            self.xticks(xlabels, p)
            self.yticks(ylabels, p)

        self.p = p
        self.x = x
        self.y = y
        self.xlabels = xlabels
        self.ylabels = ylabels

    def xticks(self, names, plotobj, empty=False):
        l = [' '] * (len(names)*2 + 1)
        if not empty:
            for i,j in zip(range(0, len(l)-1, 2), range(len(names))):
                l[i+1] = names[j]
        plotobj.axes.xaxis.set_major_locator(pl.MaxNLocator(len(l)+1))
        plotobj.axes.set_xticklabels(l)
        try:
            plotobj.axes.tick_params(length=0, width=0, labelbottom=True,
                labeltop=False)
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

class Maptrix_ma:
    '''
    Visualize the values of a matrix with NaN values in a color scale. Mostly a wrapper from
    matplotlib's 'pcolor'
    ...

    Parameters
    ----------
    x           : array
                  Array with the matrix to visualize, including NaN values
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
    nancol      : string
                  Color for NaN values. Defaults to grey.

    Attributes
    ----------
    p           : matplotlib.collections.PolyCollection
                  Plot object
    mx          : array
                  Original matrix
    y           : masked array
                  Matrix reversed so the plot looks as expected (masked format

    Methods
    -------
    show        : Displays the figure
    save        : Saves the figure to a file (requires to pass a path). Does
                  not work if 'show' has been initialized
    '''
    def __init__(self, x, xlabels=False, ylabels=False, colorbar=True,
            cmap='summer', draw_pcolor=True, orientation='horizontal',
            nancol='0.5'):
        p = None
        mx = np.ma.array(x, mask=np.isnan(x))
        y = align_ma_array(mx)
        fig = pl.figure()
        ax = fig.add_subplot(111)
        ax.set_axis_bgcolor(nancol)
        pl.pcolor(np.ones(y.data.shape), cmap=mtl.cm.Greens)
        if draw_pcolor:
            p = pl.pcolor(y, cmap=cmap)
            ax.set_xlim(xmax=x.shape[1])
            ax.set_ylim(ymax=x.shape[0])
        if colorbar:
            sep = (np.max(y) - np.min(y))/4.
            ran = np.arange(np.min(y), np.max(y) + sep, sep)
            c = pl.colorbar(p, ticks=ran, format='%0.3f', \
                     orientation=orientation)
        if not xlabels:
            xlabels=['']*y.shape[0]
        '''
        pl.xlabel(xlabels, size='small', rotation=45)
        pl.xticks(xlabels, size='small', rotation=45)
        '''
        if not ylabels:
            ylabels=['']*y.shape[1]

        if draw_pcolor:
            self.xticks(xlabels, p)
            self.yticks(ylabels, p)

        self.p = p
        self.mx = mx
        self.y = y
        self.xlabels = xlabels
        self.ylabels = ylabels

    def xticks(self, names, plotobj, empty=False):
        l = [' '] * (len(names)*2 + 1)
        if not empty:
            for i,j in zip(range(0, len(l)-1, 2), range(len(names))):
                l[i+1] = names[j]
        plotobj.axes.xaxis.set_major_locator(pl.MaxNLocator(len(l)+1))
        plotobj.axes.set_xticklabels(l)
        try:
            plotobj.axes.tick_params(length=0, width=0, labelbottom=True,
                labeltop=False)
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

def align_ma_array(x):
    '''
    Modify the masked array to display properly in Matplotlib's 'pcolor'
    ...
    
    Arguments
    ---------
    x       : masked array
             Input array
    Attributes
    ----------
    y       : masked array
              Modified array in which columns have been reversed
    '''
    y = np.zeros(x.data.shape)
    for i in np.arange(y.shape[1]):
        y[:, i] = x.data[:, i][:: -1]
    y = np.ma.array(y, mask=np.isnan(y))
    return y

def set_h_tags(y, tags, subplot, fontsize=15, rotation=0, weight=None,
        verticalalignment='center', horizontalalignment='center'):
    '''
    Set horizontal tags
    ...

    Arguments
    ---------
    y           : float
                  Horizontal axis along which tags will be plotted
    tags        : list
                  List of strings to be plotted
    subplot     : subplot
                  Pylab subplot object
    ...         : other text parameters
    '''
    n = len(tags)
    sep = 1. / (2*n)
    for i, tag in zip(range(n), tags):
        x = float(i)/n + sep
        pl.text(x, y, tag, transform=subplot.transAxes,
                fontsize=fontsize, weight=weight, rotation=rotation,
                verticalalignment=verticalalignment,
                horizontalalignment=horizontalalignment)
    return 'ph'

def set_v_tags(x, tags, subplot, fontsize=15, rotation=0, weight=None,
        verticalalignment='center', horizontalalignment='center'):
    '''
    Set vertical tags
    ...

    Arguments
    ---------
    y           : float
                  Vertical axis along which tags will be plotted
    tags        : list
                  List of strings to be plotted
    subplot     : subplot
                  Pylab subplot object
    ...         : other text parameters
    '''
    n = len(tags)
    sep = 1. / (2*n)
    for i, tag in zip(range(n), tags):
        y = float(i)/n + sep
        pl.text(x, y, tag, transform=subplot.transAxes,
                fontsize=fontsize, weight=weight, rotation=rotation,
                verticalalignment=verticalalignment,
                horizontalalignment=horizontalalignment)
    return 'ph'

if __name__ == '__main__':
    z = np.zeros((59, 5))
    z[0, 0] = 100
    z[9, 3] = 100
    m = Maptrix(z)
