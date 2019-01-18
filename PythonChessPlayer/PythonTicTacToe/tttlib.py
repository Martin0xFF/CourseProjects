class ttt(object):
	def __init__(self):
		self.store = [0,0,0,0,0,0,0,0,0]

	def Move(self,x,player):
		try:
			int(x)
			if x>8 or x<0: 
				return False
			if self.store[x] ==0:
				self.store[x] = player
				return True
			else:
				return False
		except:
			return False
	#1 is X 2 is O, 1 -> X wins,2 ->O Wins, 3 -> Full Board Tie, 0 -> Keep Playing 
	def analyzeBoard(self):
    		try:
        		count = 0
        		for i in range(0,9):
           			if self.store[i] == 0:
               				count = 1
               				break
        
        		if (self.store[0] == self.store[1] == self.store[2]==1) or (self.store[3] == self.store[4] == self.store[5]==1) or (self.store[6]==self.store[7]==self.store[8]==1) or (self.store[0]==self.store[3]==self.store[6]==1)or (self.store[1]==self.store[4]==self.store[7]==1)or (self.store[2]==self.store[5]==self.store[8]==1) or (self.store[0] == self.store[4] == self.store[8]==1) or (self.store[2] == self.store[4] == self.store[6]==1):
            			return (1)
            
        		elif (self.store[0] == self.store[1] == self.store[2]==2) or (self.store[3] == self.store[4] == self.store[5]==2) or  (self.store[6]==self.store[7]==self.store[8]==2) or (self.store[0]==self.store[3]==self.store[6]==2)or (self.store[1]==self.store[4]==self.store[7]==2)or (self.store[2]==self.store[5]==self.store[8]==2)or (self.store[0] == self.store[4] == self.store[8]==2) or (self.store[2] == self.store[4] == self.store[6]==2):

            			return (2)
        		if count == 0:
            			return(3)
        		else:
            			return(0)
        
              
    		except:
      			return(-1)
    


	def printBoard(self):
    		try:
        		if len(self.store) <> 9 :
            			return False 
        		n= range(0,9)
        		for i in range(0,9):
            			if (int(self.store[i]) == 1):
                			n[i]="X"
            			if (int(self.store[i])== 2):
                			n[i] = 'O'  
            			if (self.store[i]>2 or self.store[i]<0):
                			return false
            
        		print"", n[0],"|",n[1],"|",n[2]
       			print "---|---|---"
        		print"", n[3],"|",n[4],"|",n[5]
        		print"---|---|---"
        		print"", n[6],"|",n[7],"|",n[8]        
        		return True
    		except:
        		return False
 

       


	def genWinningMove(self,player):
    		try:
        		if (((self.store[0]==player and self.store[2]==player) or (self.store[4]== player and self.store[7] == player))and self.store[1]==0):
            			return (1)
        
        		elif (((self.store[3]==player and self.store[5]==player)or (self.store[7]==player and self.store[1]==player)or (self.store[8]==player and self.store[0]==player)or(self.store[2]==player and self.store[6]==player))and self.store[4]==0):
            			return (4)
    	 
        		elif (((self.store[6]==player and self.store[8]==player)or(self.store[1]==player and self.store[4]==player)and self.store[7]==0)):
            			return (7)
   	 
        		elif (((self.store[0]==player and self.store[6]==player)or(self.store[4]==player and self.store[5]==player)and self.store[3]==0)):
            			return (3)
	
        		elif (((self.store[0]==player and self.store[1]==player)or(self.store[8]==player and self.store[5]==player)or(self.store[4]==player and self.store[6]==player))and self.store[2]==0):
            			return (2)


        		elif (((self.store[3]==player and self.store[4]==player)or(self.store[2]==player and self.store[8]==player))and self.store[5]==0):
            			return (5)

        		elif (((self.store[0]==player and self.store[3]==player)or(self.store[7]==player and self.store[8]==player)or(self.store[4]==player and self.store[2]==player))and self.store[6]==0):
            			return (6)
   
        		elif (((self.store[5]==player and self.store[2]==player)or(self.store[7]==player and self.store[6]==player)or(self.store[0]==player and self.store[4]==player))and self.store[8]==0):
            			return (8) 

        		elif (((self.store[1]==player and self.store[2]==player)or(self.store[3]==player and self.store[6]==player)or(self.store[8]==player and self.store[4]==player))and self.store[0]==0):
            			return (0) 
			else:
	    			return (-1)
    		except:
       	 		return(-1)
     



	def genRandomMove(self,player):
    		from random import randint 
    
   	 	try:
        		if len(self.store)<> 9:
            			return(-1)    
        		for i in range(0,9):
	    			if self.store[i] == 0:
	        			while True:
                     				position = randint(0,8) 
	             				
						if self.store[position] == 0:
		        				return (position)
             
        		return (-1)
    		except:
        		return(-1) 
       


	def genNonLoser(self,player):
    		try:
        		if player == 1 :
           			player = 2
        		elif player == 2:
            			player = 1
            
        		if (((self.store[0]==player and self.store[2]==player) or (self.store[4]== player and self.store[7] == player))and self.store[1]==0):
            			return (1)
        
        		elif (((self.store[3]==player and self.store[5]==player)or (self.store[7]==player and self.store[1]==player)or (self.store[8]==player and self.store[0]==player)or(self.store[2]==player and self.store[6]==player))and self.store[4]==0):
            			return (4)
    	 
        		elif (((self.store[6]==player and self.store[8]==player)or(self.store[1]==player and self.store[4]==player)and self.store[7]==0)):
            			return (7)
   	 
        		elif (((self.store[0]==player and self.store[6]==player)or(self.store[4]==player and self.store[5]==player)and self.store[3]==0)):
            			return (3)
	
        		elif (((self.store[0]==player and self.store[1]==player)or(self.store[8]==player and self.store[5]==player)or(self.store[4]==player and self.store[6]==player))and self.store[2]==0):
            			return (2)


        		elif (((self.store[3]==player and self.store[4]==player)or(self.store[2]==player and self.store[8]==player))and self.store[5]==0):
            			return (5)

        		elif (((self.store[0]==player and self.store[3]==player)or(self.store[7]==player and self.store[8]==player)or(self.store[4]==player and self.store[2]==player))and self.store[6]==0):
            			return (6)
   
        		elif (((self.store[5]==player and self.store[2]==player)or(self.store[7]==player and self.store[6]==player)or(self.store[0]==player and self.store[4]==player))and self.store[8]==0):
            			return (8) 

        		elif (((self.store[1]==player and self.store[2]==player)or(self.store[3]==player and self.store[6]==player)or(self.store[8]==player and self.store[4]==player))and self.store[0]==0):
            			return (0) 
			else:
	    			return (-1)
    		except:
        		return(-1)
     
		         
