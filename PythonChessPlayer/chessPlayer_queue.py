class queue:
	def __init__(self):
		self.store = []

	def enqueue(self,val):
		self.store = self.store + [val]
		return 0

	def dequeue(self):
		if len(self.store) ==0:
			return [False,"Welcome to the Hotel Cali..."] 	
		else:
			val = self.store[0]
			self.store = self.store[1:len(self.store)]
			return [True,val]
