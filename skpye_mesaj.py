import sys
import requests
from skpy import Skype, SkypeChats
sk = Skype('kullaniciadi@hotmail.com', 'şifre') 

sk.user 
sk.contacts 
sk.chats 
sk.chats.recent() 
"""
mesaj = sys.argv[1]
for word in sys.argv[1:]:
    mesaj += word + ' '
"""



def msg(mesaj):
    ch = sk.chats["8:burakbakirtas"]
    ch.sendMsg(mesaj)
    
def toplu(mesaj):
    ch = sk.chats.chat('19%1234567890%40thread.skype')
    ch.sendMsg(mesaj)
 """
 Python skype ile giriş yapıp farklı kodlardan kullanmak için geliştirdiğim basit fonksiyonlu kod. msg("Merhaba Yeni Mesaj") olarak kişiye özel gönderilebilir. toplu("Gruba mesaj") toplu olan fonksiyon gruplara mesaj atmak için kullanıyorum.
 
 """
