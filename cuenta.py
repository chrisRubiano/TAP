#!/usr/bin/python
'''
Autor: Cristian Samaniego
Fecha: 10/02/2016

contamos los directorios y archivos dentro de un directorio
'''
import os
import argparse


def dir_exists(absPath):
    if os.path.exists(absPath):
        ex = True
    else:
        ex = False
    return ex


def is_dir(absPath):
    if os.path.isdir(absPath):
        ex = True
    else:
        ex = False
    return ex


def total_file_list(absPath):
    totalFileList = os.listdir(absPath)
    return totalFileList


def file_count(totalFileList, absPath):
    fc = 0
    for f in totalFileList:
        if os.path.isfile("%s/%s" % (absPath, f)):
            fc += 1
    return fc


def dir_count(totalFileList, absPath):
    dc = 0
    for d in totalFileList:
        if os.path.isdir("%s/%s" % (absPath, d)):
            dc += 1
    return dc


def file_list(totalFileList, absPath):
    files = []
    for f in totalFileList:
        if os.path.isfile("%s/%s" % (absPath, f)):
            files.append(f)
    return files


def dir_list(totalFileList, absPath):
    dirs = []
    for d in totalFileList:
        if os.path.isdir("%s/%s" % (absPath, d)):
            dirs.append(d)
    return dirs


def main(pdir):
    absPath = os.path.abspath(pdir)
    exists = dir_exists(absPath)
    if exists:
        isDir = is_dir(absPath)
        if isDir:
            totalFileList = total_file_list(absPath)
            filesInt = file_count(totalFileList, absPath)
            dirInt = dir_count(totalFileList, absPath)
            fileList = file_list(totalFileList, absPath)
            dirList = dir_list(totalFileList, absPath)
            print "Archivos:"
            for f in fileList:
                print "\t%s" % (f)
            print "Hay %i archivos en el directorio" % (filesInt)
            print "Carpetas:"
            for d in dirList:
                print "\t%s" % (d)
            print "Hay %i carpetas en el directorio" % (dirInt)
        else:
            print "La ruta especificada es de un archivo"
    else:
        print "La ruta especificada no existe"


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dir", help="nombre del directorio")
    args = parser.parse_args()
    main(args.dir)
