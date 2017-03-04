# giving full suggestion for searching a word 
f1=open("/usr/share/dict/words","r")
string=f1.read()
liz=[]
liz=string.split("\n")
suggest=raw_input()
miz=[]
for word in liz:		
	flag=0
	if len(word) > len(suggest):
		for i in range(0,len(suggest)):
			if suggest[i] != word[i]:
				flag=1
				break	
		if flag==0:
			miz.append(word)
for word in miz:
	print word 		
