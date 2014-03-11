'''
Created on Mar 9, 2014

@author: dave
'''

from filter import Filter # @UnresolvedImport

class ItemBasedFilter(Filter):
    '''
    For doing Item-Based Filtering
    '''


    def __init__(self, dataSet, scorer):
        '''
        Constructor
        '''
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
        return result