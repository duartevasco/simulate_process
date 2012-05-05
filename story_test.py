import random
import unittest
from story import *

class StoryTest(unittest.TestCase):

	def testStorySizeIsOne(self):
		s = Story(1)
		self.failUnless(s.sizeInTurns == 1)
	
	def testStorySizeIsInteger(self):
		s = Story(int(random.random()*10))
		self.failUnless(isinstance(s.sizeInTurns, (int,long)))
	
	def testStorySizeIsDecremented(self):
		s = Story(10)
		s.doWorkTurn()
		self.assertTrue(s.sizeInTurns > s.workLeftInTurns)
		
	def testStoryIsCompleted(self):
		s = Story(1)
		s.doWorkTurn()
		self.failUnless(s.isCompleted())
	
	def testStoryCalculateWorkLeft(self):
		s = Story(10)
		self.assertEqual(s.calculateWorkLeft(),10)

		
suite = unittest.TestLoader().loadTestsFromTestCase(StoryTest)
unittest.TextTestRunner(verbosity=2).run(suite)