# ramanujam numbers-------------these are numbers of kind in which  a number can be represented as the pair of sum of 2 cubic numbers
from itertools import permutations
liz=[i for i in permutations(range(1,200),2)]
sumCubes=dict()
raman=dict()
for i in range(0,len(liz)):
	a=liz[i][0]**3
	b=liz[i][1]**3
	if a+b not in sumCubes.keys():
		sumCubes[a+b]=liz[i]
	if a+b in sumCubes.keys():
		if sumCubes[a+b][0] not in liz[i]:
			x=[]
			x=sumCubes[a+b]
			raman[a+b]=(liz[i],x)
print sorted(raman.keys())
	
			
		
	





