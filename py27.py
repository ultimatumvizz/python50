#all possible english words that can be formed from a string
import enchant
from itertools import permutations
def setSubstrings(string):
	l=[]
	for i in range(1,len(string)+1):
		for j in range(0,len(string)-i+1):
			l.append(string[j:j+i])
	return l
string=raw_input()
engDic=enchant.Dict("en")
result=[]
substr=[]
substr=setSubstrings(string)
for word in substr:
	for pWord in [''.join(p) for p in permutations(word)]:
		if pWord not in result and engDic.check(pWord): 
			result.append(pWord)
print result
