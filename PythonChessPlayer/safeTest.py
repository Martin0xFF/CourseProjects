from chesslib import *
import time

board =initBoard(None)
print len(board)
board[40] = 0
print len(board),"\n\n"
while True:
	printBoard(board)

	whiteInDanger = isCheck(board,10)	
	if whiteInDanger:
		print"White king is in danger"
	if whiteInDanger == True:	
		if isCheckMate(board,10)==True:
			print "The white king has lost"
			printBoard(board)
			break
		
		savingMove = leaveCheck(board,10)
		Move(board,savingMove[0],savingMove[1])
		printBoard(board)
		print savingMove
#		raw_input( "Saving Move has been made")	

	else:

		while True:
			print"white Player Make a Move:"
			move=stratPureRandom(board,10)
			printBoard(board)
		
			if Move(board,move[0],move[1]):
				print move
#				raw_input ("Regular Move")
				break

	print "Next Step \n"
	printBoard(board)



	if isCheck(board,20) == True:
		if isCheckMate(board,20)==True:
			print "The Black king has lost"
			printBoard(board)
			break
		
			
		savingMove = leaveCheck(board,20)
		Move(board,savingMove[0],savingMove[1])	
		printBoard(board)
		print savingMove
	#	raw_input( "Black king saving move")
			
	else:		

		while True:	

		
			print"Black Player Make a Move:"
			move=stratSafeRandom(board,20)
			printBoard(board)
			if Move(board,move[0],move[1]):
				print move
	#			raw_input ("Regular Move")
				break

#	print "Next Step \n"
#	print board
#	if isCheck(board,20):		
#		printBoard(board)
#		print "The Black King is in check"
#		raw_input()
	
