'''You are given two vectors v1=(x1,x2,...,xn) and v2=(y1,y2,...,yn). The scalar product of these vectors is a single number, calculated as x1y1+x2y2+...+xnyn.

Suppose you are allowed to permute the coordinates of each vector as you wish. Choose two permutations such that the scalar product of your two new vectors is the smallest possible, and output that minimum scalar product.'''
testcase=input()
pa=dict()
for j in range(1,testcase+1):
	p=input()
	liz1=""
	liz2=""
	liz1=raw_input()
	lizz1=liz1.split(" ")
	liz2=raw_input()
	lizz2=liz2.split(" ")
	miz1=[]
	miz2=[]
	for i in range(0,p):
		miz1.append(int(lizz1[i]))		
		miz2.append(int(lizz2[i]))
	miz1.sort()
	miz2.sort()	
	val=0
	for i in range(0,p):
		val+=miz1[i]*miz2[p-1-i]
	pa.update({j:val})	
for i in pa:
	print "Case #%d: %d"%(i,pa[i])	
	





		
