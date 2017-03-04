d=input("enter upto where you want all the curious numbers: ")

for c in range(3,d+1):
	l=[]
	temp=c
	def func(k):
		ch=1
		for i in range(2,k+1):
			ch=ch*i
		return ch
	osum=0
	while temp!=0:
		k=temp%10
		temp=temp/10
		l.append(k)
#	print func(k)
		osum=osum+func(k)
#print osum
#print c
	if osum==c:
		print c
