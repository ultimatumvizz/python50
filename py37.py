	#Matrix Addition
#!/usr/bin/python
l=[]
print("Enter dimensions axb")
a=input()
b=input()
print("Enter 1st matrix")
for i in range(0,a):
	m=[]
	for j in range(0,b):
		m.append(input())
	l.append(m)
print("Enter 2nd matrix")
g=[]
res=[]
for i in range(0,a):
	h=[]
	ap=[]
	for j in range(0,b): 
		ap.append(0)
		h.append(input())
	res.append(ap)
	g.append(h)
for i in range(0,a):
	for j in range(0,b):
		res[i][j]=l[i][j]+g[i][j]
for r in res:
	print r
