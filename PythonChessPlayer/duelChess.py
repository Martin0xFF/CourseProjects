from chesslib import *
board =initBoard(None)
board[40] = 13

while True:

	printBoard(board)
	while True:
		
		print "White Player Make a Move:"
		old =int (raw_input("Old Position: "))
		new = int(raw_input("New Position: "))		
		
		flag = IsPositionUnderThreat(board,new,10)
		printBoard(board)
	#	print "Safe Candidates \n"
	#	print safeMoves(board,10)
	#	print "General Candidates\n"
	#	print generateCandidateMoves(board,10)
		if flag:
			if raw_input("Dangerous pos, still want (y/n)"):
				if Move(board,old,new):
					break
						
			
		else:
			if Move(board,old,new):
				break

	print"Next Step\n"
	printBoard(board)

	while True:
		print"Black Player Make a Move:"
		move=stratSafeRandom(board,20)
		printBoard(board)
		if Move(board,move[0],move[1]):
			break

	print "Next Step \n"


