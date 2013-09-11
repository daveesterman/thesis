'''
Created on Sep 11, 2013

@author: dave
'''

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
        
    def computeScore(self):
        #TODO generalize access to the data structure.
        return self.scorer.score(self.data[0], self.data[1])
        