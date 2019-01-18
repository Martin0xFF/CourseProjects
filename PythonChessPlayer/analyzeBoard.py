from chessLib import *
board =initBoard(None)
printBoard(board)
while True:
	flag = analyzeBoard(board)

	if flag != 0:
		if flag == 1:
			printBoard(board)
			print "White King has lost"
			break
		if flag ==2:
			printBoard(board)
			print "Black Kind has lost"
			break
		if flag == 3:
			printBoard(board)
			print "StaleMate"
			break
	if isCheck(board,10):
		print "White King is in Check"
		savingMove = leaveCheck(board,10)
		Move(board,savingMove[0],savingMove[1])
		printBoard(board)
		print savingMove
	
#		raw_input( "Saving Move has been made")	
	else:

		
		while True:
			worth(board)
			print"white Player Make a Move:"
			move=stratLeanLookAhead(board,2,10)
#			move=stratPureRandom(board,10)
				
		
			if Move(board,move[0],move[1]):
				print move,"white Move has been made"
				printBoard(board)
#				raw_input ("Regular Move")
				break
#	raw_input()
	
	print "Next Step \n"

	flag = analyzeBoard(board)

	if flag != 0:
		if flag == 1:
			printBoard(board)
			print "White King has lost"
			break
		if flag ==2:
			printBoard(board)
			print "Black Kind has lost"
			break
		if flag == 3:
			printBoard(board)
			print "StaleMate"
			break
	if isCheck(board,20):
		print "Black king is in check"	
		savingMove = leaveCheck(board,20)
		Move(board,savingMove[1][0],savingMove[1][1])	
		printBoard(board)
		print savingMove
	#	raw_input( "Black king saving move")
			
	else:		

		while True:	

		
			print"Black Player Make a Move:"
		#	move=stratLookAhead(board,1,20)
			move =stratPureRandom(board,20)
			if Move(board,move[0],move[1]):
				printBoard(board)
	#			raw_input ("Regular Move")
				break
 	print len(GetPlayerPositions(board,20) ),"black pieces left"
 	print len(GetPlayerPositions(board,10) ),"white pieces left"
	raw_input()
	
