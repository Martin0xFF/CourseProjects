from chessPlayer_queue import queue
class tree:
	def __init__(self,x):
		self.store = [x,[]]
		self.depth = 0
	def AddSuccessor(self,x):
		self.store[1]= self.store[1] + [x]
		return True

	def Print_DepthFirst(self):

		for w in range(0,self.depth):
			print '',

		print(self.store[0])		
		for i in range(0,len( self.store[1])):		
			self.store[1][i].depth = self.depth + 3 
			self.store[1][i].Print_DepthFirst()
		
		self.depth = 0	
		return 0 	
	def CleanToInt(self):
		self.store[0] = self.store[0].store[0]
		for i in range(0,len(self.store[1])):
			self.store[1][i].CleanToInt()
			
		return True
	def Get_LevelOrder(self):
	 
		temp = queue()
		out = []
		temp.enqueue(self)#Priming traversal, enqueue the first element
	
		while temp.store != []: #Keep processing values in list until its empty
			temp.store[0].ProcessLevel(temp) #We reap the benefits of FIFO, Here the index remains the same as we iterate  
			out = out + [temp.dequeue()[1].store[0]] #here we build the output list by using the dequeued element
		return out

	def ProcessLevel (self,que):
		
		for i in range(0,len(self.store[1])):
			que.enqueue(self.store[1][i])	
		return que
	'''
	#BinaryTree
	def ConvertToBinaryTree(self):
	
		binaryTree = bt.binary_tree(self)
		self.Bind(binaryTree)
	return binaryTree
	
			
	def Bind(self,tree):
		tree.store[0].BinaryProcess(tree)
		tree.store[0]= tree.store[0].store[0]
		if tree.store[1] != None:
			self.Bind(tree.store[1])
		if tree.store[2] != None:
			self.Bind(tree.store[2])
		
		return 0

	def BinaryProcess(self,binaryTree):
		if len(self.store[1]) == 0:
			return False
		extender = bt.binary_tree(self.store[1][0])
		binaryTree.AddLeft(extender)
			
		for i in range(1,len(self.store[1])):
			temp =bt.binary_tree(self.store[1][i])
			extender.AddRight(temp)
			extender = extender.store[2]
			
		
		return True
	'''
