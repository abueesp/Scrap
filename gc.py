
#import socks5 to httprequests reckesocks
import requests
#import the basis
import urllib3 
from requests.adapters import HTTPAdapter
from bs4 import BeautifulSoup
import re
import ssl
import time
requests.adapters.DEFAULT_RETRIES = 1
x = 1 #0

for x in range (1, 12): #range of ids
	x=x+1
	url = "http://github.com/search?p=" + str(x) + '&q=location%3Asevilla&ref=searchresults&type=Users&utf8=%E2%9C&93'		
 	r = requests.get(url, verify=False)	#verificar aunque el cert no es valido
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
		filtstrscrap = str(scrap)
 		f = open("Output.csv", "a")		 #append to csv to read with excel later
		f.write(filtstrscrap)
		f.close()
		print filtstrscrap
	if x % 2 == 0 or x % 3 == 0:
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
