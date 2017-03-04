''' factorial problem along with the trailing zeroes '''

def fact(n):
	if n==0:
		return 1
	return n*fact(n-1) 
def fact2(n):
	f=1
	for i in range(0,n+1):
		if i==0 or i==1:
			f=1
		else:
			f*=i
	return f
def zeroes(n):
	x=fact2(n)
	count=0
	while x%10==0:
		x=x/10
		count+=1		
	return count
print "enter the number"
p=input()
#print fact2(p)
print p , fact2(p),  zeroes(p)
