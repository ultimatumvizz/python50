'''Question:
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.'''
p=int(raw_input())
q={}
for i in range(1,p+1):
	q[i]=i*i
print q
