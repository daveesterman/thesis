'''
Created on Sep 11, 2013

@author: dave
'''

import numpy as np

class Filter:
    '''
    classdocs
    '''
    
    data = None
    scorer = None

    def __init__(self, data, scorer):
        '''
        Constructor
        '''
        self.data = data
        self.scorer = scorer
        
    def computeScoreTwo(self, user1, user2):
        '''Compute the similarity score between user1 and user2.
        
        Return:
            float in the range [-1,1]
                (These values can only be compared to values calculated with
                the same scorer.  The scores are not absolute.)
            None if the two users have no preferences in common
        '''
        
        #TODO don't rely on specific implementation of data?
        """
        Currently this relies on a data format as follows:
        {user1:{pref1:x, pref2:y},
         user2:{pref1:a, pref2:b}
         }
        """

        #get the list of shared items
        shared = []
        for item in self.data[user1]:
            if item in self.data[user2]:
                shared.append(item)
        if len(shared)==0: return 0
        
        # Create array for each user of their values for each preference item
        # they have in common.
        vec1 = np.array([self.data[user1][item] for item in shared])
        vec2 = np.array([self.data[user2][item] for item in shared])
        
        # Compute the score for these two users.
        return self.scorer.score(vec1, vec2)
        