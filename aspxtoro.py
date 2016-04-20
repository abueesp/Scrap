# -*- coding: utf-8 -*-

#pip install requests urllib2
#pip install beautifulsoup
#easy_install requests-toolbelt
#pip install contextlib #for aleatority model close session
#pip install time for aleatority model wait
#install requesocks from git --> copiar en usr/lib/python2.7/distpackages/ y ejecutar python setup.py install #tor socks5 to http
#sudo apt-get install python-socksipy #other option to socks5 not working properly yet

#install last version of openssl
#sudo dpkg --remove --force-depends openssl
#./config --prefix=/usr         \
#         --openssldir=/etc/ssl \
#         --libdir=lib          \
#         shared                \
#         zlib-dynamic
#sudo make MANDIR=/usr/share/man MANSUFFIX=ssl install
#sudo install -dv -m755 /usr/share/doc/openssl-1.0.2d #check the version
#sudo cp -vfr doc/*     /usr/share/doc/openssl-1.0.2d

#sudo apt-get install tor deb.torproject.org-keyring
#tor
#export http_proxy='http://localhost:9010'  #the port is on 9010 instead of 9050
#export https_proxy='http://localhost:9010'
#python aspxtoro.py run

#import aleatority
#from contextlib import contextmanager # to close session
#import time # to idle sessions each x ids

#import socks5 to httprequests reckesocks
import requesocks as requests
#import the basis
import urllib2
from requests_toolbelt import SSLAdapter
from bs4 import BeautifulSoup
import re
import ssl
import time

y = (V66722216, A-08663619, A91853838)

for x in y: #range of ids
#let's start the script. for function to select link id with ssl, copy it to Output.csv and print it
	s = requests.session() #ssl session
	s.proxies = {'http': 'socks5://127.0.0.1:9010', #the port is on 9010 instead of 9050
                   'https': 'socks5://127.0.0.1:9010'}
#feching url and get request
	url = "http://www.cnmv.es/Portal/Consultas/Folletos/FolletosEmisionOPV.aspx?nif=" + str(x)	
	r = s.get(url, verify=False)
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
	if x % 90 == 0:
		time.sleep(1.5)
#aleatority to avoid machine recognition
#		if x % 30 == 0: #si id múltiplo de 30 entonces hacer un idle time de 1.5s
#			time.sleep(1.5)
#		contextlib.closing(s) #this at the end to close session but then add also the next two
#		s = requests.session() s.proxies = {'http': 'socks5://127.0.0.1:9010',
#		                 'https': 'socks5://127.0.0.1:9010'}
