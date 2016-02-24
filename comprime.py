#!/usr/bin/python
'''
Autor: Cristian Samaniego
Fecha: 17/02/2016

Comprimimos un directorio origen y respaldamos en un directorio destino
TODO:   +renombrar archivos
'''
import os
import argparse
import shutil
import string


def rename_dir(abspath):
    splitPath = string.rsplit(abspath, "/", 1)
    x = splitPath[1][-1:]
    if x.isdigit():
        splitPath[1] = splitPath[1][:-1] + str(int(x)+1)
    else:
        splitPath[1] = splitPath[1]+"2"
    absPath = os.path.join(splitPath[0], splitPath[1])
    return absPath


def rename_file(path):
    splitPath = string.rsplit(path, "/", 1)
    filename = splitPath[1]
    filepath = splitPath[0]
    while file_exists(path):
        x = filename[-1:]
        if x.isdigit():
            filename = filename[:-1] + str(int(x)+1)
        else:
            filename + "2"
        fullPath = os.path.join(filepath, filename)
    return fullPath


def dir_exists(absPath):
    """

    :param absPath: el absolute path del directorio
    :return: True si existe el directorio, False si no existe
    """
    if os.path.exists(absPath):
        ex = True
    else:
        ex = False
    return ex


def file_exists(absPath):
    """

    :param absPath: el absolute path del directorio
    :return: True si existe el directorio, False si no existe
    """
    if os.path.exists(absPath+".tar.gz"):
        ex = True
    else:
        ex = False
    return ex


def is_dir(absPath):
    """

    :param absPath: el absolute path del directorio
    :return: True si es un directorio, False si es archivo
    """
    if os.path.isdir(absPath):
        ex = True
    else:
        ex = False
    return ex


def total_file_list(absPath):
    """

    :param absPath: el absolute path del directorio
    :return: la lista de archivos dentro del directorio
    """
    totalFileList = os.listdir(absPath)
    return totalFileList


def dir_copy(absPathOri, absPathRes):
    #shutil.copytree(absPathOri, absPathRes)
    if not dir_exists(absPathRes):
        os.makedirs(absPathRes)
    os.chdir(absPathRes)
    splitpath = splitPath = string.rsplit(absPathOri, "/", 1)
    filename = splitpath[1]
    fullpath = os.path.join(absPathRes, filename)
    if not file_exists(fullpath):
        shutil.make_archive(filename, "gztar", absPathRes, absPathOri)
    else:
        filename = rename_file(fullpath)
        shutil.make_archive(filename, "gztar", absPathRes, absPathOri)




def file_copy(absPathOri, absPathRes):
    shutil.copy(absPathOri, absPathRes)


def main(origen, respaldo):
    """

    :param origen: Directorio de origen
    :param respaldo: Directorio de respaldo
    """
    absPathOri = os.path.abspath(origen)
    absPathRes = os.path.abspath(respaldo)
    existsOrigen = dir_exists(absPathOri)
    existsRespaldo = dir_exists(absPathRes)
    if existsOrigen:
        if existsRespaldo:
            isDirResp = is_dir(absPathRes)
            if not isDirResp:
                print "la ruta destino es un archivo"
            else:
                if is_dir(absPathOri):
                    dir_copy(absPathOri, absPathRes)
                else:
                    file_copy(absPathOri, absPathRes)
        else:
            if is_dir(absPathOri):
                dir_copy(absPathOri, absPathRes)
            else:
                file_copy(absPathOri, absPathRes)
    else:
        print "no existe el directorio o archivo de origen"


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--origen", help="Directorio de origen")
    parser.add_argument("-r", "--respaldo", help="Directorio de destino")
    args = parser.parse_args()
    main(args.origen, args.respaldo)