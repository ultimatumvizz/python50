	#Towers of Hanoi Prob
#!/usr/bin/python
def Tower(n,fromp,to,aux):
	if n==1:
		print "Move disk 1 from peg",fromp,"to peg",to
		return
	Tower(n-1,fromp,aux,to)
	print "Move disk",n,"from peg",fromp,"to peg",to
	Tower(n-1,aux,to,fromp)
p=input()
c=raw_input("Enter From Peg: ")
g=raw_input("Enter To Peg: ")
h=raw_input("Enter Auxiliary Peg: ")
Tower(p,c,g,h)
