#!/usr/bin/python
'''
Autor: Cristian Samaniego
Fecha: 03/02/2016

modifica grados, con argumentos
TODO:
'''

import sys
import argparse


"""
    convierte_grados

        acepta:
            grados, entero o flotante
            a, tipo de grados a convertir (fahrenheit, celsius o kelvin)
        regresa:
            g, la temperatura ya convertida

"""


def convierte_grados(grados, a="centigrados"):
    if a == "fahrenheit":
        g = str(32 + (grados * 1.8)) + " fahrenheit"
    elif a == "kelvin":
        g = str(grados + 273.15) + " kelvin"
    else:
        g = str((5 * (grados - 32)) / 9) + " centigrados"
    return g

"""
    main
"""


def main(grados, tipo):
    a = convierte_grados(grados, tipo)
    print "%s son %s" % (grados, a)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--tipo", help="el tipo de grados a convertir")
    parser.add_argument("-g", "--grados", help="el numero de grados",
                        type=int)
    args = parser.parse_args()
    main(args.grados, args.tipo)
