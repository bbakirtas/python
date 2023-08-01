#FTP den tüm klasör ve dosyaları indirmek için kullandığım kod.Tüm dosyaları indir klasörüne ekler.

import ftplib
import os
import sys
local_path = ["indir/"]
ftp = ftplib.FTP("ftp.siteadresi.com")
ftp.login('kullaniciadi','şifre')
## Function ###
def downloadfiles(directory):
    global local_path
    print("Download files from ",directory)
    if directory!='.':
        local_path.append(directory)
    if(len(local_path) != 0):
        joined_str = "/".join(local_path)
        if os.path.exists(joined_str) == False:
            print("Create a local directory ", joined_str)
            os.makedirs(joined_str)
    ftp.cwd(directory)
    for name, facts in ftp.mlsd():
        if(facts["type"] == 'dir'):
            downloadfiles(name)
        if(facts["type"] == 'file'):
            print("Download a file ", name)
            ftp.retrbinary("RETR "+name, open(joined_str+"/"+name, 'wb').write)
    if len(local_path) != 0:
        local_path.pop()
    if ftp.pwd() != '/':
        ftp.cwd("..")
## End Function ##
downloadfiles("")
ftp.close()
