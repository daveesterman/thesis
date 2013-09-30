'''
Created on Sep 18, 2013

@author: dave
'''
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src", "collaborativefiltering"))
import unittest
from similarityscorealgorithms import EuclidianDistance #@UnresolvedImport
from filter import Filter #@UnresolvedImport
import numpy as np


class TestEuclidianDistance(unittest.TestCase):
    
    euclid = EuclidianDistance()

    def testPerfectMatch(self):
        'equal vectors should have a score of 1.0'
        vec1 = np.array([1, 2, 3])
        vec2 = np.array([1, 2, 3])
        score = self.euclid.score(vec1, vec2)
        self.assertEqual(score, 1.0, 'score not equal to 1.0')
            
        
class TestFilter(unittest.TestCase):
    dat={'one':{'item1':1},
         'two':{'item1':2, 'item2':4}}
    filter = Filter(dat, EuclidianDistance())
    
    def testRecommendations(self):
        'based on dat, user one should have item2 as a recommendation'
        recs = self.filter.getRecommendations("one")
        recsDict = dict(recs)
        self.assertIn('item2', recsDict)

if __name__ == "__main__":
    unittest.main()