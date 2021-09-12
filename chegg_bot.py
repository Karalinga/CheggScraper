from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
#dr = webdriver.Chrome(options=options)
import requests
s =[]
contents = []
questions = []
def changeURL(q):
	q = q.lower().replace(".","")
	qWords = q.split();
	newQ = ""
	resultwords  = [q for q in qWords if q.lower() not in list_of_small_words]
	final = "-".join(resultwords)
	s.append(final)
inFile = open("questions.txt","r")
hrefs = []
list_of_small_words = ["the","of","is","a","to","by","their"]
searchparams = []
for line in inFile:
	hrefs.append(line)
	questions.append(line)
	searchparams.append(line.replace(" ","%20"))
for h in hrefs:
	changeURL(h)
URL = 'https://www.chegg.com/search/'+searchparams[0]
outFile = open('pageContents.txt','w')
storeFile = open('qResult.txt','w')
storeFile.write("Questions found: \n")
dr = webdriver.Chrome()
dr.get(URL)
outFile.write(str(dr.page_source.encode("utf-8")))
outFile.close()
dr.quit()
oFile = open('pageContents.txt','r')
for j in oFile:
	contents.append(j)
for i in questions:
	for k in contents:
		if s[0] in j:
			print(s[0])
			storeFile.write(str(i))