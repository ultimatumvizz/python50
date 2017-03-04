# bubble sort-------------------iteration
def bubbleSort(liz):
	for i in range(0,len(liz)):
		for j in range(0,len(liz)-i-1):
			if liz[j] > liz[j+1]:
				liz[j],liz[j+1]=liz[j+1],liz[j]
	return liz
numbers=raw_input()
l=list()
l=[int(a) for a in numbers.split(" ")]
print bubbleSort(l)
