#!/usr/bin/env python

from bs4 import BeautifulSoup
import urllib2
import re
import os


def get_markup(url):
    try:
        respuesta = urllib2.urlopen(url)
        markup = respuesta.read()
        respuesta.close()
    except:
        markup = ""
        print ("No se obtuvo lenguaje de marcado desde %s"%url)
    return markup


def get_description(markup):
    sopa = BeautifulSoup(markup, "xml")
    tag = sopa.find('item').find('title') # Nombre de la puerta
    descripcion = str(sopa.find('item').find("description")) # Informacion de espera
    listaux = descripcion.split(' ')
    for l in listaux:
        if 'Date:' in l:
            fecha = listaux[listaux.index(l)+1]
    for l in listaux:
        if 'At' in l:
            hora = listaux[listaux.index(l)+1]
    for l in listaux:
        if 'delay' in l:
            delay = listaux[listaux.index(l)-2]+' '+listaux[listaux.index(l)-1]
    for l in listaux:
        if 'open' in l:
            openLanes = listaux[listaux.index(l)-2]+' '+listaux[listaux.index(l)-1]
    print delay
    print openLanes
    return tag, descripcion


def main():
    url_mariposa = "http://apps.cbp.gov/bwt/rss.asp?portList=260402&f=html"
    url_deconcini = "http://apps.cbp.gov/bwt/rss.asp?portList=260401&f=html"
    marML = get_markup(url_mariposa)
    decML = get_markup(url_deconcini)
    sopaMar = BeautifulSoup(marML, "xml")
    sopaDec = BeautifulSoup(decML, "xml")
    descripcion_mariposa = get_description(marML)

if __name__ == '__main__':
    main()