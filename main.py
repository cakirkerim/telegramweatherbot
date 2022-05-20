import tkinter
import requests
from tkinter import *
from threading import Thread
from datetime import datetime
import json
                                                       #tam altımdaki şehir ismini değiştirerek
                                                        #farklı şehirlerin haca durumunu çekebilirsin
origin_url = "http://api.openweathermap.org/data/2.5/weather?q=Aydın,tr&APPID=5c285f80b9745caa576cab310f712d78"
ap = 'https://api.telegram.org/bot5149239886:AAEuDgFjAaLnzl42kL24vC2XQvW4FKhv_YI/sendMessage'

response = requests.get(origin_url)
jsonResponse = json.loads(response.text)

city = str(jsonResponse["name"])
sicaklik = str(jsonResponse["main"]["temp"] - 273)
hissedilen = str(jsonResponse["main"]["feels_like"] - 273)
basinc =    str(jsonResponse["main"]["pressure"]) + " Pascal"
nem = int(jsonResponse["main"]["humidity"] + 75)
yagmuralert = ("HER AN YAĞMUR YAĞABİLİR")
if nem >= 95:
    requests.post(url="https://api.telegram.org/bot5149239886:AAEuDgFjAaLnzl42kL24vC2XQvW4FKhv_YI/sendMessage",
                  data={"chat_id": "975665795", "text":yagmuralert}).json()

message = "Bölge: {}\nSıcaklık: {}\nHissedilen: {}\nBasınç: {}\nNem: {}%".format(city,sicaklik,hissedilen,basinc,nem)

requests.post(url="https://api.telegram.org/bot5149239886:AAEuDgFjAaLnzl42kL24vC2XQvW4FKhv_YI/sendMessage",data={"chat_id":"975665795","text":message}).json()


"""GÜNCELLEME SADECE PYTHON'DA ÇALIŞAN BOTU TELEGRAM APİ İLE BAĞLADIM ALTTAKİLER ESKİ KOD"""

#print("Sehir: " + (jsonResponse)["name"])
#print("Sicaklik: " + str(jsonResponse["main"]["temp"] - 273)) #float yapamadım
#print("Hissedilen: " + str(jsonResponse["main"]["feels_like"] - 273 ))
#print("Basinc: " + str(jsonResponse["main"]["pressure"]) + " Pa.")
#print("Nem: %"+ str(jsonResponse["main"]["humidity"]))

