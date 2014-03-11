'''
Created on Sep 10, 2013

@author: dave
'''

import numpy as np
from filter import Filter  # @UnresolvedImport
from similarityscorealgorithms import *  # @UnresolvedImport
from dataReader import *  # @UnresolvedImport
from dataSet import DataSet  # @UnresolvedImport

if __name__ == '__main__':

    # Check DataSet functionality
    userFile = input("Where is your data?")
    dat = DataSet(userFile)
    
    # User based filtering        
    myFilter = Filter(dat, EuclidianDistance())
    n=1
    for item in myFilter.getRecommendations("Dave"):
        print(n, "{:>80} {:.5f}".format(item[0],item[1]))
        n+=1
        if n > 20:
            break
                
    print(myFilter.kNearestNeighbors("Dave",2))
    # Item based filtering
#     n=1
#     movItems = rdr.transposeUsersWithItems(movLens)
#     itemFilter = Filter(movItems, EuclidianDistance())

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
    
    