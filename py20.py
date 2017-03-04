# insertion sort----------------
def insertionSort(liz):
	for i in range(1,len(liz)):
		for j in range(i,0,-1):
			if liz[j-1] > liz[j]:
				liz[j-1],liz[j]=liz[j],liz[j-1]	
			else:
				break	
	return liz
numbers=raw_input()
liz=[]
liz=[int(a) for a in numbers.split(" ")]
print insertionSort(liz)
