from queueLib import *
import treeLib as t
class binary_tree:
	def __init__(self,x):
		self.store = [x,None,None]
		self.depth = 0

	def AddRight(self,x):
		self.store[2] = x
		return True

	def AddLeft(self,x):
		self.store[1] = x
		return True
	
	def Get_LevelOrder(self):
		temp = queue()
		out = []
		temp.enqueue(self)#Priming traversal, enqueue the first element
	
		while temp.store != []: #Keep processing values in list until its empty
			temp.store[0].ProcessLevel(temp) #We reap the benefits of FIFO, Here the index remains the same as we iterate  
			out = out + [temp.dequeue()[1].store[0]] #here we build the output list by using the dequeued element
	#	print out
		return out

	def ProcessLevel (self,que): # Level order traverse helper
			
		for i in range(1,len(self.store)):
			if self.store[i] != None:
				que.enqueue(self.store[i])	
		return que

	

	def PrintInOrder(self):
		
		if self.store[1] != None:
			self.store[1].PrintInOrder()
		
		print self.store[0]
		
		if self.store[2] != None:
			self.store[2].PrintInOrder()
		
		return True
		
	def PrintLevel(self): # for Converted trees:

		print self.store[0]
		
		if self.store[2] != None:
			self.store[2].PrintLevel()

		if self.store[1] != None:
			self.store[1].PrintLevel()	
		
				
		return True
		
	def ConvertToTree(self):
		if self.store[2] != None:
			return [False,None]

		outTree =t.tree(self)
		outTree = self.ConvertRoot(outTree)
		outTree.CleanToInt()	
		
		return[True, outTree]
#WIP		
	def ConvertRoot(self,outTree):
			 	
		extender = t.tree(self.store[1])

		if self.store[1] !=None:
				
			outTree.AddSuccessor(extender)	
			outTree.store[1][0].store[0].ConvertRoot(outTree.store[1][0])

			
		i = 1
		while extender.store[0] != None:
			extender = t.tree(extender.store[0].store[2])	
			if extender.store[0] != None:
			
				outTree.AddSuccessor(extender)
				outTree.store[1][i].store[0].ConvertRoot(outTree.store[1][i])	
			

			
			i = i+1
				
		return outTree



	def rootTraverse(self,genTree):

		
		
		if self.store[2] != None:
			self.store[2].PrintLevel(gentree)

		if self.store[1] != None:
			self.store[1].PrintLevel(gentree)	
		
				
#		return True
		
