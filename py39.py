#Evaluating a postfix expression

class stack:
	def __init__(self):
		self.items=[]
		self.t=-1
	def push(self,item):
		self.t+=1
		self.items.insert(self.t,item)
	def pop(self):
		self.t-=1
	def size(self):
		return self.t
	def isempty(self):
		return self.items==[]
	def top(self):
		return self.items[self.t] 
st=stack()
s=raw_input()
for i in range(0,len(s)):
	if s[i]>='1' and s[i]<='9':
		st.push(int(s[i]))
	else:	
		k=st.top()
		st.pop()
		j=st.top()
		st.pop()
		if s[i]=='*':
			c= j*k
			st.push(c)
		if s[i]=='+':
                        c= j+k
                        st.push(c)
		if s[i]=='-':
                        c= j-k
                        st.push(c)
		if s[i]=='/':
                        c= j/k
                        st.push(c)
print st.top()
