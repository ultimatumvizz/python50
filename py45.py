	#Program to find a,b,c,d for the equation a^3 = b^3 + c^3 + d^3
#!/usr/bin/python
def binary(a,st,end,cube):
	mid=(st+end)/2
	if(a[mid]==cube):
		return mid
	if(st>=end):
		return -1
	if(a[mid]>cube):
		return binary(a,st,mid-1,cube)
	if(a[mid]<cube):
		return binary(a,mid+1,end,cube)

l=[]
i=0
while(i<=1000):
	l.append(i**3)
	i+=1
i=0
while(i<=1000):
	j=0
	while(j<=i):
		k=0
		while(k<=i):
			w=l[i]-l[j]-l[k]
			d=binary(l,0,1000,w)
			if(d!=-1):
				print "a=",i ,"b=", j ,"c=", k ,"d=", d
			k+=1
		j+=1
	i+=1

