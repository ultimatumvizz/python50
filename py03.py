# calculating the prime factors of a number
# first i am calcuating all the prime factors of a number
import math
def valred(x)
	
	
def primechk(val)
	p=math.floor(math.sqrt(val))
	for i in range(2,p+1):
		if val%i==0:
			return 0
	return 1						
def primelist(x)
	liz=[]	
	for i in range(1,x):
		if primechk(i)==1:
			liz.append(i)
	return liz
def lizextend(liz,x)
	y=0
	for i in liz:
		y=x/i
		if primechk(y)==1:
			
								
x=input()
y=math.floor(math.sqrt(x))
	
print z		
