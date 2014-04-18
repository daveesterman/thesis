'''
Created on Mar 29, 2014

@author: dave
'''
import logging
import os
import sys
from dataSet import DataSet  # @UnresolvedImport
from userBasedFilter import UserBasedFilter  # @UnresolvedImport
from itemBasedFilter import ItemBasedFilter  # @UnresolvedImport
from similarityscorealgorithms import EuclidianDistance  # @UnresolvedImport

prompt = "==>"

class CommandLineInterface():
    '''
    classdocs
    '''
    
    dataLocation = None
    dataSet      = None
    filterType   = None
    filter       = None
    algorithm    = None
    
    back         = None
    
    def __init__(self):
        '''
        Constructor
        '''
        self.MainMenu = {1:self.data, 2:self.userItem, 3:self.setAlgorithm,
                         4:self.prepareFilter, 5:self.getRecs}
        self.LoadData = {1:self.loadData}
        self.UserItem = {1:self.setUserBased, 2:self.setItemBased}
        self.Algorithm = {1:self.setEuclidian}
        self.back = self.mainMenu
        while(True):
            try:
                self.back()
            except Exception:
                logging.exception("There's been a problem, try again:")
                input("Press Enter to continue")
                continue
            except:
                sys.exit(0)
        
    def printState(self):
        if self.filterType is None:
            self.filterTypeString = "None"
        else:
            self.filterTypeString = str(self.filterType.__name__) 
        
        if self.algorithm is None:
            self.algorithmString = "None"
        else:
            self.algorithmString = str(self.algorithm.__class__.__name__)
                 
        stateStr = ("Data Set Location:  " + str(self.dataLocation) + "\n"
                    "Filter Type      :  " + self.filterTypeString + "\n"
                    "Algorithm        :  " + self.algorithmString + "\n")
        print(stateStr)
        
    def displayMenu(self, opts):
        menuString = opts[0] + '\n' # opts[0] should be the menu title
        for item in opts[1:]:
            menuString += (str(opts.index(item)) + '.  ' + item + '\n')
        menuString += ("x.  Exit\n"
                       "b.  Go Back\n")
        menuString += prompt
        os.system('clear')
        self.printState()
        i = input(menuString)
        
        if i=='x':
            sys.exit(0)
        elif i=='b':
            self.back()
        else:
            return int(i)
        

    def mainMenu(self):
        choice = self.displayMenu(['Main Menu', 'Load Data', 'User/Item Based Filtering',
                              'Algorithm', 'Prepare Filter', 'Get Recommendations'])
        self.MainMenu[choice]()
        
    """ DATASET """        
        
    def data(self):
        choice = self.displayMenu(['Load Data', "Enter Path"])
        self.LoadData[choice]()
        self.back()
        
    def loadData(self):
        os.system('clear')
        self.dataLocation = input(prompt)
        self.dataSet = DataSet(self.dataLocation)
        
    """ FILTER """
    
    def userItem(self):
        choice = self.displayMenu(['User or Item Based Filtering', 'User Based', 'Item Based'])
        self.UserItem[choice]()
        self.back()
        
    def setUserBased(self):
        self.filterType = UserBasedFilter
                
    def setItemBased(self):
        self.filterType = ItemBasedFilter
        
    """ ALGORITHM """
    
    def setAlgorithm(self):
        choice = self.displayMenu(['Similarity Score Algorithm', 'Euclidian Distance'])
        self.Algorithm[choice]()
        self.back()
        
    def setEuclidian(self):
        self.algorithm = EuclidianDistance()
        
    """ PREPARE FILTER """
    
    def prepareFilter(self):
        self.filter = self.filterType(self.dataSet, self.algorithm)
        self.back()
        
    """ INVESTIGATE """
    
    def getRecs(self):
        user = input('Choose a user to get recs for:')
        num  = int(input('How many recs would you like?'))
        print(self.filter.getRecommendations(user, num))
        void = input('Press Enter to continue...')
        self.back()