
#import socks5 to httprequests reckesocks
import requesocks as requests
#import the basis
import urllib3
from requests_toolbelt import SSLAdapter
from bs4 import BeautifulSoup
import re
import ssl
import time

x = 1 #0
for x in range (12061, 14797): #range of ids
#let's start the script. for function to select link id with ssl, copy it to Output.csv and print it
	s = requests.session() #ssl session
	s.proxies = {'http': 'socks5://127.0.0.1:9010', #the port is on 9010 instead of 9050
                   'https': 'socks5://127.0.0.1:9010'}
#feching url and get request
 
for x in range (1, 14796): #range of ids
	x=x+1
	url = "https://github.com/search?p=" + str(x) + '&q=location%3Asevilla&ref=searchresults&type=Users&utf8=%E2%9C&93'		
	s = requests.Session() #ssl session
#	s.mount(url, SSLAdapter(ssl.PROTOCOL_SSLv23)) # ojo al protocolo ssl
	r = requests.get(url, verify=True)	#verificar aunque el cert no es valido
	f = open("Output.csv", "a")		 #append to csv
	f.write('\n'+url+",") #new line url comma
	f.close()	
	print url #print soup.prettify() #see the html
#script to scrap the soup, filter it, copy it in Output.csv and print
	rcontent = r.content.decode('latin1').encode('utf-8')
	rcontent = str(rcontent)
	print rcontent
	adv = re.search('div class="user-list-info"', rcontent) 
	if adv != None:
		adv = str(adv.group(0))
		soup = BeautifulSoup(adv, "lxml")
	for scrap in soup.find_all('div class="user-list-info"'):
		time.sleep(1.5)
		strscrap = str(scrap)
 		a=re.sub("<span.*?>","",strscrap)
		stra = str(a)
		b=re.sub("\<td.*?>","",stra)
		strb = str(b)
 		c=re.sub("</td>",",",strb)
		strc = str(c)
 		d=re.sub("</span>","",strc)
		strd = str(d)
 		filtscrap=re.sub("<a id=\"ctl00_MainContent_WebGroupBox2_lnkWeb\"></a>","",strd)
		filtstrscrap= str(filtscrap.join([s for s in filtscrap.strip().splitlines(True) if s.strip("\n" or "\r,").strip()]))
		f = open("Output.csv", "a")		 #append to csv to read with excel later
		f.write(filtstrscrap)
		f.close()
		print filtstrscrap
	if x % 2 == 0:
		time.sleep(1.5)

	#	for line in strscrap:
	#		if "<td" in line and ">" in line:
	#		        s=line.rstrip().split(">")
	#		        for n,i in enumerate(s):
	#		            if "<" in i:
	#		            	ind=i.find("<")
	#		           	s[n]=i[:ind] +""
	#				return join()
		
#filtstrscrap = strscrap.replace("'<span'.*'>'"," ").replace("</span>"," ").replace("'<td'.*'>'"," ").replace("</td>"," ").replace("<span>"," ").replace("<td>"," ")
			
#In OpenOffice, in Find and Replace, mark Regular Expressions and finding <span.*">|</span>|<td.*">|</td> delete span and td tags

#		contextlib.closing(s) #this at the end to close session but then add also the next two