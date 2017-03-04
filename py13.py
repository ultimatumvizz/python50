''' numbers which are both prime and palindrome between an interval'''
import math
def isPalindrome(strin):
	string=str(strin)	
	i=0
	while(i < len(string)-1):
		if string[i]!=string[len(string)-i-1]:			
			return False
		i=i+1
	return True
def isPrime(string):
	if string==1:
		return False
	else:
		for i in range(2,int(math.sqrt(string))+1):
			if string%i==0:
				return False
		return True
num1=input()
num2=input()
l=[]
for i in range(num1,num2):
	if (isPalindrome(i)==True and isPrime(i)==True):
		l.append(i)
print l		 		
