'''
Created on Sep 10, 2013

@author: dave
'''

import numpy as np
from filter import Filter  # @UnresolvedImport
from similarityscorealgorithms import *  # @UnresolvedImport
from dataReader import *  # @UnresolvedImport

if __name__ == '__main__':

    rdr = DataReader()

    # PCI example
#     dat = rdr.pciExampleCritics()
#     f = Filter(dat, EuclidianDistance())
#     for neb in f.kNearestNeighbors("Toby", 12):
#         print(neb)

#     for item in f.getRecommendations("Toby"):
#         print(item)
        
    # MovieLens
    movLens = rdr.convertMovieLens()
    
    # User based filtering
    movFilter = Filter(movLens, EuclidianDistance())
    """
    n=1
    for item in movFilter.getRecommendations("1"):
        print(n, "{:>80} {:.5f}".format(item[0],item[1]))
        n+=1
        if n > 20:
            break
            """
        
    # Item based filtering
    n=1
    movItems = rdr.transposeUsersWithItems(movLens)
    itemFilter = Filter(movItems, EuclidianDistance())
#     for item in itemFilter.getRecommendations("Toy Story (1995)")[0:20]:
#         print(n, "{:>80} {:.5f}".format(item[0],item[1]))
#         n+=1

#     for item in itemFilter.kNearestNeighbors("Toy Story (1995)", 2000):
#         print(item)

    itemSimData = itemFilter.getItemSimData(20)
    print("The item data has built")
    while(True):
        bad = False
        choice = input("x to exit, or choose a user (1-943)")
        numRecs = input("How many recommendations would you like?")
        try:
            choiceInt = int(choice)
            numRecsInt = int(numRecs)
        except:
            bad = True
        if (choice == "x" or numRecsInt == "x"): break
        elif (bad or not 1<=choiceInt<=943 or not numRecsInt >= 0):
            print("bad choice!")
            continue
        else:
            print(movFilter.getItemBasedRecs(itemSimData, choice, numRecsInt))
    
    