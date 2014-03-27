'''
Created on Mar 9, 2014

@author: dave
'''

from filter import Filter # @UnresolvedImport
import copy

class ItemBasedFilter(Filter):
    '''
    For doing Item-Based Filtering
    '''


    def __init__(self, dataSet, scorer):
        '''
        Constructor
        '''
        self.origData = copy.deepcopy(dataSet.dat)
        dataSet.transposeUsersWithItems()
        super(ItemBasedFilter, self).__init__(dataSet, scorer)
        self.itemSimDict = self.getItemSimData()
        
    def getItemSimData(self,n=None):
        '''
        Creates a dictionary whose keys are items and values are lists of
        similar items with their similarity rating.
        
        Arguments:
            n   Number of items to rank as similar for each key-item
            
        Return:
            Dictionary
        '''
        result={}

        c=0
        print("Creating item similarity dictionary...")
        for item in self.data:
            # Status updates for large datasets
            c+=1
            if c%100==0: print("{} / {}".format(c,len(self.data)))
            # Find the most similar items to this one
            scores=self.kNearestNeighbors(item, n)
            result[item]=scores
        print("Item similarity dictionary created.")
        return result
    
    def getRecommendations(self, user, numRecs=None):
        userRatings = self.origData[user]
        scores = {}
        totalSim = {}
        
        # Loop over items rated by this user
        for (item, rating) in userRatings.items():
            # For items similar to this one
            for (similarity, item2) in self.itemSimDict[item]:
                if item2 in userRatings: continue
                
                # Weighted sum of rating times similarity
                scores.setdefault(item2, 0)
                scores[item2]+=similarity*rating
                
                # Sum of all similarities
                totalSim.setdefault(item2, 0)
                totalSim[item2]+=similarity
                
        # Divide each total score by total weighting to get an average
        rankings=[(item,score/totalSim[item]) for item,score in scores.items( )]
        
        # Return the rankings from highest to lowest
        rankings.sort( )
        rankings.reverse( )
        return rankings[0:numRecs]
    