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

if __name__ == '__main__':

    os.system('clear')
    print("Welcome to the collaborative filter.")
    userFile = input("Where is your data?")
    dat = DataSet(userFile)
    
    os.system('clear')
    while(True):
        UorI = int(input("1. User based filtering\n2. Item based filtering\n(1|2):"))    
        if UorI==1:
            f = UserBasedFilter(dat, EuclidianDistance())
            break
        elif UorI==2:
            f = ItemBasedFilter(dat, EuclidianDistance())
            break
        else:
            print("Try again.")
    
    while(True):
        os.system('clear')
        user = input("For which user would you like recommendations?")
        os.system('clear')
        numR = int(input("How many recommendations would you like?"))
        os.system('clear')
        print("Here you go!")
        print(f.getRecommendations(user, numR))
        input("")
    
#     # User based filtering        
#     myFilter = UserBasedFilter(dat, EuclidianDistance())
#     n=1
#     for item in myFilter.getRecommendations("Dave"):
#         print(n, "{:>80} {:.5f}".format(item[0],item[1]))
#         n+=1
#         if n > 20:
#             break
#                 
#     print(myFilter.kNearestNeighbors("Dave",2))
#     # Item based filtering
#     itemF = ItemBasedFilter(dat, EuclidianDistance())
#     
#     for item in itemF.getRecommendations("Dave"):
#         print(n, "{:>80} {:.5f}".format(item[0],item[1]))
#         n+=1
#         if n > 20:
#             break
    

    
        # Top people for item
#     for item in itemFilter.getRecommendations("Toy Story (1995)")[0:20]:
#         print(n, "{:>80} {:.5f}".format(item[0],item[1]))
#         n+=1

        # Most similar items to this item
#     for item in itemFilter.kNearestNeighbors("Toy Story (1995)", 2000):
#         print(item)

#     itemSimData = itemFilter.getItemSimData(20)
#     print("The item data has built")
#     while(True):
#         bad = False
#         choice = input("x to exit, or choose a user (1-943)")
#         numRecs = input("How many recommendations would you like?")
#         try:
#             choiceInt = int(choice)
#             numRecsInt = int(numRecs)
#         except:
#             bad = True
#         if (choice == "x" or numRecsInt == "x"): break
#         elif (bad or not 1<=choiceInt<=943 or not numRecsInt >= 0):
#             print("bad choice!")
#             continue
#         else:
#             print(movFilter.getItemBasedRecs(itemSimData, choice, numRecsInt))
    
    