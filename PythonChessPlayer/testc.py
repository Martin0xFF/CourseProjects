import chesslib as c

board = c.initBoard(None)
#board[31] = 12
#board[39] = 25
#board[38] = 10
#board[38] = 14
#board[22] = 10

#board[23] = 12
#board[21] = 12
#board[39] = 12
#board[8] = 0


out = c.GetPlayerPositions(board,10)
print " positions held by Player\n\n"
for i in out:
	print i
print"Legal Moves \n"
legal =  c.GetPieceLegalMoves(board,1)
for i in legal:
	print i

c.printBoard(board);
for w in range(0,64):

	print "Legal Moves ",w,"\n"

	legal =  c.GetPieceLegalMoves(board,w)
	for i in legal:
		print i


t =c.IsPositionUnderThreat(board,48,20)
print t

print "gen Can moves"
print c.generateCandidateMoves(board,10)
 
