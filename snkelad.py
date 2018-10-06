import random
n=0
while (n==100):
	a=input("Enter r to roll dice or any char to quit")
	if(a=='r'):
		r=random.randit(1,6)
		print("u got",r)
		n=n+r
		print("ur score is",n)
		if(n=2):
			n=34
		elif(n=8):
			n=37
		elif(n=11):
			n=2
			elif(n=38):
				n=9
			elif(n=40):
				n=68
			elif(n=52):
				n=81
			elif(n=65):
				n=46
				elif(n=76):
					n=97
				elif(n=89):
					n=70
				elif(n=93):
					n=64
				elif(n=100):
					print("You Win")
				else:
					break

