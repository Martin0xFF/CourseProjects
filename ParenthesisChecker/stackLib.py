class stack():
	def __init__(self):
		self.store = []
		self.numItems = 0
		self.isEmpty = True
	def push (self,value):
		self.numItems = self.numItems + 1
		self.store = self.store + [value] 
		self.isEmpty = False
		return 0

	def pop (self,):
		if len(self.store) == 0:
			return [False, -1]
		
		else:
			self.numItems = self.numItems - 1
			temp = self.store[len(self.store)-1]
			self.store = self.store[0:len(self.store)-1]
			if self.numItems == 0:
				self.isEmpty = True
			return [True,temp]
