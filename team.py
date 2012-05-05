class Team():
	def __init__(self):
		self.storiesList = None
	
	def assignWork(self, stories):
		if self.storiesList == None:
			self.storiesList = []
			self.storiesList.append(stories)
		else:
			self.storiesList.append(stories)

	def getStoriesList(self):
		return list(self.storiesList)
		
	def calculateWorkLeft(self):
		sum = 0
		for i in range(0, len(self.storiesList)):
			sum += self.storiesList[i].calculateWorkLeft()
		return sum
		
	def doWorkTurnUnitaryCapacity(self):
		for i in range(0, len(self.storiesList)):
			if self.storiesList[i].calculateWorkLeft() > 0:
				self.storiesList[i].doWorkTurn()
				return
		return
		
	def doWorkTurn(self, capacity):
		for i in range(0, capacity):
			self.doWorkTurnUnitaryCapacity()
		return
