import re
f = open("questions.txt", "a")
q = input("Enter a question: ")
list_of_small_words = ["the","of","is","a","to","by","their"]
#re.sub(r"\bis\b", "was", "This is the best island!")
while(q != "quit"):
	#addToFile(q)
	f.write(q.lower()+"\n")
	q = input("Enter a question: ")
f.close()
# x = "The University Of Sydney Is Conducting A Survey To Determine The Annual Consumption Of Alcohol By Their Students. We Would"
# x = x.lower().strip(".")
# print(x)
# for i in list_of_small_words:
# 	x= x.replace(i,"")
# x=x.replace(" ","-")
# print(x)
