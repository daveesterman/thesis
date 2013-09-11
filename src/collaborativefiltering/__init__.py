'''
Created on Sep 10, 2013

@author: dave
'''

import numpy as np
from collaborativefiltering.filter import Filter
from collaborativefiltering.similarityscorealgorithms import EuclidianDistance

a = np.array((1, 2, 3))
b = np.array((4, 10, 6))
c = np.array(range(7,10))

f = Filter([a, a-.1], EuclidianDistance())


if __name__ == '__main__':
    print(f.computeScore())
    print(b -1)