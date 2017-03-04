""" set of all substrings of a string"""
string=raw_input()
l=[]
for i in range(1,len(string)+1):
	for j in range(0,len(string)-i+1):
		l.append(string[j:j+i])
print l	
