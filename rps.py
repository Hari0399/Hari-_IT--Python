import random

a={1:'Rock',2:'Paper',3:'Scissor'}

while True:
	p=input("Your choice Rock/Paper/Scissor")
	c=a[random.randint(1,3)]
	print("You choose",p,"Computer choose:",c)
	if (a==1 and c==2):
		print("c wins")
	elif (a==1 and a==3):
		print ("p wins")
	elif(a==1 and a==1):
		print ("its a draw")
	elif(a==2 and a==1):
		print("p wins")
	elif (p==2 and a==2):
		print("its a draw")
	elif (a==2 and a==3):
		print("c wins")
	elif (a==3 and a==1):
		print("c wins")
	elif (a==3 and a==2):
		print ("p wins")
	elif (a==3 and a==3):
		print ("its a draw")
	else:
		break	
