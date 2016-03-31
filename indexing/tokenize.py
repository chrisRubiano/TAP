'''
09/03/2016

autor: Cristian Samaniego
'''
from bs4 import BeautifulSoup
import unicodedata
import pickle
from dircache import listdir

def remove_puntuaction(text):
    
    punctutation_cats = set(['pc', 'Pd', 'Ps', 'Pe', 'P1', 'Pf', 'Po'])
    return ''.join( x for x in text
                    if unicodedata.category(x) not in punctutation_cats)

def lee_archivo(nombre_archivo):
    try:
        with open(nombre_archivo) as ft:
            html = ft.read()
        print ("se leyo el archivo %s" %nombre_archivo)
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
        print "no es archivo"
        texto = ""
    return texto

def get_words (texto):
    word_list = texto.split()
    clean_word_list = []
    for word in word_list:
        clean_word_list.append( remove_puntuaction( word ))
    return clean_word_list

def update_dictionary( diccionario, lista_palabras):
    for l in lista_palabras:
        if l not in diccionario:
            diccionario[l] = 1
        else:
            diccionario[l] +=1
        
def make_index(diccionario, lista_palabras, documento):
    for posicion,l in enumerate(lista_palabras):
        if l not in diccionario:
            diccionario[l] = [documento,[posicion]]
        else:
            temp = diccionario[l]
            temp[1].append(posicion)
            diccionario[l] = temp  
            
def guarda_indice(archivo, indice):
    try:
        with open(archivo, "wb") as fh:
            pickle.dump(indice, fh)
            print "Se guardo indice"
    except:
        print "Error al guardar el diccionario %s" % archivo  


if __name__ == '__main__':
    archivos_html = []
    archivos = listdir('.')
    for archivo in archivos:
        if archivo.endswith('.html'):
            archivos_html.append(archivo)
    print archivos_html
    
    master_index = {}
    doc_index = {}
    
    for doc,archivo in enumerate(archivos_html):
        HTML = lee_archivo(archivo)        
        sopa = BeautifulSoup(HTML,'html.parser')
        texto = get_texto(sopa)        
        words = get_words (texto)
        word_index = {}
        make_index(word_index, words, doc)
        doc_index[doc] = archivo
        try:
            for key,value in word_index.items():
                if key not in master_index:
                    master_index[key] = [value]
                else:
                    valor = master_index[key]
                    valor.append([value])
                    master_index[key] = valor
        except:
            print key
                
    print master_index
    guarda_indice("indice.pickle", master_index)
    print doc_index
    guarda_indice("indice_doc.pickle", doc_index)