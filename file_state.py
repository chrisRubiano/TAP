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
        (mode, ino, dev, nlink, uid, x, xx, xxx, ssss, sss) = os.stat(dir+"/"+file)
        print "si existe el archivo %s" % (file)
        print str(ino)
    except Exception, e:
        print "no existe el archivo"



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dir", help="Directorio del archivo")
    parser.add_argument("-f", "--file", help="nombre del archivo")
    args = parser.parse_args()
    main(args.dir, args.file)
