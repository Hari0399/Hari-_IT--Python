a=[1,2,3,4,5,6,7,8,9]
def printBoard():
	print(a[0],'|',a[1],'|',a[2])
	print("-------------")
	print(a[3],'|',a[4],'|',a[5])
	print("--------------")
	print(a[6],'|',a[7],'|',a[8])
printBoard()

player1turn = True

while True:
	printBoard()
	p = int(input("Choose your place,Player 1 >>"))
	if player1turn:
		#p = input("Choose your place,Player 1 >>")
		a[int(p)-1] = 'X'
		player1turn = not player1turn
	else:
		#p = input("Choose your place,Player 2 >>")
		a[int(p)-1] = 'O'
		player1turn = not player1turn
	#Check win condition
	for i in (0,3,6):
		if(a[i]==a[i+1] and a[i]==a[i+2]):
			if a[i]=='X':
				print("Player1 Wins")
			exit()
		else:
			print("Player2 Wins")
			exit()
	for i in range(3):
		if(a[i]==a[i+3] and a[i]==a[i+6]):
			if a[i]=='X':
				print("Player1 Wins")
				exit()
		else:
			print("Player2 Wins")
			exit()
	

