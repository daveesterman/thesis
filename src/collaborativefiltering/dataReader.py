'''
Created on Sep 16, 2013

@author: dave
'''

class DataReader():
    '''
    Contains various readers for data sets in different formats.
    '''

    def __init__(self):
        '''
        Constructor
        '''
        
    def convertMovieLens(self):
        ''' Converts MovieLens data into correct format'''
        
        # Create map of movie IDs to Titles
        movies = {}
        with open('../../data/ml-100k/u.item', encoding='latin1') as uitem:
            for line in uitem:
                (ID, title) = line.split('|')[0:2]
                movies[ID] = title
                
        dataSet = {}
        with open('../../data/ml-100k/u.data', encoding='utf-8') as udata:
            
                for line in udata:
                    (user, item, rating, time) = line.split()
                    if user in dataSet:
                        dataSet[user][movies[item]] = float(rating)
                    else:
                        dataSet[user] = {movies[item]:float(rating)} 
        return dataSet
    
    def transposeUsersWithItems(self, dat):
        '''Transposes users with items for the data set
        
        Arguments
            dat    The data set to be transposed.  The required format is a 
                   dictionary
                   {user1:{pref1:x, pref2:y},
                    user2:{pref1:a, pref2:b}
                   }
                   users will be transposed with prefs.
                   
        Return
            dict   transposed data set
        '''
        
        transposedDat = {}
        for person in dat:
            for item in dat[person]:
                transposedDat.setdefault(item, {})
                transposedDat[item][person]=dat[person][item]
        return transposedDat
        
        