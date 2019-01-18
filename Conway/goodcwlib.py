from random import randint



class conway():

	def __init__(self, x, y, word):
		interum = []
		self.store =[]
		self.x = x
		self.y = y
		if word == 'zeros':
			for i in range(0,x):
				self.store = self.store + [[0]*y]
		
		elif word == 'random':
			for i in range(0,x):
				for m in range(0,y):
					interum = interum + [randint(0,1)]
				self.store = self.store + [interum] 
				interum = []
			
		else:
			for i in range(0,x):
				self.store = self.store + [[0]*y]

	
	def getDisp(self):
		context = ""
		for i in range(0,self.x):
			for m in range(0,self.y):
				if self.store[i][m] == 0 :
					context = context +" "
				elif self.store[i][m] ==1:
					context = context +"*"
				else:
					return False
			context = context + "\n"	

		return context

	def printDisp(self):
		print self.getDisp()
		return True

	def setPos(self,row,col,val):
		if row<0 or row>= self.x:
			return False
		if col<0 or col>=self.y:
			return False
		if val<0 or val>1:
			return False
		self.store[row][col] = val
		return True


	def getNeighbours(self,row,col):
		if row<0 or row>= self.x:
			return False
		if col<0 or col>=self.y:
			return False

		
		maxcol = self.y
		maxrow = self.x

		if (col-1)<0: 	
			cl = (maxcol-1)
		else:
			cl = (col-1)   
		
		cm=col
		cr=(col+1)%maxcol

 		
		if (row-1)<0: 
			rt = (maxrow-1)
		else:
			rt = (row-1)
		rm=row
		rb=(row+1)%maxrow
		
		
		
		return[self.store[rt][cl],self.store[rt][cm],self.store[rt][cr],self.store[rm][cl],self.store[rm][cr],self.store[rb][cl],self.store[rb][cm],self.store[rb][cr]]

	

	def evolve(self,f):
		next_state =[]
		for i in range(0,self.x):
			next_state =next_state + [[0]*self.y]
		

		
		for i in range (0,self.x):
			for w in range(0,self.y):
				next_state[i][w] = f(self.store[i][w],self.getNeighbours(i,w))

		
		self.store = next_state
		return 1
