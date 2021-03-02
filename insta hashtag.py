import requests
import secrets
import sys as n
import time as mm
from time import sleep
jruksr= '\033[1;32m'
jruks = '\033[1;33m'
ruks_q = '\033[1;36m'
ruks_h = '\033[1;31m'
print(ruks_q+'='*60)
ruks_f=f"""
{jruksr}
  _____           _                    
 |_   _|         | |                   
   | |  _ __  ___| |_ __ _             
   | | | '_ \/ __| __/ _` |            
  _| |_| | | \__ \ || (_| |            
 |_____|_| |_|___/\__\__,_|      {jruks}      
  _               _     _              
 | |             | |   | |             
 | |__   __ _ ___| |__ | |_ __ _  __ _ 
 | '_ \ / _` / __| '_ \| __/ _` |/ _` |
 | | | | (_| \__ \ | | | || (_| | (_| |
 |_| |_|\__,_|___/_| |_|\__\__,_|\__, |
                                  __/ |
                                 |___/ 
"""
print(ruks_f)
print(ruks_q+'='*60)
head = {
'HOST': "www.instagram.com",
'KeepAlive' : 'True',
'user-agent' : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36",
'Cookie': 'cookie',
'Accept' : "*/*",
'ContentType' : "application/x-www-form-urlencoded",
"X-Requested-With" : "XMLHttpRequest",
"X-IG-App-ID": "936619743392459",
"X-Instagram-AJAX" : "missing",
"X-CSRFToken" : "missing",
"Accept-Language" : "en-US,en;q=0.9"
}

ruks = requests.Session()
rhaby = 'welcome to hashtag user'

#===============================#
m1 = input('Hashtag_1 : '+ruks_h)
m2 = input('Hashtag_2 : '+ruks_q)
m3 = input('Hashtag_3 :'+ruks_h)
m4 = input('Hashtag_4 : '+ruks_q)
m5 = input('Hashtag_5 : '+ruks_h)
m6 = input('Hashtag_6 : '+ruks_q)
fileuser = open('User.txt', 'a')
#===============================#
print('The rhaby developer tool is free, not for sale')
print('='*60) 
def ruks1():
	try:
		url_id = f'https://www.instagram.com/web/search/topsearch/?context=blended&query=25.{m1}'
		mn = 0
		req_id = ruks.get(url_id,headers=head).json()		
		while True:
			mn+=1			
			y = str(req_id['users'][mn]['user']['username'])
			fileuser.write(y + '\n')
			
			print(f'{y}')
	except Exception as e:
           
            print('='*60)
     
ruks1()

#===============================#
def ruks2():
	try:
		url_id = f'https://www.instagram.com/web/search/topsearch/?context=blended&query=25.{m2}'
		mn = 0
		req_id = ruks.get(url_id,headers=head).json()		
		while True:
			mn+=1			
			y = str(req_id['users'][mn]['user']['username'])
			fileuser.write(y + '\n')
			print(f'{y}')
	except Exception as e:
            
            print('='*60)
     
ruks2()	
#===============================#
def ruks3():
	try:
		url_id = f'https://www.instagram.com/web/search/topsearch/?context=blended&query=25.{m3}'
		mn = 0
		req_id = ruks.get(url_id,headers=head).json()		
		while True:
			mn+=1			
			y = str(req_id['users'][mn]['user']['username'])
			fileuser.write(y + '\n')
			print(f'{y}')
	except Exception as e:
            
            print('='*60)
     
ruks3()
#===============================#
def ruks4():
	try:
		url_id = f'https://www.instagram.com/web/search/topsearch/?context=blended&query=25.{m4}'
		ruks = 0
		req_id = ruks.get(url_id,headers=head).json()		
		while True:
			mn+=1			
			y = str(req_id['users'][mn]['user']['username'])
			fileuser.write(y + '\n')
			print(f'{y}')
	except Exception as e:
           
            print('='*60)
     
ruks4()
#===============================#
def ruks5():
	try:
		url_id = f'https://www.instagram.com/web/search/topsearch/?context=blended&query=25.{m5}'
		mn = 0
		req_id = ruks.get(url_id,headers=head).json()		
		while True:
			mn+=1			
			y = str(req_id['users'][mn]['user']['username'])
			fileuser.write(y + '\n')
			print(f'{y}')
	except Exception as e:
           
            print('='*60)
     
ruks5()			
#===============================#
def ruks6():
	try:
		url_id = f'https://www.instagram.com/web/search/topsearch/?context=blended&query=25.{m6}'
		mn = 0
		req_id = ruks.get(url_id,headers=head).json()		
		while True:
			mn+=1			
			y = str(req_id['users'][mn]['user']['username'])
			fileuser.write(y + '\n')
			print(f'{y}')
	except Exception as e:
	        print('='*60)
	        print(u'نتهى السحب')  
	        print(u' في لستة User.txt ')       
          
ruks6()			
#===============================#
