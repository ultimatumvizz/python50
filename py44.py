#Program to perform BFS and Print a spanning tree for a source
#!/usr/bin/python
class Queue:
        def __init__(self):
                self.items=[]
        def isEmpty(self):
                return self.items==[]
        def enqueue(self,item):
                self.items.insert(0,item)
        def dequeue(self):
                return self.items.pop()
        def size(self):
                return len(self.items)

def neighbors(G,l,src,count,col):
	count=0
	i=0
	l=[]
	j=0
	for i in range(1,col+1):
		if G[src][i]==1:
			l.insert(j+1,i)
			j+=1
			count+=1
S=[]
def BFS(src,Stree):
	visited=[]
	for i in range(1,100):
		visited.insert(1,0)
	count=0
	l=[]
	Stree[src]=-1
	q=Queue()
	q.enqueue(src)
	while q.isEmpty==False:
		p=q.dequeue()
		neighbors(S,l,p,count,col)
		for i in range(1,count+1):
			if l[i]!=src:
				if visited[l[i]]==0:
					q.enqueue(l[i])
					Stree[l[i]]=p
					visited[l[i]]=1
#Main	
G=[]
rows=input()
cols=input()
src=input()
for i in range(1,rows+1):
	P=[]
	for j in range(1,cols+1):
		P.insert(j,input())
	G.append(P)
for r in G:
	print r
Stree=[]
BFS(src,Stree)
print Stree
		
