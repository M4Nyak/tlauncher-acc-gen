import requests
import capsolver
import random
import string
from colorama import init
from termcolor import colored
import threading
init()
print(colored("TUM HESAPLARİN SİFRESİ: mADEBYOMOVSKY123A dir.","red"))
def rand_mail():
 mail = "".join(random.choices(kume,k=9))
 return mail
def kaydet(deger):
 r= open("tlauncheracc.txt","a")
 r.write(f"{deger}\n")
 r.close()
kume= string.digits + string.ascii_lowercase + string.ascii_uppercase
def adgen():
 viyav = "".join(random.choices(kume,k=16))
 kaydet(viyav)
 return viyav
def sesid_uret():
 m = "".join(random.choices(kume,k=26))
 return m
 
capsolver.api_key= str(input("capsolver apinizi giriniz: "))
def recby():
 cosum= capsolver.solve({
  "type": "ReCaptchaV2TaskProxyLess",
  "websiteURL": "https://tlauncher.org",
   "websiteKey": "6Lc8JfMUAAAAAOvPrJXWXQqBogvQCJNzKHe7NBe6",

 })
 return cosum
def gen():
 cookies = {
    'PHPSESSID': sesid_uret(),
    'cf_clearance': 'A1FGS242Bn0sY.01JFCyDc8BnJa0goXFmf251lC8LPnI-1712824730-1.0.1.1-X0rwK_DSaSbUOh6KpeNZq2xRnoxzymhbDeg3zBoNx3TYwjvXuSFScPRk8mHaLHrrQ6MJTa2j_sxPFlydY6QgdA',
}

 headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://tlauncher.org',
    'referer': 'https://tlauncher.org/en/reg/',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}

 data = {
    'login': adgen(),
    'email': f"{rand_mail()}@omovsky.com",
    'psw': 'mADEBYOMOVSKY123A',
    'psw1': 'mADEBYOMOVSKY123A',
    'g-recaptcha-response': recby()['gRecaptchaResponse'],
    'rule': 'on',
    'zv': '4',
}

 response = requests.post('https://tlauncher.org/en/reg/', cookies=cookies, headers=headers, data=data)
 print("yaratildi!")
while True:
 t = threading.Thread(target=gen())
 t.start()
