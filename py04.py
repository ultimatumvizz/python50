'''Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between x and y (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.'''
print "Enter the number ranges:"
p=input()
q=input()
liz=[]
for i in range(p,q):
	if i%7==0 and i%5!=0:
		liz.append(i)
r=len(liz)
for i in range(0,r):
	print liz[i],
	if i!=r-1:
		print ",",
		
