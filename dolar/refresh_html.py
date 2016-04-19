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


def main():
    html = lee_archivo('esqueleto.html')
    sopa = BeautifulSoup(html, 'html.parser')
    sopa.title.string = "Mi pagina web"
    listabancos = sopa.findAll('td', { 'class' : ['banco']})
    bancos = os.listdir('.')
    for b in bancos:
        if b.endswith('.csv'):
            #precios = leer_banco(b)
            nombrebanco = b.split('.')
            print nombrebanco[0]

if __name__ == '__main__':
    main()