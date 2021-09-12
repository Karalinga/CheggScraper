from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog  
from selenium import webdriver
import requests

fP= "questions.txt"
s =[]
contents = []
questions = []
hrefs = []
list_of_small_words = ["the","of","is","a","to","by","their"]
searchparams = []









#GUI





qW = Tk()
qW.title("Add Questions")
qW.geometry("1200x500")

filePath = Text(qW,height = 1,width = 50)
#filePath.insert(INSERT,fP)


scrollbar = Scrollbar(qW)

mylist = Listbox(qW, yscrollcommand = scrollbar.set,height = 1,width = 100 )

# qF = open("questions.txt","r")

# for i in qF:
#     mylist.insert(END,str(i))

# qF.close()

def addQuestion():
    file = filedialog.askopenfile(mode='r',title='Choose a file')
    fP = file.name
    filePath.delete(1.0,END)
    filePath.insert(END,fP)
    filePath.pack()
def uploadQuestions():
    upFile = open(fP)
    qFile = open("questions.txt","a")
    for i in upFile:
        mylist.insert(END,str(i))
        if(fP != "questions.txt"):
            qFile.write(i)
    qFile.write("\n")
    upFile.close()
    qFile.close()
def changeURL(q):
    q = q.lower().replace(".","")
    qWords = q.split();
    newQ = ""
    resultwords  = [q for q in qWords if q.lower() not in list_of_small_words]
    final = "-".join(resultwords)
    s.append(final)

def search():

    inFile = open("questions.txt","r")
    for line in inFile:
        hrefs.append(line)
        questions.append(line)
        searchparams.append(line.replace(" ","%20"))
    inFile.close()
    # for i in mylist:
    #     hrefs.append(line)
    #     questions.append(line)
    #     searchparams.append(line.replace(" ","%20"))
    for h in hrefs:
        changeURL(h)

    URL = 'https://www.chegg.com/search/'+searchparams[0]
    outFile = open('pageContents.txt','w')
    storeFile = open('qResult.txt','w')
    storeFile.write("Questions found: \n")
    dr = webdriver.Chrome()
    #dr.manage().window().setPosition(Point(-2000, 0))
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
                print("POTATO")


uploadQuestions()
uButton = Button(qW, text ="Upload Questions",command = lambda:uploadQuestions() )
aQButton = Button(qW, text ="Add Question File",command = lambda:addQuestion())
sButton = Button(qW, text ="Search Chegg",command = lambda:search())
mylist.pack( side = LEFT, fill = BOTH )
scrollbar.pack(side = LEFT,fill = Y )
filePath.pack()
aQButton.pack()
uButton.pack()
sButton.pack()
mainloop()