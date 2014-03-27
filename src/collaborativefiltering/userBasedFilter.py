'''
Created on Mar 26, 2014

@author: dave
'''

from filter import Filter # @UnresolvedImport

class UserBasedFilter(Filter):
    '''
    For doing Item-Based Filtering
    '''


    def __init__(self, dataSet, scorer):
        '''
        Constructor
        '''
        super(UserBasedFilter, self).__init__(dataSet, scorer)
        
    def getRecommendations(self, user, numRecs=None):
        '''Get an ordered list of recommendations for a user
        
        Arguments:
            user    The user for which to generate recommendations
            
        Return:
            A list of tuples.  Each tuple will contain an item and its
            predicted rating for the given user.  The tuples will be ordered
            by predicted rating with the highest recommendation as list item 0
        '''
        # Get a set of all possible items
        itemsWithDups = []
        for aUser in self.data:
            for item in self.data[aUser]:
                itemsWithDups.append(item)
        allItems = set(itemsWithDups)
        
        # Get the recommendations
        unsortedRecs = []
        for item in allItems:
            # only want to recommend items unknown to user
            if item not in self.data[user]:
                unsortedRecs.append((item, 
                             self.getNormalizedTotalWeightedItemScore(user, 
                                                                      item)))
        # Sort the recommendations
        recs = sorted(unsortedRecs, key=lambda rec: rec[1])
        recs.reverse()
        return recs[0:numRecs]
    