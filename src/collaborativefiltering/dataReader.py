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
