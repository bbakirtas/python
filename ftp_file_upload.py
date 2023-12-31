import os.path, os
from ftplib import FTP, error_perm
from datetime import datetime
host = 'ftp.siteadresi.com'
port = 21

ftp = FTP()
ftp.connect(host,port)
ftp.login('kullanici','şifre')
filenameCV = "/yüklenecekdosyalar/"

now = datetime.now()

klasorformati = now.strftime("%Y%m%d")

ftp.cwd('/public_html/ftpklasörü')
def placeFiles(ftp, path):
    for name in os.listdir(path):
        localpath = os.path.join(path, name)
        if os.path.isfile(localpath):
            print("STOR", name, localpath)
            ftp.storbinary('STOR ' + name, open(localpath,'rb'))
        elif os.path.isdir(localpath):
            print("MKD", name)

            try:
                ftp.mkd(name)

            # ignore "directory already exists"
            except error_perm as e:
                if not e.args[0].startswith('550'):
                    raise

            print("CWD", name)
            ftp.cwd(name)
            placeFiles(ftp, localpath)
            print("CWD", "..")
            ftp.cwd("..")

placeFiles(ftp, filenameCV)

ftp.quit()
