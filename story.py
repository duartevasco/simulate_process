import random

class Story():
	ONE_TURN = 1
	ZERO = 0
	
	def __init__(self, sizeInTurns):
		self.sizeInTurns = self.workLeftInTurns = sizeInTurns
		
	def doWorkTurn(self):
		self.workLeftInTurns -= self.ONE_TURN
		
	def isCompleted(self):
		return self.workLeftInTurns == self.ZERO
	
	def calculateWorkLeft(self):
		return self.workLeftInTurns