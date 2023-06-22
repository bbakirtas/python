import os
from pydub import AudioSegment

path = "dosyalar/"
for root, dirs, files in os.walk("dosyalar"):
    for file in files:
        if file.endswith(".wav"):
            cikis = "outputs/"
            yenidosya = file[0:6]
            uzanti = ".mp3"
            dosya=path+file
            AudioSegment.from_wav(root+"/"+file).export(root+"/"+yenidosya+uzanti, format="mp3",bitrate="16k")
            #print(yenidosya)
            print(root+"/"+yenidosya+uzanti)
            #print(os.path.join(root, file))
            
#dosyalar klasöründeki wav uzantılı dosyaları bulup mp3 formatına çevirir.
