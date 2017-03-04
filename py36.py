		#Program to print primes upto a certain no. using Sieve of Eratosthenes
#!/usr/bin/python

k=input()
from math import sqrt
g=0
print 2
for i in range(3,k+1):
    g=0 
    for j in range(2,int(sqrt(i)+1)):
            if i%j==0 :
                g=2
                break
  
        
    if g==0:
        print i

