'''
5/4/16

Autor: Cristian Samaniego
'''
import unicodedata


def remove_puntuaction(text):
    punctutation_cats = set(['pc', 'Pd', 'Ps', 'Pe', 'P1', 'Pf', 'Po'])
    return ''.join( x for x in text
                    if unicodedata.category(x) not in punctutation_cats)

def save_file(texto,nombre_archivo):
    try:
        with open(nombre_archivo, "w") as fh:
            fh.write(texto)
            print "se escribio %s" % nombre_archivo
    except:
        print "ruta invalida %s" % nombre_archivo


def lee_archivo(nombre_archivo):
    try:
        with open(nombre_archivo) as ft:
            html = ft.read()
        #print ("se leyo el archivo %s" %nombre_archivo)
    except:
        html = ""
        print ("no se pudo leer el archivo %s" %nombre_archivo)
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
        texto = u''.join( clean_text_list)
    except:
        print "no contiene articulos"
        texto = ""
    return texto


def get_words (texto):
    word_list = texto.split()
    clean_word_list = []
    for word in word_list:
        clean_word_list.append( remove_puntuaction( word ))
    return clean_word_list