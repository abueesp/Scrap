# -*- coding: utf-8 -*-
#include tags ENDOFTHEFILE and BEGINOFTHEFILE
#replace en Geany es Ctrl+H. Permite Regular expressions y wildcards, como re
import re 

with open('Input.csv') as inf, open('Output.csv', 'w') as ouf: #archivo de entrada archivo de salida
	for line in inf:
		line = str(line)
		if line.startswith('https:') or line.startswith(',,Direcci'): #si la línea empieza por
			ouf.write(line)
inf.close()
ouf.close()

with open('Output.csv') as ouf, open('Reutput.csv', 'w') as reuf:
	for line in ouf:
		line = str(line)
		replace = re.sub('<code>','SIN DATOS, SIN DATOS, SIN DATOS, SIN DATOS, SIN DATOS, SIN DATOS, SIN DATOS, SIN DATOS, SIN DATOS, SIN DATOS, SIN DATOS, SIN DATOS, SIN DATOS, SIN DATOS, SIN DATOS, SIN DATOS, SIN DATOS, SIN DATOS, SIN DATOS, SIN DATOS, SIN DATOS, SIN DATOS, SIN DATOS, SIN DATOS, SIN DATOS, SIN DATOS, SIN DATOS, SIN DATOS, SIN DATOS',line) #línea de etiqueta para errores
		replace = str(replace)
		reuf.write(replace)
ouf.close()
reuf.close()


with open('Reutput.csv') as reuf, open('Put.csv', 'w') as putuf:
	text = str(reuf.read())
	d = re.findall('</a>".*?Direc',text,re.DOTALL|re.MULTILINE)
	if d is not None:
		for elements in d:
			elements = str(elements)
			if not 'https' in elements:
					s = re.compile('</a>".*?Direc',re.DOTALL)
					replace = re.sub(s,'</a>",Direc',text)
	h = re.findall('</a>".*?https',text,re.DOTALL|re.MULTILINE)
	if h is not None:
		for elements in h:
			if not 'Direc' in elements:
				s = re.compile('</a>".*?https',re.DOTALL)
				replace = re.sub(s,'</a>"\nhttps',text)
		replace = str(replace)
		putuf.write(replace)


with open('Put.csv') as putuf, open('Final.csv', 'w') as final:
	for line in putuf:
		if re.search('Dirección', line): #if there is an address then there is a postal code
			match = re.search('Dirección.*?Código Postal',line) #puedes buscar 'two cats and dogs? usando re.match (y te dira  <_sre.SRE_Match object at 0xb743e720< or none) habiendo agrupado todos los elementos, puedes buscar con re.search () 'gato' y te dirá dónde está el primer elemento or None, o puedes usar re.finddall pero va con MULTILINE arrojando un objeto que agrupa todos los searched
			items = match.group(0) #selecciona el primer objeto de la lista de búsqueda
			items = str(items)
			a = re.sub(",","",items) #get out the commmas
			b = re.sub('Dirección:',"Dirección:,",a) #write the appropiate commas
			c = re.sub('Código Postal',",Código Postal",b)
			liner = re.sub('Dirección.*?Código Postal',c,line)
			liner = re.sub("[[]]","",liner)
			liner = re.sub('"',"",liner)#eliminar las comillas, que impiden que en el excel se tengan en cuenta las comas
#Assuming you're using Python 2.x, remember: there are two types of strings: str and unicode. str are byte strings, whereas unicode are unicode strings. unicode strings can be used to represent text in any language, but to store text in a computer or to send it via email, you need to represent that text using bytes. To represent text using bytes, you need an coding format. There are many coding formats, Python uses ascii by default, but ascii can only represent a few characters, mostly english letters. If you try to encode a text with other letters using ascii, you will get the famous "outside ordinal 128". 
			liner = liner.decode('utf-8').encode('utf-8') ### coding850 ? codingutf-8 ó but ascii /xb3/xc3 0xc2 codinglatin1 ~Aa
			liner = str(liner)
			final.write(liner)
		if not re.search('Dirección', line):
			line = str(line)
			final.write(line)
putuf.close()
final.close()


#INTERCALATED STRINGS I want to delete all comment. This is my regular expression : re.sub(re.compile('<!--.*-->', re.DOTALL),'', text)
#But if my text is : bzzzzzz <!-- blabla --> blibli <!-- bloblo --> blublu
# the result is : bzzzzzz blublu
# instead of : bzzzzzz blibli blublu
#the solution it is that * is greedy while *? is not; so re.sub('(?s)<!--.*?-->', '', text)


#NEWLINESnewline = re.sub(r"(?<!\n)\n[ \t]*(?!\n)", "", line)
#Explanation:
#(?<!\n) # Assert that the previous character isn't a newline
#\n      # Match a newline
#[ \t]*  # Match any number of spaces/tabs
#(?!\n)  # Assert that the next character isn't a newline

# if all you want to do is to delete all the commas and newlines, it might be clearer to write 
#replace = ''.join((c for c in text if c not in ',\n'))

#Python calls this concept "slicing" and it works on more than just strings. 
#>>> x = "Hello World!"
#>>> x[2:] 'llo World!'
#>>> x[:2] 'He'
# >>> x[:-2] 'Hello Worl'
# >>> x[-2:] 'd!'
# >>> x[2:-2] 'llo Worl'
#"H-e-l-l-o- -W-o-r-l-d"[::2] # outputs "Hello World"

#+ For example a+ matches ab and aaab. But unlike a* and a?, the pattern a+ does not match at the beginning of strings that lack an "a" character.
#http://ahkscript.org/docs/misc/RegEx-QuickRef.htm
