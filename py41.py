#Program to print the shortest path for a given spanning tree
#!/usr/bin/python
def FindSP(src,ver,P):
	if src==ver:
		print src,
	else:
		w=P[ver]
		FindSP(src,w,P)
		print ver,

P=[]
n=input()
print "Enter the source vertex"
src=input()
for i in range(1,n+1):
	P.insert(i,input())
#P[src]=-1
FindSP(src,3,P)

