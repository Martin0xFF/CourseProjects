from chessPlayer import *
board =initBoard(None)
printBoard(board)


while True:
	print" White move"
	Whitemove = chessPlayer(board,20)
	if Whitemove[0]==False:
		break
	
	else:
		Move(board, Whitemove[1][0],Whitemove[1][1])
	print"after move~~~~~~~",Whitemove[0],Whitemove[1],Whitemove[2]
	print"Status,move,CandidatesMoves,EvalTree "	
	printBoard(board)
	





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
	if isCheck(board,10):
		savingMove = leaveCheck(board,10)
#			Move(pseudoBoard,savingMove[0],savingMove[1]
#			ValueofMove = worth(pseudoBoard)	
	

		WorstCases =[]
		for i in range(0,len(savingMove)):
			WorstCases = WorstCases + [savingMove[i][1]]

		if len(savingMove)!=0:
	
		#for white want the best worst case
			
			minIndex = WorstCases.index(min(WorstCases))		
			move = savingMove[minIndex][0] 	
			if Move(board,move[0],move[1]):
				None
			else:
				break


			 
			
	
	#	print "Black king is in check"	
	#	savingMove = leaveCheck(board,20)
	#	Move(board,savingMove[0],savingMove[1])	
	#	printBoard(board)
	#	print savingMove
	#	raw_input( "Black king saving move")
		
	else:		

		while True:	

		
			print"white Player Make a Move:"
		#	move=stratLookAhead(board,1,20)
			move =stratSafeRandom(board,10)
			if Move(board,move[0],move[1]):
				printBoard(board)
				print move,"white Move has been made"
	#			raw_input ("Regular Move")
				break
	print len(GetPlayerPositions(board,10)),"White Pieces"
	print len(GetPlayerPositions(board,20)),"Black Pieces"

