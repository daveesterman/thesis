'''
Created on Sep 10, 2013

@author: dave
'''

import os
import numpy as np
from userBasedFilter import UserBasedFilter  # @UnresolvedImport
from itemBasedFilter import ItemBasedFilter  # @UnresolvedImport
from similarityscorealgorithms import *  # @UnresolvedImport
from dataReader import *  # @UnresolvedImport
from dataSet import DataSet  # @UnresolvedImport
from commandLineInterface import CommandLineInterface  # @UnresolvedImport

if __name__ == '__main__':
    
    go = CommandLineInterface()

#     os.system('clear')
#     print("Welcome to the collaborative filter.")
#     userFile = input("Where is your data?")
#     dat = DataSet(userFile)
#     
#     os.system('clear')
#     while(True):
#         UorI = int(input("1. User based filtering\n2. Item based filtering\n(1|2):"))    
#         if UorI==1:
#             f = UserBasedFilter(dat, EuclidianDistance())
#             break
#         elif UorI==2:
#             f = ItemBasedFilter(dat, EuclidianDistance())
#             break
#         else:
#             print("Try again.")
#     
#     while(True):
#         os.system('clear')
#         user = input("For which user would you like recommendations?")
#         os.system('clear')
#         numR = int(input("How many recommendations would you like?"))
#         os.system('clear')
#         print("Here you go!")
#         print(f.getRecommendations(user, numR))
#         input("")

    
        # Top people for item
#     for item in itemFilter.getRecommendations("Toy Story (1995)")[0:20]:
#         print(n, "{:>80} {:.5f}".format(item[0],item[1]))
#         n+=1

        # Most similar items to this item
#     for item in itemFilter.kNearestNeighbors("Toy Story (1995)", 2000):
#         print(item)
    
    