#!/usr/bin/python

import urllib2
import argparse


def get_html(url):
    try:
        respuesta = urllib2.urlopen(url)
        html = respuesta.read()
        respuesta.close()
        print "se obtuvo html de %s" % url
    except:
        html = ""
        print "no se obtuvo html de %s" %url
    return html


def main(url):
    get_html(url)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", help="la url del sitio del cual se desea obtener el html")
    args = parser.parse_args()
    main(args.url)