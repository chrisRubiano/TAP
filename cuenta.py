#!/usr/bin/python
'''
Autor: Cristian Samaniego
Fecha: 10/02/2016

contamos los directorios y archivos dentro de un directorio
'''
import os
import argparse


def file_list(absPath):
    fileList = os.listdir(absPath)
    return fileList


def file_count(fileList, absPath):
    fc = 0
    for f in fileList:
        if os.path.isfile("%s/%s" % (absPath, f)):
            fc += 1
    return fc


def dir_count(fileList, absPath):
    dc = 0
    for d in fileList:
        if os.path.isdir("%s/%s" % (absPath, d)):
            dc += 1
    return dc


def main(pdir):
    absPath = os.path.abspath(pdir)
    fileList = file_list(absPath)
    filesInt = file_count(fileList, absPath)
    dirInt = dir_count(fileList, absPath)
    print "Hay %i archivos en el directorio" % (filesInt)
    print "Hay %i carpetas en el directorio" % (dirInt)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dir", help="nombre del directorio")
    args = parser.parse_args()
    main(args.dir)
