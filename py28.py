# armstrong numbers between a particular interval
start=input()
end=input()
liz=[]
for i in range(start,end):
	val=0	
	for j in str(i):
		val+=(int(j))**3
	if val==i:
		liz.append(i)
print liz

	
