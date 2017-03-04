n=input("")
for i in range(2,n+1):
	temp=i
	l=[]
	osum=0
	while temp!=0:
		k=temp%10
		l.append(k)
		osum=osum+k**5
	if osum==i:
		print i	
