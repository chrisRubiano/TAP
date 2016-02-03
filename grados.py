# Cristian Raul Samaniego Rubiano
# grados.py convierte centigrados a fahrenheit o kelvin,
# y fahrenheit a centigrados
# 19/01/2015

import sys


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


def main():
    if len(sys.argv) == 3:
        a = convierte_grados(float(sys.argv[1]), sys.argv[2])
        print "%s son %s" % (sys.argv[1], a)
    elif len(sys.argv) == 2:
        a = convierte_grados(float(sys.argv[1]))
        print "%s son %s" % (sys.argv[1], a)
    else:
        print "El numero de argumentos no es el correcto."

if __name__ == '__main__':
    main()
