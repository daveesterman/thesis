'''
Created on Sep 18, 2013

@author: dave
'''
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src", "collaborativefiltering"))
import unittest
from collaborativefiltering.similarityscorealgorithms import EuclidianDistance
import numpy as np


class TestEuclidianDistance(unittest.TestCase):
    
    euclid = EuclidianDistance()

    def testPerfectMatch(self):
        'equal vectors should have a score of 1.0'
        vec1 = np.array([1, 2, 3])
        vec2 = np.array([1, 2, 4])
        score = self.euclid.score(vec1, vec2)
        self.assertEqual(score, 1.0, 'score not equal to 1.0')
        
    def testOneUnitAway(self):
        vec1 = np.array([1])
        vec2 = np.array([0])
        score = self.euclid.score(vec1, vec2)
        self.assertEqual(score, 0.0, 'score not equal to 0.0')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()