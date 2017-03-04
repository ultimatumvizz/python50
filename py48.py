import math
print "enter the angle in degrees at which the ladder is inclined on the wall"
deg=input("")
k=math.radians(deg)
ans=math.sin(k)
print "enter the height to which the ladder stands on the wall"
height=input("")
length=height/ans
print "length of the ladder is %0.2f" %length
