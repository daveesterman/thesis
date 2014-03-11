'''
Created on Feb 22, 2014

@author: dave
'''

from dataReader import *  # @UnresolvedImport

class DataSet():
    '''
    Represents a data set to be used for filtering.  Consists of users, items,
    and ratings.
    '''


    def __init__(self, filePath=None):
        '''
        Constructor
        
        filePath    Path to file containing data to be used as the data set.
        '''
        self.reader = DataReader()
        self.dat    = self.reader.readFromFile(filePath)
        
        
    def transposeUsersWithItems(self):
        '''Transposes users with items for the data set
                   
        Return
            None    Modifies dat attribute of instance
        '''
        
        transposedDat = {}
        for person in self.dat:
            for item in self.dat[person]:
                transposedDat.setdefault(item, {})
                transposedDat[item][person]=self.dat[person][item]
        self.dat = transposedDat
        
    def __str__(self):
        return "{}".format(self.dat)