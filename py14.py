# Binary search -----------
def binarySearch(liz,e):
	if len(liz)==0:
		return False
	elif e==liz[len(liz)//2]:
		return True	
	elif e > liz[len(liz)//2]:
		return binarySearch(liz[len(liz)//2:],e)	
	elif e < liz[len(liz)//2]:
		return binarySearch(liz[:len(liz)//2],e) 
key=input()
string=raw_input()
liz=string.split(" ")
for i in range(len(liz)):
	liz[i]=int(liz[i])				 	
if binarySearch(liz,key)==True:
	print "element found"
else:
	print "element not found"		
