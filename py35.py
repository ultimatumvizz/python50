''' check whether a text is french , german ,spanish or english '''
import enchant
import operator
f=open('sampspa.txt','r')
fre=enchant.Dict('fr')
eng=enchant.Dict('en')
ger=enchant.Dict('de_DE')
spa=enchant.Dict('es')
string=f.read()
liz=string.split(" ")
count=dict()
count["English"]=0
count["French"]=0
count["Spanish"]=0
count["German"]=0
for word in liz:
	if fre.check(word):
		count["French"]=count["French"]+1
	if ger.check(word):
		count["German"]=count["German"]+1
	if eng.check(word):
		count["English"]=count["English"]+1
	if spa.check(word):
		count["Spanish"]=count["Spanish"]+1
print max(count.iteritems(),key=operator.itemgetter(1))[0]
f.close()
	  		

