#!/usr/bin/python
'''
Autor: Cristian Samaniego
Fecha: 04/02/2016

vemos si existe un archivo
'''
import os
import argparse


def main(dir, file):
    try:
        #(mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(dir+"/"+file)
        m = os.stat(dir+"/"+file)
        inode = m.st_ino
        print "%s si existe en el directorio %s" % (file, dir)
        print str(inode)
    except Exception, e:
        print "no existe el archivo"
        print e




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dir", help="Directorio del archivo")
    parser.add_argument("-f", "--file", help="nombre del archivo")
    args = parser.parse_args()
    main(args.dir, args.file)
