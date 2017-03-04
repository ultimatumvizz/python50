#Calculating the value ncr and npr
#!/usr/bin/python
def C(n,r):
	if r>=n:
		r=n-r
	ans=1
	i=1
	for i in range(1,r+1):
		ans*=n-r+i
		ans/=i
	return ans

print C(input(),input())

