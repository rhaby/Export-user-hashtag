import requests
import os
import json
from bs4 import BeautifulSoup
from time import sleep
def rhaby(s):
    for ASU in s + '\n':
        sys.stdout.write(ASU)
        sys.stdout.flush()
        sleep(50. / 100)
rhaby = 'welcome to Export user hashtag : my name is arhaby the tools is free'
print (rhaby)


fileuser = open('accounts.txt', 'w')
def giveuser():
    try:
        
        print(' ☠' * 15)
        zero = 0
        while True:
            data = response.json()
            idname = str(data['users'][zero].get('user').get('username'))
            fileuser.write(idname + '\n')
            zero += 1
            print("[*] User : {}".format(idname))
    except Exception as e:
            fileuser.close()
def giveuserA():
    try:
        
        zero = 0
        while True:
            data = response.json()
            idname = str(data['users'][zero].get('user').get('username'))
            fileuser.write(idname + '\n')
            zero += 1
            print("[*] User : {}".format(idname))
    except Exception as e:
            print(' ☠' * 15)            
a1 = input("$ type hashtag : ")
a2 = input("$ type hashtag : ")
a3 = input("$ type hashtag : ")
a4 = input("$ type hashtag : ")
a5 = input("$ type hashtag : ")

payload = ''
url = "https://www.instagram.com/web/search/topsearch/?context=blended&query=" + a3 + "&count=25"
headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "max-age=0",
    "cookie": "ig_did=57C594DF-134B-4172-BCF1-C32A7A21989B; mid=X_sqxgALAAE7joUQdF9J2KQUb0bw; ig_nrcb=1; shbid=14062; shbts=1613662905.833805; rur=ATN; ds_user=dgwegcdsaf4q; ds_user_id=45569690013; csrftoken=KLIRZwUnZVj93cvhk24S4icZZjEghmIA; sessionid=45569690013%3AS0pqLhQRIQyTug%3A2",
    "sec-ch-ua": '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36",
    "x-ig-app-id": "936619743392459"
}
response = requests.Session().get(url, data=payload, headers=headers)

if "username" in response.text:
    giveuserA()
#@########################################################################################

payload = ''
url = "https://www.instagram.com/web/search/topsearch/?context=blended&query=" + a3 + "&count=25"
headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "max-age=0",
    "cookie": "ig_did=57C594DF-134B-4172-BCF1-C32A7A21989B; mid=X_sqxgALAAE7joUQdF9J2KQUb0bw; ig_nrcb=1; shbid=14062; shbts=1613662905.833805; rur=ATN; ds_user=dgwegcdsaf4q; ds_user_id=45569690013; csrftoken=KLIRZwUnZVj93cvhk24S4icZZjEghmIA; sessionid=45569690013%3AS0pqLhQRIQyTug%3A2",
    "sec-ch-ua": '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36",
    "x-ig-app-id": "936619743392459"
}
response = requests.Session().get(url, data=payload, headers=headers)

if "username" in response.text:
    giveuserA()
#@########################################################################################
payload = ''
url = "https://www.instagram.com/web/search/topsearch/?context=blended&query=" + a3 + "&count=25"
headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "max-age=0",
    "cookie": "ig_did=57C594DF-134B-4172-BCF1-C32A7A21989B; mid=X_sqxgALAAE7joUQdF9J2KQUb0bw; ig_nrcb=1; shbid=14062; shbts=1613662905.833805; rur=ATN; ds_user=dgwegcdsaf4q; ds_user_id=45569690013; csrftoken=KLIRZwUnZVj93cvhk24S4icZZjEghmIA; sessionid=45569690013%3AS0pqLhQRIQyTug%3A2",
    "sec-ch-ua": '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36",
    "x-ig-app-id": "936619743392459"
}
response = requests.Session().get(url, data=payload, headers=headers)

if "username" in response.text:
    giveuserA()
#@########################################################################################
    
payload = ''
url = "https://www.instagram.com/web/search/topsearch/?context=blended&query=" + a3 + "&count=25"
headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "max-age=0",
    "cookie": "ig_did=57C594DF-134B-4172-BCF1-C32A7A21989B; mid=X_sqxgALAAE7joUQdF9J2KQUb0bw; ig_nrcb=1; shbid=14062; shbts=1613662905.833805; rur=ATN; ds_user=dgwegcdsaf4q; ds_user_id=45569690013; csrftoken=KLIRZwUnZVj93cvhk24S4icZZjEghmIA; sessionid=45569690013%3AS0pqLhQRIQyTug%3A2",
    "sec-ch-ua": '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36",
    "x-ig-app-id": "936619743392459"
}
response = requests.Session().get(url, data=payload, headers=headers)

if "username" in response.text:
    giveuserA()
#@########################################################################################
    
payload = ''
url = "https://www.instagram.com/web/search/topsearch/?context=blended&query=" + a1 + "&count=25"
headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "max-age=0",
    "cookie": "ig_did=57C594DF-134B-4172-BCF1-C32A7A21989B; mid=X_sqxgALAAE7joUQdF9J2KQUb0bw; ig_nrcb=1; shbid=14062; shbts=1613662905.833805; rur=ATN; ds_user=dgwegcdsaf4q; ds_user_id=45569690013; csrftoken=KLIRZwUnZVj93cvhk24S4icZZjEghmIA; sessionid=45569690013%3AS0pqLhQRIQyTug%3A2",
    "sec-ch-ua": '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36",
    "x-ig-app-id": "936619743392459"
}
response = requests.Session().get(url, data=payload, headers=headers)

if "username" in response.text:
    giveuserA()
#@########################################################################################

payload = ''
url = "https://www.instagram.com/web/search/topsearch/?context=blended&query=" + a2 + "&count=25"
headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "max-age=0",
    "cookie": "ig_did=57C594DF-134B-4172-BCF1-C32A7A21989B; mid=X_sqxgALAAE7joUQdF9J2KQUb0bw; ig_nrcb=1; shbid=14062; shbts=1613662905.833805; rur=ATN; ds_user=dgwegcdsaf4q; ds_user_id=45569690013; csrftoken=KLIRZwUnZVj93cvhk24S4icZZjEghmIA; sessionid=45569690013%3AS0pqLhQRIQyTug%3A2",
    "sec-ch-ua": '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36",
    "x-ig-app-id": "936619743392459"
}
response = requests.Session().get(url, data=payload, headers=headers)

if "username" in response.text:
    giveuserA()
#@########################################################################################

payload = ''
url = "https://www.instagram.com/web/search/topsearch/?context=blended&query=" + a3 + "&count=25"
headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "max-age=0",
    "cookie": "ig_did=57C594DF-134B-4172-BCF1-C32A7A21989B; mid=X_sqxgALAAE7joUQdF9J2KQUb0bw; ig_nrcb=1; shbid=14062; shbts=1613662905.833805; rur=ATN; ds_user=dgwegcdsaf4q; ds_user_id=45569690013; csrftoken=KLIRZwUnZVj93cvhk24S4icZZjEghmIA; sessionid=45569690013%3AS0pqLhQRIQyTug%3A2",
    "sec-ch-ua": '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36",
    "x-ig-app-id": "936619743392459"
}
response = requests.Session().get(url, data=payload, headers=headers)

if "username" in response.text:
    giveuserA()
#@########################################################################################

payload = ''
url = "https://www.instagram.com/web/search/topsearch/?context=blended&query=" + a4 + "&count=25"
headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "max-age=0",
    "cookie": "ig_did=57C594DF-134B-4172-BCF1-C32A7A21989B; mid=X_sqxgALAAE7joUQdF9J2KQUb0bw; ig_nrcb=1; shbid=14062; shbts=1613662905.833805; rur=ATN; ds_user=dgwegcdsaf4q; ds_user_id=45569690013; csrftoken=KLIRZwUnZVj93cvhk24S4icZZjEghmIA; sessionid=45569690013%3AS0pqLhQRIQyTug%3A2",
    "sec-ch-ua": '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36",
    "x-ig-app-id": "936619743392459"
}
response = requests.Session().get(url, data=payload, headers=headers)

if "username" in response.text:
    giveuserA()
#@########################################################################################

payload = ''
url = "https://www.instagram.com/web/search/topsearch/?context=blended&query=" + a5 + "&count=25"
headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "max-age=0",
    "cookie": "ig_did=57C594DF-134B-4172-BCF1-C32A7A21989B; mid=X_sqxgALAAE7joUQdF9J2KQUb0bw; ig_nrcb=1; shbid=14062; shbts=1613662905.833805; rur=ATN; ds_user=dgwegcdsaf4q; ds_user_id=45569690013; csrftoken=KLIRZwUnZVj93cvhk24S4icZZjEghmIA; sessionid=45569690013%3AS0pqLhQRIQyTug%3A2",
    "sec-ch-ua": '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36",
    "x-ig-app-id": "936619743392459"
}
response = requests.Session().get(url, data=payload, headers=headers)

if "username" in response.text:
    giveuser()
#@########################################################################################

print("Done..""\n""telegram:ciku370")
