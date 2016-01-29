'''
Autor: Cristian Samaniego
Fecha: 26/01/2016

Lee y escribe nombres
'''


def modifica_calificaciones(lista_alumnos, porcentaje):
    for al in lista_alumnos:
        if al[1] < 100:
            al[1] += ((al[1]/100) * 5)
            if al[1] > 100:
                al[1] = 100.0
            if al[1] < 0:
                al[1] = 0
        print al[1]


def escribe_archivo(nombreArchivo, nuevaLista):
    with open(nombreArchivo, "w") as fh:
        for n in nuevaLista:
            s = "%s, %f\n" % (n[0], n[1])
            fh.write(s)
            print s


def lee_archivo(nombreArchivo):
    nuevaLista = []
    with open(nombreArchivo) as fh:
        lista = fh.read().splitlines()
        for l in lista:
            nuevaLista.append(l.split(","))
        for n in nuevaLista:
            n[1] = float(n[1])
    return nuevaLista


def main(archivoEntrada, archivoSalida, porcentaje):
    nombres = lee_archivo(archivoEntrada)
    if len(nombres) > 0:
        for nombre in nombres:
            print ": %s" % nombre
        modifica_calificaciones(nombres, porcentaje)
        for nombre in nombres:
            print ": %s" % nombre
        escribe_archivo(archivoSalida, nombres)
    else:
        print "no existen nombres"

if __name__ == '__main__':
    main("nombres.csv", "salida.csv", 5)
