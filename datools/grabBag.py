'''
Different utils with no common topic, just to make your life easier when you
work with data
'''


def fix_file(file):
    fo = open(file)
    foo = open(file[:-4] + '_fixed.csv', 'w')
    lines = fo.readlines()[0]
    foo.write(lines.replace('\r', '\n'))
    foo.close()
    fo.close()
    return 'Done!'


