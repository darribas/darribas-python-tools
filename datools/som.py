'''
Utils to work with Self-Organizing Maps
'''

import numpy as N
import numpy.ma as ma

def load_dat(dat_link):
    '''
    Load the data of a .dat file into a numpy array

    Arguments
    ---------
    dat_link        : string
                      Path to the file

    Returns
    -------
    a               : ndarray
                      Numpy array with the data from the .dat file
    '''
    a = []
    dat = open(dat_link)
    for line in dat:
        if line[0] != '#':
            line = line.strip('\n').strip('\r').split(' ')
            a.append(line)
    dat.close()
    a = N.array(a[1:])
    af = N.zeros(a.shape)
    for col in range(a.shape[1]):
        try:
            af[:, col] = map(float, a[:, col])
        except:
            print 'Column with strings'
    return af

def csv2dat(csv_link):
    '''
    Convert a csv file into .dat format suitable for SOM_PAK and other
    libraries

    NOTE: includes the csv header in the first line preceded by '#'
    ...

    Arguments
    ---------
    csv_link        : string
                      path of the csv to be converted. The .dat file will be
                      created at the same location with the same name but .dat
                      extension
    '''
    fo = open(csv_link + '.csv', 'r')
    ofo = open(csv_link + '.dat', 'w')
    head = fo.readline().replace(',', ' ')
    ofo.write('#' + head)
    ofo.write(str(len(head.strip('\n').split(' ')) - 2) + '\n') #-2 because of '#' and names column
    for line in fo:
        ofo.write(line.replace(',', ' '))
    ofo.close()
    fo.close()
    return 'Done!'

def stdDat(datIN_link, names=True):
    """
    Standardize a dat file and create a new one with same link (+'Z').

    NOTE: Assumes first line as header (preceded by '#')
    ...

    Arguments
    ---------
    datIN_link      : string
                      path to the .dat file to be converted
    names           : boolean 
                      If True (default) takes the last column as names and leaves it
                      out of the standardization
    """
    fo = open(datIN_link + '.dat')
    h0, h1 = fo.readline(), fo.readline()
    lines = fo.readlines()
    fo.close()
    a = []
    for line in lines:
        line = line.strip('\n').split(' ')
        a.append(line)
    a = N.array(a)
    print a.shape

    data, names = a[:, :-1], N.array([a[:, -1]]).T
    z = getZmv(data, 'x')
    #z = N.hstack((z, names))

    fo = open(datIN_link + 'Z.dat', 'w')
    fo.write(h0 + h1)
    for row, name in zip(z, names):
        line = ' '.join(row)
        line += ' %s\n'%name
        fo.write(line)
    fo.close()
    return 'Done'

def getZmv(a,mv):
    """
    Helper for stdDat

    Arguments:
    * a: array of strings with the input data
    * mv: string for missing values (e.g. 'x')
    Returns:
    * z: standardized masked array
    """
    mascara=N.zeros(a.shape)
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            if a[i,j]==mv:
                mascara[i,j]=1
                a[i,j]=0
    am=ma.masked_array(a,mask=mascara)
    am=N.array(am,dtype=float)
    z=N.copy(am)
    z=(z-z.mean(axis=0))/z.std(axis=0)
    z=ma.masked_array(z,dtype=str)
    for i in range(mascara.shape[0]):
        for j in range(mascara.shape[1]):
            if mascara[i,j]==1:
                z[i,j]='x'
    return z


