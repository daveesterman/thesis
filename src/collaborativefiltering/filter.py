'''
Created on Sep 11, 2013

@author: dave
'''

import numpy as np

class Filter:
    '''
    classdocs
    '''
    
    def __init__(self, data, scorer):
        '''
        Create Filter object.
        
        Arguments:
            data    dataset to be filtered
            scorer  Algorithm for determining similarity scores
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
        if len(shared)==0: return None
        
        # Create array for each user of their values for each preference item
        # they have in common.
        vec1 = np.array([self.data[user1][item] for item in shared])
        vec2 = np.array([self.data[user2][item] for item in shared])
        
        # Compute the score for these two users.
        return self.scorer.score(vec1, vec2)
        
    def getRecommendations(self, user):
        '''Get an ordered list of recommendations for a user
        
        Arguments:
            user    The user for which to generate recommendations
            
        Return:
            A list of tuples.  Each tuple will contain an item and its
            predicted rating for the given usvalider.  The tuples will be ordered
            by predicted rating with the highest recommendation as list item 0
        '''
        # Get a set of all possible items
        itemsWithDups = []
        for aUser in self.data:
            for item in self.data[aUser]:
                itemsWithDups.append(item)
        allItems = set(itemsWithDups)
        
        # Create the list of tuples
        unsortedRecs = []
        for item in allItems:
            # only want to recommend items unkown to user
            if item not in self.data[user]:
                unsortedRecs.append((item, 
                             self.getNormalizedTotalWeightedItemScore(user, 
                                                                      item)))
        recs = sorted(unsortedRecs, key=lambda rec: rec[1])
        recs.reverse()
        return recs
    
    def getWeightedItemScore(self, user1, user2, item): 
        '''
        Get a weighted score for an item based on the similarity of two users.
        
        Arguments:
            user1   The user who needs recommendations
            user2   The user whose rating will be weighted by similarity
            item    The item whose weighted score will be determined
        
        Return:
            float   weighted score
        '''
        
        simScore = self.computeScoreTwo(user1, user2)
        user2ItemRating = self.data[user2][item]
        weightedScore = simScore * user2ItemRating
        return weightedScore
    
    def getNormalizedTotalWeightedItemScore(self, user1, item):
        '''
        Get the normalized total weighted score for an item.
        
        Arguments:
            user1   The user who needs recommendations
            item    The item whose normalized score will be determined
        
        Return:
            float   The normalized weighted score for item
        '''
        
        # Get a list of all the users except user1
        otherUsers = list(self.data.keys())
        otherUsers.remove(user1)

        # For each of the other users who has a valid score for item, get
        # their weighted score for item and add to the total, then divide
        # that total by the total similarity of those users to user1.
        total    = 0
        simTotal = 0
        for user in otherUsers:
            if item in self.data[user]:
                total += self.getWeightedItemScore(user1, user, item)
                simTotal += self.computeScoreTwo(user1, user)
                
        return total/simTotal
