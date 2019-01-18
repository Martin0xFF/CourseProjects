import tttlib as t
gameboard = t.ttt()
playerx = 1
playero = 2

while True:
   print"Human Player's Turn"
   char = 'X'
   Flag = False

   while (Flag == False):
	try:
		ValIn =int( raw_input("Input a location player "+char+" :"))
		Flag = gameboard.Move(ValIn,playerx)
	except:
		print("Try a different location")

   gameboard. printBoard()
   if (gameboard.analyzeBoard()== 1):
	print("PlayerX has won!!!!")
        break
   if (gameboard.analyzeBoard()== 3):
	print("Tie!!!!")
	break
  
   print("Bot Players Turn")
   Flag = False
   char ='O'
	
   botWin = gameboard.genWinningMove(playero)
   botNonLoser = gameboard.genNonLoser(playero)
   if  botWin <> -1:
	gameboard.Move(botWin,playero)
   elif botNonLoser <> -1:
	gameboard.Move(botNonLoser,playero)
   else:
	gameboard.Move(gameboard.genRandomMove(playero),playero)

   if (gameboard.analyzeBoard()== 2):
	print("PlayerO has won!!!!")
        break
   gameboard. printBoard()




   
   #while (Flag==False):
#	try:
#		ValIn =int( raw_input("Input a location player "+char+" :"))
#		Flag = gameboard.Move(ValIn,playero)
#	except:
#		print("Try a different location")

	
 #   gameboard. printBoard()
  # if (gameboard.analyzeBoard()== 2):
#	print("PlayerO has won!!!!")
 # 	break
   if (gameboard.analyzeBoard()== 3):
	print("Tie!!!!")
	break
    

 
