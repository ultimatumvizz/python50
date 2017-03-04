n=int(raw_input("enter your first number: "))
m=int(raw_input("enter your second number: "))
if n>m:
	min=m
	max=n
else:
	min=n
	max=m

for i in range(min,-1,-1):
	if n%i==0 and m%i==0:
		print "hcf is %d" %(i) 
		break
lcm=n*m/i
print "lcm is %d" %(lcm)
