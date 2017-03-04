# selection sort----------------
def selectionSort(liz):
	lin=list()	
	for i in range(0,len(liz)):
		lin.append(min(liz))
		liz.remove(min(liz))
	return lin
numbers=raw_input()
liz=[]
liz=[int(a) for a in numbers.split(" ")]
print selectionSort(liz)	
	
