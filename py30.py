# nth catalan number catalan numbers ------------------range[0,80000]
import math
catNum=dict()
catNum[0]=1
for i in range(1,80000):
	catNum[i]=(catNum[i-1]*2*(2*i+1))//(i+2)
n=input()
print catNum[n]
	
	
