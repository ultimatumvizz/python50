# permutation of a string ------------ using recursion
def permute(string,pos,end):
	if pos==end:
		print string	
	else:
		for j in range(pos,end+1):
			liz=list(string)
			temp=string[pos]
			liz[pos]=liz[j]
			liz[j]=temp
			permute("".join(liz),pos+1,end)
			temp=liz[pos]
			liz[pos]=liz[j]
			liz[j]=temp
			
string=raw_input()
permute(string,0,len(string)-1)	
