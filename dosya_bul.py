#dosyalar klasörü altında klasör ayırımı yapmadan .wav uzantılı dosyaları bulur.
import os
for root, dirs, files in os.walk("dosyalar"):
    for file in files:
        if file.endswith(".wav"):
             print(os.path.join(root, file))
