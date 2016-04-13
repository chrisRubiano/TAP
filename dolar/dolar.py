# -*- coding: utf-8 -*-
'''
Links:
Banamex:            http://portal.banamex.com.mx/c719_004/economiaFinanzas/es/home?xhost=http://www.banamex.com/
Bancomer:
Banjercito:         http://www.banjercito.com.mx/index.jsp?hd_ligaContenido=Informacion_financiera/redirectInfFin.jsp?operacion=6
Banco del bajio:    http://www.bb.com.mx/

TODO:   try exception en cada metodo
        escribir archivos
'''
import urllib2
from bs4 import BeautifulSoup
import time

def acumula_valores(acu, dolar):
    acu['compra'].append(dolar['compra'])
    acu['venta'].append(dolar['venta'])

def console_print(banco, dolar):
    print banco+' : %.4f | %.4f' % (dolar['compra'], dolar['venta'])


def write_file(fileName, dolar):
    file_name = fileName+".csv"
    with open(file_name, 'a') as fh:
        fh.write(time.strftime("%d-%m-%Y")+' '+time.strftime("%H:%M:%S")+', %.4f, %.4f' % (dolar['compra'], dolar['venta']))


def get_html(url):
    try:
        respuesta=urllib2.urlopen(url)
        html=respuesta.read()
        respuesta.close()
    except:
        html=""
        print ("no se obtuvo html de %s"%url)
    return html


def get_value_banamex(html):
    dolar = {}
    sopa = BeautifulSoup(html,'html.parser')
    minisopas = sopa.find(id='cotizaciones').find('div').find(id='monedas').find('tbody').findAll('tr') #len=2
    dolar['compra'] = float(minisopas[0].find('td').text)
    dolar['venta'] = float(minisopas[1].find('td').text)
    return dolar


def get_value_banbajio(html):
    dolar = {}
    sopa = BeautifulSoup(html,'html.parser')
    minisopa = sopa.findAll('div', {'class' : ['mod_inFin_central_2_compra', 'mod_inFin_central_2_venta']})
    dolar['compra'] = float(minisopa[0].text)
    dolar['venta'] = float(minisopa[1].text)
    return dolar


def main():
    acu = {'compra':[],'venta':[]}
    #banamex
    banco = 'banamex'
    url = 'http://portal.banamex.com.mx/c719_004/economiaFinanzas/es/home?xhost=http://www.banamex.com/'
    html = get_html(url)
    dolar = get_value_banamex(html)
    write_file(banco, dolar)
    console_print(banco, dolar)
    acumula_valores(acu, dolar)
    #banbajio
    url = 'http://www.bb.com.mx/'
    html = get_html(url)
    dolar = get_value_banbajio(html)
    write_file(banco, dolar)
    console_print(banco, dolar)
    acumula_valores(acu, dolar)

if __name__ == '__main__':
    main()