'''
Different utils with no common topic, just to make your life easier when you
work with data
'''


def fixXLScsv(file):
    '''
    Replace '\r' by '\n' in csv's created by MS Excel
    '''
    fo = open(file)
    out_path = file[:-4] + '_fixed.csv'
    foo = open(out_path, 'w')
    lines = fo.readlines()[0]
    foo.write(lines.replace('\r', '\n'))
    foo.close()
    fo.close()
    return out_path


