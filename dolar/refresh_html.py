##!/usr/bin/python
'''
TODO:
    +funcion leer_banco
    +leer todos los archivos del directorio
    +editar los nombres de los bancos y rellenar los precios de compra y venta
'''

from bs4 import BeautifulSoup
from funciones import *
import os


def leer_banco(banco):
    compraventa = {}
    try:
        with open(banco, 'r') as fh:
            valores = fh.read().splitlines()
            v = valores[-1].split(',')
            compraventa['fecha'] = v[0].split(' ')[0]
            compraventa['compra'] = v[1]
            compraventa['venta'] = v[2]
    except:
        compraventa['compra'] = 0
        compraventa['venta'] = 0
    return compraventa


def main():
    i = 0
    c = 0
    v = 0
    precios = []
    nombresbanco = []
    html = lee_archivo('esqueleto.html')
    sopa = BeautifulSoup(html, 'html.parser')
    sopa.title.string = "Precios del Dolar"
    sopa.h1.string = "Dolar"
    x = leer_banco('Banamex.csv')
    sopa.p.string = "Valores de compra y venta del dolar al dia %s" % x['fecha']
    listabancos = sopa.findAll('td',{ 'class': ['banco']})
    listacompra = sopa.findAll('td',{ 'class': ['compra']})
    listaventa = sopa.findAll('td',{ 'class': ['venta']})
    bancos = os.listdir('.')
    for b in bancos:
        if b.endswith('.csv'):
            precios.append(leer_banco(b))
            nombresbanco.append(b.split('.')[0])
    for l in listabancos:
        l.string = nombresbanco[i]
        i += 1
    i = 0
    for l in listacompra:
        l.string = precios[i]['compra']
        i += 1
    i = 0
    for l in listaventa:
        l.string = precios[i]['venta']
        i += 1
    for p in precios:
        c += float(p['compra'])
        v += float(p['venta'])
    promcompra = c / len(precios)
    promventa = v / len(precios)
    sopa.find('td', {'class': 'compra-prom'}).string = str("%.4f" % promcompra)
    sopa.find('td', {'class': 'venta-prom'}).string = str("%.4f" % promventa)

    with open('index.html', 'w') as fh:
        fh.write(sopa.prettify())


if __name__ == '__main__':
    main()