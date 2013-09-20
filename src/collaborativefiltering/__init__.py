'''
Created on Sep 10, 2013

@author: dave
'''

import numpy as np
from collaborativefiltering.filter import Filter
from collaborativefiltering.similarityscorealgorithms import EuclidianDistance

if __name__ == '__main__':

    data = {}

    # read data from file
    with open('../../data/PCI.ch2.critics.txt', encoding='utf-8') as a_file:
        data = eval(a_file.read())

    f = Filter(data, EuclidianDistance())

    print(f.computeScoreTwo('Lisa Rose', 'Jack Matthews'))
    print(f.computeScoreTwo('Lisa Rose', 'Gene Seymour'))
