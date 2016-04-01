#!/usr/bin/python
'''
Autor: Cristian Samaniego


'''
import urllib2
from bs4 import BeautifulSoup


def get_url(html):
    lista_urls=[]
    sopa=BeautifulSoup(html,'html.parser')
    lista_links=sopa.find_all(role='article')
    #print (lista_links)
    for link in lista_links:
        a_list=link.find_all('a')
        #print (a_list)
        for a in a_list:
            url=a.get('href')
            lista_urls.append(url)
        
    return lista_urls


def lee_archivo(archivo):
    try:
        with open(archivo, "r") as fh:
            texto=fh.read()
    except:
        texo=" "
    return texto


def save_file(texto,nombre_archivo):
    try:
        with open(nombre_archivo, "w") as fh:
            fh.write(texto)
            print "se escribio %s" % nombre_archivo
    except:
        print "ruta invalida %s" % nombre_archivo
        

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


def main():
    archivo="wired.html"
    url="http://www.wired.com"
    HTML =get_html(url)
    save_file(HTML, archivo)
    url_list=get_url(HTML)
    archivo_contador="contador.txt"
    contador=int(lee_archivo("contador.txt"))
    for url in url_list:
        HTML=get_html(url)
        get_url(HTML)
        archivo="pagina_%03d"%contador
        print "se obtuvo html de %s" % url
        save_file(HTML,archivo)
        contador+=1
    contador_str=str(contador)
    save_file(contador_str, archivo_contador)


if __name__ == '__main__':  
    main()