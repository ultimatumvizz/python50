io=input("")
while(io):
	n=int(raw_input("enter the year: "))
	if n%4==0:
		if n%400==0:
			print "its leap year"
		elif n%100==0:
			print "not leap year"
		else:
			print "its leap year"	
	io=io-1
