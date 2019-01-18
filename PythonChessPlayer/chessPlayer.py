from random import randint
import chessPlayer_tree as tree

def initBoard(x):
	if x == None:
		out = [0]*64
		for i in range(8,16):
			out[i] = 10
		out[0]=13	
		out[7]=13
	
		out[1] =11
		out[6] =11
		
		out[2] =12
		out[5] =12
		
		out[3] =14
		out[4] =15
		for i in range(48,56):
			out[i] = 20
		out[-1] =23 
		out[-8] =23

		out[-2] =21
		out[-7] =21
		
		out[-3] =22
		out[-6] =22
		
		out[-4] =25
		out[-5] =24
		

	if x ==1:
		out =[0]*64
 
	return out
	#Note dividing index by 8 will give you the row, moding by 8 will give you the column indexing can be done as board[8*r + c]  
def Move(board,oldPos,newPos):	
	try:	
		oldPos = int(oldPos)
		newPos =  int(newPos)
		legal = GetPieceLegalMoves(board,oldPos)
#		if board[oldPos]%10 == 5:
#			print oldPos,newPos
#			raw_input("A King has been Moved")
		if newPos>63 or newPos<0: 
			return False
		if newPos in legal:
			board[newPos] = board[oldPos]
			board[oldPos] = 0
			return True
		return False
	except:
		return False

def GetPlayerPositions(board,player):
     	out = []
	for i in range(0,len(board)):
		if board[i]/10 == player/10:
			out = out + [i]
	
		
	return out

def GetPieceLegalMoves(board,position):
#	print len(board),"Board Size"
	if board[position] == 0:
		return []
	legalPos = []
	piece = board[position]%10
	temp = position

	enemyPos = [] 
	row = position/8
	col = position%8

	if piece>5:
		return []
	
	if board[position]/10 == 1:
		player = 10
		enemyPos = GetPlayerPositions(board,20)
	else:
		player = 20
		enemyPos = GetPlayerPositions(board,10)
	
	#Pawn
	if piece ==0:
		#Player is White they can only move up 1 unit
		if player == 10:
			if (position/8 + 1) <= 7 : 
				if board[position + 8]==0:
					legalPos = legalPos +[position + 8]
				
				if position+7 in enemyPos and (position%8 -1) >=0:
					legalPos = legalPos + [position +7]
				if position+9 in enemyPos  and (position%8 +1) <=7 :
					legalPos = legalPos + [position +9]
			return legalPos
		
		#if player is Black only move down 1 unit
		if player == 20:
			if (position/8 - 1) >= 0 : 
				if board[position - 8] ==0:
					legalPos =[ position - 8]
	
				if ((position-7 in enemyPos) and (position%8 +1) <=7):
					legalPos = legalPos + [position -7]
				if ((position-9 in enemyPos) and (position%8 -1) >=0) :
					legalPos = legalPos + [position -9]
	
			return legalPos
	#Knight
	if piece ==1:
		#Up and to the left
		if (temp/8 + 2 <=7) and(temp%8 - 1 >=0): 
		

			if (board[temp + 15]==0 or (temp+15 in enemyPos)):
				legalPos = legalPos + [temp+15]

	 	if (temp/8 + 1 <=7) and(temp%8 - 2 >=0) :
			if (board[temp+6]==0 or (temp+6 in enemyPos)): 
				legalPos = legalPos + [temp+6]
		#down and to the left
		if (temp/8 - 2 >=0) and(temp%8 - 1 >=0):
			if( board[temp - 17]==0 or (temp-17 in enemyPos)):
				legalPos = legalPos + [temp-17]

		if (temp/8 - 1 >=0) and(temp%8 - 2 >=0):
			if (board[temp-10]==0 or (temp-10 in enemyPos)) :
				legalPos = legalPos +[temp -10]
		#down and to the right
		if(temp/8 - 2>=0) and(temp%8 +1 <=7):
			if( board[temp - 15]==0 or (temp-15 in enemyPos)):
				legalPos = legalPos + [temp-15]
		if (temp/8 - 1>=0) and(temp%8 +2 <=7):

			if (board[temp-6]==0 or (temp-6 in enemyPos)) :
				legalPos = legalPos +[temp -6]
		#up and Right
		if (temp/8 + 2 <=7) and(temp%8 +1 <=7): 	
		
		#	print temp +17
			if (board[temp + 17]==0 or (temp+17 in enemyPos)):
				legalPos = legalPos + [temp+17]
		if (temp/8 + 1 <=7) and(temp%8 +2 <=7):
		
			if (board[temp+10]==0 or (temp+10 in enemyPos)):
				legalPos = legalPos +[temp +10]
	
		return legalPos	
	#Bishop
	if piece ==2:		
		while (temp/8 - 1) >= 0 and  (temp%8-1) >= 0 :
			if board[temp-9]==0:#Keep going down and left until there is something in the way
				legalPos = legalPos +[temp-9]
			else:
				if (temp-9 in enemyPos):
					legalPos = legalPos +[temp-9]
				break
			temp = temp - 9
		
		
		temp = position
		
		while (temp/8 + 1) <= 7 and (temp%8-1) >=0 :# keep going up and left until there is something in the way
			if board[temp+7]==0:
				legalPos = legalPos + [temp + 7]	
			else:
				if (temp+7 in enemyPos):
					legalPos = legalPos +[temp + 7]	
				break
			temp = temp + 7

			if temp >63:
				break
		
		temp = position

		while  (temp/8 + 1) <= 7  and (temp%8 + 1) <= 7:#keep going up and right until there is something in the way
			if board[temp + 9]==0:
				legalPos = legalPos + [temp +9]
			else:
				if (temp+9 in enemyPos):
					legalPos = legalPos +[temp+9]
				break
			temp = temp + 9
			if temp >63:
				break
		
		temp = position
		
		while  (temp/8 -1) >=0 and (temp%8+1) <= 7:#keep going down and right until there is something in the way
			if board[temp-7] ==0:
				legalPos = legalPos + [temp - 7]
			else:
				if (temp-7 in enemyPos):
					legalPos = legalPos +[temp-7]
				break
		   	temp = temp - 7
		
		return legalPos


	
	#Rook
	if piece ==3:	
		
		while (temp/8 - 1) >= 0:
			if board[temp-8]==0:#Keep going down until there is something in the way
				legalPos = legalPos +[temp-8]
			else:
				if (temp-8 in enemyPos):
					legalPos = legalPos +[temp-8]
				break
			temp = temp - 8
		
		temp = position
		
		while (temp/8 + 1) <= 7:# keep going up until there is something in the way
			if temp+8 >63:
				break
		
		#	print temp +8
			if board[temp+8]==0:
				legalPos = legalPos + [temp + 8]	
			else:
				if (temp+8 in enemyPos):
					legalPos = legalPos +[temp+8]
				break
			temp = temp + 8
			if temp >63:
				break
		


		temp = position

		while (temp%8 + 1) <= 7:#keep going right until there is something in the way
			
		
		#	print temp+1
			if board[temp + 1]==0:
				legalPos = legalPos + [temp +1]
			else:
				if (temp+1 in enemyPos):
					legalPos = legalPos +[temp+1]
				break
			temp = temp + 1
			if temp >63:
				break
		

		
		temp = position
		
		while (temp%8-1) >= 0:#keep going left until there is something in the way
			if board[temp-1] ==0:
				legalPos = legalPos + [temp - 1]
			else:
				if (temp-1 in enemyPos):
					legalPos = legalPos +[temp-1]
				break
		   	temp = temp - 1
		
		
		return legalPos


	#Queen
	if piece ==4:
		while (temp/8 - 1) >= 0 and  (temp%8-1) >= 0 :
			if board[temp-9]==0:#Keep going down and left until there is something in the way
				legalPos = legalPos +[temp-9]
			else:

				if (temp-9 in enemyPos):
					legalPos = legalPos +[temp-9]
				break
			temp = temp - 9
		
		temp = position
		
		while (temp/8 + 1) <= 7 and (temp%8-1) >=0 :# keep going up and left until there is something in the way
		

			if board[temp+7]==0:
				legalPos = legalPos + [temp + 7]	
			else:
				if (temp+7 in enemyPos):
					legalPos = legalPos +[temp+7]
				break
			temp = temp + 7
			if temp >63:
				break
		


		temp = position

		while  (temp/8 + 1) <= 7  and (temp%8 + 1) <= 7:#keep going up and right until there is something in the way
			if board[temp + 9]==0:
				legalPos = legalPos + [temp +9]
			else:
				if (temp+9 in enemyPos):
					legalPos = legalPos +[temp+9]
				break
			temp = temp + 9
			if temp >63:
				break
		

		temp = position
		
		while  (temp/8 -1) >=0 and (temp%8+1) <= 7:#keep going down and right until there is something in the way
			if board[temp-7] ==0:
				legalPos = legalPos + [temp - 7]
			else:
				if (temp-7 in enemyPos):
					legalPos = legalPos +[temp-7]
				break
		   	temp = temp - 7
			if temp >63:
				break
		

		temp = position	
		while (temp/8 - 1) >= 0:
			if board[temp-8]==0:#Keep going down until there is something in the way
				legalPos = legalPos +[temp-8]
			else:
				if (temp-8 in enemyPos):
					legalPos = legalPos +[temp-8]
				break
			temp = temp - 8
		

		temp = position
		
		while (temp/8 + 1) <= 7:# keep going up until there is something in the way
			if board[temp+8]==0:
				legalPos = legalPos + [temp + 8]	
			else:
				if (temp+8 in enemyPos):
					legalPos = legalPos +[temp+8]
				break
			temp = temp + 8
			if temp >63:
				break
		

		temp = position

		while (temp%8 + 1) <= 7:#keep going right until there is something in the way
		#	print temp+1
		#	print len(board)
			if board[temp + 1]==0:
				legalPos = legalPos + [temp +1]
			else:
				if (temp+1 in enemyPos):
					legalPos = legalPos +[temp+1]
				break
			temp = temp + 1
			if temp >63:
				break
		

		temp = position
		
		while (temp%8-1) >= 0:#keep going left until there is something in the way
			if board[temp-1] ==0:
				legalPos = legalPos + [temp - 1]
			else:
				if (temp-1 in enemyPos):
					legalPos = legalPos +[temp-1]
				break
		   	temp = temp - 1
			
		
		return legalPos	
	#King
	if piece ==5:
		if (temp/8 - 1) >= 0 and  (temp%8-1) >= 0 :
			if board[temp-9]==0 or (temp-9 in enemyPos):#Keep going down and left until there is something in the way
				legalPos = legalPos +[temp-9]
		
		temp = position
		
		if (temp/8 + 1) <= 7 and (temp%8-1) >=0 :# keep going up and left until there is something in the way
			if board[temp+7]==0 or (temp+7 in enemyPos):
				legalPos = legalPos + [temp + 7]	

		temp = position

		if  (temp/8 + 1) <= 7  and (temp%8 + 1) <= 7:#keep going up and right until there is something in the way
			if board[temp + 9]==0 or (temp+9 in enemyPos):
				legalPos = legalPos + [temp +9]
		
		temp = position
		
		if  (temp/8 -1) >=0 and (temp%8+1) <= 7:#keep going down and right until there is something in the way
			if board[temp-7] ==0 or (temp-7 in enemyPos):
				legalPos = legalPos + [temp - 7]
		temp = position	
		if (temp/8 - 1) >= 0:
			if board[temp-8]==0 or (temp-8 in enemyPos):#Keep going down until there is something in the way
				legalPos = legalPos +[temp-8]
		
		temp = position
		
		if (temp/8 + 1) <= 7:# keep going up until there is something in the way
			if board[temp+8]==0 or (temp+8 in enemyPos):
				legalPos = legalPos + [temp + 8]	

		temp = position

		if (temp%8 + 1) <= 7:#keep going right until there is something in the way
			if board[temp + 1]==0 or (temp+1 in enemyPos):
				legalPos = legalPos + [temp +1]
			
		temp = position
		
		if (temp%8-1) >= 0:#keep going left until there is something in the way
			if board[temp-1] ==0 or (temp-1 in enemyPos):
				legalPos = legalPos + [temp - 1]
			
		temp = position	
	
		return legalPos

	return legalPos

def gameOver(board):
	
    return None
def printBoard(board):
	for i in range(7,-1,-1):
		for x in range(0,21):
			print "-",
		print "\n"
		
		for w in range(0,8):
			print "|",
			if board[i*8 +w] == 0:
			
				if i%2 == 0 and w%2 == 0:
					print "__",
				elif i%2 == 1 and w%2 == 0:
					print "##",
				elif i%2 == 0 and w%2 ==1:
					print "##",
				else:
					print "__",
			else:
				print board[i*8 + w],
		print "|\n"
	return True

def IsPositionUnderThreat(board,position,player):
	threat = False	
	enemyMoves = []
	enemyPos = []
	pseudoBoard = board[0:64]	
	#Placed a test pawn on the pseudoBoard to calculate the threats
	if player/10 == 1:
		player = 10
		pseudoBoard[position] = 10
		enemyPos = GetPlayerPositions(pseudoBoard,20)
	else:
		player = 20
		pseudoBoard[position] = 20
		enemyPos = GetPlayerPositions(pseudoBoard,10)
	
	for i in enemyPos:
		enemyMoves = enemyMoves + GetPieceLegalMoves(pseudoBoard,i)

	check = position in enemyMoves
	if position in enemyMoves:
		threat = True
			 
	
	return threat

#evaluates the worth of a move by examining the state of the board assume pos gains are white and negative gains are black
def worth(board):
	#for White pieces
	whitePos = GetPlayerPositions(board,10)
	blackPos = GetPlayerPositions(board,20)

	whiteWeight = 0
	blackWeight = 0	
	PieceWeighting = [20.0,45.0,45.0,100.0,100.0,180.0,1000.0]
	whitePawnPref = [0,0,0,0,0,0,0,0,0,10,10,10,10,10,10,0,0,15,15,15,15,15,15,0,0,20,20,20,20,20,20,0,0,20,20,20,20,20,20,0,0,15,15,15,15,15,15,0,0,10,10,10,10,10,10,0,0,0,0,0,0,0,0,0,0]


	'''
	whiteKnightPref = [-50,-40,-30,-30,-30,-30,-40,-50,-40,-20,  0,  5,  5,  0,-20,-40,-30,  5, 10, 15, 15, 10,  5,-30,-30,  0, 15, 20, 20, 15,  0,-30,-30,  5, 15, 20, 20, 15,  5,-30,-30,  0, 10, 15, 15, 10,  0,-30,-40,-20,  0,  0,  0,  0,-20,-40,-50,-40,-30,-30,-30,-30,-40,-50]


	whiteBishopPref = [-20,-10,-10,-10,-10,-10,-10,-20,-10,  5,  0,  0,  0,  0,  5,-10,-10, 10, 10, 10, 10, 10, 10,-10,-10,  0, 10, 10, 10, 10,  0,-10,-10,  5,  5, 10, 10,  5,  5,-10,-10,  0,  5, 10, 10,  5,  0,-10,-10,  0,  0,  0,  0,  0,  0,-10,-20,-10,-10,-10,-10,-10,-10,-20]

	whiteRookPref = [0,  0,  0,  5,  5,  0,  0,  0, -5,  0,  0,  0,  0,  0,  0, -5,-5,  0,  0,  0,  0,  0,  0, -5,-5,  0,0,  0,  0,  0,  0, -5,-5,  0,  0,  0,  0,  0,  0, -5,-5,  0,  0,  0,  0,  0,  0, -5,5, 10, 10, 10, 10, 10, 10,  5,0,  0,  0,  0,  0,  0,  0,  0]

	whiteQueenPref=[-20,-10,-10, -5, -5,-10,-10,-20,-10,  0,  0,  0,  0,  0,  0,-10,-10,  0,  5,  5,  5,  5,  0,-10, 5,  0,  5,  5,  5,  5,  0, -5,-5,  0,  5,  5,  5,  5,  0, -5,-10,  0,  5,  5,  5,  5,  0,-10,-10,  0,  0,  0,  0,  0,  0,-10,-20,-10,-10, -5, -5,-10,-10,-20]

	whiteKingPrefMid = [20, 30, 10,  0,  0, 10, 30, 20,20, 20,  0,  0,  0,  0, 20, 20,-10,-20,-20,-20,-20,-20,-20,-10,-20,-30,-30,-40,-40,-30,-30,-20,-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30]

	whiteKingPrefEnd = [-50,-30,-30,-30,-30,-30,-30,-50,-30,-30,  0,  0,  0,  0,-30,-30,-30,-10, 20, 30, 30, 20,-10,-30,-30,-10, 30, 40, 40, 30,-10,-30,-30,-10, 30, 40, 40, 30,-10,-30,-30,-10, 20, 30, 30, 20,-10,-30,-30,-20,-10,  0,  0,-10,-20,-30,-50,-40,-30,-20,-20,-30,-40,-50]
	'''
#black peice prefences
	blackPawnPref = whitePawnPref[::-1]
 	'''
	blackKnightPref =whiteKnightPref[::-1]	
	blackBishopPref=whiteBishopPref[::-1]
	blackRookPref=whiteRookPref[::-1]
	blackQueenPref =whiteQueenPref[::-1]
	blackKingPrefMid =whiteKingPrefMid[::-1]
	blackKingPrefEnd =whiteKingPrefEnd[::-1]
	'''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~	

	for i in range(0,6):
		whiteWeight = whiteWeight +PieceWeighting[i]* board.count( 10+i)

	'''
	for w in blackPos:
		piece = board[w]%10
	
		if piece == 0:
			con = 15.0
		if piece == 1:
			con =75.0
		if piece == 2:
			con =75.0
		if piece ==3:
			con = 75.0
		if piece ==3:
			con = 75.0
		if piece ==4:
			con =120.0
		if piece == 5:
			con = 900.0
	
	

		if IsPositionUnderThreat(board,w,20) == True:
			whiteWeight = con*1 + whiteWeight	

	'''


	
 
	for i in range(0,6):	
		blackWeight = blackWeight + PieceWeighting[i]*board.count(20+i)

	'''
	for w in whitePos:
		piece = board[w]%10
		if piece == 0:
			con = 15.0
		if piece == 1:
			con =75.0
		if piece == 2:
			con =75.0
		if piece ==3:
			con = 75.0
		if piece ==3:
			con = 75.0
		if piece ==4:
			con =120.0
		if piece == 5:
			con = 900.0

		if IsPositionUnderThreat(board,w,10) == True:
			blackWeight = con*1 + blackWeight	

	'''


	#if player/10==1:
	
#	if isCheck(board,10):
#		blackWeight = blackWeight + 10000.0
#	if isCheck(board,20):
#		whiteWeight =whiteWeight + 10000.0
	
	#else: 
	difference = blackWeight - whiteWeight
	
	if difference == 0:
		position = [10,15,15,30,30,0]	
		for i in whitePos:
			piece = board[i]%10
			whiteWeight = whiteWeight + position[piece]* whitePawnPref[i]


		
		for i in blackPos:
			piece = board[i]%10
			blackWeight = blackWeight +  position[piece]*blackPawnPref[i]



	
	difference = whiteWeight - blackWeight
	

	return difference







def safeMoves(board,player):
	candidateMoves =[]
	heldPositions = GetPlayerPositions(board,player)
	#element 0 of the lists is the currentposition, the following is the positions you can move to	
	for i in heldPositions:
		legalMoves = GetPieceLegalMoves(board,i)
 		
		for w in range(0,len(legalMoves)):
			if IsPositionUnderThreat(board,legalMoves[w],player) ==False:
				candidateMoves = candidateMoves + [[i,legalMoves[w]]]
		
	return candidateMoves

	
def generateCandidateMoves(board,player):
	candidateMoves =[]
	illegalMoves = []
	pseudoBoard = board[0:64]
	heldPositions = GetPlayerPositions(board,player)
	#element 0 of the lists is the currentposition, the following is the positions you can move to	
	kingPos = board.index(player+5)
	
	for i in heldPositions:
		legalMoves = GetPieceLegalMoves(board,i)
		
		if len(legalMoves) !=0: 
			for h in legalMoves:
				pseudoBoard = board[0:64]
				Move(pseudoBoard,i,h)
				if isCheck(pseudoBoard,player)==False:	
					candidateMoves = candidateMoves + [[i] + [h]]
			
		
	return candidateMoves
#0 continue game
#1 white Player Losers
#2 black Player Losers
#3 Stalemate

def analyzeBoard(board):
	flag = 0
	
	if isStaleMate(board )==True:
		flag = 3
		return flag


	if isCheckMate(board,10) == True:
		flag = 1
		return flag

	if isCheckMate(board,20) == True:
		flag = 2
		return flag
	
	return flag


def leaveCheck(board,player):
	waysOut =[]
	worthVec =[]
	outVec = []
	pseudoBoard = board[0:64]
	possibleMoves = generateCandidateMoves(board,player)
	for i in possibleMoves:
		pseudoBoard = board[0:64]
		Move(pseudoBoard,i[0],i[1])
		if isCheck(pseudoBoard,player) == False:
#			print i
			worthVec = worthVec + [worth(pseudoBoard)]
		 	waysOut = waysOut + [i]
	for w in range(0,len(waysOut)):
		outVec= outVec+[[waysOut[w],worthVec[w]]]


	'''
	if len(waysOut) !=0:

		if player/10 ==1:
			maxIndex = waysOut.index(max(waysOut))
			return waysOut[maxIndex]
			
		else:
			minIndex = waysOut.index(min(waysOut))
			return waysOut[minIndex]		
	else:
#		print "This shouldnt print"
	'''
	return outVec

def isStaleMate(board):
	stalemate = False
	whiteMoves = generateCandidateMoves(board,10)
	blackMoves = generateCandidateMoves(board,20)
#	print "White moves",whiteMoves
#	print "Black Moves",blackMoves
	if isCheck(board,20)==False and  len(blackMoves)==0:
		stalemate = True
		return stalemate
	if isCheck(board,10)==False and len(whiteMoves)==0:
		stalemate = True
		return stalemate
	
	blackpieces =len( GetPlayerPositions(board,20))
	whitepieces =len(GetPlayerPositions(board,10))
	if blackpieces == 1 and whitepieces == 1:
		stalemate =True
		return stalemate
	return stalemate
		
		
def isCheckMate(board,player):
	pseudoBoard = board[0:64]
	possibleMoves = generateCandidateMoves(board,player)

	if isCheck(board,player) == False:
		return False
	if len(possibleMoves)==0:
		return True
	for i in possibleMoves:
		pseudoBoard = board[0:64]
		Move(pseudoBoard,i[0],i[1])
		if isCheck(pseudoBoard,player) == False:
			return False

	 
	return True
		

def isCheck(board,player):
	check = False
#	allPieces = GetPlayerPositions(board,player)
	kingPos = board.index(player+5)
	if IsPositionUnderThreat(board,kingPos,player) == True:
		check = True
	return check
	

def onBoard(position):
	row =position/8
	col = position%8
		
	
	if row+1  >7 or row-1 <0 :
		return False
	if col+1 > 7 or col-1 <0 :
		return False
	return True


'''
def stratSafeRandom(board,player):
	moveSet=safeMoves(board,player)
	ran = randint(0,len(moveSet)-1)
	move = moveSet[ran]
	return move

def stratPureRandom(board,player):
	moveSet=generateCandidateMoves(board,player)
	ran = randint(0,len(moveSet)-1)
	move = moveSet[ran]
	return move
'''

def stratSafeLookAhead(board,depth,player):
	outMoves = []
	Root = tree.tree(list(board))

	moveSet = safeMoves(board,player)
	Root = safeExtend(Root,depth,player)
	#if flag is true, player is white
	if player/10 == 1:
		flag=True
	else:
		flag = False
	
		
		

	if len(Root.store[1])!=0:
		for i in range(0,len(Root.store[1])):
#			print "depth going in",depth
			temp = processNode(Root.store[1][i],depth-1)
#			print "First successor"
#			raw_input()
			if len(temp) != 0:
				if flag ==True:
				#	print temp,"The nodal values"
					Root.store[1][i]= min(temp)
#					print min(temp), "min of moves(white) want the worst white case" 
#					raw_input()
				else:
					Root.store[1][i]= max(temp)
#					print max(temp),"max of moves (black) want the worst black case"
#					raw_input()
			else:
				Root.store[1][i] = None

#	print Root.store[1],"The successors of Root"
#	raw_input()
	WorstCases = Root.store[1]
	if len(temp) !=0:
		for w in range(0,len(WorstCases)):
			outMoves = outMoves + [[moveSet[w],WorstCases[w]]]

	'''

		#for white want the best worst case
		if flag == True:
			maxIndex = WorstCases.index(max(WorstCases))
			move = moveSet[maxIndex]
			print maxIndex 
		#for black want best worst case(black is negative)
		else:
			minIndex = WorstCases.index(min(WorstCases))		
			move = moveSet[minIndex] 
			print minIndex	
	'''
	
	return outMoves


	
def stratLookAhead(board,depth,player):
	
	outMoves=[]
	values = []
	Root = tree.tree(list(board))
	
	moveSet = generateCandidateMoves(board,player)
	Root = extend(Root,depth,player)
	#if flag is true, player is white
	if player/10 == 1:
		flag=True
	else:
		flag = False
 
	if len(Root.store[1])!=0:
		for i in range(0,len(Root.store[1])):
			temp = processNode(Root.store[1][i],depth-1,flag)			
			outMoves = outMoves + [[moveSet[i],temp.store[0]]]
			values = values + [temp.store[0]]
			Root.store[1][i] = temp
	if flag ==True:
		
		Root.store[0] = max(values)
		
	else:
	
		Root.store [0] = min(values)
#	print Root.Get_LevelOrder()
#	raw_input()
	return [outMoves,Root.Get_LevelOrder()]	





def stratLeanLookAhead(board,depth,player):

	Root = tree.tree(list(board))
	
	moveSet = generateCandidateMoves(board,player)
#	print moveSet, "mmoves set"
	Pathways = ExpandNode(Root,depth,player)
	#if flag is true, player is white
#	print Pathways,"lean pathways"
#	print "length of pathways",len(Pathways),len(moveSet)
#	raw_input()
	if player/10 == 1:
		flag=True
	else:
		flag = False
	
	#player is white
	if flag ==True:
		for i in range(0,len(moveSet)):
			Pathways[i]= min(Pathways[i])
#		print min(temp), "min of moves(white) want the worst white case" 
#		raw_input()

	else:#player is black
		for i in range(0,len(moveSet)):
			Pathways[i]= max(Pathways[i])
#	
#		print max(temp),"max of moves (black) want the worst black case"
#		raw_input()


 
	'''if len(Root.store[1])!=0:
		for i in range(0,len(Root.store[1])):
#			print "depth going in",depth
			temp = processNode(Root.store[1][i],depth-1)
#			print "First successor"
#			raw_input()
			if len(temp) != 0:
				if flag ==True:
					Root.store[1][i]= min(temp)
#					print min(temp), "min of moves(white) want the worst white case" 
#					raw_input()
				else:
					Root.store[1][i]= max(temp)
#					print max(temp),"max of moves (black) want the worst black case"
#					raw_input()
			else:
				Root.store[1][i] = None

	print Root.store[1],"The successors of Root"
#	raw_input()
	'''
	WorstCases = Pathways
#	print"Pathways",Pathways
	if len(Pathways) !=0:
	
		#for white want the best worst case
		if flag == True:
			maxIndex = WorstCases.index(max(WorstCases))
			move = moveSet[maxIndex]
		#for black want best worst case(black is negative)
		else:
			minIndex = WorstCases.index(min(WorstCases))		
			move = moveSet[minIndex] 	

	return move








def stratSafeRandom(board,player):
	moveSet=safeMoves(board,player)
	ran = randint(0,len(moveSet)-1)
	move = moveSet[ran]
	return move

def stratPureRandom(board,player):
	moveSet=generateCandidateMoves(board,player)
	ran = randint(0,len(moveSet)-1)
	move = moveSet[ran]
	return move






def safeExtend(root,depth,player):
#	print depth,"depth of root"
	if depth == 0:
		return root

	pseudoBoard = list(root.store[0])
	moveSet = safeMoves(root.store[0],player)
	
	for i in moveSet:
		pseudoBoard = root.store[0][0:64]
		Move(pseudoBoard,i[0],i[1])
		tempRoot =tree.tree(pseudoBoard)
		root.AddSuccessor(tempRoot)
		
	for i in range(0,len(root.store[1])):
		if player/10 ==1:
			safeExtend(root.store[1][i],depth-1,20)
		else:
			safeExtend(root.store[1][i],depth-1,10)

	return root	


def chessPlayer(board,player):
	EvalTree = []
	if len(board) != 64:
		return [False,[],[],[]]

	pseudoBoard = list(board)
	if player == 10 or player== 20:
		flag = analyzeBoard(pseudoBoard)
		if flag != 0:
			if flag == 1:
#				printBoard(board)
#				print "White King has lost"
				return [False,[],[],[]]
			if flag ==2:
#				printBoard(board)
#				print "Black Kind has lost"
				return [False,[],[],[]]
			if flag == 3:
#				printBoard(board)
#				print "StaleMate"
				return [False,[],[],[]]

		if isCheck(board,player):
			savingMove = leaveCheck(board,player)
#			Move(pseudoBoard,savingMove[0],savingMove[1]
#			ValueofMove = worth(pseudoBoard)
			if savingMove[0] == False:	
				return [False,[],[],[]]
	

			WorstCases =[]
			for i in range(0,len(savingMove)):
				WorstCases = WorstCases + [savingMove[i][1]]

			if len(savingMove)!=0:
	
		#for white want the best worst case
				if player == 10:
					maxIndex = WorstCases.index(max(WorstCases))
					move = savingMove[maxIndex][0]
					return[True,move,savingMove,EvalTree]
		#for black want best worst case(black is negative)
				else:
					minIndex = WorstCases.index(min(WorstCases))	
					move = savingMove[minIndex][0] 	
					return [True,move, savingMove,EvalTree]
			 
			
	
#		raw_input( "Saving Move has been made")	
		else:	
			'''
			saveCandidates = stratSafeLookAhead(board,3,player)
			
			WorstCases =[]
			for i in range(0,len(saveCandidates)):
				WorstCases = WorstCases +[saveCandidates[i][1]]
			if len(saveCandidates)!=0:

					#for white want the best worst case
				if player == 10:
					
					maxIndex = WorstCases.index(max(WorstCases))
					move = saveCandidates[maxIndex][0] 
					print "worst Cases",WorstCases,move,maxIndex

					return[True,move,saveCandidates,EvalTree]

	#				print maxIndex 
		#for black want best worst case(black is negative)
				else:
					minIndex = WorstCases.index(min(WorstCases))		
					move = saveCandidates[minIndex][0] 
					return[True,move,saveCandidates,EvalTree]
	#				print minIndex	
			
					
				
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


			
			for i in range(0,len(saveCandidates)):
				WorstCases = WorstCases +[saveCandidates[i][1]]
#			print WorstCases,"Worst cases"
		
			if len(candidateMoves)!=0:
	
		#for white want the best worst case
				if player == 10:	
					maxIndex = WorstCases.index(max(WorstCases))		
					move = candidateMoves[maxIndex][0]
					return[True,move,candidateMoves,EvalTree]
		#for black want best worst case(black is negative)
				else:
					minIndex = WorstCases.index(min(WorstCases))		
					move = candidateMoves[minIndex][0] 	
					return[True,move,candidateMoves,EvalTree]
#				raw_input ("Regular Move")
				'''		

	

			candidateMoves=stratLookAhead(board,3,player)
			WorstCases =[]
			EvalTree = candidateMoves[1]
			for i in range(0,len(candidateMoves[0])):
				WorstCases = WorstCases +[ candidateMoves[0][i][1]]
#			print WorstCases,"Worst cases"
#			raw_input()
			if len(candidateMoves[0])!=0:
	
		#for white want the best worst case
				if player == 10:	
					maxIndex = WorstCases.index(max(WorstCases))		 
					move = candidateMoves[0][maxIndex][0]
					return[True,move,candidateMoves[0],EvalTree]
		#for black want best worst case(black is negative)
				else:
					minIndex = WorstCases.index(min(WorstCases))		
					move = candidateMoves[0][minIndex][0] 	
					return[True,move,candidateMoves[0],EvalTree]
#				raw_input ("Regular Move")
				

	else:
		return [False,[],[],[]]

def extend(root,depth,player):
#	print depth,"depth of root"
	if depth == 0:
		return root

	pseudoBoard = list(root.store[0])
	moveSet = generateCandidateMoves(root.store[0],player)
	
	for i in moveSet:
		pseudoBoard = root.store[0][0:64]
		Move(pseudoBoard,i[0],i[1])
		tempRoot =tree.tree(pseudoBoard)
		root.AddSuccessor(tempRoot)
		
	for i in range(0,len(root.store[1])):
		if player/10 ==1:
			extend(root.store[1][i],depth-1,20)
		else:
			extend(root.store[1][i],depth-1,10)

	return root	




def ExpandNode(root,depth,player):
#	print depth,root.store[0],"depth of root"
	if depth == 1:
		moveSet = generateCandidateMoves(root.store[0],player)
	
		for i in range(0,len(moveSet)):
			pseudoBoard = root.store[0][0:64]
			Move(pseudoBoard,moveSet[i][0],moveSet[i][1])
			tempRoot =tree.tree(pseudoBoard)
			root.AddSuccessor(tempRoot)
	


		root.store[0] = []
#		print root.store[1] 
		for i in range(0,len(root.store[1])):
	#		print root.store[0],"Printing Root layer"
			if player ==10:
				root.store[0]=root.store[0] +  processNode(root.store[1][i],depth-1,True)		
			else:
				root.store[0]=root.store[0] +  processNode(root.store[1][i],depth-1,False)		
			
	#	print root.store[0], depth,"list of moves + depth"	
		return root.store[0] 

	moveSet = generateCandidateMoves(root.store[0],player)
	
	for i in range(0,len(moveSet)):
		pseudoBoard = root.store[0][0:64]
		Move(pseudoBoard,moveSet[i][0],moveSet[i][1])
		tempRoot =tree.tree(pseudoBoard)
		root.AddSuccessor(tempRoot)
		
		if player/10 ==1:
			ExpandNode(root.store[1][i],depth-1,20)
		else:
			ExpandNode(root.store[1][i],depth-1,10)

	'''		
	for i in range(0,len(root.store[1])):
		if player/10 ==1:
			extend(root.store[1][i],depth-1,20)
		else:
			extend(root.store[1][i],depth-1,10)
	'''
	for i in range(0,len(root.store[1])):
		root.store[1][i] = root.store[1][i].store[0]
#	print root.store[1],"All the positions"
	return root.store[1]	



def processNode(root,depth,isWhite):
#	print root,"at Depth",depth
	if depth == 0:
#		print "breakout"
		leafworth = worth(root.store[0])
		root.store[0] = leafworth 
#		print leafworth,"LeafyValue"
		return root
	else:
		root.store[0]= []
	
		for i in range(0,len(root.store[1])): 
			
			root.store[0] = root.store[0] +[ processNode(root.store[1][i],depth-1, isWhite).store[0]]
#			print "Root value is", root.store[0]
#		print root.store[0],"Total val" 
		if isWhite == True:
			if len(root.store[0])!=0:
				root.store[0]= min(root.store[0])
		else:
			if len(root.store[0])!=0:
				root.store[0] = max(root.store[0]) 
#		print root.store[0],depth,"Root value at depth"		
#		raw_input()
		return root

