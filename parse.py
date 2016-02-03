#!/usr/bin/python
'''
Autor: Cristian Samaniego
Fecha: 26/01/2016

Lee y escribe nombres
'''

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-l", "--lado", help = "es un lado",
                    type = int)
parser.add_argument("-a", "--ancho", help = "es un ancho",
                    type = int)
args = parser.parse_args()
print args.lado * args.ancho
