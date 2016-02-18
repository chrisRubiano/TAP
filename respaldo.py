#!/usr/bin/python
'''
Autor: Cristian Samaniego
Fecha: 17/02/2016

Respaldamos un directorio origen a un directorio destino
'''
import os
import argparse
import shutil


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


def main(origen, respaldo):
    """

    :param origen: Directorio de origen
    :param respaldo: Directorio de respaldo
    """
    absPathOri = os.path.abspath(origen)
    absPathRes = os.path.abspath(respaldo)
    existsOrigen = dir_exists(absPathOri)
    existsRespaldo = dir_exists(absPathRes)
    if existsRespaldo:
        isDirResp = is_dir(absPathRes)
        if not isDirResp:
            print "la ruta destino es un archivo"
    else:
       os.makedirs(absPathRes,0755)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--origen", help="Directorio de origen")
    parser.add_argument("-r", "--respaldo", help="Directorio de destino")
    args = parser.parse_args()
    main(args.origen, args.respaldo)
