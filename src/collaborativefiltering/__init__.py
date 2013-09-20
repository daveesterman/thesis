'''
Created on Sep 10, 2013

@author: dave
'''

import numpy as np
from collaborativefiltering.filter import Filter
from collaborativefiltering.similarityscorealgorithms import EuclidianDistance

if __name__ == '__main__':

    dat = {}

    # read data from file
    with open('../../data/PCI.ch2.critics.txt', encoding='utf-8') as a_file:
        dat = eval(a_file.read())

    f = Filter(dat, EuclidianDistance())

    print(f.computeScoreTwo('Lisa Rose', 'Jack Matthews'))
    print(f.computeScoreTwo('Lisa Rose', 'Gene Seymour'))
#     print(f.data)
#     print(f.getData())
