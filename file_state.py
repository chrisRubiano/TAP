#!/usr/bin/python
'''
Autor: Cristian Samaniego
Fecha: 04/02/2016

vemos si existe un archivo
'''
import os
import argparse


def find_file(dir, file):
    try:
        m = os.stat(dir+"/"+file)
        inode = m.st_ino
        ex = "%s si existe en el directorio %s" % (file, dir)
        ex +="\nSu inode es: "+str(inode)
    except Exception, e:
        ex = "no existe el archivo, error: "+e
    return ex


def main(dir, file):
    ar = find_file(dir, file)
    print ar





if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dir", help="Directorio del archivo", default=".")
    parser.add_argument("-f", "--file", help="nombre del archivo")
    args = parser.parse_args()
    main(args.dir, args.file)
