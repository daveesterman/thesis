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
        
    def pciExampleCritics(self):
        '''Reads the example critics from PCI and returns a data set'''
        dat = {}

        # read data from file
        with open('../../data/PCI.ch2.critics.txt', encoding='utf-8') as a_file:
            dat = eval(a_file.read())
        return dat
        
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

    def readFromFile(self, filePath):
        '''
        Reads from a file to produce a data set for filtering.
        
        Arguments: 
            filePath
                The file to be read.  Format of the file should be text with
                each line containing one entry of the data set.  There must be
                three columns, separated by whitespace, with data in order as:
                
                <user>    <item>    <rating>
                <user>    <item>    <rating>
                ...
                
                There is no required order from line to line.  In other words,
                you don't need all entries for a single user to be on
                consecutive lines, or all items for a single item.
        
        Return:
            dictionary with format
            {user1:{<item>:<rating>, <item>:<rating>},
             user2:{<item>:<rating>, <item>:<rating>}
             }
          '''
        dataSet = {}
        with open(filePath, encoding="utf-8") as dataFile:
            for line in dataFile:
                (user, item, rating) = line.split()
                if user in dataSet:
                    dataSet[user][item] = float(rating)
                else:
                    dataSet[user] = {item:float(rating)} 
            return dataSet