from team import *
from story import *
import unittest
 
class TeamTest(unittest.TestCase):
	ARBITRARY_STORY_SIZE = 10
	CAPACITY_ONE = 1
	CAPACITY_THREE = 3
	TWO_STORIES = 2

	def setUp(self):
		self.t = Team()
		self.t.assignWork(Story(self.ARBITRARY_STORY_SIZE))
		
	def testTeamAssignWork(self):
		self.failUnless(self.t.getStoriesList() != None)
	
	def testTeamCalculateWorkLeft(self):
		self.assertEqual(self.t.calculateWorkLeft(), self.ARBITRARY_STORY_SIZE)
		
	def testTeamAssignSeveralStories(self):
		self.t.assignWork(Story(self.ARBITRARY_STORY_SIZE))
		self.assertEqual(len(self.t.getStoriesList()), self.TWO_STORIES)

	def testTeamCalculateWorkForSeveralStories(self):
 		self.t.assignWork(Story(self.ARBITRARY_STORY_SIZE))
		self.assertEqual(self.t.calculateWorkLeft(), self.ARBITRARY_STORY_SIZE * 2)
	
	def testTeamDoWorkTurn(self):
		w1 = self.t.calculateWorkLeft()
		self.t.doWorkTurn(self.CAPACITY_ONE)
		w2 = self.t.calculateWorkLeft()
		self.assertEqual(w1, w2 + 1)
	
	def testTeamDoWorkTurnWithCapacity(self):
		w1 = self.t.calculateWorkLeft()
		self.t.doWorkTurn(self.CAPACITY_THREE)
		w2 = self.t.calculateWorkLeft()
		self.assertEqual(w1, w2 + self.CAPACITY_THREE)
		

suite = unittest.TestLoader().loadTestsFromTestCase(TeamTest)
unittest.TextTestRunner(verbosity=2).run(suite)