##!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Integrantes:
    Cristian Samaniego
    Emmanuelle Guerrero
    Martin Ruiz
    Erick Saldamando
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
        fh.write(time.strftime("%d-%m-%Y")+' '+time.strftime("%H:%M:%S")+', %.4f, %.4f\n' % (dolar['compra'], dolar['venta']))


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


def get_value_bancomer(html):
    dolar={}
    sopa=BeautifulSoup(html, 'html.parser')
    minisopa = sopa.find('tbody').findAll('td', { 'class' : ['letra']})
    dolar ['compra'] = float(minisopa[3].text)
    dolar ['venta'] = float(minisopa[5].text)
    return dolar


def get_value_banjercito(html):
    dolar = {}
    sopa = BeautifulSoup(html,'html.parser')
    minisopas = sopa.find(id='cuerpo_principal').find(id='cuerpo').find( 'div',{'class':'cuadro'}).find(id='nota_interna').findAll('div')
    minisopas = minisopas[1].findAll('table')[1].findAll('tr')[2].findAll('td')
    dolar['compra'] = float(minisopas[2].text)
    dolar['venta'] = float(minisopas[3].text)
    return dolar


def main():
    promCompra = 0
    promVenta = 0
    acu = {'compra':[],'venta':[]}
    promedio = {}
    #banamex
    banco = 'Banamex'
    url = 'http://portal.banamex.com.mx/c719_004/economiaFinanzas/es/home?xhost=http://www.banamex.com/'
    html = get_html(url)
    dolar = get_value_banamex(html)
    write_file(banco, dolar)
    console_print(banco, dolar)
    acumula_valores(acu, dolar)
    #banbajio
    banco = 'BanBajio'
    url = 'http://www.bb.com.mx/'
    html = get_html(url)
    dolar = get_value_banbajio(html)
    write_file(banco, dolar)
    console_print(banco, dolar)
    acumula_valores(acu, dolar)
    #bancomer
    banco = 'Bancomer'
    url = 'https://bbv.infosel.com/bancomerindicators/indexV5.aspx'
    html = get_html(url)
    dolar = get_value_bancomer(html)
    write_file(banco, dolar)
    console_print(banco, dolar)
    acumula_valores(acu, dolar)
    #banjercito
    banco = 'Banjercito'
    url = 'http://banjercito.com.mx/informacionFinancieraCNT?operacion=6'
    html = get_html(url)
    dolar = get_value_banjercito(html)
    write_file(banco, dolar)
    console_print(banco, dolar)
    acumula_valores(acu, dolar)
    #promedio
    for valor in acu['compra']:
        promCompra += valor
    promedio['compra'] = promCompra / len(acu['compra'])
    for valor in acu['venta']:
        promVenta += valor
    promedio['venta'] = promVenta / len(acu['venta'])
    print 'promedio : %.4f | %.4f' % (promedio['compra'], promedio['venta'])


if __name__ == '__main__':
    main()