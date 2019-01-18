import tttlib.py as t

def playerMov(playerNumber):
 
        if (playerNumber == 1) :
            char = "x"
        elif (playerNumber == 2):
            char = "o"
        while True:
             try:
                 position = int(raw_input("Choose a place to plot "+char+" :"))
                 if (position < 9 and position >= 0): 
                     if (playField[position]== 0):
                         playField[position] = playerNumber
                         return
                     else: 
                        print( "The plot is full, choose a different plot :")
                 else:
                     position = int(raw_input("Choose a different plot, on the board this time :"))
     
             except:
                 print("Please input an integer for location :")        

        
def checkState(board):
    count = 0
    
    for i in range(0,9):
        count = board[i] + count
       
    if (count < 13):
            
        return(False) 
    else:
   
        print("Game Over")
        return(True)

def printBoard(board):
    n= range(0,9)
    for i in range(0,9):
        if (board[i] == 1):
            n[i]="x"
        if (board[i] == 2):
            n[i] = 'o'
       # print n[i]  
    
    print n[0],n[1],n[2]
    print n[3],n[4],n[5]
    print n[6],n[7],n[8]         
            
playField = [0,0,0,0,0,0,0,0,0]
playerx = 1
playero = 2

while True:
    playerMov(playerx)
    printBoard(playField)
    if (checkState(playField))):
        break

    playerMov(playero)
    printBoard(playField)
    if (checkState(playField)):
        break
    
