#merge sort ---- one of the comparison sort
# recursion 
def mergesort(liz):
	if len(liz) > 1:
		mid=len(liz)//2
		liz1=liz[:mid]
		liz2=liz[mid:]				
		mergesort(liz1)
		mergesort(liz2)
		i=0
		j=0
		k=0
		while i < len(liz1) and j < len(liz2):
			if liz1[i] >= liz2[j]:
				liz[k]=liz1[i]
				k=k+1
				i=i+1
			else:
				liz[k]=liz2[j]
				k=k+1
				j=j+1
		while i < len(liz1):
			liz[k]=liz1[i]
			k=k+1
			i=i+1
		while j < len(liz2):
			liz[k]=liz2[j]
			k=k+1
			j=j+1
k=raw_input()
ll=k.split(" ")
l=[]
for i in range(0,len(ll)):
	l.append(int(ll[i]))
mergesort(l)
print l						
