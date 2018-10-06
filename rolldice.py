import random
while True:
	n=(input("Enter r to roll the dice,or q to quit:"))
	a=input("enter r or q")
	if(a=='r'):
		r=random.randint(1,6)
		print(r)
	else:
 		break


	