n=input("enter the number:  ")
while n!=0:
#	for i in range(1,n+1)
	def recap(zo):
		kp= inum(zo)
#	print kp
		if inum(zo)>=5:
			kl=[]
			for i in zo:
				kl.append(i)
			five=5
			while five!=0:
				kl.remove('X')
				five=five-1
#		print kl
			zo=""
			for i in kl:
				zo=zo+i
			return zo
		elif inum(zo)==4:
			kl=[]
	                for i in zo:
        	                kl.append(i)
                	four=4
	                while four!=0:
        	                kl.remove('X')
                	        four=four-1
#                print kl
	                zo=""
        	        for i in kl:
                	        zo=zo+i
	        	return zo

	def inum(zo):
		k=0
		for i in zo:
			if i=='X':
				k=k+1
		return k
	k=[]
	I=1
	V=5
	X=10
	zo=""
	rt=n%10
	kira=""
	if rt==4:
		n=n-4	
		kira="IV"
	if rt==9:
		n=n-9
		kira="IX"
	while n!=0:
		if n>=10:
			zo=zo+"X"
			n=n-10
		elif n>=5:
			zo=zo+"V"
			n=n-5
		elif n>=1:
			zo=zo+"I"
			n=n-1
	if inum(zo)>=5:
        	zo=recap(zo)
	        zo="L"+zo
	elif inum(zo)==4:
        	zo=recap(zo)
        	zo="XL"+zo

	zo=zo+kira
	print zo
	n=0	
