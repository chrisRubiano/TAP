from __future__ import print_function
import os
from ftplib import FTP


def place_file(ftp, filename):
    ftp.storbinary('STOR ' + filename,open(filename, 'rb'))


if __name__ == '__main__':
    url = 'ftp.k-bits.com'
    ftp = FTP(url)
    user = 'usuario1@k-bits.com'
    passw = 'happy1234'
    ftp.login(user, passw)
    remoto = []
    ftp.dir(remoto.append)
    for r in remoto:
        print(r)
    directorio_local = os.listdir('.')
    place_file(ftp, 'Banamex.csv')

