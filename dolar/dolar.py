'''
Links:
Banamex:            http://portal.banamex.com.mx/c719_004/economiaFinanzas/es/home?xhost=http://www.banamex.com/
Bancomer:
Banjercito:         http://www.banjercito.com.mx/index.jsp?hd_ligaContenido=Informacion_financiera/redirectInfFin.jsp?operacion=6
Banco del bajio:    http://www.bb.com.mx/


'''
import urllib2
from bs4 import BeautifulSoup
import time


def get_html(url):
    try:
        respuesta=urllib2.urlopen(url)
        html=respuesta.read()
        respuesta.close()
        print ("Se obtuvo hmtl de %s"%url)
    except:
        html=""
        print ("no se obtuvo html de %s"%url)
    return html


def get_value_banamex(html):
    dolar = {}
    sopa=BeautifulSoup(html,'html.parser')
    minisopas = sopa.find(id='cotizaciones').find('div').find(id='monedas').find('tbody').findAll('tr') #len=2
    dolar['compra'] = float(minisopas[0].find('td').text)
    dolar['venta'] = float(minisopas[1].find('td').text)
    return dolar


def get_value_banbajio(html):
    dolar={}
    sopa=BeautifulSoup(html,'html.parser')
    minisopa = sopa.findAll('div', {'class' : ['mod_inFin_central_2_compra', 'mod_inFin_central_2_venta']})
    dolar['compra'] = float(minisopa[0].text)
    dolar['venta'] = float(minisopa[1].text)
    return dolar


def main():
    url_banamex = 'http://portal.banamex.com.mx/c719_004/economiaFinanzas/es/home?xhost=http://www.banamex.com/'
    html_banamex = get_html(url_banamex)
    dolar_banamex = get_value_banamex(html_banamex)
    print time.strftime("%d-%m-%Y")+' '+time.strftime("%H:%M:%S")+', %.4f, %.4f' % (dolar_banamex['compra'], dolar_banamex['venta'])
    url_banbajio = 'http://www.bb.com.mx/'
    html_banbajio = get_html(url_banbajio)
    dolar_banbajio = get_value_banbajio(html_banbajio)
    print time.strftime("%d-%m-%Y")+' '+time.strftime("%H:%M:%S")+', %.4f, %.4f' % (dolar_banbajio['compra'], dolar_banbajio['venta'])

if __name__ == '__main__':
    main()