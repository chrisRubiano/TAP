#!/usr/bin/env python
from bs4 import BeautifulSoup
import urllib2


def refresh_html(mar, dec, sopa):
    try:
        tds = sopa.findAll('td', {'class': 'puerta'})
        tds[0].string = mar[0]
        tds[1].string = dec[0]
        tds = sopa.findAll('td', {'class': 'fecha'})
        tds[0].string = mar[1]
        tds[1].string = dec[1]
        tds = sopa.findAll('td', {'class': 'hora'})
        tds[0].string = mar[2]
        tds[1].string = dec[2]
        tds = sopa.findAll('td', {'class': 'espera'})
        tds[0].string = mar[3]
        tds[1].string = dec[3]
        tds = sopa.findAll('td', {'class': 'lineas'})
        tds[0].string = mar[4]
        tds[1].string = dec[4]
        with open('index.html', 'w') as fh:
            fh.write(sopa.prettify())
    except:
        print "no se pudo escribir el archivo html"


def read_html(fileName):
    try:
        with open(fileName) as fh:
            html = fh.read()
    except:
        html = ""
        print "no se pudo leer el archivo %s" % fileName
    return html


def read_file(fileName):
    try:
        with open(fileName, 'r') as fh:
            valores = fh.read().splitlines()
            v = valores[-1].split(',')
    except:
        v = []
        print "no se pudo leer del archivo %s" % fileName
    return v


def write_file(fileName, desc):
    with open(fileName, 'a') as fh:
        fh.write(desc[0]+", "+desc[1]+", "+desc[2]+", "+desc[3]+", "+desc[4]+"\n")


def get_markup(url):
    try:
        respuesta = urllib2.urlopen(url)
        markup = respuesta.read()
        respuesta.close()
    except:
        markup = ""
        print ("No se obtuvo lenguaje de marcado desde %s"%url)
    return markup


def get_info(markup):
    sopa = BeautifulSoup(markup, "xml")
    tag = sopa.find('item').find('title').text # Nombre de la puerta
    descripcion = str(sopa.find('item').find("description")) # Informacion de espera
    listaux = descripcion.split(' ')
    for l in listaux:
        if 'Date:' in l:
            date = listaux[listaux.index(l)+1]
        if 'At' in l:
            hour = listaux[listaux.index(l)+1]
        if 'delay' in l:
            delay = listaux[listaux.index(l)-2]+' '+listaux[listaux.index(l)-1]
        if 'open' in l:
            openLanes = listaux[listaux.index(l)-2]+' '+listaux[listaux.index(l)-1]
            break
    return tag, date, hour, delay, openLanes


def main():
    mariposa = 'mariposa.csv'
    deconcini = 'deconcini.csv'
    url_mariposa = "http://apps.cbp.gov/bwt/rss.asp?portList=260402&f=html"
    url_deconcini = "http://apps.cbp.gov/bwt/rss.asp?portList=260401&f=html"
    marML = get_markup(url_mariposa)
    decML = get_markup(url_deconcini)
    info_mariposa = get_info(marML)
    print info_mariposa
    write_file(mariposa, info_mariposa)
    info_deconcini = get_info(decML)
    print info_deconcini
    write_file(deconcini,info_deconcini)
    mar = read_file(mariposa)
    dec = read_file(deconcini)
    html = read_html("esqueleto.html")
    sopa = BeautifulSoup(html,"html.parser")
    refresh_html(mar, dec, sopa)


if __name__ == '__main__':
    main()