# Dudeney number : is a positive integer that is  a perfect cube such that the sum of its decimal digits is equal to the cube root of the number "
start=input()
end=input()
cubes=[]
Dude=dict()
i=1
while i < end :
	p=str(i**3)
	if sum([int(a) for a in p])==i:
		Dude[i]=i**3
	i=i+1
print Dude		
