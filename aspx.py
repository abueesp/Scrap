
#pip install requests urllib2
#pip install beautifulsoup
#easy_install requests-toolbelt
#python aspx.py run

#the next script import the basis
import requests
import ssl
import urllib2
from requests_toolbelt import SSLAdapter
from bs4 import BeautifulSoup
import re
import time


#let's start the script. for function to select link id with ssl, copy it to Output.csv and print it

y = (V66722216, A-08663619, A91853838)

for x in y: #range of ids
	x=x+1
	url = "https://secretaria.icas.es:444/web/ColegiadoBusquedaColegiado.aspx?id=" + str(x)	
	s = requests.Session() #ssl session
	s.mount(url, SSLAdapter(ssl.PROTOCOL_TLSv1)) # ojo al protocolo ssl
	r = requests.get(url, verify=False)	#verificar aunque el cert no es valido
	f = open("Output.csv", "a")		 #append to csv
	f.write('\n'+url+",") #new line url comma
	f.close()	
	print url
#print soup.prettify()

	url = "http://www.cnmv.es/Portal/Consultas/Folletos/FolletosEmisionOPV.aspx?nif=" + str(x)	
	s = requests.Session() #ssl session
	s.mount(url, SSLAdapter(ssl.PROTOCOL_TLSv1)) # ojo al protocolo ssl
	r = requests.get(url, verify=False)	#verificar aunque el cert no es valido
	f = open(str(x+".csv"), "a")		 #append to csv
	f.write('\n'+url+",") #new line url comma
	f.close()	
	print url #print soup.prettify() #see the html
#script to scrap the soup, filter it, copy it in Output.csv and print
	soup = BeautifulSoup(r.content)	
	for titulo in soup.find_all("<span id="ctl00_ContentPrincipal_lblSubtitulo">"):
		strtitulo = str(titulo)
		f = open(str(x+".csv"), "a")		 #append to csv to read with excel later
		f.write(titulo)
		f.close()
		print titulo
	for scrap in soup.find_all("http://www.cnmv.es/Portal/verDoc.axd?t={*}"):
		strscrap = str(scrap)
 		a=re.sub("http://www.cnmv.es/Portal/verDoc.axd?t={*}","",strscrap)
		f = open(str(x+".csv"), "a")		 #append to csv to read with excel later
		f.write(strscrap)
		f.close()
		print strscrap
	if x % 120 == 0:
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
