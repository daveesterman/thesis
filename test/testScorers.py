'''
Created on Sep 18, 2013

@author: dave
'''
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src", "collaborativefiltering"))
import unittest
from similarityscorealgorithms import EuclidianDistance #@UnresolvedImport
from filter import Filter #@UnresolvedImport
from itemBasedFilter import ItemBasedFilter #@UnresolvedImport
from dataSet import DataSet #@UnresolvedImport
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
#     path = os.environ.get("THESIS") + "/data/testData"
    path = "../data/testData"
    data = DataSet(path)
    filter = Filter(data, EuclidianDistance())
    itemFilt = ItemBasedFilter(data, EuclidianDistance())
    
    def testRecommendations(self):
        'based on data, Dave should have HungerGames as a recommendation'
        recs = self.filter.getRecommendations("Dave")
        recsDict = dict(recs)
        self.assertIn('HungerGames', recsDict)
        
    def test_kNearestNeighbors(self):
        '''Bob should be one of Dave's nearest neighbors'''
        nearest = self.filter.kNearestNeighbors("Dave", 2)
        print(nearest)
        nearestNames = [tup[1] for tup in nearest]
        self.assertIn("Bob", nearestNames)
        
    def test_getItemSimData(self):
        '''Should be a dict with items as keys'''
        print(self.itemFilt.itemSimDict)
        self.assertIn("HungerGames", self.itemFilt.itemSimDict, 
                      "HungerGames is not in itemSimDict")
        self.assertIsInstance(self.itemFilt.itemSimDict, dict, 
                              "itemSimDict is not a dict.")

if __name__ == "__main__":
    unittest.main()