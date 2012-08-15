'''
Different utils with no common topic, just to make your life easier when you
work with data
'''

def copy_shp(shp_in, shp_out):
    '''
    Copy files from a shapefile other than the dbf
    '''
    cmd = 'cp %s %s'%(shp_in, shp_out)
    os.system(cmd)
    cmd = 'cp %s %s'%(shp_in.replace('shp', 'shx'), shp_out.replace('shp', 'shx'))
    os.system(cmd)
    cmd = 'cp %s %s'%(shp_in.replace('shp', 'prj'), shp_out.replace('shp', 'prj'))
    os.system(cmd)
    return None

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


