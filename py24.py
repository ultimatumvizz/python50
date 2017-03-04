io=input("")
while(io):
	s=raw_input("enter the string: ")
	count1=1
	count2=0
	for i in s:
		if i==" ":
			count1+=1
		else:
			count2+=1	
	print "the number of words are %d and number of chars are %d" %(count1,count2)
	io=io-1	
