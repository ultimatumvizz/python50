#checking whether a sentence is a pangram or not ----------------
string=raw_input()
alphabets="abcdefghijklmnopqrstuvwxyz"
d=dict()
for i in alphabets:
	d[i]=False
for i in string :
	if i in d.keys():
		d[i]=True
flag=True
for i in d:
	if d[i]==False:
		print "string is not a pangram"
		flag=False
		break
if flag==True:
	print "string is a pangram"	
