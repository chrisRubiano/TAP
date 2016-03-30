#!/usr/bin/python
'''
Created on 21/02/2016

@author: fcirett

TODO: crear indice global
'''
import argparse
from bs4 import BeautifulSoup
import unicodedata
import os


def get_html_files():


def save_index(fileName, index):
    try:
        with open(fileName, "wb") as fh:
            pickle.dump(index, fh)
    except:
        print("error al guardar diccionario %s" % archivo)


def remove_punctuation(text):
    """
    >>> remove_punctuation(u'something')
    u'something'

    >>> remove_punctuation(u'something.,:else really')
    u'somethingelse really'
    """
    punctutation_cats = set(['Pc', 'Pd', 'Ps', 'Pe', 'Pi', 'Pf', 'Po'])
    return ''.join(x for x in text
                   if unicodedata.category(x) not in punctutation_cats)


def lee_archivo_html(nombre_archivo):
    try:
        #carga los datos
        with open(nombre_archivo) as fh:
            html = fh.read()
        print ("se leyo el archivo %s" % nombre_archivo)
    except:
        html = ""
        print ("NO se pudo leer el archivo %s" % nombre_archivo)
    return html


def get_texto (soup):
    html_body = soup.find_all(itemprop='articleBody')
    try:
        paragraphs = html_body[0].find_all('p')
        raw_text_list = []
        raw_text_list = raw_text_list + [p.get_text() for p in paragraphs]
        clean_text_list = []
        for t in raw_text_list:
            clean_text_list.append( t )
        texto  = u''.join( clean_text_list)
    except Exception, e:
        print " "
    return texto


def get_words (texto):
    word_list = texto.split()
    clean_word_list = []
    for word in word_list:
        clean_word_list.append( remove_punctuation( word ) )
    return clean_word_list


def update_dictionary( diccionario, lista_palabras):
    for l in lista_palabras:
        if l not in diccionario:
            diccionario[l] = 1
        else:
            diccionario[l] += 1


def make_index( diccionario,lista_palabras, id):
    for posicion, palabra in enumerate(lista_palabras):
        if palabra not in diccionario:
            diccionario[palabra] = [ id, [posicion]]
        else:
            lista_temp = diccionario[palabra]
            lista_temp[1].append(posicion)
            diccionario[palabra] = lista_temp


def main( archivo_html):
    HTML  = lee_archivo_html(archivo_html)
    sopa  = BeautifulSoup( HTML )
    texto = get_texto(sopa)
    #html_text = soup.get_text()

    print texto

    words = get_words (texto)
    word_dict = {}
    update_dictionary(word_dict, words)
    print "diccionario: %d" % len(word_dict)

    #print(word_dict)
    for k, v in sorted(word_dict.items()):
        print '%s: %d' % (k,v)
        #print u'{0}: {1}'.format(k, v)
    word_index = {}
    make_index( word_index, words, 1)

    print (word_index['they'])
    lista_they = word_index['they']
    indice = lista_they[1][0]
    print words[indice]
    print (word_index['Yesterday'])

    archivos_html = get_html_files():
    for doc,archivo in enumerate(archivos_html):
        HTML = lee_archivo_html(archivo)
        sopa = BeautifulSoup(HTML, 'html.parser')
        texto = get_texto(sopa)
        words = get_words(texto)
        word_index = {}
        make_index(word_index, words, doc)
        print word_index


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--archivo", help="archivo HTML a leer")
    args = parser.parse_args()
    main( args.archivo )
