# largest substring palindrome
import time
def isPalindrome(string):
	i=0
	while(i < len(string)-i):
		if string[i]!=string[len(string)-1-i]:
			return False
		i=i+1
	return True					
string=raw_input()
start=time.time()
l=[]
for i in range(1,len(string)+1):
	for j in range(0,len(string)-i+1):
		l.append(string[j:j+i])	
for i in range(len(l)-1,-1,-1):
	if(isPalindrome(l[i])==True):
		print len(l[i])
		print l[i]
		break
print "%s seconds"% (str(time.time()-start))

