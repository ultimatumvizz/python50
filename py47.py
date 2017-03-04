# meaning of the expression similes of chat language
f=open("vizz3.txt","r")
string=f.read()
liz=string.split("\n")
miz=dict()
for i in range(0,len(liz)):
	lis=[]
	lis=liz[i].split(" ")
	miz[lis[len(lis)-1]]="".join([ lis[a]+" " for a in range(len(lis)-1)]) 
lix=[]
for expr in miz.keys():
	lix.append(expr)	
print lix
print "pick your expression from above list"
strip=raw_input()
print miz[strip]
