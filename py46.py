# converting an english sentence into short cut language or sms language
f1=open("/usr/share/dict/words","r")
string=f1.read()
liz=string.split("\n")
modliz=dict()
vowels=['a','e','i','o','u']
for strip in liz:
	newstrip=""
	for i in range(0,len(strip)):
		if strip[i] not in vowels:
			newstrip+=strip[i]	
	modliz[strip]=newstrip
sentin=raw_input()
sentliz=sentin.split(" ")
sentout=""
for word in sentliz:
	if word in modliz.keys():
		strip=""
		strip=modliz[word]
		sentout+=strip+" "
	else :	
		sentout+=word+" "	
print sentout`
					 	
