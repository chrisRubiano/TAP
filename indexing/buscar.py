import sys
import argparse
import pickle


def read_index(pickleFile):
    pickleFile = open(pickleFile, 'rb')
    index = pickle.load(pickleFile)
    return index


def main(args):
    wordIndex = read_index('indice.pickle')
    docIndex = read_index('indice_doc.pickle')
    wordList = args.palabras
    for word in wordList:
        print wordIndex[word]
    #    print docIndex


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Busca palabras')
    parser.add_argument('palabras', metavar='N', type=str, nargs='+', help='Palabras a buscar en el indice')
    args = parser.parse_args()
    main(args)
