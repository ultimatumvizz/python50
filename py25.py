kl=input("enter total numbers of test cases ")
def cube(y):
	for i in range(2,y/3):
		if i**3==y:
			print i
			return i
while kl:
	import itertools
	n=raw_input("enter the number: ")
	nn=[]
	for i in n:
		nn.append(i)
	k=itertools.permutations(nn)
	#print list(k)
	l=list(k)
#	print len(l)
	new=[]
#	print "the total permutations are: "
	for i in l:
		zo=""
		for j in i:
			zo=zo+j
		new.append(zo)
###		print zo,
#	print "\nthe numbers that are even are:"
	#print new
	o=0
	for i in new:
		i=int(i)
		i=int(i)
		cube(i)

"""	if o==0:
		print "no even number found"
	kl=kl-1"""
#	print "\n"
