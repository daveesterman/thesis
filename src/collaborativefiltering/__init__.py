'''
Created on Sep 10, 2013

@author: dave
'''

import numpy as np
from collaborativefiltering.filter import Filter
from collaborativefiltering.similarityscorealgorithms import *

if __name__ == '__main__':

    dat = {}

    # read data from file
    with open('../../data/PCI.ch2.critics.txt', encoding='utf-8') as a_file:
        dat = eval(a_file.read())

    f = Filter(dat, EuclidianDistance())
    fPCI = Filter(dat, EuclidPCI())

#     print("Rose v Seymour w/ PCI Euclid:  ", fPCI.computeScoreTwo('Lisa Rose', 'Gene Seymour'))
#     print(f.getWeightedItemScore("Toby", "Lisa Rose", "The Night Listener"))
    print(f.getNormalizedTotalWeightedItemScore("Toby", "The Night Listener"))
    print(f.getNormalizedTotalWeightedItemScore("Toby", "Lady in the Water"))
    print(f.getNormalizedTotalWeightedItemScore("Toby", "Just My Luck"))
    for item in f.getRecommendations("Toby"):
        print(item)
