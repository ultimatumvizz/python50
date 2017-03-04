#question 1
'''If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 in range(x,y)'''
def som(liz):
	i=0
	for j in liz:
		i+=j
	return i
print "enter the starting of the range "
x=input()
print "now enter the ending of the range "
y=input()		
lz3=[]
lz5=[]
lz15=[]
for i in range(x,y):
	if i%3==0:
		lz3.append(i)
	if i%5==0:
		lz5.append(i)
	if i%15==0:
		lz15.append(i)	
summ=som(lz3)+som(lz5)-som(lz15)
print summ
