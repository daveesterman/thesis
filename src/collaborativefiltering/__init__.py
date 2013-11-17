'''
Created on Sep 10, 2013

@author: dave
'''

import numpy as np
from filter import Filter  # @UnresolvedImport
from similarityscorealgorithms import *  # @UnresolvedImport
from dataReader import *  # @UnresolvedImport

if __name__ == '__main__':

    dat = {}

    # read data from file
    with open('../../data/PCI.ch2.critics.txt', encoding='utf-8') as a_file:
        dat = eval(a_file.read())

    f = Filter(dat, EuclidianDistance())
#     for neb in f.kNearestNeighbors("Toby", 12):
#         print(neb)

#     for item in f.getRecommendations("Toby"):
#         print(item)
        
    # MovieLens
    rdr = DataReader()
    movLens = rdr.convertMovieLens()
    
    # User based filtering
#     movFilter = Filter(movLens, EuclidianDistance())
#     n=1
#     for item in movFilter.getRecommendations("1"):
#         print(n, "{:>80} {:.5f}".format(item[0],item[1]))
#         n+=1
        
    # Item based filtering
    n=1
    movItems = rdr.transposeUsersWithItems(movLens)
    itemFilter = Filter(movItems, EuclidianDistance())
#     for item in itemFilter.getRecommendations("Toy Story (1995)")[0:20]:
#         print(n, "{:>80} {:.5f}".format(item[0],item[1]))
#         n+=1

    for item in itemFilter.kNearestNeighbors("Toy Story (1995)", 2000):
        print(item)